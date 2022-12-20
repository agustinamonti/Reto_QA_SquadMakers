from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from features.steps.homepage import *
from features.steps.login import *

@given("El usuario está logueado")
def verify_logged_in_user(context):
    verify_login(context)
    complete_username_password(context)
    click_login(context)
    verify_exist(context, By.CLASS_NAME, "app_logo")
    time.sleep(2)

@when("Se hace click en el menú de hamburguesa")
def click_burger_menu(context):
    context.driver.find_element("id", "react-burger-menu-btn").click()
    time.sleep(2)

@when("Se hace click en Logout")
def click_logout_item(context):
    context.driver.find_element("id", "logout_sidebar_link").click()
    time.sleep(2)

@then("Muestra página de login")
def verify_login_page(context):
    verify_login_button(context)
    time.sleep(2)