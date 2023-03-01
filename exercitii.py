# def gen_nume():
#     lista_exceptii_fete = ['Carmen', 'Beatrice']
#     lista_exceptii_baieti = ['Mircea', 'Luca']
#     nume = input('Scrie numele:\n')
#     if nume in lista_exceptii_fete:
#         print("Nume de fata")
#     elif nume in lista_exceptii_baieti:
#         print("Nume de baiat")
#     elif nume[-1] == 'a' and nume not in lista_exceptii_fete:
#         print("Nume de fata")
#     else:
#         print("Nume de baiat")
#
#
# gen_nume()


class ContBancar:
    # iban = 'iban'
    # titular_cont = 'titular_cont'
    # sold = 1500
    # suma = 500

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = int(sold)

    def afisare_sold(self):
        print(f'Titularul:', self.titular_cont, 'are in contul', self.iban, 'suma de', str(self.sold))

    def debitare_cont(self, suma):
        if int(suma) > self.sold:
            print(f'Fonduri insuficiente in contul {self.iban}')
        else:
            self.sold -= int(suma)
            print(f'S-a debitat suma de {int(suma)} lei din contul {self.iban} Soldul curent este {self.sold} lei.')
            return self.sold

    def creditare_cont(self, suma):
        self.sold += int(suma)
        print(f'S-a creditat suma de {int(suma)}lei in contul {self.iban} Soldul curent este {self.sold} lei.')


cont = ContBancar('TESADSERAD', 'Matei Oltean', '1500')
cont.afisare_sold()
cont.debitare_cont('200')
cont.creditare_cont('500')
