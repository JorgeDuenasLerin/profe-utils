#!/bin/python3
import pandas as pd
import sys
import unidecode
import argparse

text = 'Genera el fichero para creación masiva de usuarios.'
parser = argparse.ArgumentParser(description=text)
parser.add_argument('--ficheroAlumnos', type=str, required=True, help="Fichero de alumnos")
parser.add_argument('--domain', type=str, required=True, help="dominio")
parser.add_argument('--subfix', type=str, required=True, help="subfijo")
parser.add_argument('--tutor', type=str, required=True, help="tutor")
parser.add_argument('--salida', type=str, required=True, help="salida")
args = parser.parse_args()


data = pd.read_csv(args.ficheroAlumnos, keep_default_na=False)

# Nombre de usuario,Nombre,Apellido,Nombre para mostrar,
# nombre@dominio.com,nombre,apellido1 apellido2,nombre a mostrar,

# Pandas
# Nombre,Apellido1,Apellido2,Ciclo,Turno

data['Apellido1'] = data['Apellido1'].str.replace(" ","") 
data['Apellido2'] = data['Apellido2'].str.replace(" ","") 
data['Nombre'] = data['Nombre'].str.replace(" ","") 
data['Ciclo'] = data['Ciclo'].str.replace(" ","") 
data['Turno'] = data['Turno'].str.replace(" ","")

data['Apellido'] = data['Apellido1'] + ' ' + data['Apellido2']
data['Apellido'] = data['Apellido'].str.replace(" ","") 
data['Nombre de usuario'] = data['Nombre'] + data['Apellido1'] + args.subfix + '@' + args.domain
data['Nombre de usuario'] = data['Nombre de usuario'].apply(lambda x: unidecode.unidecode(x.lower()))
data['Nombre para mostrar'] = data['Nombre'] + ' ' + data['Apellido1'] + ' ' + data['Apellido2']
data['Nombre para mostrar'] = data['Nombre para mostrar'].str.strip()

# Dirección de correo electrónico alternativa
# tutor@email.com
data['Dirección de correo electrónico alternativa'] = args.tutor

# Puesto,Departamento,Número del trabajo,Teléfono de la oficina,Teléfono móvil,Fax,Dirección de correo electrónico alternativa,Dirección,Ciudad,Estado o provincia,Código postal,País o región
# puesto,departamento,9166666666,9166666666,9166666666,9166666666,tutor@email.com,Caoba 1,Madrid,Madrid,28000,España
data['Puesto'] = 'Alumno'
data['Departamento'] = data['Ciclo']
data['Número del trabajo'] = '915064610'
data['Teléfono de la oficina'] = '915064610'
data['Teléfono móvil'] = '915064610'
data['Fax'] = '915064610'
data['Dirección'] = "Calle Caoba 1"
data['Ciudad'] = 'Madrid'
data['Estado o provincia'] = 'Madrid'
data['Código postal'] = '28005'
data['País o región'] = 'España'

columns=[
    "Nombre de usuario","Nombre","Apellido","Nombre para mostrar","Puesto","Departamento",
    "Número del trabajo","Teléfono de la oficina","Teléfono móvil","Fax",
    "Dirección de correo electrónico alternativa","Dirección","Ciudad","Estado o provincia",
    "Código postal","País o región"]

data.to_csv(
    args.salida,
    columns=columns,
    index=False
)
print(data)