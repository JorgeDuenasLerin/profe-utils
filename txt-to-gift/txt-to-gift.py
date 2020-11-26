#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
import html
import re
import base64

parser = argparse.ArgumentParser("txt-to-gift")
parser.add_argument("categoria", help="Categoría para las preguntas Moodle.", type=str)
parser.add_argument("fichero_preguntas", help="Fichero txt con las preguntas.", type=str)
args = parser.parse_args()

def limpia_caracteres(info):
    info = info.rstrip('\n')
    info = html.escape(info)
    info = re.sub(r'([={}:~%#])', r'\\\1', info.rstrip('\n'))
    return info

def carga_imagen(ruta):
    ruta = ruta.rstrip('\n')
    if ruta == "":
        return ""
    else:
        with open(ruta, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        return "<img src='data:image;base64,{0}'>".format(image_data)

#print("Abriendo fichero lectura {0}".format(args.fichero_preguntas))
fpreguntas = open(args.fichero_preguntas, "r")

print("//Generado por txt-to-gift.\n")
print("//Programado por: Jorge Dueñas Lerín.\n")
print("$CATEGORY:{0}\n".format(args.categoria))

pregunta = fpreguntas.readline()

while pregunta:
    pregunta = limpia_caracteres(pregunta)
    cuerpo = limpia_caracteres(fpreguntas.readline())
    img = fpreguntas.readline() # Quizá no haya
    op1 = limpia_caracteres(fpreguntas.readline()) # Siempre la correcta, Moodle desordena
    op2 = limpia_caracteres(fpreguntas.readline())
    op3 = limpia_caracteres(fpreguntas.readline())
    op4 = limpia_caracteres(fpreguntas.readline())

    fpreguntas.readline()

    pregunta_gift = "::{0}::[html]{1}{2}{{\n".format(pregunta, cuerpo, carga_imagen(img))
    pregunta_gift += "=<p>{0}</p>\n".format(op1)
    pregunta_gift += "~%-33.33333%<p>{0}</p>\n".format(op2)
    pregunta_gift += "~%-33.33333%<p>{0}</p>\n".format(op3)
    pregunta_gift += "~%-33.33333%<p>{0}</p>\n".format(op4)
    pregunta_gift += "}}\n\n".format(op4)

    print(pregunta_gift)

    pregunta = fpreguntas.readline()

fpreguntas.close()
