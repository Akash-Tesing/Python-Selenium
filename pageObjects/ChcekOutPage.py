from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver


    cardTitles = (By.XPATH, "//div[@class='card h-100']")
    checkOut = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitles)

    def getCheckOut(self):

         self.driver.find_element(*CheckOutPage.checkOut).click()
         confirmPage = ConfirmPage(self.driver)
         return confirmPage




