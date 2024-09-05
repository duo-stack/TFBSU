# 若不引入 logging，读取配置文件中的 level 会报错
import logging

from datetime import datetime
from logging import getLogger, Formatter, StreamHandler
from logging.handlers import TimedRotatingFileHandler
from os import mkdir, listdir
from os.path import abspath, dirname, join, exists, isdir, getctime
from shutil import rmtree

from Config.config import config_log, config_screen

_home = abspath(dirname(dirname(__file__)))

_name = config_log["name"]
_folder = config_log["folder"]
_file = join(_home, _folder, _name)

_level = eval(config_log["level"])
_format = config_log["format"]
_date_format = config_log["date_format"]

_screen_path = join(_home, _folder, config_screen["folder"])


def log_init():
    """
    初始化日志。
    """
    if not exists(_folder):
        mkdir(_folder)
    logger = getLogger(config_log["module"])
    logger.setLevel(_level)
    formatter = Formatter(_format)

    handler = TimedRotatingFileHandler(
        filename=_file, when=config_log["when"],
        interval=eval(config_log["interval"]),
        backupCount=eval(config_log["backup"]),
        atTime=config_log["attime"]
    )
    handler.setLevel(_level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    console = StreamHandler()
    console.setLevel(_level)
    console.setFormatter(formatter)
    logger.addHandler(console)


def delete_old_folders():
    """
    删除较早的截图文件夹。
    """
    if isdir(_screen_path):
        current_time = datetime.now()
        for folder in listdir(_screen_path):
            folder_path = join(_screen_path, folder)
            if isdir(folder_path):
                creation_time = datetime.fromtimestamp(getctime(folder_path))
                time_difference = current_time - creation_time
                if time_difference.days > eval(config_screen["backup"]):
                    rmtree(folder_path)
