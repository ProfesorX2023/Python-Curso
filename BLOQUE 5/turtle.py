import turtle


# Crear un objeto turtle
mi_turtle = turtle.Turtle()

# Dibujar un patrón de estrella sin bucle
mi_turtle.forward(100)  # Primer brazo
mi_turtle.right(144)    # Giro entre brazos
mi_turtle.forward(100)  # Segundo brazo
mi_turtle.right(144)
mi_turtle.forward(100)  # Tercer brazo
mi_turtle.right(144)
mi_turtle.forward(100)  # Cuarto brazo
mi_turtle.right(144)
mi_turtle.forward(100)  # Quinto brazo

# Cerrar la ventana al hacer clic
turtle.exitonclick()