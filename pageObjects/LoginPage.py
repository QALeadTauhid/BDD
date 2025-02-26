
#
# class LoginPage:
#     testbox_username_xpath = "(//input[@placeholder='johndoe'])"
#     testbox_password_xpath = "(//input[@id='auth-login-v2-password'])"
#     button_login_xpath = "(//button[normalize-space()='Login'])"
#     button_logout_xpath = "//button[normalize-space()='LOG OUT']"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def setUsername(self, username):
#         self.driver.find_element_by_id(self.testbox_username_xpath).clear()
#         self.driver.find_element_by_id(self.testbox_username_xpath).send_keys(username)
#
#     def setPaswword(self, password):
#         self.driver.find_element_by_id(self.testbox_password_xpath).clear()
#         self.driver.find_element_by_id(self.testbox_password_xpath).send_keys(password)
#
#
#     def clickLogin(self):
#         self.driver.find_element_by_id(self.button_login_xpath).click()
#
#     def clickLogout(self):
#         self.driver.find_element_by_id(self.button_logout_xpath).click()
#
#
#
# from selenium.webdriver.common.by import By
#
# class LoginPage:
#     testbox_username_xpath = "//input[contains(@placeholder, 'johndoe')]"
#     testbox_password_xpath = "(//input[@id='auth-login-v2-password'])"
#     button_login_xpath = "(//button[normalize-space()='Login'])"
#     button_logout_xpath = "//button[normalize-space()='LOG OUT']"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def setUsername(self, username):
#         # self.driver.find_element(By.XPATH, self.testbox_username_xpath).clear()
#         self.driver.find_element(By.XPATH, self.testbox_username_xpath).send_keys(username)
#
#     def setPassword(self, password):  # Fixed the typo here from `setPaswword` to `setPassword`
#         # self.driver.find_element(By.XPATH, self.testbox_password_xpath).clear()
#         self.driver.find_element(By.XPATH, self.testbox_password_xpath).send_keys(password)
#
#     def clickLogin(self):
#         self.driver.find_element(By.XPATH, self.button_login_xpath).click()
#
#     def clickLogout(self):
#         self.driver.find_element(By.XPATH, self.button_logout_xpath).click()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    testbox_username_xpath = "(//input[@placeholder='johndoe'])"
    testbox_password_xpath = "(//input[@id='auth-login-v2-password'])"
    button_login_xpath = "(//button[normalize-space()='Login'])"
    button_logout_xpath = "//button[normalize-space()='LOG OUT']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        # Wait until the username field is visible
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.testbox_username_xpath))
        )
        username_field.clear()
        username_field.send_keys(username)

    def setPassword(self, password):
        # Wait until the password field is visible
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.testbox_password_xpath))
        )
        password_field.clear()
        password_field.send_keys(password)

    def clickLogin(self):
        # Wait until the login button is clickable
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
        )
        login_button.click()

    def clickLogout(self):
        # Wait until the logout button is clickable
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_logout_xpath))
        )
        logout_button.click()
