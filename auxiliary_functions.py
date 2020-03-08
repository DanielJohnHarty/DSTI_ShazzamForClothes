import configparser


def get_config_parser(config_file="config.ini"):
    # ConfigParser to read config.ini
    Config = configparser.ConfigParser()
    Config.read(config_file)
    return Config


CONFIG_PARSER = get_config_parser()
