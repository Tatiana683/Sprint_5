from selenium.webdriver.common.by import By

class TestLocators:
    NAME_INPUT_FIELD_CREATE = By.XPATH, ".//fieldset[1]//input" # Поле ввода имени на странице регистрации
    LOGIN_INPUT_FIELD_CREATE = By.XPATH, ".//fieldset[2]//input" # Поле ввода логина на странице регистрации
    PASSWORD_INPUT_FIELD_CREATE = By.XPATH, ".//fieldset[3]//input" # Поле ввода пароля на странице регистрации
    BUTTON_CREATE_PROFILE = By.XPATH, ".//button[text()='Зарегистрироваться']" # Кнопка создания профиля на странице регистрации
    LOGIN_INPUT_FIELD_LOGIN = By.XPATH, "//fieldset[1]//input" # Поле ввода логина на странице авторизации
    PASSWORD_INPUT_FIELD_LOGIN = By.XPATH, "//fieldset[2]//input" # Поле ввода пароля на странице авторизации
    BUTTON_LOGIN_PROFILE = By.XPATH, ".//button[text()='Войти']" # Кнопка входа на странице авторизации
    BUTTON_CREATE_ORDER = By.XPATH, ".//button[text()='Оформить заказ']" # Кнопка создания заказа на странице конструктора
    TEXT_ERROR_PASSWORD = By.XPATH, ".//p[text()='Некорректный пароль']" # Текст ошибки при вводе некорректного пароля
    BUTTON_LOGIN_ON_MAIN_PAGE = By.XPATH, ".//button[text()='Войти в аккаунт']" # кнопка входа в профиль на странице конструктора
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, ".//p[text()='Личный Кабинет']" # Кнопка входа в кабинет на странице конструктора
    LINK_AUTHORIZATION_PAGE = By.CLASS_NAME, "Auth_link__1fOlj" # Гипертекст перехода на страницу входа
    LOGIN_INPUT_FIELD_RESTORE = By.XPATH, ".//input" # Поле ввода адреса почты на странице восстановления доступа
    BUTTON_LOGOUT_PERSONAL_ACCOUNT = By.XPATH, ".//button[text()='Выход']" # Кнопка выхода из профиля
    BUTTON_HEADER_CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']" # Кнопка в хеддере "Конструктор"
    BUTTON_HEADER_LABEL = By.CLASS_NAME, "AppHeader_header__logo__2D0X2" # Лого "Stellar Burgers" в хеддере
    BREAD_SECTION = By.XPATH, ".//div/span[text()='Булки']" # Таб "Булки" на странице "Конструктор"
    SAUCE_SECTION = By.XPATH, ".//div/span[text()='Соусы']" # Таб "Соусы" на странице "Конструктор"
    FILLING_SECTION = By.XPATH, ".//div/span[text()='Начинки']" # Таб "Начинки" на странице "Конструктор"
    ACTIVE_BREAD = By.XPATH, ".//*[@id='root']/div/main/section[1]/div[1]/div[1]" # Изменяемый атрибут класса, когда таб "Булки" активен
    ACTIVE_SAUSE = By.XPATH, ".//*[@id='root']/div/main/section[1]/div[1]/div[2]" # # Изменяемый атрибут класса, когда таб "Соусы" активен
    ACTIVE_FILLING = By.XPATH, ".//*[@id='root']/div/main/section[1]/div[1]/div[3]" # # Изменяемый атрибут класса, когда таб "Начинки" активен

