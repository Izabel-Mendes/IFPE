
# -*- coding: utf-8 -*-
while True:
  try:
    inputAP1 = float(input("Insira o valor da aposta do primeiro apostador:"))
    inputAP2 = float(input("Insira o valor da aposta do segundo apostador:"))
    inputAP3 = float(input("Insira o valor da aposta do terceiro apostador:"))
    inputP = float(input("Insira o prêmio atualmente acumulado:"))
    break
  except:
      print("Insira apenas números")

if float(inputAP1) < 0 or float(inputAP2) < 0 or float(inputAP3) < 0:
 print("Não existe aposta negativa")
elif float(inputAP1) + float(inputAP2) + float(inputAP3) == 0:
  print("Não foram feitas apostas")
elif float(inputP) < 0:
  print("Não existe prêmio negativo")
elif float(inputP) == 0:
  print("Não existe prêmio acumulado")
else:
  inputT = (inputAP1 + inputAP2 + inputAP3)
  z = float(inputAP1)/float(inputT)
  x = float(inputAP2)/float(inputT)
  y = float(inputAP3)/float(inputT)

  premio = float(inputAP1) + float(inputAP2) + float(inputAP3) + float(inputP)

  AP1 = premio*z
  AP2 = premio*x
  AP3 = premio*y

  print(premio,"BRL  É o prêmio total acumulado")
  print(AP1,"BRL  É o quanto receberá o Apostador 1")
  print(AP2,"BRL  É o quanto receberá o Apostador 2")
  print(AP3,"BRL  É o quanto receberá o Apostador 3")