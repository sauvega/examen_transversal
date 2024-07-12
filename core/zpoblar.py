import sqlite3
from django.contrib.auth.models import User, Permission
from django.db import connection
from datetime import date, timedelta
from random import randint
from core.models import Categoria, Producto, Carrito, Perfil, Boleta, DetalleBoleta, Bodega

def eliminar_tabla(nombre_tabla):
    conexion = sqlite3.connect('db.sqlite3')
    cursor = conexion.cursor()
    cursor.execute(f"DELETE FROM {nombre_tabla}")
    conexion.commit()
    conexion.close()

def exec_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)

def crear_usuario(username, tipo, nombre, apellido, correo, es_superusuario, 
    es_staff, rut, direccion, subscrito, imagen):

    try:
        print(f'Verificar si existe usuario {username}.')

        if User.objects.filter(username=username).exists():
            print(f'   Eliminar {username}')
            User.objects.get(username=username).delete()
            print(f'   Eliminado {username}')
        
        print(f'Iniciando creación de usuario {username}.')

        usuario = None
        if tipo == 'Superusuario':
            print('    Crear Superuser')
            usuario = User.objects.create_superuser(username=username, password='123')
        else:
            print('    Crear User')
            usuario = User.objects.create_user(username=username, password='123')

        if tipo == 'Administrador':
            print('    Es administrador')
            usuario.is_staff = es_staff
            
        usuario.first_name = nombre
        usuario.last_name = apellido
        usuario.email = correo
        usuario.save()

        if tipo == 'Administrador':
            print(f'    Dar permisos a core y apirest')
            permisos = Permission.objects.filter(content_type__app_label__in=['core', 'apirest'])
            usuario.user_permissions.set(permisos)
            usuario.save()
 
        print(f'    Crear perfil: RUT {rut}, Subscrito {subscrito}, Imagen {imagen}')
        Perfil.objects.create(
            usuario=usuario, 
            tipo_usuario=tipo,
            rut=rut,
            direccion=direccion,
            subscrito=subscrito,
            imagen=imagen)
        print("    Creado correctamente")
    except Exception as err:
        print(f"    Error: {err}")

def eliminar_tablas():
    eliminar_tabla('auth_user_groups')
    eliminar_tabla('auth_user_user_permissions')
    eliminar_tabla('auth_group_permissions')
    eliminar_tabla('auth_group')
    eliminar_tabla('auth_permission')
    eliminar_tabla('django_admin_log')
    eliminar_tabla('django_content_type')
    #eliminar_tabla('django_migrations')
    eliminar_tabla('django_session')
    eliminar_tabla('Bodega')
    eliminar_tabla('DetalleBoleta')
    eliminar_tabla('Boleta')
    eliminar_tabla('Perfil')
    eliminar_tabla('Carrito')
    eliminar_tabla('Producto')
    eliminar_tabla('Categoria')
    #eliminar_tabla('authtoken_token')
    eliminar_tabla('auth_user')

def poblar_bd(test_user_email=''):
    eliminar_tablas()

    crear_usuario(
        username='vl.rendic@duocuc.cl',
        tipo='Administrador', 
        nombre='Vladimir', 
        apellido='Rendic', 
        correo=test_user_email if test_user_email else 'vl.rendic@duocuc.cl', 
        es_superusuario=False, 
        es_staff=True, 
        rut='18.340.505-5',    
        direccion='Dora 3634, \nRecoleta Norte \nChile', 
        subscrito=False, 
        imagen='perfiles/rendic.jpg'
    )

    crear_usuario(
        username='ro.ysla@duocuc.cl',
        tipo='Administrador', 
        nombre='Rogger', 
        apellido='Ysla', 
        correo=test_user_email if test_user_email else 'ro.ysla@duocuc.cl', 
        es_superusuario=False, 
        es_staff=True, 
        rut='27.953.711-4',    
        direccion='Av. El Parque 219, \nBuin \nChile', 
        subscrito=False, 
        imagen='perfiles/ysla.jpg'
    )

    crear_usuario(
        username='ro.faundez@duocuc.cl',
        tipo='Cliente', 
        nombre='Rodrigo', 
        apellido='Faundez', 
        correo=test_user_email if test_user_email else 'ro.faundez@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='21.368.266-0', 
        direccion='Papa San Ponciano 370, \nPudahuel Sur \nChile', 
        subscrito=True, 
        imagen='perfiles/faundez.jpg'
    )

    crear_usuario(
        username='ma.abarcat@duocuc.cl',
        tipo='Cliente', 
        nombre='Martin', 
        apellido='Abarca', 
        correo=test_user_email if test_user_email else 'ma.abarcat@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='21.650.859-9', 
        direccion='Los Europeos 1521 \nQuilicura \nChile', 
        subscrito=False, 
        imagen='perfiles/abarca.jpg'
    )

    crear_usuario(
        username='super',
        tipo='Superusuario',
        nombre='Saul',
        apellido='Vega',
        correo=test_user_email if test_user_email else 'sau.vega@duocuc.cl',
        es_superusuario=True,
        es_staff=True,
        rut='21.196.698-k',
        direccion='Republica 10, \nSantiago \nChile',
        subscrito=False,
        imagen='perfiles/vega.jpg'
    )

    
    categorias_data = [
        { 'id': 1, 'nombre': 'Acción'},
        { 'id': 2, 'nombre': 'Aventura'},
        { 'id': 3, 'nombre': 'Estrategia'},
        { 'id': 4, 'nombre': 'RPG'},
    ]

    print('Crear categorías')
    for categoria in categorias_data:
        Categoria.objects.create(**categoria)
    print('Categorías creadas correctamente')

    
    productos_data = [
        {
            'id': 1,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Control',
            'descripcion': 'Un juego de acción y aventura con elementos sobrenaturales. Juegas como Jesse Faden, explorando una misteriosa agencia gubernamental y desentrañando sus secretos.',
            'precio': 31900,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000001.jpg'
        },
        {
            'id': 2,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Death Stranding',
            'descripcion': 'Un juego de acción y exploración en un mundo postapocalíptico. Juegas como Sam Porter Bridges, transportando recursos y conectando asentamientos aislados.',
            'precio': 27999,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000002.jpg'
        },
        {
            'id': 3,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Disco Elysium',
            'descripcion': 'Un RPG centrado en la narrativa donde asumes el papel de un detective en una ciudad sumida en la corrupción. Destaca por su profunda historia y diálogos complejos.',
            'precio': 14900,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000003.jpg'
        },
        {
            'id': 4,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Divinity: Original Sin 2',
            'descripcion': 'Un RPG isométrico con combate por turnos. Ofrece una historia rica y opciones de juego profundas, permitiendo gran libertad en cómo abordar las misiones y combates.',
            'precio': 22000,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000004.jpg'
        },
        {
            'id': 5,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Hogwarts Legacy',
            'descripcion': 'Un RPG de acción ambientado en el mundo mágico de Harry Potter. Juegas como un estudiante de Hogwarts en el siglo XIX, explorando el castillo y sus alrededores, asistiendo a clases, aprendiendo hechizos y tomando decisiones que influirán en tu aventura mágica.',
            'precio': 39999,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000005.jpg'
        },
        {
            'id': 6,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Dying Light 2',
            'descripcion': 'Un juego de supervivencia en un mundo abierto infestado de zombis. Combina parkour y combate en un entorno dinámico y peligroso.',
            'precio': 39990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000006.jpg'
        },
        {
            'id': 7,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Far Cry 6',
            'descripcion': 'Un juego de acción y aventura en un mundo abierto ambientado en la isla ficticia de Yara. Juegas como Dani Rojas, un guerrillero que lucha contra el régimen opresivo del dictador Antón Castillo.',
            'precio': 44900,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000007.jpg'
        },
        {
            'id': 8,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Final Fantasy XIV: Dawntrail',
            'descripcion': 'Quinta expansión de Final Fantasy XIV, un MMORPG de larga duración. Los jugadores explorarán un nuevo continente y participarán en nuevas aventuras y desafíos.',
            'precio': 22900,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000008.jpg'
        },
        {
            'id': 9,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Forza Motorsport',
            'descripcion': 'Simulador de carreras con una experiencia de conducción realista, numerosos coches y pistas. Ideal para aficionados a los deportes de motor.',
            'precio': 54900,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000009.jpg'
        },
        {
            'id': 10,
            'categoria': Categoria.objects.get(id=3),
            'nombre': 'Frostpunk',
            'descripcion': 'Un simulador de supervivencia y construcción de ciudades en un mundo postapocalíptico congelado. Debes gestionar recursos y tomar decisiones difíciles para sobrevivir.',
            'precio': 15500,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000010.jpg'
        },
        {
            'id': 11,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Hades',
            'descripcion': 'Un roguelike de acción donde juegas como Zagreus, el hijo de Hades, tratando de escapar del inframundo. Ofrece una historia robusta y alto valor de rejugabilidad.',
            'precio': 13000,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000011.jpg'
        },
        {
            'id': 12,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Half-Life: Alyx',
            'descripcion': 'Un juego de realidad virtual que actúa como precuela de Half-Life 2. Juegas como Alyx Vance, luchando contra una invasión alienígena.',
            'precio': 28500,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000012.jpg'
        },
        {
            'id': 13,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Hitman 3',
            'descripcion': 'Un juego de sigilo donde asumes el rol del Agente 47, un asesino a sueldo. Debes completar misiones eliminando objetivos de manera creativa.',
            'precio': 5750,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000013.jpg'
        },
        {
            'id': 14,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Horizon Zero Dawn',
            'descripcion': 'Un juego de acción y aventura en un mundo postapocalíptico donde cazas máquinas gigantes. Juegas como Aloy, una cazadora en busca de respuestas sobre su pasado.',
            'precio': 35000,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000014.jpg'
        },
        {
            'id': 15,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'It Takes Two',
            'descripcion': 'Un juego cooperativo donde dos jugadores deben trabajar juntos para superar diversos desafíos. Ofrece una narrativa emotiva y mecánicas de juego variadas.',
            'precio': 31900,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000015.jpg'
        },
        {
            'id': 16,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Kunitsu-Gami: Path of the Goddess',
            'descripcion': 'Un nuevo juego de acción de Capcom que recuerda a títulos artísticos como Okami. Juegas como un guerrero que escolta a una doncella para purificar la tierra de espíritus demoníacos.',
            'precio': 44680,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000016.jpg'
        },
        {
            'id': 17,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Monster Hunter: World',
            'descripcion': 'Un juego de rol de acción donde cazas monstruos gigantes en diversos ecosistemas. Ofrece una gran variedad de armas y armaduras para personalizar tu estilo de juego.',
            'precio': 24100,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000017.jpg'
        },
        {
            'id': 18,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Outer Wilds',
            'descripcion': 'Un juego de exploración espacial donde investigas un sistema solar en bucle temporal. Cada 22 minutos, el universo se reinicia, y debes descubrir los secretos antes de que el tiempo se agote.',
            'precio': 12500,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000018.jpg'
        },
        {
            'id': 19,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Resident Evil Village',
            'descripcion': 'Un juego de terror y supervivencia donde Ethan Winters debe rescatar a su hija de un pueblo lleno de criaturas aterradoras. Continúa la historia de Resident Evil 7.',
            'precio': 32200,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000019.jpg'
        },
        {
            'id': 20,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Sekiro: Shadows Die Twice',
            'descripcion': 'Un juego de acción y aventura ambientado en Japón feudal. Juegas como un shinobi en busca de venganza, enfrentándote a enemigos desafiantes con un combate preciso.',
            'precio': 47650,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000020.jpg'
        },
        {
            'id': 21,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Marvel\'s Spider-Man Remastered',
            'descripcion': 'Un juego de acción y aventura donde juegas como Spider-Man, balanceándote por Nueva York y enfrentándote a villanos icónicos. La versión remasterizada mejora los gráficos y el rendimiento.',
            'precio': 42000,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000021.jpg'
        },
        {
            'id': 22,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Stardew Valley',
            'descripcion': 'Un juego de simulación agrícola donde cultivas, crías animales y formas relaciones con los habitantes del pueblo. Ideal para los amantes de los juegos relajantes.',
            'precio': 7500,
            'descuento_subscriptor': 5,
            'descuento_oferta': 0,
            'imagen': 'productos/000022.jpg'
        }
    ]

    print('Crear productos')
    for producto in productos_data:
        Producto.objects.create(**producto)
    print('Productos creados correctamente')

    print('Crear carritos')
    for rut in ['21.368.266-0', '21.650.859-9']:
        cliente = Perfil.objects.get(rut=rut)
        for cantidad_productos in range(1, 11):
            producto = Producto.objects.get(pk=randint(1, 10))
            if cliente.subscrito:
                descuento_subscriptor = producto.descuento_subscriptor
            else:
                descuento_subscriptor = 0
            descuento_oferta = producto.descuento_oferta
            descuento_total = descuento_subscriptor + descuento_oferta
            descuentos = int(round(producto.precio * descuento_total / 100))
            precio_a_pagar = producto.precio - descuentos
            Carrito.objects.create(
                cliente=cliente,
                producto=producto,
                precio=producto.precio,
                descuento_subscriptor=descuento_subscriptor,
                descuento_oferta=descuento_oferta,
                descuento_total=descuento_total,
                descuentos=descuentos,
                precio_a_pagar=precio_a_pagar
            )
    print('Carritos creados correctamente')

    print('Crear boletas')
    nro_boleta = 0
    perfiles_cliente = Perfil.objects.filter(tipo_usuario='Cliente')
    for cliente in perfiles_cliente:
        estado_index = -1
        for cant_boletas in range(1, randint(6, 21)):
            nro_boleta += 1
            estado_index += 1
            if estado_index > 3:
                estado_index = 0
            estado = Boleta.ESTADO_CHOICES[estado_index][1]
            fecha_venta = date(2023, randint(1, 5), randint(1, 28))
            fecha_despacho = fecha_venta + timedelta(days=randint(0, 3))
            fecha_entrega = fecha_despacho + timedelta(days=randint(0, 3))
            if estado == 'Anulado':
                fecha_despacho = None
                fecha_entrega = None
            elif estado == 'Vendido':
                fecha_despacho = None
                fecha_entrega = None
            elif estado == 'Despachado':
                fecha_entrega = None
            boleta = Boleta.objects.create(
                nro_boleta=nro_boleta, 
                cliente=cliente,
                monto_sin_iva=0,
                iva=0,
                total_a_pagar=0,
                fecha_venta=fecha_venta,
                fecha_despacho=fecha_despacho,
                fecha_entrega=fecha_entrega,
                estado=estado)
            detalle_boleta = []
            total_a_pagar = 0
            for cant_productos in range(1, randint(4, 6)):
                producto_id = randint(1, 10)
                producto = Producto.objects.get(id=producto_id)
                precio = producto.precio
                descuento_subscriptor = 0
                if cliente.subscrito:
                    descuento_subscriptor = producto.descuento_subscriptor
                descuento_oferta = producto.descuento_oferta
                descuento_total = descuento_subscriptor + descuento_oferta
                descuentos = int(round(precio * descuento_total / 100))
                precio_a_pagar = precio - descuentos
                bodega = Bodega.objects.create(producto=producto)
                DetalleBoleta.objects.create(
                    boleta=boleta,
                    bodega=bodega,
                    precio=precio,
                    descuento_subscriptor=descuento_subscriptor,
                    descuento_oferta=descuento_oferta,
                    descuento_total=descuento_total,
                    descuentos=descuentos,
                    precio_a_pagar=precio_a_pagar)
                total_a_pagar += precio_a_pagar
            monto_sin_iva = int(round(total_a_pagar / 1.19))
            iva = total_a_pagar - monto_sin_iva
            boleta.monto_sin_iva = monto_sin_iva
            boleta.iva = iva
            boleta.total_a_pagar = total_a_pagar
            boleta.fecha_venta = fecha_venta
            boleta.fecha_despacho = fecha_despacho
            boleta.fecha_entrega = fecha_entrega
            boleta.estado = estado
            boleta.save()
            print(f'    Creada boleta Nro={nro_boleta} Cliente={cliente.usuario.first_name} {cliente.usuario.last_name}')
    print('Boletas creadas correctamente')

    print('Agregar productos a bodega')
    for producto_id in range(1, 11):
        producto = Producto.objects.get(id=producto_id)
        cantidad = 0
        for cantidad in range(1, randint(2, 31)):
            Bodega.objects.create(producto=producto)
        print(f'    Agregados {cantidad} "{producto.nombre}" a la bodega')
    print('Productos agregados a bodega')

