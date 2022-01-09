# -*- coding: utf-8 -*-
#PROYECTO 02 BLANCAS SERGIO

def flujo_de_rutas(lista_rutas):
    #Crea una lista con la ruta y los viajes totales de esa ruta, además de ordenarlos
    
    flujo_rutas=[]
    ruta_contador=[0,0]
    for ruta in lista_rutas:
        contador=lista_rutas.count(ruta)
        ruta_contador[0]=contador
        ruta_contador[1]=ruta
        
        decision=True
        for flujo in flujo_rutas: #Este ciclo es para evitar que una misma ruta se repita
            c=flujo[1]!=ruta
            if c==False:
                decision=False
                
        if decision==True:
            flujo_rutas.append(ruta_contador)
            
        ruta_contador=[0,0]
    
    flujo_rutas.sort()
    flujo_rutas.reverse()
    
    return flujo_rutas

def rutas():
    lista_rutas_exp=[]
    lista_rutas_imp=[]
    ruta=[0,0,0]
    with open("synergy_logistics_database.csv","r") as archivo_csv:
        lector=csv.reader(archivo_csv)
        for linea in lector: #bucle para obtener el origin, destination y transport_mode de las rutas de exportación e importación
            if linea[2]!="origin": #no toma el encabezado
                if linea[1]=="Exports":
                    ruta[0]=linea[2] #origin
                    ruta[1]=linea[3] #destination
                    ruta[2]=linea[7] #medio de transporte
                    lista_rutas_exp.append(ruta)
                    ruta=[0,0,0]
                else: #imports
                    ruta[0]=linea[2] #origin
                    ruta[1]=linea[3] #destination
                    ruta[2]=linea[7] #medio de transporte
                    lista_rutas_imp.append(ruta)
                    ruta=[0,0,0]
    
    #rutas de exportación
    flujo_rutas_exp=flujo_de_rutas(lista_rutas_exp)
    print("El total de rutas de exportación es:",len(flujo_rutas_exp))
    
    total_rutas_exp=0
    for ruta in flujo_rutas_exp:
        total_rutas_exp+=ruta[0]
    print("El número total de viajes en exportación es:",total_rutas_exp)
    
    n=0
    print("Las 10 rutas de exportación más demandadas son:")
    for ruta in flujo_rutas_exp:
        if n<10:
            print(f"De {ruta[1][0]} a {ruta[1][1]} por medio {ruta[1][2]} con {ruta[0]} viajes")
        else:
            break
        n+=1
    
    print(" ")
    
    #rutas de importación
    flujo_rutas_imp=flujo_de_rutas(lista_rutas_imp)
    print("El total de rutas de importación es:",len(flujo_rutas_imp))
    
    total_rutas_imp=0
    for ruta in flujo_rutas_imp:
        total_rutas_imp+=ruta[0]
    print("El número total de viajes en importación es:",total_rutas_imp)
    
    n=0
    print("Las 10 rutas de importación más demandadas son:")
    for ruta in flujo_rutas_imp:
        if n<10:
            print(f"De {ruta[1][0]} a {ruta[1][1]} por medio {ruta[1][2]} con {ruta[0]} viajes")
        else:
            break
        n+=1
    
    print(" ")
    
    return 0

def transporte():
    #Función para obtener y ordenar el valor acumulado de cada modo de transporte
    
    valor_modo_transporte_exp={}
    valor_modo_transporte_imp={}
    
    with open("synergy_logistics_database.csv","r") as archivo_csv:
        lector=csv.reader(archivo_csv)
        for linea in lector: #El siguiente ciclo es para agregar las claves al diccionario de modos de transporte
            if linea[7]!="transport_mode":
                if linea[1]=="Exports":
                    valor_modo_transporte_exp[linea[7]]=0 #agrega primer valor
                    
                else:
                    valor_modo_transporte_imp[linea[7]]=0 #agrega primer valor
    
    with open("synergy_logistics_database.csv","r") as archivo_csv:
        lector=csv.reader(archivo_csv)
        for linea in lector: #El siguiente ciclo es para acumular el total_value en los valores del diccionario para cada modo
            if linea[7]!="transport_mode":
                if linea[1]=="Exports":
                    valor_modo_transporte_exp[linea[7]]+=int(linea[9]) #acumulación de valores
                    
                else:
                    valor_modo_transporte_imp[linea[7]]+=int(linea[9]) #acumulación de valores
    
    print("Los medios de transporte más utilizados (en orden) para exportación son:")
    #Transformar el diccionario en lista y ordenarlo
    lista_valor_modo_transporte_exp=list(zip(valor_modo_transporte_exp.values(),valor_modo_transporte_exp.keys()))
    lista_valor_modo_transporte_exp.sort()
    lista_valor_modo_transporte_exp.reverse()
    for modo in lista_valor_modo_transporte_exp:
        print(f"Modo: {modo[1]}, con un valor de: {modo[0]}")
    
    print(" ")
    
    print("Los medios de transporte más utilizados (en orden) para importación son:")
    lista_valor_modo_transporte_imp=list(zip(valor_modo_transporte_imp.values(),valor_modo_transporte_imp.keys()))
    lista_valor_modo_transporte_imp.sort()
    lista_valor_modo_transporte_imp.reverse()
    for modo in lista_valor_modo_transporte_imp:
        print(f"Modo: {modo[1]}, con un valor de: {modo[0]}")
    
    return 0

def transporte_pandas():
    #Obtener algunas gráficas
    import pandas as pd
    
    synergy_df = pd.read_csv('synergy_logistics_database.csv', index_col=0, encoding='utf-8', parse_dates=[4, 5])
    
    import seaborn as sns
    
    datos=synergy_df.copy()
    datos['year_month'] = datos['date'].dt.strftime('%Y-%m')
    
    #Gráfica de exportación
    datos_exp=datos[datos["direction"]=="Exports"].copy()
    datos_year_month_exp = datos_exp.groupby(['year_month', 'transport_mode','direction'])
    serie_exp = datos_year_month_exp.sum()["total_value"]
    datos_frame_exp = serie_exp.to_frame().reset_index()
    datos_frame_exp = datos_frame_exp.pivot(index='year_month', columns= 'transport_mode', values='total_value')
    sns.lineplot(data=datos_frame_exp)
    
    #Gráfica de exportación para el 2020 (ejemplo)
    datos_2020_exp = synergy_df[synergy_df['year'] == '2020'].copy()
    datos_2020 = datos_2020_exp[datos_2020_exp["direction"]=="Exports"].copy()
    datos_2020['month'] = datos_2020['date'].dt.month
    datos_por_mes = datos_2020.groupby(['month', 'transport_mode'])
    serie = datos_por_mes.sum()['total_value']
    data_2020 = serie.to_frame().reset_index()
    data_2020 = data_2020.pivot('month', 'transport_mode', 'total_value')
    sns.lineplot(data=data_2020)
    
    #Gráfica de importación
    datos_imp=datos[datos["direction"]=="Imports"].copy()
    datos_year_month_imp = datos_imp.groupby(['year_month', 'transport_mode','direction'])
    serie_imp = datos_year_month_imp.sum()["total_value"]
    datos_frame_imp = serie_imp.to_frame().reset_index()
    datos_frame_imp = datos_frame_imp.pivot(index='year_month', columns= 'transport_mode', values='total_value')
    sns.lineplot(data=datos_frame_imp)
    
    #Gráfica de importación para el 2020 (ejemplo)
    datos_2020_imp=synergy_df[synergy_df['year'] == '2020'].copy()
    datos_2020=datos_2020_imp[datos_2020_imp["direction"]=="Imports"].copy()
    datos_2020['month']=datos_2020['date'].dt.month
    datos_por_mes=datos_2020.groupby(['month', 'transport_mode'])
    serie=datos_por_mes.sum()['total_value']
    data_2020=serie.to_frame().reset_index()
    data_2020=data_2020.pivot('month', 'transport_mode', 'total_value')
    sns.lineplot(data=data_2020)
    
    return 0

def top_paises_rutas(lista):
    #obtención del top 80%
    top=[]
    acumulado=0
    n=0
    for pais in lista:
        if acumulado<=80:
            acumulado+=pais[2]
            top.append(pais)
            n+=1
    
    return top

def paises():
    #Función para obtener aquellos países con la mayor participación del valor total
    valor_pais_exp={}
    valor_pais_imp={}
    
    with open("synergy_logistics_database.csv","r") as archivo_csv:
        lector=csv.reader(archivo_csv)
        for linea in lector: #El siguiente ciclo es para agregar las claves al diccionario de los países (los "clientes")
            if linea[2]!="origin":
                if linea[1]=="Exports": 
                    valor_pais_exp[linea[2]]=0 #agrega el primer valor (origin)
                    
                else:
                    valor_pais_imp[linea[3]]=0 #agrega el primer valor (destination)
    
    with open("synergy_logistics_database.csv","r") as archivo_csv:
        lector=csv.reader(archivo_csv)
        for linea in lector: #El siguiente ciclo es para acumular el total_value en los valores del diccionario para cada país
            if linea[2]!="origin":
                if linea[1]=="Exports":
                    valor_pais_exp[linea[2]]+=int(linea[9]) #obtiene el acumulado
                    
                else:
                    valor_pais_imp[linea[3]]+=int(linea[9]) #obtiene el acumulado
    
    lista_exp_mod=[]
    lista_imp_mod=[]
    
    #Obtención de porcentajes para exportación
    lista_valor_pais_exp=list(zip(valor_pais_exp.values(),valor_pais_exp.keys())) #transforma el diccionario en lista
    for pais in lista_valor_pais_exp:
        lista_exp_mod.append(list(pais)) #creación de una lista modificable (sin tuplas dentro de la lista)
    for pais in lista_exp_mod: #se agrega el porcentaje que representa el valor del país
        pais.append(pais[0]/sum(valor_pais_exp.values()))
        pais[2]*=100
    lista_exp_mod.sort()
    lista_exp_mod.reverse()
    
    #Obtención de porcentajes para importación
    lista_valor_pais_imp=list(zip(valor_pais_imp.values(),valor_pais_imp.keys()))
    for pais in lista_valor_pais_imp:
        lista_imp_mod.append(list(pais))
    for pais in lista_imp_mod:
        pais.append(pais[0]/sum(valor_pais_imp.values()))
        pais[2]*=100
    lista_imp_mod.sort()
    lista_imp_mod.reverse()    
    
    print("Los países que representan alrededor del 80% del valor en exportación son:")
    lista_paises_exp=top_paises_rutas(lista_exp_mod) #obtiene el 80%
    for pais in lista_paises_exp:
        print(f"País: {pais[1]}, con un valor de: {pais[0]} siendo el: {pais[2]}% del valor total")
    
    print(" ")
    
    print("Los países que representan alrededor del 80% del valor en importación son:")
    lista_paises_imp=top_paises_rutas(lista_imp_mod)
    for pais in lista_paises_imp:
        print(f"País: {pais[1]}, con un valor de: {pais[0]} siendo el: {pais[2]}% del valor total")
    
    print(" ")
    print("Para mayor información de estos paises, explore la función 'paises_pandas'.")
    
    return 0

def paises_pandas():
    import pandas as pd
    
    synergy_df = pd.read_csv('synergy_logistics_database.csv', index_col=0, encoding='utf-8', parse_dates=[4, 5])
    
    agrupados = synergy_df.groupby(by=['direction','origin', 'destination','transport_mode'])
    descripcion = agrupados.describe()

    datos_clas=synergy_df[synergy_df["direction"]=="Imports"].copy() #Exports, Imports
    
    datos_grupos= datos_clas.groupby(by=["destination"]) #Origin, Destination
    suma=datos_grupos.sum()["total_value"]
    #print(suma)
    
    return 0

def conjuntos_columnas():
    with open("synergy_logistics_database.csv","r") as archivo_csv:
        lector=csv.reader(archivo_csv) #esto lee el archivo linea por línea
        
        #Lo siguiente es para conocer las categorías de las distintas columnas
        lista_direction=[]
        lista_origin=[]
        lista_destination=[]
        lista_year=[]
        lista_product=[]
        lista_transport=[]
        lista_company=[]
        
        for linea in lector:
            if linea[1]=="direction":
                continue
            lista_direction.append(linea[1])
            lista_origin.append(linea[2])
            lista_destination.append(linea[3])
            lista_year.append(linea[4])
            lista_product.append(linea[6])
            lista_transport.append(linea[7])
            lista_company.append(linea[8])
        
    conjunto_direction=set(lista_direction)
    conjunto_origin=set(lista_origin)
    conjunto_destination=set(lista_destination)
    conjunto_year=set(lista_year)
    conjunto_product=set(lista_product)
    conjunto_transport=set(lista_transport)
    conjunto_company=set(lista_company)
    
    print("Direction:")
    print(conjunto_direction)
    print(" ")
    print("Países de origen:")
    print(conjunto_origin)
    print(" ")
    print("Países destino:")
    print(conjunto_destination)
    print(" ")
    print("Años:")
    print(conjunto_year)
    print(" ")
    print("Productos:")
    print(conjunto_product)
    print(" ")
    print("Modos de transporte:")
    print(conjunto_transport)
    print(" ")
    print("Compañías:")
    print(conjunto_company)
    print(" ")
    
    return 0

if __name__ == "__main__":
    import csv
    
    opcion=0
    opcion=input("¿Desea conocer los conjuntos de las columnas del archivo?(si/no):")
    if opcion=="si":
        conjuntos_columnas() #Para conocer las categorías de las columnas
        
    opcion=0
    print("Opciones: \n 1-Rutas de importación y exportación \n 2-Medio de transporte \n 3-Valor total de importaciones y exportaciones \n 4-Salir")
    opcion=int(input("Ingrese número de opción:"))
    print(" ")
    
    if opcion==1:
        #Definir rutas más usadas
        rutas()
        print("Fin programa")
    elif opcion==2:
        #Definir medios de transporte más utilizados
        transporte()
        transporte_pandas()
        print("Fin programa")
    elif opcion==3:
        #Definir paises que generan mayor valor
        paises()
        paises_pandas()
        print("Fin programa")
    else:
        print("Fin programa")
        
        