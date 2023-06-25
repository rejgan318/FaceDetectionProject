from random import choice
from pathlib import Path


def get_video_urls(config):
    base_video_url = config['data.video']['base_video_url']
    video_names = config['data.video']['video_files'].split('\n')
    return {video_name: base_video_url.format(video_name) for video_name in video_names}


def get_video_name(cfg) -> Path:
    video_urls = get_video_urls(cfg)
    video_dir = cfg['Paths']['video_dir']

    video_name = choice(list(video_urls))
    if not Path(video_dir).exists():
        Path(video_dir).mkdir(parents=True)

    if (Path(video_dir) / video_name).exists():
        print(f"Video {video_name} already exists")
    else:
        print(f"Downloading video {video_urls[video_name]}...")

    return (Path(video_dir) / video_name)
