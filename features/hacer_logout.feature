Feature: Hacer logout

Scenario: Desloguearse
Given El usuario está logueado
When Se hace click en el menú de hamburguesa
And Se hace click en Logout
Then Muestra página de login