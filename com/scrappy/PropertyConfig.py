from configparser import ConfigParser


def initialize():
    config = ConfigParser()
    config.read("config.properties")
    return config


def getFolderPath():
    config = initialize()
    return config.get("FolderLocation", "folder.location")


def getDriverPath():
    config = initialize()
    return config.get("seleniumConfig", "selenium.driver.location")
