#!/bin/python3
import pandas as pd
import sys

CODCENTRO='28039891'

if len(sys.argv)<2:
    print("Especifica fichero con datos")

print("Formato")
print("Nombre,Primer apellido,Segundo apellido,Nº id. Alumno,Unidad")

listado = pd.read_csv(sys.argv[1])
listado['centro']='28039891'
listado['Segundo apellido']=listado['Segundo apellido'].fillna('')
listado['apellido']=listado['Primer apellido'] + ' ' + listado['Segundo apellido']
listado['apellido']=listado['apellido'].str.strip()
listado['apellido_ascii']=listado['apellido'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
listado['Unidad']=listado['Unidad'].fillna('SIN_UNIDAD')

listado = listado.sort_values(by=['Unidad','apellido_ascii','Nombre'])
unidades = listado.Unidad.unique()

for unidad in unidades:
    filtrado = listado[listado.Unidad == unidad]
    filtrado.to_csv(
                path_or_buf='alta_'+unidad+'.csv',
                columns=['centro','Nombre', 'apellido','Nº id. Alumno'],
                index=False,
                header=False,
                encoding='utf-8'
            )
