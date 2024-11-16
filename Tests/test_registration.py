from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import RandomCred
from locators import TestLocators
from data import Constants
from conftest import driver

class TestRegistration:
    def test_correct_registration(self, driver):
        name = RandomCred.generate_name()
        login = RandomCred.generate_login()
        password = RandomCred.generate_password()
        driver.get(Constants.url_registration)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.NAME_INPUT_FIELD_CREATE)))
        driver.find_element(*TestLocators.NAME_INPUT_FIELD_CREATE).send_keys(name)
        driver.find_element(*TestLocators.LOGIN_INPUT_FIELD_CREATE).send_keys(login)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_CREATE).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_CREATE_PROFILE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_LOGIN_PROFILE)))
        driver.find_element(*TestLocators.LOGIN_INPUT_FIELD_LOGIN).send_keys(login)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_LOGIN).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_PROFILE).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_CREATE_ORDER)))
        assert "Оформить заказ" in driver.find_element(*TestLocators.BUTTON_CREATE_ORDER).text

    def test_error_password(self, driver):
        driver.get(Constants.url_registration)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((TestLocators.NAME_INPUT_FIELD_CREATE)))
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD_CREATE).send_keys("111")
        driver.find_element(*TestLocators.BUTTON_CREATE_PROFILE).click()
        assert "Некорректный пароль" == driver.find_element(*TestLocators.TEXT_ERROR_PASSWORD).text
