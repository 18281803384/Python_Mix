from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import warnings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

warnings.filterwarnings("ignore", category=DeprecationWarning)
ACCOUNT = '18281803384'
PASSWORD = 'qishi5201314'


class CrackGeetest:
    def __init__(self):
        self.url = 'https://www.pingan.com/official/login/' # 请求地址
        self.s = Service('C:\Program Files\Google\Chrome\Application/chromedriver.exe')  # Service传参,取消掉警告提示
        self.browser = webdriver.Chrome(service=self.s) # 实例化一个浏览器对象
        self.browser.maximize_window()  # 设置窗口为最大化
        self.wait = WebDriverWait(self.browser, 20) # 元素等待
        self.account = ACCOUNT
        self.password = PASSWORD

    def get_browser(self):
        """
        跳转请求地址页面
        """
        self.browser.get(self.url)

    def get_account(self):
        """
        填写初始账号密码
        """
        self.wait.until(EC.presence_of_element_located((By.ID, 'password-account'))).send_keys(self.account)
        self.wait.until(EC.presence_of_element_located((By.ID, 'password-pwd'))).send_keys(self.password)

    def get_geetest_button(self):
        """
        获取初始验证按钮
        """
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'login-protocol-label'))).click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_radar_tip_content'))).click()


if __name__ == "__main__":
    Plar_test = CrackGeetest()
    # 1.跳转请求地址页面
    Plar_test.get_browser()
    # 2.填写初始账号密码
    Plar_test.get_account()
    # 3.获取初始验证按钮
    Plar_test.get_geetest_button()
    # 4.太难了、还没有找到解决办法


