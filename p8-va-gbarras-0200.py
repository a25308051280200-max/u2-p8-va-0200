import matplotlib.pyplot as plt
import numpy as np 
# Alejandra Rivera Valenzuela NC 0200

diasX = ["Lun", "Mar", "Mie", "Jue", "Vie"]
califa_va_y = [5, 6, 3, 8, 10]

plt.bar(diasX, califa_va_y)
plt.title("Califas en VA de Alejandra Rivera Valenzuela NC 0200")
plt.xlabel("Dias semana habilitados")
plt.ylabel("Calificaciones en VA")
plt.grid()
plt.show()

