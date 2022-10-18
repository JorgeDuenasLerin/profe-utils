#!/bin/python3
import pandas as pd
import sys

CODCENTRO='28020910'

if len(sys.argv)<2:
    print("Especifica fichero con datos")

print("Formato")
print("Nombre,Primer apellido,Segundo apellido,Nº id. Alumno,Unidad")

listado = pd.read_csv(sys.argv[1])
listado['centro']=CODCENTRO
listado['Nombre']=listado['NOMBRE'].str.strip()
listado['SEGUNDO APELLIDO']=listado['SEGUNDO APELLIDO'].fillna('')
listado['apellido']=listado['PRIMER APELLIDO'] + ' ' + listado['SEGUNDO APELLIDO']
listado['apellido']=listado['apellido'].str.strip()
listado['apellido_ascii']=listado['apellido'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
listado['Unidad']=listado['UNIDAD'].fillna('SIN_UNIDAD')
listado['id']=listado['NIA'].astype(str).str.pad(8,fillchar='0')

listado = listado.sort_values(by=['Unidad','apellido_ascii','Nombre'])
unidades = sorted(listado.Unidad.unique())

print("Listado de unidades")
for unidad in unidades:
    print(unidad)
    filtrado = listado[listado.Unidad == unidad]
    filtrado.to_csv(
                path_or_buf='alta_'+unidad+'.csv',
                columns=['centro','Nombre', 'apellido','id'],
                index=False,
                header=False,
                encoding='utf-8'
            )
