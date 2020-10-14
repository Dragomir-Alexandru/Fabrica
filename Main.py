import json

class Fabrica:
    log_token = 0
    functie = ""
    def __init__(self,locatie,productie):
        self.locatie = locatie
        self.productie = productie

    def log_in():
        read_angajati_json = open('Angajati.json', 'r')
        converted_json_dict_angajat = json.load(read_angajati_json)
        read_angajati_json.close()
        log_in = input("Introduceti adresa de e-mail\n=>")
        for i in converted_json_dict_angajat:
            if converted_json_dict_angajat[i]['email'].lower() == log_in.lower():
                print("User valid")
                Fabrica.log_token = 1
                Fabrica.functie = converted_json_dict_angajat[i]['functie']
            else:
                print("User inexistent")
                Fabrica.log_token = 0

class Angajat(Fabrica):

    def __init__(self,nume, prenume, functie, telefon, locatie, productie):
        super().__init__(locatie,productie)
        self.nume = nume
        self.prenume = prenume
        self.telefon = telefon
        self.functie = functie

    def adaugare_angajt():
        read_angajati_json = open('Angajati.json', 'r')
        converted_json_dict_angajat = json.load(read_angajati_json)
        read_angajati_json.close()

        converted_json_dict_angajat[len(converted_json_dict_angajat)+1]:{
            'nume': f"{Angajat.nume}",
            'prenume' : f"{Angajat.prenume}",
            'telefon' : f"{Angajat.telefon}",
            'email' : f"{Angajat.prenume}.{Angajat.nume}@fabrica.ro",
            'functie' : f"{Angajat.functie}"
        }

        angajat_nou_json = json.dumps(converted_json_dict_angajat, indent=4)
        write_angajati_json = open('Angajati.json', 'w')
        write_angajati_json.write(angajat_nou_json)
        write_angajati_json.close()
        return "Angajat adaugat"

Angajat.adaugare_angajt()

class Meniu:
    admin = ['1.Adaugare Angajat', '2.Stergere Angajat', '3.Acces Magazie', '4.Adaugare/Stergere Calificare', '5.Exit']





while True:
    Fabrica.log_in()
    #LOG-IN ADMIN
    if Fabrica.log_token == 1 and Fabrica.functie == "Admin" :
        for i in Meniu.admin:
            print(i)
        x = int(input('=>'))
        if x == 1:
            nume = input('Numele Angajatului\n=>')
            prenume = input('Prenumele Angajatului\n=>')
            telefon = input('Telefon Angajat\n=>')
            functie = input('Functia Angajatului\n=>')
            locatie = input('Locatia Angajatului\n=>')
            productie = input('Productie Angajat\n=>')
            Angajat = Angajat(nume,prenume,functie,telefon, locatie,productie)
            Angajat.adaugare_angajt()


