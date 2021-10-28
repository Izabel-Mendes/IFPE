# -*- coding: utf-8 -*-
import math
from decimal import Decimal

class_inputKM = input("Insira a quilometragem percorrida:")
class_inputDAY = input("Insira a quantidade de dias nas quais o carro foi usado:")

if float(class_inputKM) < 0 : 
    print("Quilometragem inválida")
elif float(class_inputDAY) < 0 :
    print("Insira uma quantidade de dias válida")
elif int(class_inputKM) == 0 and int(class_inputDAY) == 0:
    print("O carro não foi alugado, muito menos utilizado")
elif float(class_inputKM) == 0:
    print("O carro não foi usado, somente a taxa nominal de 60R$/dia será contabilizada")
    print(float(class_inputDAY)*60, "BRL")
else:
    if float(class_inputDAY) < 0:
            print("Quantidade de dias inexistente")
    elif float(class_inputDAY) == 0:
        print("O carro não foi alugado, ainda")
    else:
        x = float(class_inputDAY)*60
        output = round(x,3)
        print(output, "BRL pelos dias de uso do carro")
        x2 = float(class_inputKM)*0.15
        output2 = round(x2,3)
        print(output2, "BRL pela quilometragem que o carro percorreu")
        print(output+output2, "Total em BRL") 