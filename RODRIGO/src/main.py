from models.producto_builder import ProductoBuilder
from negocio.kiosco import Kiosco
from negocio.servicio_ventas import ServicioVentas

def main():
    kiosco = Kiosco("Mi Kiosquito")
    ventas = ServicioVentas(kiosco.inventario)

    # 🧱 Construcción paso a paso con Builder
    builder = ProductoBuilder()

    coca = builder.set_nombre("Coca-Cola").set_precio(2.5).set_tipo("bebida").set_extra(False).build()
    vino = builder.set_nombre("Vino Toro").set_precio(4.0).set_tipo("bebida").set_extra(True).build()
    papas = builder.set_nombre("Papas Fritas").set_precio(1.5).set_tipo("snack").set_extra(True).build()
    postre = builder.set_nombre("Tarta de frutilla").set_precio(3.5).set_tipo("postre").set_extra(True).build()

    kiosco.agregar_producto(coca)
    kiosco.agregar_producto(vino)
    kiosco.agregar_producto(papas)
    kiosco.agregar_producto(postre)

    kiosco.mostrar_productos()
    ventas.vender("Coca-Cola")

if __name__ == "__main__":
    main()
