from helper import Scoala

# Intalnirea 5  - functie care sa returneze daca un nume este de baiat sau fata
# def gen_nume():
#     nume = input('Scrie numele: \n')
#     if nume[-1] == 'a':
#         print('Acesta este nume de fata.')
#     elif nume == 'Carmen' or nume == 'Beatrice':
#         print('Acesta este nume de fata')
#     else:
#         print('Acesta este nume de baiat')
#
#
# gen_nume()

# def alege_genul():
#     nume = input("Introdu un nume: ")
#     if nume[-1] == "a":
#         print("Numele introdus este de fata.")
#     else:
#         print("Numele introdus este de baiat.")
#
#
# alege_genul()

# def gen_nume():
#     lista_exceptii_fete = ['Carmen', 'Beatrice']
#     lista_exceptii_baieti = []
#     nume = input('Scrie numele: \n')
#     if nume[-1] == 'a':
#         print('Acesta este nume de fata.')
#     elif nume in lista_exceptii_fete:
#         print('Acesta este nume de fata')
#     else:
#         print('Acesta este nume de baiat')
#
#
# gen_nume()

# Intalnirea 6
# Clasa, obiect, constructor, clasa importata din alt fisier

class Car:
    # fields / attributes (atribute = caracteristicile pe care poate sa le aiba clasa Car (masina)
    make = 'Dacia'
    model = None
    year = 2023
    color = 'alb'

    #constructor - dupa atribute si inainte de metode

    def __init__(self, model, color):
        self.model = model
        self.color = color


    # metode (methods) - actiunile pe care poate sa le faca sau sa le suporte clasa noastra
    def accelerate(self):                #  def accelerate(self):
        print('Masina accelereaza')


    def change_color(self, color):
        self.color = color


    def model_masina(self, model):
        self.model = model

    def stop(self):                   # def stop(self):
        print('Masina s-a oprit')



# obiecte  de tipul Car() - ne instantiem/creem masinile pe care vrem sa le vedem/folosim/testam
# fiecare dintre obiecte are acces la toate atributele si metodele clasei
car1 = Car('Duster', 'galben') #  car1 va trebui sa aiba argumentele model si culoare din cauza constructorului
car2 = Car('Logan', 'albastru') #  la fel si car 2 cu argumentele aferente
# car1 = obiect de tip Car()
print(car1.color)
print(car1.model)
print(car1.accelerate())
print(car1.stop())
print(car2.color)
print(car2.model)
print(car2.accelerate())
print(car2.stop())


# scoala1 = Scoala('tip-seral', 'profil_mate_info')
# print(scoala1.profil_real)
# print(scoala1.tip)
# print(scoala1.nr_elevi)
#
# scoala2 = Scoala('tip-liceu_teoretic', 'profil_uman')
# print(scoala2.profil_real)
# print(scoala2.tip)
# print(scoala2.nr_elevi)