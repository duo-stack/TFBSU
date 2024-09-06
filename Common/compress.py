import zipfile
from logging import getLogger
from os import walk
from os.path import isfile, isdir, join

from Config.config import config_log

_log_module = ".compress"  # 日志模块名称
_logger = getLogger(config_log["module"] + _log_module)


def compress(files: list, output_file: str):
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for path in files:
            if isfile(path):
                zipf.write(path)
            elif isdir(path):
                for root, dirs, files in walk(path):
                    for file in files:
                        file_path = join(root, file)
                        zipf.write(file_path)
            else:
                _logger.warning(f"This path is neither a file "
                                f"nor a folder: {path}")
        else:
            _logger.info(f"Successfully compressed files to {output_file}")
