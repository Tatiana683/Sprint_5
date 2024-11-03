from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import Constants
from conftest import driver

class TestAuthorization:
    def test_login_on_main_page(self, driver):
        driver.get(Constants.url_main_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_LOGIN_ON_MAIN_PAGE)))
        driver.find_element(*TestLocators.BUTTON_LOGIN_ON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.LOGIN_INPUT_FIELD_LOGIN).send_keys(Constants.login)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_LOGIN).send_keys(Constants.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_PROFILE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_CREATE_ORDER)))
        assert "Оформить заказ" in driver.find_element(*TestLocators.BUTTON_CREATE_ORDER).text

    def test_login_button_personal_account(self, driver):
        driver.get(Constants.url_main_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.LOGIN_INPUT_FIELD_LOGIN).send_keys(Constants.login)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_LOGIN).send_keys(Constants.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_PROFILE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_CREATE_ORDER)))
        assert "Оформить заказ" in driver.find_element(*TestLocators.BUTTON_CREATE_ORDER).text

    def test_login_from_registration_page(self, driver):
        driver.get(Constants.url_registration)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.NAME_INPUT_FIELD_CREATE)))
        driver.find_element(*TestLocators.LINK_AUTHORIZATION_PAGE).click()
        driver.find_element(*TestLocators.LOGIN_INPUT_FIELD_LOGIN).send_keys(Constants.login)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_LOGIN).send_keys(Constants.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_PROFILE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_CREATE_ORDER)))
        assert "Оформить заказ" in driver.find_element(*TestLocators.BUTTON_CREATE_ORDER).text

    def test_login_from_fogot_password_page(self, driver):
        driver.get(Constants.url_fogot_password)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.LOGIN_INPUT_FIELD_RESTORE)))
        driver.find_element(*TestLocators.LINK_AUTHORIZATION_PAGE).click()
        driver.find_element(*TestLocators.LOGIN_INPUT_FIELD_LOGIN).send_keys(Constants.login)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_LOGIN).send_keys(Constants.password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_PROFILE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_CREATE_ORDER)))
        assert "Оформить заказ" in driver.find_element(*TestLocators.BUTTON_CREATE_ORDER).text
