from django.urls import path
from .views import inicio, registrarme, nosotros, productos, administracion
from .views import usuarios, bodega, ventas, boleta, ingresar, eliminar_usuario
from .views import misdatos, miscompras, salir, carrito, ficha
from .views import cambiar_estado_boleta, poblar, obtener_productos, eliminar_producto_en_bodega, detalle_boleta
from .views import premio, eliminar_producto_en_carrito, agregar_producto_al_carrito, eliminar_producto
from .views import vaciar_carrito, mipassword, cambiar_password, comprar_ahora, nuevo_producto

urlpatterns = [
    path('', inicio, name='inicio'),
    path('ropa', inicio, name='index'),
    path('inicio', inicio, name='inicio'),
    path('registrarme', registrarme, name='registrarme'),
    path('administracion', administracion, name='administracion'),
    path('nosotros', nosotros, name='nosotros'),
    path('productos', productos, name='productos'),
    path('nuevo_producto', nuevo_producto, name='nuevo_producto'),
    path('usuarios', usuarios, name='usuarios'),
    path('eliminar_usuario/<usuario_id>', eliminar_usuario, name='eliminar_usuario'),
    path('cambiar_password', cambiar_password, name='cambiar_password'),
    path('bodega', bodega, name='bodega'),
    path('obtener_productos', obtener_productos, name='obtener_productos'),
    path('eliminar_producto/<producto_id>', eliminar_producto, name='eliminar_producto'),
    path('eliminar_producto_en_bodega/<bodega_id>', eliminar_producto_en_bodega, name='eliminar_producto_en_bodega'),
    path('ventas', ventas, name='ventas'),
    path('boleta', boleta, name='boleta'),
    path('detalle_boleta/<boleta_id>', detalle_boleta, name='detalle_boleta'),
    path('cambiar_estado_boleta/<nro_boleta>/<estado>', cambiar_estado_boleta, name='cambiar_estado_boleta'),
    path('ingresar', ingresar, name='ingresar'),
    path('misdatos', misdatos, name='misdatos'),
    path('mipassword', mipassword, name='mipassword'),
    path('miscompras', miscompras, name='miscompras'),
    path('salir', salir, name='salir'),
    path('carrito', carrito, name='carrito'),
    path('eliminar_producto_en_carrito/<carrito_id>', eliminar_producto_en_carrito, name='eliminar_producto_en_carrito'),
    path('vaciar_carrito', vaciar_carrito, name='vaciar_carrito'),
    path('agregar_producto_al_carrito/<producto_id>', agregar_producto_al_carrito, name='agregar_producto_al_carrito'),
    path('ficha/<producto_id>', ficha, name='ficha'),
    path('comprar_ahora', comprar_ahora, name='comprar_ahora'),
    path('premio', premio, name='premio'),
    path('poblar', poblar, name='poblar'),
]