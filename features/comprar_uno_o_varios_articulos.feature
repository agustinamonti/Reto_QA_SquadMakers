Feature: Comprar uno o varios articulos

Scenario: Verificar homepage
Given El navegador es lanzado
When Se abre la homepage
Then Muestra pagina de login

Scenario: Iniciar sesion
Given Esta disponible la pantalla de login
When Se ingresa usuario y contraseña
And Se hace click en el boton login
Then Muestra pagina de productos

Scenario: Agregar productos al carrito
Given Esta disponible la pantalla de productos 
When Se hace click en el boton Add to cart para agregar una mochila al carrito
And Se hace click en el boton Add to cart para agregar una remera al carrito
And Se hace click en el carrito de compras
Then Muestra la pagina del carrito de compras con los productos seleccionados

Scenario: Completar el checkout con la informacion personal y terminar la compra
Given Esta disponible la pantalla de checkout  
When Se hace click en el boton checkout
And Se ingresa nombre, apellido y codigo postal
And Se hace click en el boton Continue
And Se hace click en el boton Finish
Then Muestra la pagina del checkout:complete