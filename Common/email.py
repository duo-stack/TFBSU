from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from logging import getLogger
from os.path import isfile, getsize, basename
from smtplib import SMTP_SSL, SMTPException

from Config.config import config_log, config_email

_log_module = ".email"  # 日志模块名称
_logger = getLogger(config_log["module"] + _log_module)


class Email:
    def __init__(self, subject, content=None, attachment=None):
        self.subject = subject
        self.content = content
        self.attachment = attachment
        self.message = MIMEMultipart()
        self._message_init()

    def _message_init(self):
        if self.subject:
            self.message["subject"] = Header(self.subject, "utf-8")
        else:
            raise ValueError("Invalid subject")

        self.message["from"] = config_email["sender"]
        self.message["to"] = config_email["receiver"]

        if self.content:
            self.message.attach(MIMEText(self.content, "html",
                                         "utf-8"))

        if self.attachment:
            if isinstance(self.attachment, str):
                self._attach(self.attachment)
            elif isinstance(self.attachment, list):
                count = 0
                for file in self.attachment:
                    if count <= eval(config_email["count"]):
                        self._attach(file)
                        count += 1
                    else:
                        _logger.warning(f"Attachments is more "
                                       f"than {config_email['count']}")
                        break
            else:
                _logger.warning("Invalid attachment")

    def _attach(self, file):
        if (isfile(file) and getsize(file) <=
                eval(config_email["size"]) * 1024 * 1024):
            attach = MIMEApplication(open(file, "rb").read())
            attach.add_header("Content-Disposition",
                              "attachment",
                              filename=basename(file))
            attach["Content-Type"] = "application/octet-stream"
            self.message.attach(attach)
        else:
            _logger.error(f"The attachment is not exist "
                         f"or more than {config_email['size']}M: {file}")

    def send(self):
        smtp = SMTP_SSL(config_email["host"], int(config_email["port"]))
        try:
            smtp.login(config_email["username"], config_email["password"])
            smtp.sendmail(config_email["sender"],
                          config_email["receiver"],
                          self.message.as_string())
            _logger.info("Email sent successfully")
        except SMTPException as e:
            _logger.error(f"Failed to send email: {e}")
        finally:
            smtp.quit()
