
# 🏪 Proyecto Kiosco POO en Python

Este proyecto simula un kiosco donde se pueden gestionar distintos tipos de productos utilizando **Programación Orientada a Objetos (POO)** en Python.
Incluye la aplicación de los principios **SOLID** y el **patrón de diseño Builder** para construir productos de manera flexible.

---

## 💡 Descripción general

El kiosco permite manejar productos de tipo **Bebida**, **Snack** y **Postre**, cada uno con características específicas.
El sistema utiliza:

* **POO**: herencia, polimorfismo, encapsulamiento y abstracción.
* **SRP**: separa responsabilidades entre el inventario (`Kiosco`) y la venta de productos (`ServicioVentas`).
* **OCP**: se pueden agregar nuevos tipos de productos (como `Postre`) sin modificar las clases existentes.
* **Builder**: se puede construir cualquier producto paso a paso de manera flexible.

---

## ⚙️ Estructura del proyecto

```
src
│
├── main.py
│
├── entidades/
│   ├── bebidas.py
│   ├── postre.py
│   ├── productos_builder.py
│   ├── productos.py
│   ├── snacks.py
│   
│
└── servicios/
    ├── kiosco.py
    ├── servicio_ventas.py
    
```

### 🧩 Carpetas y archivos

* **entidades/** → Clases que representan los productos y el Builder (`ProductoBuilder`).
* **servicio/** → Clases que manejan la lógica del kiosco: inventario y ventas.
* **main.py** → Entrada del programa y ejemplo de construcción de productos con Builder.

---

## 🧱 Principales clases y responsabilidades

### 🔹 `Producto` (abstracta)

Define la estructura básica de un producto: nombre y precio.
Aplica **abstracción** y **encapsulamiento** con getters y setters.

### 🔹 `Bebida`, `Snack`, `Postre`

Heredan de `Producto` (**herencia**) y redefinen `mostrar_info()` (**polimorfismo**) para mostrar sus atributos específicos.

### 🔹 `ProductoBuilder`

Permite construir productos paso a paso sin llamar directamente a los constructores de cada clase, aplicando el **patrón Builder**.

### 🔹 `Kiosco`

Administra el **inventario** del kiosco (cumpliendo **SRP**).

### 🔹 `ServicioVentas`

Se encarga de **vender productos** (también cumple **SRP**).

---

## 🧠 Principios aplicados

| Principio   | Qué significa                                              | Implementación                                                         |
| ----------- | ---------------------------------------------------------- | ---------------------------------------------------------------------- |
| **SRP**     | Cada clase tiene una única responsabilidad                 | `Kiosco` maneja inventario; `ServicioVentas` maneja ventas             |
| **OCP**     | El sistema puede extenderse sin modificar código existente | Se agregó `Postre` sin tocar clases existentes                         |
| **Builder** | Construcción de objetos paso a paso de manera flexible     | `ProductoBuilder` permite crear cualquier producto encadenando métodos |



## 📋 Ejemplo de uso

```text
🛒 Productos del kiosco Mi Kiosquito:
 - Bebida: Coca-Cola - $2.50 (sin alcohol)
 - Bebida: Vino Toro - $4.00 (alcohólica)
 - Snack: Papas Fritas - $1.50 (salado)
 - Postre: Tarta de frutilla - $3.50 (con crema)

✅ Vendido: Coca-Cola por $2.50

🛒 Productos del kiosco Mi Kiosquito:
 - Bebida: Vino Toro - $4.00 (alcohólica)
 - Snack: Papas Fritas - $1.50 (salado)
 - Postre: Tarta de frutilla - $3.50 (con crema)
```







