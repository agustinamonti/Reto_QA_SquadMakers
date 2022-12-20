from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from features.steps.homepage import *

@given("Esta disponible la pantalla de login")
def verify_login(context):
    load_browser(context)
    load_login(context)
    verify_login_button(context)
    time.sleep(2)

@when("Se ingresa usuario y contraseña")
def complete_username_password(context):
    username = context.driver.find_element("id", "user-name")
    password = context.driver.find_element("id", "password")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    time.sleep(2)

@when("Se hace click en el boton login")
def click_login(context):
    context.driver.find_element("id", "login-button").click()
   
@then("Muestra pagina de productos")
def product_page(context):
    try:
        my_span = context.driver.find_element(By.CLASS_NAME, 'title').text
        if my_span == "PRODUCTS":
            print ("Test passed")
            pass
        else:
            print ("Test failed")  
    except:
        assert False, "Test failed"
time.sleep(2)  
        
   
