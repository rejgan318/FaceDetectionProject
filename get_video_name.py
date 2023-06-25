from random import choice
from pathlib import Path

import requests

def get_video_urls(config):
    base_video_url = config['data.video']['base_video_url']
    video_names = config['data.video']['video_files'].split('\n')
    return {video_name: base_video_url.format(video_name) for video_name in video_names}


def get_video_size(url):
    return requests.head(url).headers['content-length']


def download_video(url, filename, chunk_size: int = None):

    CHUNK_SIZE = 4 * 1024 * 1024
    chunk_size = chunk_size or CHUNK_SIZE

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, "wb") as file:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                file.write(chunk)

def get_video_name(cfg) -> Path:
    video_urls = get_video_urls(cfg)
    video_dir = cfg['Paths']['video_dir']

    video_name = choice(list(video_urls))
    if not Path(video_dir).exists():
        Path(video_dir).mkdir(parents=True)

    if (Path(video_dir) / video_name).exists():
        print(f"Video {video_name} already exists")
    else:
        print(f"Downloading video {video_name} to {video_dir} from {video_urls[video_name]}...")
        video_size = int(get_video_size(video_urls[video_name]))
        print(f"Video size: {video_size:,}")
        download_video(video_urls[video_name], Path(video_dir) / video_name)

    return Path(video_dir) / video_name
