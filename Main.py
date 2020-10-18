import json

class Fabrica:
    log_token = 0
    functie = ""
    def __init__(self,locatie,productie):
        self.locatie = locatie
        self.productie = productie

    def log_in(self):
        read_angajati_json = open('Angajati.json', 'r')
        converted_json_dict_angajat = json.load(read_angajati_json)
        read_angajati_json.close()
        log_in = input("Introduceti adresa de e-mail\n=>")
        lista_angajati = []
        lista_funcite = []
        for i in converted_json_dict_angajat:
            lista_angajati.append(converted_json_dict_angajat[i]['mail'])
            lista_funcite.append(converted_json_dict_angajat[i]['function'])
        for i in lista_angajati:
            if log_in.lower() == i.lower():
                print("User Valid")
                self.log_token = 1
                index_ = lista_angajati.index(i)
                self.functie = lista_funcite[index_]

    def eliminare_angajat(self):
        read_angajati_json = open('Angajati.json', 'r')
        converted_json_dict_angajat = json.load(read_angajati_json)
        read_angajati_json.close()
        print('Angajati curenti:')
        for i in converted_json_dict_angajat:
            print(f"ID:{i}\tNume:{converted_json_dict_angajat[i]['name']} Prenume:{converted_json_dict_angajat[i]['surname']}")
        while True:
            eliminare = input('Scrie ID-ul\n=>')
            if converted_json_dict_angajat[eliminare]['function'] == "Admin":
                print('Nu poti sa stergi Admin')
                continue
            else:
                del converted_json_dict_angajat[f'{eliminare}']
                break
        angajati_actualizati = json.dumps(converted_json_dict_angajat, indent=4)
        actualizare_angajati_json = open('Angajati.json', 'w')
        actualizare_angajati_json.write(angajati_actualizati)
        actualizare_angajati_json.close()

    def adaugare_eliminare_calificare(self,optiune,ID,calificare):
        read_angajati_json = open('Angajati.json', 'r')
        converted_json_dict_angajat = json.load(read_angajati_json)
        read_angajati_json.close()
        if optiune == 1:
            if len(converted_json_dict_angajat[ID]['qualification']) == 0:
                converted_json_dict_angajat[ID]['qualification'] = [calificare]
            else:
                list_qualification = converted_json_dict_angajat[ID]['qualification']
                list_qualification.append(calificare)
                converted_json_dict_angajat[ID]['qualification'] = list_qualification
        if optiune == 2:
            list_qualification = [calificare]
            converted_json_dict_angajat[ID]['qualification'] = list_qualification
        angajat_nou_json = json.dumps(converted_json_dict_angajat, indent=4)
        write_angajati_json = open('Angajati.json', 'w')
        write_angajati_json.write(angajat_nou_json)
        write_angajati_json.close()










class Angajat():

    def __init__(self,nume, prenume, functie, telefon):
        self.nume = nume
        self.prenume = prenume
        self.telefon = telefon
        self.functie = functie

    def adaugare_angajat(self,nume,prenume,telefon,functie,calificare):
        read_angajati_json = open('Angajati.json', 'r')
        converted_json_dict_angajat = json.load(read_angajati_json)
        read_angajati_json.close()

        angajat_nou = {
            'name': nume,
            'surname': prenume,
            'telephone': telefon,
            'mail': f"{prenume}.{nume}@fabrica.ro",
            'function': functie,
            'qualification': calificare
        }
        key_list = list(converted_json_dict_angajat.keys())
        converted_json_dict_angajat[int(key_list[-1])+1]= angajat_nou
        angajat_nou_json = json.dumps(converted_json_dict_angajat, indent=4)
        write_angajati_json = open('Angajati.json', 'w')
        write_angajati_json.write(angajat_nou_json)
        write_angajati_json.close()
        return print('Adaugat')











class Meniu:
    admin = ['1.Adaugare Angajat', '2.Stergere Angajat', '3.Adaugare/Stergere Calificari', '4.Exit']




angajat_curent = Fabrica('Timisoara','Electronice si Electrocasnice')
angajat_curent.log_in()
while True:
    if angajat_curent.log_token == 1 and (angajat_curent.functie == "Admin" or angajat_curent.functie == "Manager") :
        for i in Meniu.admin:
            print(i)
        x = int(input('=>'))
        if x == 1:
            nume = input('Numele Angajatului\n=>')
            prenume = input('Prenumele Angajatului\n=>')
            telefon = input('Telefon Angajat\n=>')
            functie = input('Functia Angajatului\n=>')
            calificare = []
            angajat_nou = Angajat(nume,prenume,functie,telefon)
            angajat_nou.adaugare_angajat(nume,prenume,telefon,functie,calificare)
        if x == 2:
            angajat_curent.eliminare_angajat()
        if x == 3 and (angajat_curent.functie == "Admin" or angajat_curent.functie == "Manager"):
            read_angajati_json = open('Angajati.json', 'r')
            converted_json_dict_angajat = json.load(read_angajati_json)
            read_angajati_json.close()
            for i in converted_json_dict_angajat:
                print(f"ID:{i}\tAngajat: {converted_json_dict_angajat[i]['name']} {converted_json_dict_angajat[i]['surname']}")
            id_angajat = input('Scrie ID-ul angajatului:\n=>')
            optiune = int(input("1.Adaugare calificare\n2.Eliminare calificare\n=>"))
            if optiune == 1:
                qual = input('Adauga calificarea\n=>')
                angajat_curent.adaugare_eliminare_calificare(optiune,id_angajat,qual)
            if optiune == 2:
                qual_list = converted_json_dict_angajat[id_angajat]['qualification']
                print(f"ID:{id_angajat}\tAngajat: {converted_json_dict_angajat[id_angajat]['name']} {converted_json_dict_angajat[id_angajat]['surname']}")
                print('CALIFICARI:')
                for i in qual_list:
                    print(i)
                qual = input('Ce calificare vrei sa ramana. Daca vrei sa elimini toate calificarile scrie ""\n=>')
                angajat_curent.adaugare_eliminare_calificare(optiune, id_angajat, qual)





