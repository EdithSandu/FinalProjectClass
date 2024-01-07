from abc import ABC, abstractmethod

# Interfața pentru algoritmul de calculare a salariului
class CalculSalariu(ABC):
    @abstractmethod
    def obtine_salariu(self):
        pass

# Implementare concretă a algoritmului pentru un anumit tip de job
class CalculSalariuProgramator(CalculSalariu):
    def obtine_salariu(self):
        return 5000  # Exemplu: Programatorul primește un salariu fix de 5000 lei

class CalculSalariuManager(CalculSalariu):
    def obtine_salariu(self):
        return 7000  # Exemplu: Managerul primește un salariu fix de 7000 lei

class Job:
    def __init__(self, titlu, calcul_salariu):
        self.titlu = titlu
        self.calcul_salariu = calcul_salariu

    def obtine_salariu(self):
        return self.calcul_salariu.obtine_salariu()

# Clasa pentru a reprezenta un cont bancar
class ContBancar:
    def __init__(self, sold_initial=0):
        self.sold = sold_initial

    def depune_bani(self, suma):
        self.sold += suma
        return f"Ați depus {suma} lei. Sold curent: {self.sold} lei."

    def retrage_bani(self, suma):
        if suma <= self.sold:
            self.sold -= suma
            return f"Ați retras {suma} lei. Sold curent: {self.sold} lei."
        else:
            return "Fonduri insuficiente."

# Clasa pentru a reprezenta o persoană
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


# Creăm obiecte pentru fiecare clasă cu design pattern-ul Strategy
job_programator = Job(titlu="Programator", calcul_salariu=CalculSalariuProgramator())
job_manager = Job(titlu="Manager", calcul_salariu=CalculSalariuManager())
cont_persoana = ContBancar(sold_initial=1000)

persoana1 = Persoana(nume="Alice", job=job_programator, cont_bancar=cont_persoana)

print(persoana1.primeste_salariu())
print(persoana1.cheltuie(2000))
