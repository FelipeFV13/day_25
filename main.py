# with open("weather_data.csv") as data_c:
#     data = data_c.readlines()
#     print(data)

# Para leer archivos csv, usamos la libreria csv
# import csv
#
# with open("weather_data.csv") as data_c:
#     data = csv.reader(data_c)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
# print(temperature)

#-------------------PANDAS------------------------------------

"""pandas es una importnate libreria de python, esta libreria es esencial en manejar y crear
archivos csv, al comprenderla puedo realizar cosas maravillosas en el mundo deanalisis de datos."""
#
# import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
#
# #Data frame = hace referencia a toda la tabla.
# #series=columna
# #row = fila
#
# #podemos trabajar nuestro data frame como un diccionario usando el metodo .to_dict()
# # data_dic = data.to_dict()
# # print(data_dic)
#
# # data_list= data.temp.to_list()
# # promedio = sum(data_list)/len(data_list)
# # print(promedio)
# #
# #
# # promedio = data.temp.mean()
# # print(promedio)
# #
# # # valor maximo
# # print(data.temp.max())
#
# #obtener una fila
#
# #print(data[data.temp == data.temp.max()])
#
# #Ejercicio.
# #obtener la temperatura del dia lunes y pasarla de grados centigrados a celcius.
# monday = data[data.day  == "Monday"]
# change_temp = (int(monday.temp)*(9/5)+32)
# print(f"temperatura de {int(monday.temp)} C a F = {change_temp}")
#
# #crear un archivo data frame desde 0 solo usando un diccionario
#
# note_class ={
#     "students":["Felipe","Diego","Jessik"],
#     "Note":[9,9.5,8.3]
# }
#
# new_data= pd.DataFrame(note_class)
#
# #como pasamos este data frame a un documento .csv
#
# new_data.to_csv("Notas JE")

import pandas as pd

data_s = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#decidi trabajar el data frame como una lista, solo me interesa la serie del color de la ardilla
color_squirrels = data_s["Primary Fur Color"].to_list()

#cree una variable la cuale es un diccionario, va alvergar como clave el color de las ardillas
ardi = {}


#use este bucle for para iterar la lista, con el condicional que excluye el titulo de la serie y agrega los colores
#como las claves del diciconario inicializandolos en 0.
for color in color_squirrels:
    if color != "Primary Fur Color":
        if color not in ardi:
            ardi[color] = 0

#con este bucle comparo si el color que hay en la lista con la clave del diccionari,
#cada vez que un color se repita le suma una unidad a el valor de la clave del diccionario
for a in ardi.keys():
    for color in color_squirrels:
        if color != "Primary Fur Color":
            if a == color:
                ardi[a] += 1

#nueva variable diccionario, la cree para crear los valores del data frame.
new = {}

#esta varaible tipo lista va a guardar los colores
color_ardillas = []
#esta variable va a guardar la cantidad de ardillas por color
cantidad_ardillas = []

#con este bucle for separo las claves de sus valores, y guardo las claves en una variable tipo diccionario
#y los valores en otra varaible tipo diccionario
for a,c in ardi.items():
    color_ardillas.append(a)
    cantidad_ardillas.append(c)


#ingreso los valores
new={"ardillas":color_ardillas,
    "cantidad":cantidad_ardillas
}

#creaccion del nuevo dataFrame
new_data = pd.DataFrame(new)

#convierto ese data frame a un documento .csv
new_data.to_csv("squirrel_count")

#se que parece mucho proceso pero lo cree asi, pensando en que no conosco la cantidad de colores de ardillas,
#por que digamos, en caso que ubieran ardillas de 1000 colores, me tomaria mucho tiempo crear la variable. y
#contar cada una, como lo hizo la profesora angela en la clase.

