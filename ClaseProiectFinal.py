class Job:
    def __init__(self, titlu, salariu):
        self.titlu = titlu
        self.salariu = salariu

    def obtine_salariu(self):
        return self.salariu


class ContBancar:
    def __init__(self, sold_initial=0):
        self.sold = sold_initial

    def depune_bani(self, suma):
        self.sold += suma
        return f"Ați primit {suma} lei. Sold curent: {self.sold} lei."

    def retrage_bani(self, suma):
        if suma <= self.sold:
            self.sold -= suma
            return f"Ați retras {suma} lei. Sold curent: {self.sold} lei."
        else:
            return "Fonduri insuficiente."


class Persoana:
    def __init__(self, nume, job, cont_bancar):
        self.nume = nume
        self.job = job
        self.cont_bancar = cont_bancar

    def primeste_salariu(self):
        salariu = self.job.obtine_salariu()
        self.cont_bancar.depune_bani(salariu)
        return f"{self.nume} a primit salariul de {salariu} lei."

    def cheltuie(self, suma):
        return self.cont_bancar.retrage_bani(suma)


# Se creeaza obiecte pentru fiecare clasa
job_programator = Job(titlu="Programator", salariu=7000)
cont_persoana = ContBancar(sold_initial=1000)
persoana1 = Persoana(nume="Alina", job=job_programator, cont_bancar=cont_persoana)

# Testam functiile claselor
print(persoana1.primeste_salariu())
print(persoana1.cheltuie(2000))
