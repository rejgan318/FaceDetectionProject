import configparser

from get_video_name import get_video_name


config = configparser.ConfigParser()
config.read('config.ini')

video_file = get_video_name(config)

print("Done.")
