from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from features.steps.homepage import *
from features.steps.login import *
from features.steps.cart import *

@given("Esta disponible la pantalla de checkout")
def verify_checkout_page(context):
    verify_products_page(context)
    add_backpack(context)
    add_tshirt(context)
    click_cart(context)
    verify_checkout(context)
    time.sleep(2)

@when("Se hace click en el boton checkout")
def click_checkout(context):
    context.driver.find_element("id", "checkout").click()

@when("Se ingresa nombre, apellido y codigo postal")    
def complete_checkout(context):
    context.firstname = context.driver.find_element("id", "first-name")
    context.firstname.send_keys("Agustina")
    time.sleep(1)
    lastname = context.driver.find_element("id", "last-name")
    lastname.send_keys("Monti")
    time.sleep(1)
    postalcode = context.driver.find_element("id", "postal-code")
    postalcode.send_keys("2000")
    time.sleep(2)

@when("Se hace click en el boton Continue")
def click_continue(context):
    context.driver.find_element("id", "continue").click()
    time.sleep(2)

@when("Se hace click en el boton Finish")
def click_continue(context):
    context.driver.find_element("id", "finish").click()
    time.sleep(2)

@then("Muestra la pagina del checkout:complete")
def verify_checkout_complete_page(context):
    try:
        checkoutname = context.driver.find_element(By.CLASS_NAME, 'title').text
        print(checkoutname)
        if checkoutname.lower() == "checkout: complete!":
            print ("Test passed")
            pass
        else:
            print ("Test failed")  
    except:
        assert False, "Test failed"
