# 🦙 Hello World Podcast Feed Updater

A Python application that updates the [Hello World podcast](https://open.spotify.com/show/2mKAHUneit9BzihtBvBq4J?si=fTn8zTiNQx2Jk1yv7jPQ5A&dl_branch=1) feed based on the latest content hosted on Channel 9. The entire update process relies on GitHub Actions - there is a scheduled run that happens every day and makes sure that the latest episodes are covered.

## Running locally

Make sure that you have [Python 3](https://www.python.org/downloads/) installed.

1. Create a virtual enviornment: `python3 -m venv .env`
2. Activate the environment:
	1. On Windows: `.env/Scripts/activate`
	2. On Linux: `source .env/bin/activate`
3. Install dependencies: `pip install -r src/requirements.txt`
4. Run the project: `cd src && python -m hwu`

A local XML feed will be generated in the `src` directory.

## FAQ

### Why does this project need to exist?

Channel 9 doesn't produce a clean audio-only feed, which breaks Spotify ingress for the podcast. The application cleans up the updated feed, and commits it [to a forked one](https://github.com/dendeli-work/feeds), that only has the required content.

### Is this a long-term solution?

No.
