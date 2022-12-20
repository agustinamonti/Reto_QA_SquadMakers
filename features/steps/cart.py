from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from features.steps.homepage import *
from features.steps.login import *


@given("Esta disponible la pantalla de productos")
def verify_products_page(context):
    verify_login(context)
    complete_username_password(context)
    click_login(context)
    product_page(context)
    time.sleep(2)

@when("Se hace click en el boton Add to cart para agregar una mochila al carrito")
def add_backpack(context):
    context.driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    time.sleep(2)

@when("Se hace click en el boton Add to cart para agregar una remera al carrito")
def add_tshirt(context):
    context.driver.find_element("id", "add-to-cart-sauce-labs-bolt-t-shirt").click()
    time.sleep(2)

@when("Se hace click en el carrito de compras")
def click_cart(context):
    context.driver.find_element("id", "shopping_cart_container").click()
    time.sleep(2)

@then("Muestra la pagina del carrito de compras con los productos seleccionados")
def verify_checkout(context):
    verify_exist(context, By.CLASS_NAME, "cart_item")
    time.sleep(2)
