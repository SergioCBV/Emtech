#PROYECTO 01 BLANCAS SERGIO
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

#función parra inicio de sesión
def login(username, password):
    #usuario y contraseña están predefinidos
    usuario = 'admin'
    contrasena = '1289'

    if username == usuario:
        if password == contrasena:
            #este es el caso en el que el usuario y la contraseña son correctos
            print("Bienvenido al programa, administrador")
            login=True
        else:
            #este es el caso de que la contraseña no sea correcta
            print("Contraseña incorrecta")
            login=False
    else:
        #en este caso se aclara si el usuario no es correcto
        print("El usuario no existe")
        login=False

    return login #se regresa un valor de True o False para que pueda continuar el flujo del programa

#función para pasar el nombre del mes a un string con números
def define_mes():
    posibles_meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre","todo el año"]
    print("¿De qué periodo desea ver el reporte?")
    for opcion in posibles_meses: #mostrar opciones de meses
        print("*",opcion)
    print("* salir")
    
    seguir=True
    while seguir==True: #ciclo para introducir el mes que se desea, se repite en caso de no estar bien escrito
        mes_numero=0
        mes=input("Ingrese cualquier opción: ")
    
        if mes=="enero":
            mes_numero="/01/"
            seguir=False
        elif mes=="febrero":
            mes_numero="/02/"
            seguir=False
        elif mes=="marzo":
            mes_numero="/03/"
            seguir=False
        elif mes=="abril":
            mes_numero="/04/"
            seguir=False
        elif mes=="mayo":
            mes_numero="/05/"
            seguir=False
        elif mes=="junio":
            mes_numero="/06/"
            seguir=False
        elif mes=="julio":
            mes_numero="/07/"
            seguir=False
        elif mes=="agosto":
            mes_numero="/08/"
            seguir=False
        elif mes=="septiembre":
            mes_numero="/09/"
            seguir=False
        elif mes=="octubre":
            mes_numero="/10/"
            seguir=False
        elif mes=="noviembre":
            mes_numero="/11/"
            seguir=False
        elif mes=="diciembre":
            mes_numero="/12/"
            seguir=False
        elif mes=="todo el año":
            mes_numero="/13/"
            seguir=False
        elif mes=="salir":
            break
        else:
            print("Vuelva a ingresarlo")
    
    return mes_numero #opciones, del "/01/" al "/12/", "/13/"(todo el año) y 0 (salir)

#función para generar la lista de los 5 productos más vendidos
def mayores_ventas(mes):
    #lifestore_searches = [id_search, id product]
    #lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
    #lifestore_products = [id_product, name, price, category, stock]
    
    ventas=[] #se define una lista en la que se enlistará el id del producto y cuántas unidades se vendieron
    cantidad_productos=len(lifestore_products)
    max=0
    id_max=0
    id=1 

    for i in range(cantidad_productos): #este ciclo es para sacar la longitud de la lista
        id=i+1
        ventas.append([id,0])
    for venta in lifestore_sales: #este ciclo acumula las ventas en la lista ventas
        fecha_venta=venta[3]
        if mes in fecha_venta:
            id=venta[1]
            ventas[id-1][1]+=1
            if ventas[id-1][1]>max: #se define la cantidad y el id de producto del máximo número de vendidos
                max=ventas[id-1][1]
                id_max=venta[1]
        if mes=="/13/":
            id=venta[1]
            ventas[id-1][1]+=1
            if ventas[id-1][1]>max: #se define la cantidad y el id de producto del máximo número de vendidos
                max=ventas[id-1][1]
                id_max=venta[1]
    
    top5=[] #lista del top 5 más vendidos
    for indice in range(5): #se establece un ciclo que permita ir del 0 al 4 (para sacar 5 artículos)
        if indice==0: #cuando el índice es 0 (primera posición), se agrega el artículo más vendido
            top5.append([id_max,max])
        else: #cuando el índice no es 0 (de la segunda a quinta posición)
            valor=[0,0]
            for venta in ventas: #de la lista donde estan las ventas, se sacan los más vendidos
                #El siguiente bucle es para establecer la condición de que los id de productos 
                #no sean iguales, de forma que si hay dos productos diferentes con el mismo número de 
                #ventas que deberían estar en el top, aparezcan como tal en el top
                decision=True
                for i in top5:
                    c=venta[0]!=i[0]
                    if c==False:
                        decision=False
                #los más vendidos se sacan con la condición de que sean mayor o igual al valor contenido en la posición de ventas en la lista valor
                #pero menor o igual al número de ventas del producto que ocupa la posición anterior en el top, de esta forma se asegura 
                #que los valores sean los más altos pero que haya un orden descendente en el top, por último se pone la condición de que no se repitan los id
                if venta[1]>=valor[1] and venta[1]<=top5[indice-1][1] and decision==True: 
                    valor=venta
            top5.append(valor)
    
    i=0 
    for cantidad in top5: #el bucle es para cambiar el id del producto por el nombre del producto
        for producto in lifestore_products:
            if cantidad[0]==producto[0]:
                top5[i][0]=producto[1] 
        i+=1

    print("La cantidad de productos más vendidos son: ")
    for cantidad in top5: #muestra el top 5 por producto y cantidad vendida
        print(f"* Producto:{cantidad[0]}, con una venta de: {cantidad[1]} unidades")
    
    return 0

#función para generar la lista de los 10 productos con más busquedas
def mayores_busquedas():
    #lifestore_searches = [id_search, id product]
    #lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
    #lifestore_products = [id_product, name, price, category, stock]

    busquedas=[] #se define una lista en la que se enlistará el id del producto y cuántas veces se buscó
    cantidad_productos=len(lifestore_products)
    max=0
    id_max=0
    id=1 

    for i in range(cantidad_productos): #este ciclo es para sacar la longitud de la lista
        id=i+1
        busquedas.append([id,0])
    for busqueda in lifestore_searches: #este ciclo acumula las busquedas en la lista busquedas
        id=busqueda[1]
        busquedas[id-1][1]+=1
        if busquedas[id-1][1]>max: #se define la cantidad y el id de producto del máximo número de buscado
            max=busquedas[id-1][1]
            id_max=busqueda[1]

    top10=[] #lista del top 10 más buscado
    for indice in range(10): #se establece un ciclo que permita ir del 0 al 9 (para sacar 10 artículos)
        if indice==0:  #cuando el índice es 0 (primera posición), se agrega el artículo más buscado
            top10.append([id_max,max])
        else: #cuando el índice no es 0 (de la segunda a décima posición)
            valor=[0,0] #se establece una lista que contenga el id y número de búsquedas de los artículos
            for busqueda in busquedas: #de la lista donde estan las busquedas, se sacan los más vendidos
                #El siguiente bucle es para establecer la condición de que los id de productos 
                #no sean iguales, de forma que si hay dos productos diferentes con el mismo número de 
                #busquedas que deberían estar en el top, aparezcan como tal en el top
                decision=True
                for i in top10:
                    c=busqueda[0]!=i[0]
                    if c==False:
                        decision=False
                #los más buscados se sacan con la condición de que sean mayor o igual al valor contenido en la posición de búsquedas en la lista valor
                #pero menor o igual al número de búsquedas del producto que ocupa la posición anterior en el top, de esta forma se asegura 
                #que los valores sean los más altos pero que haya un orden descendente en el top, por último se pone la condición de que no se repitan los id
                if busqueda[1]>=valor[1] and busqueda[1]<=top10[indice-1][1]and decision==True: #busqueda[0]!=top10[indice-1][0]:
                    valor=busqueda
            top10.append(valor) #se agregan los valores al top

    i=0
    for cantidad in top10: #el bucle es para cambiar el id del producto por el nombre del producto
        for producto in lifestore_products:
            if cantidad[0]==producto[0]:
                top10[i][0]=producto[1] #cambio de id por nombre
        i+=1

    print("La cantidad de productos más buscados son: ")
    for cantidad in top10: #muestra el top 10 por producto y cuantas búsquedas tuvo
        print(f"{cantidad[0]}, con {cantidad[1]} búsquedas")
                #* Producto:
    return 0

#función para obtener los productos menos vendidos del mes para una categoría en específico
def menor_venta(productos,mes):
    #lifestore_searches = [id_search, id product]
    #lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
    #lifestore_products = [id_product, name, price, category, stock]

    ventas=[] #se define una lista en la que se enlistará el id del producto y cuántas unidades se vendieron
    min=100000
    id_min=0
    id=0 
    for producto in productos: #agrega a la lista ventas el id de producto
        id=producto[0]
        ventas.append([id,0])
    for sale in lifestore_sales: #este ciclo acumula las ventas en la lista ventas
        fecha_venta=sale[3]
        i=0
        for venta in ventas:
            if venta[0]==sale[1]:
                if mes in fecha_venta:
                    ventas[i][1]+=1
                if mes=="/13/":
                    if venta[0]==sale[1]:
                        ventas[i][1]+=1
            i+=1
    
    for venta in ventas: #este ciclo saca el producto menos vendido y su id
        if venta[1]<min:
            min=venta[1]
            id_min=venta[0]
    
    top5=[] #lista del top 5 menos vendidos
    for indice in range(5): #se establece un ciclo que permita ir del 0 al 4 (para sacar 5 artículos)
        if indice==0:
            top5.append([id_min,min])
        else: #cuando el índice no es 0 (de la segunda a quinta posición)
            valor=[0,10000]
            for venta in ventas: #de la lista donde estan las ventas, se sacan los menos vendidos
                #El siguiente bucle es para establecer la condición de que los id de productos 
                #no sean iguales, de forma que si hay dos productos diferentes con el mismo número de 
                #ventas que deberían estar en el top, aparezcan como tal en el top
                decision=True
                for i in top5:
                    c=venta[0]!=i[0]
                    if c==False:
                        decision=False
                #los menos vendidos se sacan con la condición de que sean menor o igual al valor contenido en la posición de ventas en la lista valor
                #pero mayot o igual al número de ventas del producto que ocupa la posición anterior en el top, de esta forma se asegura 
                #que los valores sean los más bajos pero que haya un orden ascendente en el top, por último se pone la condición de que no se repitan los id
                if venta[1]<=valor[1] and venta[1]>=top5[indice-1][1] and decision==True: 
                    valor=venta
            top5.append(valor)
    
    i=0 
    for cantidad in top5: #el bucle es para cambiar el id del producto por el nombre del producto
        for producto in productos:
            if cantidad[0]==producto[0]:
                top5[i][0]=producto[1] 
        i+=1
    
    return top5

#función para definir los productos menos vendidos del mes por cada categoría
def menores_ventas(mes):
    #lifestore_products = [id_product, name, price, category, stock]
    categorias=[0]
    i=0
    for producto in lifestore_products: #agrega las categorías a la lista categorías
        if categorias[i]!=producto[3]:
            categorias.append(producto[3])
            i+=1
    categorias.remove(0)

    lifestore_products_category1=[]
    lifestore_products_category2=[]
    lifestore_products_category3=[]
    lifestore_products_category4=[]
    lifestore_products_category5=[]
    lifestore_products_category6=[]
    lifestore_products_category7=[]
    lifestore_products_category8=[]

    for producto in lifestore_products: #agrega los productos a una lista correspondiente a cada categoría
        if producto[3]==categorias[0]:
            lifestore_products_category1.append(producto)
        elif producto[3]==categorias[1]:
            lifestore_products_category2.append(producto)
        elif producto[3]==categorias[2]:
            lifestore_products_category3.append(producto)
        elif producto[3]==categorias[3]:
            lifestore_products_category4.append(producto)
        elif producto[3]==categorias[4]:
            lifestore_products_category5.append(producto)
        elif producto[3]==categorias[5]:
            lifestore_products_category6.append(producto)
        elif producto[3]==categorias[6]:
            lifestore_products_category7.append(producto)
        else:
            lifestore_products_category8.append(producto)

    #las siguientes líneas son para mostrar los productos menos vendidos por categoría
    top_categoria1=menor_venta(lifestore_products_category1,mes)
    print(f"La categoría {categorias[0]} tiene {len(lifestore_products_category1)} elementos")
    print(f"Los productos menos vendidos del mes {mes} y categoría {categorias[0]} son: ")
    for producto in top_categoria1:
        print(f"* Producto: {producto[0]} con {producto[1]} unidades vendidas")

    top_categoria2=menor_venta(lifestore_products_category2,mes)
    print(f"La categoría {categorias[1]} tiene {len(lifestore_products_category2)} elementos")
    print(f"Los productos menos vendidos del mes {mes} y categoría {categorias[1]} son: ")
    for producto in top_categoria2:
        print(f"* Producto: {producto[0]} con {producto[1]} unidades vendidas")

    top_categoria3=menor_venta(lifestore_products_category3,mes)
    print(f"La categoría {categorias[2]} tiene {len(lifestore_products_category3)} elementos")
    print(f"Los productos menos vendidos del mes {mes} y categoría {categorias[2]} son: ")
    for producto in top_categoria3:
        print(f"* Producto: {producto[0]} con {producto[1]} unidades vendidas")

    top_categoria4=menor_venta(lifestore_products_category4,mes)
    print(f"La categoría {categorias[3]} tiene {len(lifestore_products_category4)} elementos")
    print(f"Los productos menos vendidos del mes {mes} y categoría {categorias[3]} son: ")
    for producto in top_categoria4:
        print(f"* Producto: {producto[0]} con {producto[1]} unidades vendidas")

    top_categoria5=menor_venta(lifestore_products_category5,mes)
    print(f"La categoría {categorias[4]} tiene {len(lifestore_products_category5)} elementos")
    print(f"Los productos menos vendidos del mes {mes} y categoría {categorias[4]} son: ")
    for producto in top_categoria5:
        print(f"* Producto: {producto[0]} con {producto[1]} unidades vendidas")

    top_categoria6=menor_venta(lifestore_products_category6,mes)
    print(f"La categoría {categorias[5]} tiene {len(lifestore_products_category6)} elementos")
    print(f"Los productos menos vendidos del mes {mes} y categoría {categorias[5]} son: ")
    for producto in top_categoria6:
        print(f"* Producto: {producto[0]} con {producto[1]} unidades vendidas")

    top_categoria7=menor_venta(lifestore_products_category7,mes)
    print(f"La categoría {categorias[6]} tiene {len(lifestore_products_category7)} elementos")
    print(f"Los productos menos vendidos del mes {mes} y categoría {categorias[6]} son: ")
    for producto in top_categoria7:
        print(f"* Producto: {producto[0]} con {producto[1]} unidades vendidas")

    top_categoria8=menor_venta(lifestore_products_category8,mes)
    print(f"La categoría {categorias[7]} tiene {len(lifestore_products_category8)} elementos")
    print(f"Los productos menos vendidos del mes {mes} y categoría {categorias[7]} son: ")
    for producto in top_categoria8:
        print(f"* Producto: {producto[0]} con {producto[1]} unidades vendidas")

    return 0

#función para obtener los productos menos buscados del mes para una categoría en específico
def menor_busqueda(productos):
    #lifestore_searches = [id_search, id product]
    #lifestore_products = [id_product, name, price, category, stock]

    busquedas=[] #se define una lista en la que se enlistará el id del producto y cuántas unidades se buscaron
    min=100000
    id_min=0
    id=0 
    for producto in productos: #agrega a la lista busquedas el id de producto
        id=producto[0]
        busquedas.append([id,0])
    for search in lifestore_searches: #este ciclo acumula las búsquedas en la lista busquedas
        i=0
        for busqueda in busquedas:
            if busqueda[0]==search[1]:
                busquedas[i][1]+=1
            i+=1
    
    for busqueda in busquedas: #este ciclo saca el producto menos buscado y su id
        if busqueda[1]<min:
            min=busqueda[1]
            id_min=busqueda[0]
    
    top10=[] #lista del top 10 menos buscado
    for indice in range(10): #se establece un ciclo que permita ir del 0 al 9 (para sacar 10 artículos)
        if indice==0:
            top10.append([id_min,min])
        else: #cuando el índice no es 0 (de la segunda a última posición)
            valor=[0,10000]
            for busqueda in busquedas: #de la lista donde estan las búsquedas, se sacan los menos buscados
                #El siguiente bucle es para establecer la condición de que los id de productos 
                #no sean iguales, de forma que si hay dos productos diferentes con el mismo número de 
                #búsquedas que deberían estar en el top, aparezcan como tal en el top
                decision=True
                for i in top10:
                    c=busqueda[0]!=i[0]
                    if c==False:
                        decision=False
                #los menos buscados se sacan con la condición de que sean menor o igual al valor contenido en la posición de búsquedas en la lista valor
                #pero mayor o igual al número de ventas del producto que ocupa la posición anterior en el top, de esta forma se asegura 
                #que los valores sean los más bajos pero que haya un orden ascendente en el top, por último se pone la condición de que no se repitan los id
                if busqueda[1]<=valor[1] and busqueda[1]>=top10[indice-1][1] and decision==True: 
                    valor=busqueda
            top10.append(valor)
    
    i=0 
    for cantidad in top10: #el bucle es para cambiar el id del producto por el nombre del producto
        for producto in productos:
            if cantidad[0]==producto[0]:
                top10[i][0]=producto[1] 
        i+=1
    
    return top10

#función para definir los productos menos buscados del mes por cada categoría
def menores_busquedas():
    #lifestore_products = [id_product, name, price, category, stock]
    categorias=[0]
    i=0
    for producto in lifestore_products: #agrega las categorías a la lista categorías
        if categorias[i]!=producto[3]:
            categorias.append(producto[3])
            i+=1
    categorias.remove(0)

    lifestore_products_category1=[]
    lifestore_products_category2=[]
    lifestore_products_category3=[]
    lifestore_products_category4=[]
    lifestore_products_category5=[]
    lifestore_products_category6=[]
    lifestore_products_category7=[]
    lifestore_products_category8=[]

    for producto in lifestore_products: #agrega los productos a una lista correspondiente a cada categoría
        if producto[3]==categorias[0]:
            lifestore_products_category1.append(producto)
        elif producto[3]==categorias[1]:
            lifestore_products_category2.append(producto)
        elif producto[3]==categorias[2]:
            lifestore_products_category3.append(producto)
        elif producto[3]==categorias[3]:
            lifestore_products_category4.append(producto)
        elif producto[3]==categorias[4]:
            lifestore_products_category5.append(producto)
        elif producto[3]==categorias[5]:
            lifestore_products_category6.append(producto)
        elif producto[3]==categorias[6]:
            lifestore_products_category7.append(producto)
        else:
            lifestore_products_category8.append(producto)
    
    #las siguientes líneas son para mostrar los productos menos buscados por categoría
    top_categoria1=menor_busqueda(lifestore_products_category1)
    print(f"La categoría {categorias[0]} tiene {len(lifestore_products_category1)} elementos")
    print(f"Los productos menos buscados de la categoría {categorias[0]} son: ")
    for producto in top_categoria1:
        print(f"* Producto: {producto[0]} con {producto[1]} búsquedas")
    
    top_categoria2=menor_busqueda(lifestore_products_category2)
    print(f"La categoría {categorias[1]} tiene {len(lifestore_products_category2)} elementos")
    print(f"Los productos menos buscados de la categoría {categorias[1]} son: ")
    for producto in top_categoria2:
        print(f"* Producto: {producto[0]} con {producto[1]} búsquedas")
    
    top_categoria3=menor_busqueda(lifestore_products_category3)
    print(f"La categoría {categorias[2]} tiene {len(lifestore_products_category3)} elementos")
    print(f"Los productos menos buscados de la categoría {categorias[2]} son: ")
    for producto in top_categoria3:
        print(f"* Producto: {producto[0]} con {producto[1]} búsquedas")
    
    top_categoria4=menor_busqueda(lifestore_products_category4)
    print(f"La categoría {categorias[3]} tiene {len(lifestore_products_category4)} elementos")
    print(f"Los productos menos buscados de la categoría {categorias[3]} son: ")
    for producto in top_categoria4:
        print(f"* Producto: {producto[0]} con {producto[1]} búsquedas")
    
    top_categoria5=menor_busqueda(lifestore_products_category5)
    print(f"La categoría {categorias[4]} tiene {len(lifestore_products_category5)} elementos")
    print(f"Los productos menos buscados de la categoría {categorias[4]} son: ")
    for producto in top_categoria5:
        print(f"* Producto: {producto[0]} con {producto[1]} búsquedas")
    
    top_categoria6=menor_busqueda(lifestore_products_category6)
    print(f"La categoría {categorias[5]} tiene {len(lifestore_products_category6)} elementos")
    print(f"Los productos menos buscados de la categoría {categorias[5]} son: ")
    for producto in top_categoria6:
        print(f"* Producto: {producto[0]} con {producto[1]} búsquedas")
    
    top_categoria7=menor_busqueda(lifestore_products_category7)
    print(f"La categoría {categorias[6]} tiene {len(lifestore_products_category7)} elementos")
    print(f"Los productos menos buscados de la categoría {categorias[6]} son: ")
    for producto in top_categoria7:
        print(f"* Producto: {producto[0]} con {producto[1]} búsquedas")
    
    top_categoria8=menor_busqueda(lifestore_products_category8)
    print(f"La categoría {categorias[7]} tiene {len(lifestore_products_category8)} elementos")
    print(f"Los productos menos buscados de la categoría {categorias[7]} son: ")
    for producto in top_categoria8:
        print(f"* Producto: {producto[0]} con {producto[1]} búsquedas")
    
    return 0

#función para obtener los productos con mejor y peor reseña promedio por mes
def resena(mes):
    #lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
    #lifestore_products = [id_product, name, price, category, stock]
    ventas_mes=[]
    cantidad_productos=len(lifestore_products)
    id=1 
    for i in range(cantidad_productos): #este ciclo es para sacar la longitud de la lista
        id=i+1
        ventas_mes.append([id,0])
    for venta in ventas_mes: #este ciclo es para agregar un promedio de las reseñas por producto a la lista ventas_mes
        contador=0
        id=venta[0]
        for sale in lifestore_sales:
            if sale[2]>0:
                fecha_venta=sale[3]
                if mes in fecha_venta: 
                    if sale[1]==venta[0]: 
                        ventas_mes[id-1][1]+=sale[2]
                        contador+=1
                if mes=="/13/":
                    if sale[1]==venta[0]: 
                        ventas_mes[id-1][1]+=sale[2]
                        contador+=1
        if contador!=0:
            ventas_mes[id-1][1]=ventas_mes[id-1][1]/contador #promedio de reseña para un producto en específico
    
    ventas_con_resena=[]
    for venta in ventas_mes: #ciclo para quitar productos sin reseña (los agrega a otra lista)
        if venta[1]!=0:
            ventas_con_resena.append(venta)
    
    mejor_top=[]
    max=0
    id_max=0
    id=1
    for venta in ventas_con_resena: #ciclo para obtener el producto con la mejor reseña
        if ventas_con_resena[id-1][1]>max: 
            max=ventas_con_resena[id-1][1]
            id_max=ventas_con_resena[id-1][0]
        id+=1

    for indice in range(5): #se establece el top 5
        if indice==0: #cuando el índice es 0 (primera posición), se agrega el artículo con mejor reseña
            mejor_top.append([id_max,max])
        else: #cuando el índice no es 0
            valor=[0,0]
            for venta in ventas_con_resena:
                #El siguiente bucle es para establecer la condición de que los id de productos 
                #no sean iguales, de forma que si hay dos productos diferentes con el mismo promedio 
                #de reseñas que deberían estar en el top, aparezcan como tal en el top
                decision=True
                for i in mejor_top:
                    c=venta[0]!=i[0]
                    if c==False:
                        decision=False
                if venta[1]>=valor[1] and venta[1]<=mejor_top[indice-1][1] and decision==True: 
                    valor=venta
            mejor_top.append(valor)
    
    i=0 
    for cantidad in mejor_top: #el bucle es para cambiar el id del producto por el nombre del producto
        for producto in lifestore_products:
            if cantidad[0]==producto[0]:
                mejor_top[i][0]=producto[1] 
        i+=1

    print("Los artículos con mejor reseña son: ")
    for producto in mejor_top:
        print(f"* {producto[0]} con reseña promedio de: {producto[1]}")

    peor_top=[]
    min=10
    id_min=0
    id=1
    for venta in ventas_con_resena: #obtener el producto con la peor reseña
        if ventas_con_resena[id-1][1]<min: 
            min=ventas_con_resena[id-1][1]
            id_min=ventas_con_resena[id-1][0]
        id+=1

    for indice in range(5): #se establece el top 5
        if indice==0: #cuando el índice es 0 (primera posición), se agrega el artículo con peor reseña
            peor_top.append([id_min,min])
        else: #cuando el índice no es 0
            valor=[0,10]
            for venta in ventas_con_resena:
                #El siguiente bucle es para establecer la condición de que los id de productos 
                #no sean iguales, de forma que si hay dos productos diferentes con el mismo promedio 
                #de reseñas que deberían estar en el top, aparezcan como tal en el top
                decision=True
                for i in peor_top:
                    c=venta[0]!=i[0]
                    if c==False:
                        decision=False
                if venta[1]<=valor[1] and venta[1]>=peor_top[indice-1][1] and decision==True: 
                    valor=venta
            peor_top.append(valor)
    
    i=0 
    for cantidad in peor_top: #el bucle es para cambiar el id del producto por el nombre del producto
        for producto in lifestore_products:
            if cantidad[0]==producto[0]:
                peor_top[i][0]=producto[1] 
        i+=1

    print("Los artículos con peor reseña son: ")
    for producto in peor_top:
        print(f"* {producto[0]} con reseña promedio de: {producto[1]}")

    return 0

#función para definir los ingresos y número de ventas por mes
def ingresos_ventas_promedio(mes):
    #lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
    #lifestore_products = [id_product, name, price, category, stock]
    
    ingresos_total=0
    for sale in lifestore_sales: #ciclo para acumular el ingreso total
        fecha_venta=sale[3]
        if mes in fecha_venta:
            precio=lifestore_products[sale[1]-1][2]
            ingresos_total+=precio
        if mes=="/13/":
            precio=lifestore_products[sale[1]-1][2]
            ingresos_total+=precio
    print("Ingresos totales en el periodo:")
    print("$",ingresos_total)

    num_ventas=0
    for sale in lifestore_sales: #ciclo para acumular el número de ventas
        fecha_venta=sale[3]
        if mes in fecha_venta:
            if sale[4]==0:
                num_ventas+=1
        if mes=="/13/":
            if sale[4]==0:
                num_ventas+=1
    print("Número de ventas en el periodo (sin devoluciones):")
    print(num_ventas)

    cantidad_en_devoluciones=0
    for sale in lifestore_sales: #ciclo para acumular la cantidad monetaria de las devoluciones
        fecha_venta=sale[3]
        if mes in fecha_venta:
            if sale[4]==1:
                precio=lifestore_products[sale[1]-1][2]
                cantidad_en_devoluciones+=precio
        if mes=="/13/":
            if sale[4]==1:
                precio=lifestore_products[sale[1]-1][2]
                cantidad_en_devoluciones+=precio
    print("Cantidad monetaria devuelta en el periodo:")
    print("$",cantidad_en_devoluciones)

    num_devolciones=0
    for sale in lifestore_sales: #ciclo para acumular el número de devoluciones
        fecha_venta=sale[3]
        if mes in fecha_venta:
            if sale[4]==1:
                num_devolciones+=1
        if mes=="/13/":
            if sale[4]==1:
                num_devolciones+=1
    print("Número de devoluciones en el periodo:")
    print(num_devolciones)
    
    return 0

#función para definir los ingresos anuales totales, con y sin devolución
def total_anual():
    #lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
    #lifestore_products = [id_product, name, price, category, stock]
    
    ingresos_total=0
    for sale in lifestore_sales: #ciclo para acumular el ingreso total
        precio=lifestore_products[sale[1]-1][2]
        ingresos_total+=precio
    print("Ingresos totales en el año:")
    print("$",ingresos_total)

    num_ventas=0
    for sale in lifestore_sales: #ciclo para acumular el número de ventas
        if sale[4]==0:
            num_ventas+=1
    print("Número de ventas en el año (sin devoluciones):")
    print(num_ventas)

    cantidad_en_devoluciones=0
    for sale in lifestore_sales: #ciclo para acumular la cantidad monetaria de las devoluciones
        if sale[4]==1:
            precio=lifestore_products[sale[1]-1][2]
            cantidad_en_devoluciones+=precio
    print("Cantidad monetaria devuelta en el año:")
    print("$",cantidad_en_devoluciones)

    num_devolciones=0
    for sale in lifestore_sales: #ciclo para acumular el número de devoluciones
        if sale[4]==1:
            num_devolciones+=1
    print("Número de devoluciones en el año:")
    print(num_devolciones)

    #se calcula cuanto sería el ingreso si se descuentan las devoluciones
    ingresos_sin_devoluciones=ingresos_total-cantidad_en_devoluciones
    print("Los ingresos descontando las devoluciones son:")
    print("$",ingresos_sin_devoluciones)

    return 0

#función para obtener los 5 meses con mmás ventas en el año
def meses_con_mas_ventas():
    #lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
    #lifestore_products = [id_product, name, price, category, stock]

    ventas_mes=[ # se define una lista con los meses
        ["enero",0],
        ["febrero",0],
        ["marzo",0],
        ["abril",0],
        ["mayo",0],
        ["junio",0],
        ["julio",0],
        ["agosto",0],
        ["septiembre",0],
        ["octubre",0],
        ["noviembre",0],
        ["diciembre",0],
    ]

    for sale in lifestore_sales: #ciclo para acumular las ventas en cada mes
        fecha_venta=sale[3]
        if sale[4]==0: #para considerar aquellas ventas sin devoluciones
            if "/01/" in fecha_venta:
                ventas_mes[0][1]+=1
            elif "/02/" in fecha_venta:
                ventas_mes[1][1]+=1
            elif "/03/" in fecha_venta:
                ventas_mes[2][1]+=1
            elif "/04/" in fecha_venta:
                ventas_mes[3][1]+=1
            elif "/05/" in fecha_venta:
                ventas_mes[4][1]+=1
            elif "/06/" in fecha_venta:
                ventas_mes[5][1]+=1
            elif "/07/" in fecha_venta:
                ventas_mes[6][1]+=1
            elif "/08/" in fecha_venta:
                ventas_mes[7][1]+=1
            elif "/09/" in fecha_venta:
                ventas_mes[8][1]+=1
            elif "/10/" in fecha_venta:
                ventas_mes[9][1]+=1
            elif "/11/" in fecha_venta:
                ventas_mes[10][1]+=1
            else: 
                ventas_mes[11][1]+=1
    print("Las ventas por mes son: ")
    for venta in ventas_mes:
        print(f"* {venta[0]} con {venta[1]} ventas")

    top_ventas=[]
    max=0
    mes=""
    id_mes=1
    for venta in ventas_mes: #obtener el mes con más ventas
        if ventas_mes[id_mes-1][1]>max: 
            max=ventas_mes[id_mes-1][1]
            mes=ventas_mes[id_mes-1][0]
        id_mes+=1
    
    for indice in range(5): #se establece el top 5
        if indice==0: 
            top_ventas.append([mes,max])
        else: 
            valor=[0,0]
            for venta in ventas_mes:
                decision=True
                for i in top_ventas:
                    c=venta[0]!=i[0]
                    if c==False:
                        decision=False
                if venta[1]>=valor[1] and venta[1]<=top_ventas[indice-1][1] and decision==True: 
                    valor=venta
            top_ventas.append(valor) #se agregan los meses con más ventas a la lista top_ventas
    print("Los 5 meses con más ventas son: ")
    for venta in top_ventas:
        print(f"* {venta[0]} con {venta[1]} ventas")

    return 0

if __name__ == "__main__":

    username = input('Ingrese su nombre de usuario:\n > ')
    password = input('Ingrese la contraseña:\n > ')
    entrada=login(username, password)
    
    if entrada==True:
        mes=define_mes() #opciones, del "/01/" al "/12/", "/13/" (todo el año) y 0 (salir)

    if entrada==True and mes!=0:
        mayores_ventas(mes)
        print(" ")
        mayores_busquedas()
        print(" ")
        menores_ventas(mes)
        print(" ")
        menores_busquedas()
        print(" ")
        resena(mes)
        print(" ")
        if mes!="/13/":
            ingresos_ventas_promedio(mes) 
            print(" ")
        total_anual()
        print(" ")
        meses_con_mas_ventas()
