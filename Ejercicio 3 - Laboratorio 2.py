import math

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

solucion_cuadratica = lambda a,b,c: (
        (-b + math.sqrt(b**2 - 4*a*c))/(2*a),
        (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    )
    
solucion1,solucion2 = solucion_cuadratica(a,b,c)

print(f"La primera solucion X1 es: {solucion1}")
print(f"La segunda solucion X2 es: {solucion2}")