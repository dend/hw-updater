import requests
import xml.etree.ElementTree as ET

CH9_FEED_URL = "https://channel9.msdn.com/Shows/Hello-World/feed/mp3"
CURRENT_FEED_URL = "https://raw.githubusercontent.com/dendeli-work/feeds/main/hello-world/feed.xml"
HW_FEED_IMAGE = "https://raw.githubusercontent.com/dendeli-work/feeds/main/hello-world/helloworld.png"

namespaces = {'media': 'http://search.yahoo.com/mrss/',
			  'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
			  'dc': 'http://purl.org/dc/elements/1.1/',
			  'atom': 'http://www.w3.org/2005/Atom',
			  'trackback': 'http://madskills.com/public/xml/rss/module/trackback/',
			  'wfw': 'http://wellformedweb.org/CommentAPI/',
			  'slash': 'http://purl.org/rss/1.0/modules/slash/',
			  'googleplay': 'http://www.google.com/schemas/play-podcasts/1.0',
			  'c9': 'http://channel9.msdn.com'}

for prefix, uri in namespaces.items():
    ET.register_namespace(prefix, uri)
    
raw_ch9_feed = requests.get(CH9_FEED_URL).text
ch9_feed = ET.fromstring(raw_ch9_feed)

raw_current_feed = requests.get(CURRENT_FEED_URL).text
current_feed = ET.fromstring(raw_current_feed)

target_node = current_feed.find('channel', namespaces)

# Get all the items from the new feed
candidate_items = ch9_feed.findall('.//item', namespaces)
current_items = current_feed.findall('.//item', namespaces)

for item in candidate_items:
	item_title = item.find('title').text
	title_exists = False
	for current_item in current_items:
		current_item_title = current_item.find('title').text

		title_exists = (current_item_title.lower() == item_title.lower())
		if title_exists:
			break

	# If this is a new node, then process it.
	if not title_exists:
		media_group = item.find(".//media:group", namespaces)
		video_nodes = media_group.findall('.//media:content[@medium="video"]', namespaces)

		if video_nodes:
			for video_node in video_nodes:
				media_group.remove(video_node)

		audio_nodes = media_group.findall('.//media:content[@type="audio/mp3"]', namespaces)
		if audio_nodes:
			target_node.append(item)

tree = ET.ElementTree(current_feed)
tree.write('feed.xml')
