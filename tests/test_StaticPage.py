import time

from selenium.webdriver.common.by import By

from pageObjects.StaticPage import StaticPage
from utilities.BaseClass import BaseClass


class TestStaticPage(BaseClass):

    def test_staticPage(self):
        page = StaticPage(self.driver)
        page.getOnStaticPage().click()

        pageheader = page.getPageHeader().text
        assert "STATISTICS" == pageheader

        formDateLabel = page.getformDateLabel().text
        assert "From Date" in formDateLabel
        #page.getformDate().send_keys("2024-03-20")
        page.getformDate().click()
        self.selectCalenderToDate(2)
        page.getformDateIMG().is_displayed()

        toDateLabel = page.getToDateLabel().text
        assert "To Date" in toDateLabel
        #page.getToDate().send_keys("2024-03-22")
        page.getToDate().click()
        self.selectCalenderToDate(20)
        page.getToDateIMG().is_displayed()

        categoriesText = page.getCategories().text
        assert "Categories" in categoriesText
        self.selectOptionByText(page.getSelectCategories(),"Monthly Statistics Summary")

        page.getTextSearch().is_displayed()
        page.getTextSearch().send_keys("Free Text")
        time.sleep(3)




