import json
import time

class Fabrica:
    log_token = 0
    functie = ""
    calificare = []
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
        lista_calificare = []
        for i in converted_json_dict_angajat:
            lista_angajati.append(converted_json_dict_angajat[i]['mail'])
            lista_funcite.append(converted_json_dict_angajat[i]['function'])
            lista_calificare.append(converted_json_dict_angajat[i]['qualification'])
        for i in lista_angajati:
            if log_in.lower() == i.lower():
                print("User Valid")
                self.log_token = 1
                index_ = lista_angajati.index(i)
                self.functie = lista_funcite[index_]
                self.calificare = lista_calificare[index_]

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

    def adaugare_depozit(self):
        read_depozit_json = open('Depozit.json', 'r')
        dict_depozit = json.load(read_depozit_json)
        read_depozit_json.close()

        print('PRODUSE:')
        for i in dict_depozit:
            print(i)

        produs = input('Scrie produsul pe care vrei sa il alimentezi\n')
        cantitate = int(input('Scrie cantitatea pe care o adaugi\n'))

        dict_depozit[produs.capitalize()] += cantitate
        time.sleep(2)
        print('Depozit actualizat')
        print('Daca doresti sa mai adaugi, repeta procesul')

        depozit_actualizat = json.dumps(dict_depozit, indent=4)
        write_depozit_actualizat = open('Depozit.json', 'w')
        write_depozit_actualizat.write(depozit_actualizat)
        write_depozit_actualizat.close()

class Angajat:

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
    operator = ['1.Creare Produs', '2.Interogare Depozit', '3.Exit']
    operator_produse = ['1.Frigider', '2.Aragaz', '3.Cuptor cu microunde']
    gestionar = ['1.Interogare Depozit', '2.Alimentare Depozit', '3.Exit']

class Frigider:

    frigider = 0

    def __init__(self,tabla,suruburi,freon,bec,motor_mare):
        self.tabla = tabla
        self.suruburi = suruburi
        self.freon = freon
        self.bec = bec
        self.motor_mare = motor_mare
        Frigider.frigider += 1
        time.sleep(1)
        print('Se asambleaza frigiderul')
        time.sleep(3)
        print('Se ambaleaza frigiderul')
        time.sleep(2)
        print('Frigider Creat')


        read_depozit_json = open('Depozit.json', 'r')
        dict_depozit = json.load(read_depozit_json)
        read_depozit_json.close()

        if Frigider.frigider > 0:
            dict_depozit["Tabla"] -= 5
            dict_depozit["Suruburi"] -= 50
            dict_depozit["Freon"] -= 1
            dict_depozit["Bec"] -= 2
            dict_depozit["Motor mare"] -= 1

        depozit_actualizat = json.dumps(dict_depozit, indent=4)
        actualizare_depozit_json = open('Depozit.json', 'w')
        actualizare_depozit_json.write(depozit_actualizat)
        actualizare_depozit_json.close()

class Aragaz:

    aragaz = 0

    def __init__(self, tabla, suruburi, sigurante, bec, motor_mediu):
        self.tabla = tabla
        self.suruburi = suruburi
        self.sigurante = sigurante
        self.bec = bec
        self.motor_mediu = motor_mediu
        Aragaz.aragaz += 1
        time.sleep(1)
        print('Se asambleaza aragazul')
        time.sleep(3)
        print('Se ambaleaza aragazul')
        time.sleep(2)
        print('Aragaz Creat')

        read_depozit_json = open('Depozit.json', 'r')
        dict_depozit = json.load(read_depozit_json)
        read_depozit_json.close()

        if Aragaz.aragaz > 0:
            dict_depozit["Tabla"] -= 4
            dict_depozit["Suruburi"] -= 30
            dict_depozit["Sigurante"] -= 4
            dict_depozit["Bec"] -= 1
            dict_depozit["Motor mediu"] -= 1

        depozit_actualizat = json.dumps(dict_depozit, indent=4)
        actualizare_depozit_json = open('Depozit.json', 'w')
        actualizare_depozit_json.write(depozit_actualizat)
        actualizare_depozit_json.close()

class Cuptor_Microunde:

    cuptor_microunde = 0

    def __init__(self, tabla, suruburi, sigurante, bec, motor_mic):
        self.tabla = tabla
        self.suruburi = suruburi
        self.sigurante = sigurante
        self.bec = bec
        self.motor_mic = motor_mic
        Cuptor_Microunde.cuptor_microunde += 1
        time.sleep(1)
        print('Se asambleaza cuptorul cu microunde')
        time.sleep(3)
        print('Se ambaleaza cuptorul cu microunde')
        time.sleep(2)
        print('Cuptor cu microunde creat')

        read_depozit_json = open('Depozit.json', 'r')
        dict_depozit = json.load(read_depozit_json)
        read_depozit_json.close()

        if Cuptor_Microunde.cuptor_microunde > 0:
            dict_depozit["Tabla"] -= 3
            dict_depozit["Suruburi"] -= 20
            dict_depozit["Sigurante"] -= 2
            dict_depozit["Bec"] -= 1
            dict_depozit["Motor mic"] -= 1

        depozit_actualizat = json.dumps(dict_depozit, indent=4)
        actualizare_depozit_json = open('Depozit.json', 'w')
        actualizare_depozit_json.write(depozit_actualizat)
        actualizare_depozit_json.close()


program_var = True
while program_var:
    angajat_curent = Fabrica('Timisoara','Electronice si Electrocasnice')
    angajat_curent.log_in()
    while angajat_curent.log_token != 0:
        ###ADMIN_MANAGER
        if angajat_curent.log_token == 1 and (angajat_curent.functie == "Admin" or angajat_curent.functie == "Manager") :
            for i in Meniu.admin:
                print(i)
            x = int(input('=>'))
            #ADAUGARE ANGAJAT
            if x == 1:
                nume = input('Numele Angajatului\n=>')
                prenume = input('Prenumele Angajatului\n=>')
                telefon = input('Telefon Angajat\n=>')
                functie = input('Functia Angajatului\n=>')
                calificare = []
                angajat_nou = Angajat(nume,prenume,functie,telefon)
                angajat_nou.adaugare_angajat(nume,prenume,telefon,functie,calificare)
            #STERGERE ANGAJAT
            if x == 2:
                angajat_curent.eliminare_angajat()
            #ADAUGARE STERGERE CALIFICARI
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
            #EXIT
            if x == 4:
                print('Sesiune Incheiata')
                program_var = False
                break
        ####OPERATOR
        if angajat_curent.log_token == 1 and angajat_curent.functie == "Operator":
            read_depozit_json = open('Depozit.json', 'r')
            dict_depozit = json.load(read_depozit_json)
            read_depozit_json.close()

            for i in Meniu.operator:
                print(i)
            x = int(input('Selecteaza o optiune\n=>'))
            #CREARE PRODUSE
            if x == 1:
                for i in Meniu.operator_produse:
                    print(i)
                y = int(input('Selecteaza o optiune\n=>'))
                #CREARE FRIGIDER
                if y == 1 and "Frigotehnist" in angajat_curent.calificare:
                    if dict_depozit['Tabla'] >= 5 and dict_depozit['Suruburi'] >= 50 and dict_depozit['Freon'] >= 1 and dict_depozit['Bec'] >= 2 and dict_depozit['Motor mare'] >= 1:
                        frigider = Frigider(5,50,1,2,1)
                    else:
                        print('Nu aveti materia prima necesara')
                elif y == 1 and "Frigotehnist" not in angajat_curent.calificare:
                    print('Nu ai calificarea')
                #CREARE ARAGAZ
                if y == 2 and "Gazotehnist" in angajat_curent.calificare:
                    if dict_depozit['Tabla'] >= 4 and dict_depozit['Suruburi'] >= 30 and dict_depozit['Sigurante'] >= 4 and dict_depozit['Bec'] >= 1 and dict_depozit['Motor mediu'] >= 1:
                        aragaz = Aragaz(4,30,4,1,1)
                    else:
                        print('Nu aveti materia prima necesara')
                    print()
                elif y == 2 and "Gazotehnist" not in angajat_curent.calificare:
                    print('Nu ai calificarea')
                #CREARE CUPTOR MICROUNDE
                if y == 3 and "Electrician" in angajat_curent.calificare:
                    if dict_depozit['Tabla'] >= 3 and dict_depozit['Suruburi'] >= 20 and dict_depozit['Sigurante'] >= 2 and dict_depozit['Bec'] >= 1 and dict_depozit['Motor mic'] >= 1:
                        cuptor_microunde = Cuptor_Microunde(3,20,2,1,1)
                    else:
                        print('Nu aveti materia prima necesara')
                elif y == 3 and "Electrician" not in angajat_curent.calificare:
                    print('Nu ai calificarea')
            #INTEROGARE DEPOZIT
            if x == 2:
                for i in dict_depozit:
                    print(f'{i} {dict_depozit[i]}')
                iesire = input("Apasa tasta ENTER ca sa te intorci la meniu")
                if iesire == "":
                    continue
            if x == 3:
                print('Sesiune Incheiata')
                program_var = False
                break
        ####GESTIONAR
        if angajat_curent.log_token == 1 and angajat_curent.functie == "Gestionar":
            read_depozit_json = open('Depozit.json', 'r')
            dict_depozit = json.load(read_depozit_json)
            read_depozit_json.close()

            for i in Meniu.gestionar:
                print(i)
            x = int(input('Selecteaza o optiune\n=>'))
            # INTEROGARE DEPOZIT
            if x == 1:
                for i in dict_depozit:
                    print(f'{i} {dict_depozit[i]}')
                iesire = input("Apasa tasta ENTER ca sa te intorci la meniu")
                if iesire == "":
                    continue
            #UPDATE DEPOZIT
            if x == 2:
                angajat_curent.adaugare_depozit()
                continue
            if x == 3:
                program_var = False
                print('Sesiune incheiata')
                break











