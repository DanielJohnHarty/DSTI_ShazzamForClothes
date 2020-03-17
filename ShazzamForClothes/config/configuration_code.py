import os
import configparser

# Hardcoded path to the file with all the credentials
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.ini")


def get_config_parser(config_file=CONFIG_FILE):
    # ConfigParser to read config.ini
    Config = configparser.ConfigParser()
    Config.read(config_file)
    return Config


# Used through teh package to retrive credentials
LOADED_CONFIG = get_config_parser()
