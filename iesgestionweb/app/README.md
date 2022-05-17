# Introducción

Gestión web


for i in range(100):
  l = Lugar()
  l.lugar = "Aula " + str(i)
  l.save()

import random

for i in range(1000):
  l = Lugar.objects.get(pk=random.randint(1,100))
  inci = Incidencia()
  inci.lugar = l
  inci.text = "Incidencias de algo. " + str(random.randint(10000,1000000))
  inci.estado = random.choice(['R','A','C','P'])
  inci.save()
  #
  for resx in range(random.randint(0,3)):
    res = Respuesta()
    res.incidencia = inci
    res.texto = "Respuesta " + str(resx)
    res.save()
