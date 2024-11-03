from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import Constants
from conftest import driver

class TestTransitionsInConstructor:
    def test_transitions_in_section(self, driver):
        driver.get(Constants.url_main_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_LOGIN_ON_MAIN_PAGE)))
        driver.find_element(*TestLocators.BUTTON_LOGIN_ON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.LOGIN_INPUT_FIELD_LOGIN).send_keys(Constants.login)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_LOGIN).send_keys(Constants.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_PROFILE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_CREATE_ORDER)))
        driver.find_element(*TestLocators.SAUCE_SECTION).click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(*TestLocators.ACTIVE_SAUSE).get_attribute('class')
        driver.find_element(*TestLocators.FILLING_SECTION).click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(*TestLocators.ACTIVE_FILLING).get_attribute('class')
        driver.find_element(*TestLocators.BREAD_SECTION).click()
        assert "tab_tab_type_current__2BEPc" in driver.find_element(*TestLocators.ACTIVE_BREAD).get_attribute('class')
