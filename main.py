import unittest
from os import mkdir
from os.path import abspath, dirname, join, exists
from time import strftime, localtime

from BeautifulReport import BeautifulReport

from Common.compress import compress
from Common.email import Email


test_case_folder = "Case"
report_folder = "Report"
# 修改模板文件路径，原模板文件存在部分显示异常
template = "Static/template/template.html"

_home = abspath(dirname(__file__))
test_case_path = join(_home, test_case_folder)
report_path = join(_home, report_folder)


def format_email_content(result) -> str:
    """
    格式化邮件内容。
    :param result: 测试结果。
    :return: 格式化后的邮件内容。
    """
    content = (f"\n<p>          测试结果汇总信息          </p>\n"
               f"<p> 开始时间：{result['beginTime']}</p>\n"
               f"<p> 运行时间：{result['totalTime']}</p>\n"
               f"<p> 执行用例数：{result['testAll']}</p>\n"
               f"<p> 通过用例数：{result['testPass']}</p>\n"
               f"<p> 失败用例数：{result['testFail']}</p>\n"
               f"<p> 失败用例数：{result['testSkip']}</p>\n")
    return content


def send_email(content, file):
    """
    发送邮件。
    :param content: 邮件内容。
    :param file: 邮件附件。
    :return: None
    """
    title = strftime("%Y-%m-%d %H:%M:%S", localtime()) + "自动化测试报告"
    email = Email(title, content, file)
    email.send()


def get_suite(path=test_case_path, rule="test_*.py"):
    """
    获取测试套件。
    :param path: 测试用例路径。
    :param rule: 测试用例规则。
    :return: 测试套件。
    """
    unittest_suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(path, rule)
    for case in discover:
        unittest_suite.addTest(case)
    return unittest_suite


def run(unittest_suite):
    """
    执行测试套件。
    :param unittest_suite: 测试套件。
    :return: 测试结果。
    """
    if not exists(report_path):
        mkdir(report_path)

    result = BeautifulReport(unittest_suite)
    result.config_tmp_path = join(_home, template)
    now = strftime("%Y%m%d%H%M%S", localtime())
    name = now + "_report.html"
    result.report(filename=name, description="测试报告",
                  report_dir=report_path)
    content = format_email_content(result.fields)
    return name, content


if __name__ == '__main__':
    suite = get_suite()
    report_name, report_content = run(suite)

    # 静态文件无法从url访问，只能下载后访问本地文件
    # 为了维持文件层级关系，保证报告正常显示
    # 因此对报告及静态文件进行打包发送
    compress_file = report_name.split(".")[0] + ".zip"
    compress([f"Report/{report_name}", "Static/css", "Static/js"],
             compress_file)
    send_email(report_content, compress_file)
