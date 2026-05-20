"""nombres = ["Ana","Juan","Ana","Pedro","Juan"]
print(len(set(nombres)))"""

producto = {"nombre": "leche", "precio": 1200, "stock": 10}
producto["precio"] *= 1.1
producto["stock"] -= 2
print(f"producto, {producto['nombre']}, precio actualizado, {producto['precio']}, stock, {producto["stock"]}")