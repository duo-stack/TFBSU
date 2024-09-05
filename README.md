# TFBSU
**Test Framework Base on Selenium and Unittest**

## 简介
这是一个基于 Selenium 和 unittest 的使用 Python 语言开发的测试框架，用于自动化测试 Web 应用。

## 功能模块
- Common：公共模块。包含一些常用的方法，如日志、邮件等。
- Config：配置模块。包含一些配置信息，如日志配置、邮箱服务器配置等。
- Base：基类。包含一些常用的方法，如打开浏览器、关闭浏览器、点击、输入等。
- Page：页面类。用于封装页面元素和操作。
- Api：接口类。用于封装 API 请求。
- Flow：流程类。用于封装页面的一些固定操作流程，如登录操作。
- Case：测试用例类。用于编写具体的测试用例。
- Log：日志输出目录。
- Report：测试报告输出目录。
- Static：静态资源目录。

## Python版本
Python 3.8.5

## 依赖
- BeautifulReport==0.1.3
- ddddocr==1.4.7
- ddt==1.7.2
- openpyxl==3.1.5
- pandas==2.0.3
- requests==2.31.0
- selenium==4.8.2

## 注意事项
1. main 文件中已经初始化日志模块，在别的文件中使用日志时，使用以下命令即可。
```python
from logging import getLogger

from Config.config import config_log

_log_module = ".xxx"  # 日志模块名称
_logger = getLogger(config_log["module"] + _log_module)
```

2. 由于 BeautifulReport 库中原本依赖的静态资源文件的 URL 无法访问，所以将静态资源文件下载到本地，并在实例化 BeautifulReport 后修改了配置信息，使其使用本地的静态资源文件。若删除 Static 文件夹，会导致测试报告异常。
