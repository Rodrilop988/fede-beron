from models.bebida import Bebida
from models.snack import Snack
from negocio.kiosco import Kiosco
from negocio.servicio_ventas import ServicioVentas
from models.postre import Postre



def main():
    kiosco = Kiosco("Mi Kiosquito")
    ventas = ServicioVentas(kiosco.inventario)

    coca = Bebida("Coca-Cola", 2.5, False)
    vino = Bebida("Vino Toro", 4.0, True)
    papas = Snack("Papas Fritas", 1.5, True)
    chocolate = Snack("Chocolate Milka", 2.0, False)
    postre = Postre("Tarta de frutilla", 3.5, True)

    kiosco.agregar_producto(coca)
    kiosco.agregar_producto(vino)
    kiosco.agregar_producto(papas)
    kiosco.agregar_producto(chocolate)
    kiosco.agregar_producto(postre)

    kiosco.mostrar_productos()

    ventas.vender("Coca-Cola")
    kiosco.mostrar_productos()



if __name__ == "__main__":
    main()
