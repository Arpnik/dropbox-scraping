from configparser import ConfigParser


def initialize():
    config = ConfigParser()
    config.read("config.properties")
    return config


def get_folder_path():
    config = initialize()
    return config.get("FolderLocation", "folder.location")


def get_web_driver_path():
    config = initialize()
    return config.get("seleniumConfig", "selenium.driver.location")
