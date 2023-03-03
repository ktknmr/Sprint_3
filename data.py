# урлы сайта
urls = {
    'main_page': 'https://stellarburgers.nomoreparties.site/',
    'login_page': 'https://stellarburgers.nomoreparties.site/login',
    'account_page': 'https://stellarburgers.nomoreparties.site/account/profile'
}

# данные для авторизации/регистрации
login_data = {
    'name': 'Maria',
    'email': 'mariakotkina6367@yandex.ru',
    'password': '123456',
    'bad_password': '12345',
    'old_email': 'mariakotkina6350@yandex.ru'
}

# xpath для кнопок
xpath_buttons = {
    'Войти в аккаунт': ".//button[text()='Войти в аккаунт']",
    'Войти': ".//button[text()='Войти']",
    'Личный Кабинет': ".//p[text()='Личный Кабинет']/parent::a",
    'Конструктор': ".//p[text()='Конструктор']/parent::a"
}

# xpath для уведомлений об ошибках
xpath_alerts = {
    'Некорректный пароль': ".//p[text()='Некорректный пароль']"
}

# xpath для данных в полях
xpath_inputs = {
    'Email': ".//label[text()='Email']/parent::div/input",
    'Имя в ЛК': f".//input[@value='{login_data['name']}']"
}

# xpath для ссылок
xpath_links = {
    'Войти': ".//a[text()='Войти']",
    'Восстановить пароль': ".//a[text()='Восстановить пароль']",
    'Зарегистрироваться': ".//button[text()='Зарегистрироваться']",
    'Лого': ".//div[@class='AppHeader_header__logo__2D0X2']/a",
    'Выход': ".//button[text()='Выход']",
    'Соусы': ".//span[text()='Соусы']",
    'Булки': ".//span[text()='Булки']",
    'Начинки': ".//span[text()='Начинки']",
    'Флюоресцентная булка R2-D3': ".//p[text()='Флюоресцентная булка R2-D3']",
    'Соус Spicy-X': ".//p[text()='Соус Spicy-X']",
    'Говяжий метеорит (отбивная)': ".//p[text()='Говяжий метеорит (отбивная)']"
}
