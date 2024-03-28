from selenium.webdriver.common.by import By

from pageObjects.ChcekOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.XPATH, "(//input[@name='name'])[1]")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    gender = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMSG = (By.CLASS_NAME,"alert-success")



    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccess(self):
        return self.driver.find_element(*HomePage.successMSG)


