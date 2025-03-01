# import pytest
# from selenium import webdriver
# from pageObjects.LoginPage import LoginPage
# from testCases.conftest import setup
#
#
# class test_001_Login:
#     baseURL = "https://admin-ptm-panel.pay2me.co/login"
#     username = "----"
#     password = "----"
#
#
#     def test_homepageTite(self,setup):
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         act_title = self.driver.title
#         self.driver.close()
#         if act_title == "PayToMe Admin":
#             assert True
#         else:
#             assert False
#
#     def test_login(self,setup):
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.lp=LoginPage(self.driver)
#         self.lp.setUsername(self.username)
#         self.lp.setPaswword(self.password)
#         self.lp.clickLogin()
#         act_title = self.driver.title
#         self.driver.close()
#         if act_title=="PayToMe Admin":
#             assert True
#         else:
#             assert False


# import pytest
# from selenium import webdriver
# from pageObjects.LoginPage import LoginPage
# from testCases.conftest import setup
#
#
#
# class Test_001_Login:
#     baseURL = "https://admin-ptm-panel.pay2me.co/login"
#     username = "-------"
#     password = "------------"
#
#     def test_homepageTitle(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         act_title = self.driver.title
#         assert act_title == "PayToMe Admin"  # Direct assertion instead of if/else
#
#     def test_login(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.lp = LoginPage(self.driver)
#         self.lp.setUsername(self.username)
#         self.lp.setPassword(self.password)  # Corrected method name
#         self.lp.clickLogin()
#         act_title = self.driver.title
#         assert act_title == "PayToMe Admin"  # Direct assertion instead of if/else
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup


class Test_001_Login:
    baseURL = "https://admin-ptm-panel.pay2me.co/login"
    username = "----"
    password = "----"

    def test_homepageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        assert act_title == "PayToMe Admin"

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)  # Using wait in this method
        self.lp.setPassword(self.password)  # Using wait in this method
        self.lp.clickLogin()  # Using wait in this method
        act_title = self.driver.title
        assert act_title == "PayToMe Admin"
