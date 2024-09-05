from selenium.webdriver.common.by import By

image_path = "login"  # 保存截图的文件夹名称

username = By.CSS_SELECTOR, "#username"  # 用户名输入框
username_message = By.CSS_SELECTOR, "#username_message"  # 用户名不符合规则的消息

password = By.CSS_SELECTOR, "#password"  # 密码输入框
password_message = By.CSS_SELECTOR, "#password_message"  # 密码不符合规则的消息

verify_code = By.CSS_SELECTOR, "#theValidateCode"  # 验证码输入框
verify_image = By.CSS_SELECTOR, "#validateImg"  # 验证图
verify_image_path = "D:\\verify_image.png"  # 验证图存储路径

login = By.CSS_SELECTOR, "#loginBtn"  # 登录按钮
