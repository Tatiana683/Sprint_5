from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import Constants
from conftest import driver

class TestGoToConstructor:
    def test_go_to_constructor_button(self, driver):
        driver.get(Constants.url_main_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_LOGIN_ON_MAIN_PAGE)))
        driver.find_element(*TestLocators.BUTTON_LOGIN_ON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.LOGIN_INPUT_FIELD_LOGIN).send_keys(Constants.login)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_LOGIN).send_keys(Constants.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_LOGOUT_PERSONAL_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_HEADER_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_CREATE_ORDER)))
        assert "Оформить заказ" in driver.find_element(*TestLocators.BUTTON_CREATE_ORDER).text

    def test_go_to_constructor_from_label(self, driver):
        driver.get(Constants.url_main_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_LOGIN_ON_MAIN_PAGE)))
        driver.find_element(*TestLocators.BUTTON_LOGIN_ON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.LOGIN_INPUT_FIELD_LOGIN).send_keys(Constants.login)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_LOGIN).send_keys(Constants.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_LOGOUT_PERSONAL_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_HEADER_LABEL).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_CREATE_ORDER)))
        assert "Оформить заказ" in driver.find_element(*TestLocators.BUTTON_CREATE_ORDER).text