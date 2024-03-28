from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    checkOut1 = (By.XPATH, "//button[@class='btn btn-success']")
    searchCountry = (By.ID, "country")
    selectIndia = (By.LINK_TEXT, "India")
    selectCheckBox = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")
    clickOnPurchase = (By.CSS_SELECTOR, "input[type='submit']")
    successMSG = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def getCheckOut(self):
        return self.driver.find_element(*ConfirmPage.checkOut1)

    def getSearchCountry(self):
        return self.driver.find_element(*ConfirmPage.searchCountry)

    def getSelectIndia(self):
        return self.driver.find_element(*ConfirmPage.selectIndia)

    def getSelectCheckBox(self):
        return self.driver.find_element(*ConfirmPage.selectCheckBox)

    def getClickOnPurchase(self):
        return self.driver.find_element(*ConfirmPage.clickOnPurchase)

    def getSuccessMSG(self):
        return self.driver.find_element(*ConfirmPage.successMSG)




