import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        #log = self.getLogger()

        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["Name"])
        homepage.getEmail().send_keys(getData["Email"])

        # for that we create customise method in utilities--> BaseClass
        # sel = Select(homepage.getGender())
        # sel.select_by_visible_text("Male")

        self.selectOptionByText(homepage.getGender(), getData["Gender"])
        homepage.getSubmit().click()

        alertText = homepage.getSuccess().text
       # log("Get success MSG : "+ alertText)
        assert "Success" in alertText

        self.driver.refresh()

    @pytest.fixture(params= HomePageData.test_HomePage_Data)
    def getData(self,request):
        return request.param