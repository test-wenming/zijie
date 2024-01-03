from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# 创建 WebDriver 对象
driver = webdriver.Chrome()
driver.maximize_window()
# 全局隐式等待
driver.implicitly_wait(20)

# 调用WebDriver 对象的get方法打开飞书网站
driver.get("https://www.feishu.cn/")

# 判断是否有弹窗
popup = driver.find_elements(By.CSS_SELECTOR, ".hc_Popup .hc_Popup-content > div > div > div")
if popup:
    popup[0].click()

# 点击登录
driver.find_elements(By.CSS_SELECTOR, ".ftHeader-content .ftHeader_ExtraButton")[0].click()

# 判断是否有扫码登录页面
code = driver.find_elements(By.CSS_SELECTOR, ".switch-login-mode-box .universe-icon")
if code:
    code[0].click()

# 选择邮箱登录
email = driver.find_element(By.CSS_SELECTOR, ".base-tabs-bar-container div:nth-child(2)")
email.click()

# 输入邮箱号
driver.find_element(By.CSS_SELECTOR, ".ud__input-input-wrap .ud__native-input").clear()
driver.find_element(By.CSS_SELECTOR, ".ud__input-input-wrap .ud__native-input").send_keys("604451714@qq.com")

# 我已阅读并同意
driver.find_element(By.CSS_SELECTOR, ".ud__checkbox__input").click()

# 点击下一步
driver.find_element(By.CSS_SELECTOR, ".step-box__body button").click()
# 等待2秒
sleep(2)

# 输入密码
password = driver.find_element(By.CSS_SELECTOR, ".ud__input-password-input-wrap .ud__native-input")
password.clear()
password.send_keys("@abc123456")

# 点击下一步
driver.find_element(By.CSS_SELECTOR, ".step-box__footer>.ud__button").click()
# 等待2秒
sleep(2)

# 点击9个点
nine = driver.find_element(By.CSS_SELECTOR, "._pp-product-icon")
nine.click()

# 点击消息
driver.find_element(By.CSS_SELECTOR, "._pp_grid_list ul:nth-child(1) li:nth-child(1)").click()

sleep(5)

# 切换到新窗口
windows = driver.window_handles
driver.switch_to.window(windows[-1])

# 刷新页面,以免通讯录总是加载不出
address_book = driver.find_elements(By.CSS_SELECTOR, ".nav-items .larkc-badge")
if len(address_book) == 5:
    driver.refresh()

# 强制点击通讯录
driver.execute_script("arguments[0].click();", address_book[4])

# 点击外部联系人
external_contacts = driver.find_elements(By.CSS_SELECTOR, ".contactPageNav_item")
if len(external_contacts) == 4 or external_contacts[1].text != "外部联系人":
    sleep(3)
driver.find_elements(By.CSS_SELECTOR, ".contactPageNav_item")[1].click()

# 点击tester2用户
tester2 = driver.find_element(By.CSS_SELECTOR, ".avatarMsgCard_body")
tester2.click()

# 输入内容并发送消息
send_message = driver.find_element(By.CSS_SELECTOR, ".larkc-usercard__footer__input")
send_message.send_keys("你好呀，这是自动化测试", Keys.ENTER)
sleep(5)
driver.quit()


