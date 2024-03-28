import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


from pageObjects.ChcekOutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        #log = self.getLogger()
        homepage = HomePage(self.driver)
        #homepage.shopItems().click() #no need here

        # for checkOutPage we create a object into shopItems Method in HomePage class
        checkOutPage = HomePage.shopItems(self)

        #checkOutPage = CheckOutPage(self.driver) no need to create object
        products = checkOutPage.getCardTitle()

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH,"div/button").click()

        # checkOutPage.getCheckOut().click() #no need here
        # for ConfirmPage we create a object into getCheckOut(self) Method in CheckOutPage class
        #confirmPage = ConfirmPage(self.driver)

        confirmPage = CheckOutPage.getCheckOut(self)

        confirmPage.getCheckOut().click()
        confirmPage.getSearchCountry().send_keys("Ind")
        self.verifyLinkPresence("India")
        confirmPage.getSelectIndia().click()
        confirmPage.getSelectCheckBox().click()
        confirmPage.getClickOnPurchase().click()

        successText = confirmPage.getSuccessMSG().text
        #log.info("Confirm MSG IS" + " "+ successText)
        assert "Success" in successText


