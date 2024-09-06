from configparser import ConfigParser
from os.path import dirname, join, isfile

_dir = dirname(__file__)
_file = join(_dir, "config.ini")

_parser = ConfigParser()

config = {}

if isfile(_file):
    try:
        _parser.read(_file, encoding="UTF-8")
        d = _parser.sections()
        for k in d:
            config[k] = dict(_parser.items(k))
    except OSError:
        raise ValueError(f"Read Common file failed: {OSError}")

config_info = config["info"]
config_log = config["log"]
config_screen = config["screen"]
config_email = config["email"]
