from selenium.webdriver.common.by import By


class StaticPage:

    def __init__(self, driver):
        self.driver = driver

    clickOnStatics = (By.XPATH, "//span[text()='Statistics ']")
    pageHeader = (By.XPATH, "//header[@class='componentHeader']/h1")

    formDateLabel = (By.XPATH, "//label[@for='FromDate']")
    formDate = (By.XPATH, "//input[@id='FromDate']")
    formDateIMG = (By.XPATH, "(//img[@class='ui-datepicker-trigger'])[1]")

    toDateLabel = (By.XPATH, "//label[@for='ToDate']")
    toDate = (By.XPATH, "//input[@id='ToDate']")
    toDateIMG = (By.XPATH, "(//img[@class='ui-datepicker-trigger'])[2]")

    categories = (By.XPATH, "//label[@for='cnscategoryId']")
    selectCategories = (By.XPATH, "//select[@id='cnscategoryId']")

    textSearch = (By.XPATH, "//input[@id='freeTextId']")

    def getOnStaticPage(self):
        return self.driver.find_element(*StaticPage.clickOnStatics)

    def getPageHeader(self):
        return self.driver.find_element(*StaticPage.pageHeader)

    def getformDateLabel(self):
        return self.driver.find_element(*StaticPage.formDateLabel)

    def getformDate(self):
        return self.driver.find_element(*StaticPage.formDate)

    def getformDateIMG(self):
        return self.driver.find_element(*StaticPage.formDateIMG)

    def getToDateLabel(self):
        return self.driver.find_element(*StaticPage.toDateLabel)

    def getToDate(self):
        return self.driver.find_element(*StaticPage.toDate)

    def getToDateIMG(self):
        return self.driver.find_element(*StaticPage.toDateIMG)

    def getCategories(self):
        return self.driver.find_element(*StaticPage.categories)

    def getSelectCategories(self):
        return self.driver.find_element(*StaticPage.selectCategories)

    def getTextSearch(self):
        return self.driver.find_element(*StaticPage.textSearch)
