#Exceptii
# print('Before')
#
#
# try:
#     list = [1, 2, 3]
#     list[6]
# except IndexError as e:
#     print(e)
#
#
# print('After')
#
# x = 'str'
#
# if type(x) is int:
#     print('Ai folosit un tip de date valid')
# else:
#     raise TypeError('Folsiti doar tipul int')


# try:
#     x = 10
#     rez = x / 0
#     print(rez)
# except ZeroDivisionError:
#     print('Impartirea cu zero nu are sens')



# try:
#     # x = 'salut'
#     print(x)
# except TypeError as e: #  e reprezinta o variabila in care se salveaza eroarea
#                         # generata de exectiile predefinite gen: IndexError, TypeError, etc
#     print(e)
#
# try:
#   print(x)
# except:
#   print("An exception occurred")

# finally:
#     print('In concluzie am ')

# Inheritance - mostenire

# class Chef:
#     tava = 'Am o tava si mai faina'
#     def make_salad(self):
#         print('Pot sa gatesc salata')
#
#     def make_soup(self):
#         print('Pot sa gatesc supa')
#
# class Chef2:
#     tava2 = "Am o tava faina"
#     def make_salad2(self):
#         print('Pot sa gatesc salata2')
#
#     def make_soup2(self):
#         print('Pot sa gatesc supa2')
#
#
# class ChefJaponez(Chef, Chef2):
#
#     def make_sushi(self):
#         print('Pot sa gatesc sushi')
#
#
# class ChefItalian(Chef, Chef2):
#
#     def make_pizza(self):
#         print('Pot sa gatesc pizza')
#
# class Chef2:
#     tava2 = 1
#     def make_salad2(self):
#         print('Pot sa gatesc salata2')
#
#     def make_soup2(self):
#         print('Pot sa gatesc supa2')
#
#
# std_jap = ChefJaponez()
# std_jap.make_salad()
# std_jap.make_soup()
# std_jap.make_sushi()
# print(std_jap.tava)
#
# std_it = ChefItalian()
# std_it.make_salad()
# std_it.make_soup()
# std_it.make_pizza()
# print(std_it.tava2)


# Polymorphism

# print(len('testrewtdsfgsdfgsdfg'))
#
# print(len([1, 2, 3, 10, 20, 30]))

# class Romania():
#     def language(self):
#         print('Romanian')
#
# class USA():
#     def language(self):
#         print('English')
# obj_ro = Romania()
# obj_usa = USA()
# obj_usa.language()
# obj_ro.language()
#
# for country in (obj_ro, obj_usa):
#     country.language()


# def adunare(x, y, z=0): # atribute in momentul in care definim functia
#     # print(x)
#     # print(y)
#     # print(z)
#
#     return x + y + z
#
#
# print('Prima adunare', adunare(4, 67, 5)) # argumente in momentul in care apelam functia
# #
# #
# print('A doua adunare', adunare(2, 3, 9))
# #
# print('A treia adunare', adunare(2, 3, 4))

# class Romania:
#     def language(self):
#         print('Romaneste')
#
#     def danseaza(self):
#         print('Dans romanesc')
#
# class Italia:
#     def language(self):
#         print('Italiana')
#
#     def danseaza(self):
#         print('Dans italian')
#
# class Brazilia:
#     def language(self):
#         print('Portrugheza')
#
#
#     def danseaza(self):
#         print('Dans portughez')
#
#
# x_ro = Romania()
# x_it = Italia()
# x_br = Brazilia()
#
#
# for tara in (x_ro, x_br, x_it):
#     tara.language()
#     tara.danseaza()

# exemplu de polimorfism + mostenire
# class Pasari:
#
#     def descriere(self):
#         print('Exista mai multe specii de pasari')
#
#     def zboara(self):
#         print('Majoritatea pasarilor pot sa zboare')
#
#     def metoda_test(self):
#         print('Test')
#
#
# class Bufnita(Pasari):
#
#     def descriere(self):
#         print('Bufnitele sunt pasari nocturne')
#
#     def zboara(self):
#         print('Bufnitele pot sa zboare')
#
#     def metoda_test(self):
#         print('Altceva')
#
#
# class Pinguin(Pasari):
#
#     # def descriere(self):
#     #     print('Pinguinii traiesc la Polul Sud')
#
#     def zboara(self):
#         print('Pinguinii nu pot sa zboare')
#
# x_pasari = Pasari()
# x_bufnita = Bufnita()
# x_pinguin = Pinguin()
#
#
# x_pasari.descriere()
# x_pasari.zboara()
# print(' ')
# x_bufnita.descriere()
# x_bufnita.zboara()
# x_bufnita.metoda_test()
# print(' ')
# x_pinguin.descriere()
# x_pinguin.zboara()



# Abstract class

# from abc import ABC, abstractmethod  #  asa se foloseste in python
#  de tinut minte "O Interfata contine doar metode abstracte"
#
# class Car(ABC):
#     @abstractmethod # decorator folosit pentru a evidentia mai bine faptul ca metoda este abstracta
#     def accelereaza(self):
#         """
#         Specificatii pentru metoda accelereaza
#         :return viteza cu care accelereaza de la 0 la 100
#         """
#         raise NotImplementedError
#
#     @classmethod
#     def stop(self):
#         print('Stop')
#
#
# class Ferrari(Car):
#     def accelereaza(self):
#         print('Atinge 100km/h in 2.8 secunde')
#
#
# class Lastun(Car):
#     def accelereaza(self):
#         print('Atinge 100km/h in 14 secunde')
#
# car1 = Ferrari()
# car1.accelereaza()
# car1.stop()
#
# car2 = Lastun()
# car2.accelereaza()
# car2.stop()

#Encapsulation

# cand ascundem atributele si folosim getter, setter si deleter sa ajungem le ele/le stergem
# si metodele pot fi private, nu doar atributele
# le ascundem cu __
# nu toate atributele trebuie sa aiba setter getter si deleter

# class Car:
#     __color = 'albastru'
#
#     def get_color(self): # folosim getter ca sa afisam culoarea
#         return self.__color
#
#     def set_color(self, culoarea_dorita):  #folosim setter ca sa setam o alta culoare
#         self.__color = culoarea_dorita
#
#     def delete_color(self):
#         self.__color = None
#
#     def __hidden(self):
#         pass
# #
#
# volvo = Car()
# print(volvo.get_color())
# volvo.set_color('ROSU')
# print(volvo.get_color())



# class CarPy:
#
#     def __init__(self, color):
#         self.__color = color
#
#     @property # decorator
#     def color(self): # color reprezinta obiectul in spatele in care vom pune metodele
#         return self.__color
#
#     @color.getter
#     def color(self):
#         print(f'Getter: Culoarea este {self.__color}')
#         return self.__color
#
#     @color.setter
#     def color(self, color):
#         print(f'Setter: Noua culoare este {color}')
#
#     @color.deleter
#     def color(self):
#         print(f'Deleter: Am sters culoarea')
#         self.__color = None
#
#
# car2 = CarPy('alb')
# car2.color = 'galben'
# del car2.color
# car2.color = 'Test'
