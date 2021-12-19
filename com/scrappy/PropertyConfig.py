import json

CONFIG = {}


def initialize():
    with open(r'C:\Users\USER\Documents\dropbox-scraping\config.json') as config_file:
        data = json.load(config_file)
        for key in data.keys():
            CONFIG[key] = data[key]
    # print(CONFIG)


def getFolderPath():
    return CONFIG["folder_path"]


def getDriverPath():
    return CONFIG["driver_path"]


initialize()
