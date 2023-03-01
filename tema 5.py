#1 suma a doua numere

# def suma_a_doua_numere(a, b):
#     suma = a + b
#     return suma
#
#
# print(suma_a_doua_numere(6, 123))


#2 TRUE=par FALSE=impar

# def true_false():
#     x = int(input('Introduceti un numar\n'))
#     if x < 0:
#         print('Introduceti un numar par sau impar POZITIV')
#     elif x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# print(true_false())


# #3 nr de caractere
#
#
# def nume_prenume():
#     x = str(input('Introduceti numele\n'))
#     y = str(input('Introduceti prenumele\n'))
#     nr_caractere = len(x) + len(y)
#     return 'Nr de caractere din numele complet este' + ' ' +  str(nr_caractere)
#
#
# print(nume_prenume())

#4 aria dreptunghiului

# def aria_dreptunghi():
#     x = int(input(f'introduceti lungime\n'))
#     y = int(input(f'introduceti latime\n'))
#     aria = x * y
#     return aria
#
#
# print(aria_dreptunghi())


# 5 aria cercului
# import math
#
# def aria_cercului():
#     x = int(input('Introuceti raza cercului\n'))
#     aria = math.pi * x ** 2
#     return aria
#
#
# print(f'Aria cercului este {aria_cercului()}')

#6 caracter

# def caracter():
#     x = str(input('Introduceti un string\n'))
#     y = str(input('Ce caracter doriti sa cautati in string?\n'))
#     if y in x:
#         return True
#     else:
#         return False
#
#
# print(caracter())

#7

# def lower_upper():
#     lower = 0
#     upper = 0
#     x = str(input('Introduceti un string\n'))
#     for letter in x:
#         if letter.isupper():
#             upper += 1
#         else:
#             lower += 1
#     print(f'Literele mari sunt in numar de {upper}')
#     print(f'Literele mici sunt in numar de {lower}')
#
#
# lower_upper()


#8
# def lista_poz():
#     lista_initiala = []
#     lista_pozitiva = []
#     x = int(input('Introduceti nr de elemente ale listei'))
#     # create the list from input elements
#     for i in range(0, x):
#         element = (int(input()))
#         lista_initiala.append(element)
#
#     for number in lista_initiala:
#         if number > 0:
#             lista_pozitiva.append(number)
#     return lista_pozitiva
#
#
# print(f'{lista_poz()}')


#9
# def numere():
#     x = int(input('Primul nr'))
#     y = int(input('Al doilea nr'))
#     if x > y:
#         print(f'Primul nr {x} este mai mare decat al doilea nr {y}')
#     elif x < y:
#         print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
#     else:
#         print('Numerele sunt egale')
#
#
# numere()


#10
# def ex_set():
#     lista_initiala = []
#     x = int(input('Introdu un numar'))
#     y = int(input('Introduceti nr de elemente ale listei'))
#     # create the list from input elements
#     for i in range(0, y):
#         element = (int(input()))
#         lista_initiala.append(element)
#     set_initial = set(lista_initiala)
#
#     if x in set_initial:
#         print('Nu am adaugat numarul in set, exista deja')
#         return False
#     else:
#         set_initial.add(x)
#         print('Am adaugat numarul in set')
#         return True
#
#
# ex_set()


#11
# from calendar import monthrange
#
# def numdays():
#     x = int(input('Introdu anul'))
#     y = int(input('Introdu luna'))
#     numar_de_zile = monthrange(x, y)
#     print(numar_de_zile)
#
#
# numdays()


# def monthrange(year, month):
#     """Return weekday (0-6 ~ Mon-Sun) and number of days (28-31) for
#        year, month."""
#     if not 1 <= month <= 12:
#         raise IllegalMonthError(month)
#     day1 = weekday(year, month, 1)
#     ndays = mdays[month] + (month == February and isleap(year))
#     return day1, ndays

#12


# def calculeaza(a, b):
#     suma = a + b
#     diferenta = a - b
#     inmultirea = a * b
#     impartirea = a / b
#     return suma, diferenta, inmultirea, impartirea
#
#
# a, b, c, d = calculeaza(9, 3)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

#13

# lista1 = [1, 2, 2, 2, 7, 7, 7]
#
#
# def count(lista):
#     cnt = {
#         0: 0,
#         1: 0,
#         2: 0,
#         3: 0,
#         4: 0,
#         5: 0,
#         6: 0,
#         7: 0,
#         8: 0,
#         9: 0
#     }
#     for i in cnt.keys():
#         for j in lista:
#             if i == j:
#                 cnt[i] = cnt[i] + 1
#     for key, value in cnt.items():
#         print(key, ':', value)
#
#
# count(lista1)

# 14

# def max_numere():
#     x = int(input('Introduceti primul numar'))
#     y = int(input('Introduceti al doilea numar'))
#     z = int(input('Introduceti al treilea numar'))
#     return max(x, y, z)
#
#
# print(f'Numarul cel mai mare este {max_numere()}')


#15


# def sum_until():
#     number = int(input("Number: "))
#     sum = 0
#     for i in range(1, number + 1): # asta se face deoarece range-ul se opreste la limita-1, si pentru ca sa se opreasca la numarul dorit ii punem numarul dorit +1
#         sum += i
#     print(sum)
#
#
# sum_until()