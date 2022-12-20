from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

@given("El navegador es lanzado")
def load_browser(context):
    context.driver = webdriver.Chrome(executable_path= r"C:\chromedriver_win32\chromedriver.exe")
    time.sleep(2)

@when("Se abre la homepage")
def load_login(context):
    context.driver.get("http://www.saucedemo.com")
    time.sleep(2)

# Para verificar que es la página de login se verifica la existencia del botón cuyo id es "login-button"
@then("Muestra pagina de login")
def verify_login_button(context):
    verify_exist(context, "id", "login-button")

def verify_exist(context, property, idName):
    try:
        context.driver.find_element(property, idName)
    except NoSuchElementException:
        return False
    return True
