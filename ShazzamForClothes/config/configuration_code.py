import os
import configparser

# __all__ = ["LOADED_CONFIG", "get_config_parser"]
__all__ = ["LOADED_CONFIG"]


CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.ini")


def get_config_parser(config_file=CONFIG_FILE):
    # ConfigParser to read config.ini
    Config = configparser.ConfigParser()
    Config.read(config_file)
    return Config


LOADED_CONFIG = get_config_parser()
