# import math
# print('Hello world')  # cel mai simplu cod python
# cel mai simplu programa python
#
#
# print('acesta este un comment')
#
# '''
# Comment pe mai multe linii
# Comment pe mai multe linii
# Comment pe mai multe linii
# '''
#
# """
# Comment pe mai multe linii
# Comment pe mai multe linii
# Comment pe mai multe linii
# """
#
#
# CTRL + / = bulk comment
#
# print('Numele meu este Matei')
#
# print("Numele meu este Matei")
#
# print('Mc\'Donalds1\nTest\nTest2\nTest3')  # escapare
# #
# print("Mc'Donalds2")
#
# print('Mc"Donalds')
# #
# print('Mc\"Donalds')
#
# declaram variabilele
# marcaMasina = 'XC90'
# an_fabricatie = 1990
# pret = 7.500
# inmatriculata = False
#
# print(marcaMasina)
# print(an_fabricatie)
# print(pret)
# print(inmatriculata)
#
# suprascriem si schimbam tipul daca dorim
# marcaMasina = 1785
# an_fabricatie = '2005'
# pret = 155.234
# inmatriculata = True
#
# print(marcaMasina)
# print(an_fabricatie)
# print(pret)
# print(inmatriculata)
#
#
# one line initialization
#
# x, y, z = 'test1', 'test2', 'test3'
# #
# print(f'{x} \n{y} \n{z}')
# print(f'Numele meu este {x}')
#
# x = y = z = 799
#
# print(x, y, z)
# print(f'{x} \n{y} \n{z}')
#
# a = 5.5445645645654
# print('{:.5f}'.format(a))
# print(round(a))
#
# rotunjire
# folosim import math
# print(math.floor(a))
# print(math.ceil(a))
#
# type casting
#
# x = int(191238781732)
# y = int(22323.83214234)
# z = int('34324234')
# #
# print(x, y, z)
# print(type(x))
# print(type(y))
# print(type(z))
#
# x = float(1)
# y = float(2.8)
# z = float("r")
# w = float("4.2")
#
# print(x, y, z, w)
# print(type(x))
# print(type(y))
# print(type(z))
#
# x = str("s1")
# y = str(2)
# z = str(3.0)
#
# print(f'{x} \n{y} \n{z}')
# print(type(x))
# print(type(y))
# print(type(z))
#
# functia print
#
# nume = 'Matei'
# prenume = 'Oltean'
# print(nume + prenume)
#
#
# varsta = 32.34
# job = 'tester'
# print('Numele meu este ' + nume + ' si am ' + str(varsta) + ' de ani')
# print(f'Numele meu este {nume} si am {varsta} de ani')  # cea mai buna solutie pentru print, de tinut minte
# print('Numele meu este {0} si am {1} de ani si sunt {2}'.format(nume, varsta, job))
#
#
# assert
#
# a = 1
# b = 2
# c = a + b
# assert c == 3
# print('C este corect')
# myText = 'asdsjhgbfhujwsdgfhjkasdfgajlkfgdkas'
# print(a == 1)
# assert a == 1
# assert myText == 'asdsjhgbfhujwsdgfhjkasdfgajlkfgdkas'
# daca assert-ul e corect, nu o sa existe niciun un feedback vizual
# print('Assertul meu e corect')
# assert a == 2
# print('Nu ajung aici')
#
# input
# se poate face type casting pe input
#
# parola_user = input('Introdu parola\n')
# parola = 'parola1234'
# assert parola_user == parola
# print('Te-ai autentificat cu succes')
#
#
# var = 12345
# user_var = int(input('Introdu un numar de la tastatura\n'))
# assert var == user_var
# print('Cele 2 numere sunt egale')
# print(var + user_var)
#
#
# str index
# indexarea incepe de la 0 !!!! DE TINUT MINTE
# str = 'Acesta este string-ul meu si fac ce vreau cu el'
# print(len(str))
# print(str[46])
# print(str[0])
# print(str[1])
# print(str[2])
# print(str[3])
# print(str[4])
# print(str[5])
#
#
# metode string
#
# print(str.upper())
# print(str.count('e'))
# print(str.replace('e', 'E'))
#
# string slicing
#
# str2 = 'Azi_e_miercuri'
# print(str2[0])
# print(str2[3:5])
# print(str2[:5])  # daca nu punem index de start el porneste by default de la zero
#
# # parcurgere inversa1
# print(str2[::-1])
#
#
# cum determinam ultimul index
# ne folosim de functia len
# dar luand in considerare ca indexarea incepe de la 0, ultimul index va fi len-1
#
# str3 = 'String_de_test'
# print(len(str3))
# last_index = len(str3)-1
# print(str3[last_index])
# print(str3[13])
# print(str3[0:last_index])
# print(str3[0:13:3])
# [0:13:2]
# 0 = indexul de start, 13 = indexul la care se opreste, 2 = din cat in cat "sare"
#
# alte sintaxa
#
# String = 'ASTRINGASTRING'
#
# s1 = slice(3)
# s2 = slice(1, 5, 2)
# s3 = slice(1, 10, 2)
# print(String[s1])
# print(String[s2])
# print(String[s3])
#
#
# mai multe informatii despre string methods
# https://www.w3schools.com/python/python_strings_methods.asp