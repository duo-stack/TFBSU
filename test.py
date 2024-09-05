# 用于快速测试某些操作。
from logging import getLogger

from Config.config import config, config_log
from Common.log import log_init

print(config)

log_init()
logger = getLogger(config_log["module"] + ".test")
logger.info("log test")
