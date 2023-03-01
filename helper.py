class Scoala:
    profil_real = 'mate_info'
    profil_uman = 'romana_engleza'
    profil_stiintele_naturii = 'bio_geogra_istorie'
    nr_elevi = 1000
    tip = 'liceu teoretic'

    def __init__(self, tip, profil_real):
        self.tip = tip
        self.profil_real = profil_real

    def inscriere(self):
        print(f'Te-ai inscris la profilul {self.profil_real}')
