from datetime import date
from datetime import datetime
from tinydb import TinyDB
from models.player_model import Player

class Tournament:
    """Creation an instance of a tournament"""
    def __init__(self, tournament_name=None, location=None, tournament_date=None, number_of_tours=4, time_control=None,
                 description=None, players_ids=None, list_of_tours=[], tournament_id=None):
        self.tournament_name = tournament_name
        self.location = location
        self.tournament_date = tournament_date
        self.numbers_of_tours = number_of_tours
        self.time_control = time_control
        self.description = description
        self.players_ids = players_ids
        self.list_of_tours = list_of_tours
        self.tournament_id = tournament_id

    def __repr__(self):
        return f"{self.tournament_name} ---- {self.location} \n\n {self.list_of_tours}\n"

    def serialized(self):
        serialized_tournament_datas = {}
        serialized_tournament_datas["nom_du_tournoi"] = self.tournament_name
        serialized_tournament_datas["lieu"] = self.location
        serialized_tournament_datas["date"] = self.tournament_date
        serialized_tournament_datas["nombre_de_tours"] = self.numbers_of_tours
        serialized_tournament_datas["controle_du_temps"] = self.time_control
        serialized_tournament_datas["description"] = self.description
        serialized_tournament_datas["joueurs id"] = self.players_ids
        serialized_tournament_datas["tours"] = self.list_of_tours
        serialized_tournament_datas["tournoi_id"] = self.tournament_id
        return serialized_tournament_datas

    def unserialized(self, serialized_tournament):
        tournament_name = serialized_tournament["nom_du_tournoi"]
        location = serialized_tournament["lieu"]
        tournament_date = serialized_tournament["date"]
        numbers_of_tours = serialized_tournament["nombre_de_tours"]
        time_control = serialized_tournament["controle_de_temps"]
        description = serialized_tournament["description"]
        players_ids = serialized_tournament["joueurs_id"]
        list_of_tours = serialized_tournament["tours"]
        tournament_id = serialized_tournament["tournoi_id"]
        return Tournament(tournament_name,
                          location,
                          tournament_date,
                          numbers_of_tours,
                          time_control,
                          description,
                          players_ids,
                          list_of_tours,
                          tournament_id
                          )


    def add_undefined_tournament_name(self):
        # methode pour definir le nom du tournoi
        tournament_name = False
        informed_tournament_name = False
        while not informed_tournament_name:
            tournament_name= input(f"Veuillez renseigner le Nom du Tournoi: ")
            if tournament_name != "":
                informed_tournament_name= True
            else:
                print(f"vous devez entrer un nom pour ce tournoi ")
        return tournament_name


    def add_undefined_location(self):
        # methode pour definir le lieu du tournoi
        location = False
        informed_location= False
        while not informed_location:
            location = input(f"Veuillez renseigner le lieu du Tournoi: ")
            if location != "":
                informed_location = True
            else:
                print(f"vous devez entrer un LIEU pour ce tournoi ")
        return location

    def add_tournament_date(self):
        tournament_date_list = []

        informed_tournament_day = False
        while not informed_tournament_day:
            day = input("entrer le jour du tournoi: ")
            # birthday = int(birthday)
            if (day.isdigit()) and (len(day) == 2) and (int(day) < 32):
                informed_tournament_day = True
                tournament_date_list.append(day)
            else:
                print("vous devez entrer un chiffre inférieur ou égal à 31")

        informed_tournament_month = False
        while not informed_tournament_month:
            month = input("entrer le mois du tournoi : ")
            if month.isdigit() and len(month) == 2 and int(month) < 13:
                informed_tournament_month = True
                tournament_date_list.append(month)
            else:
                print("vous devez entrer un chiffre inférieur ou égal à 12")

        informed_tournament_year = False
        while not informed_tournament_year:
            year = input("entrer l'année du tournoi: ")
            # birthyear = int(birthyear)
            if year.isdigit() and len(year) == 4:
                informed_tournament_year = True
                tournament_date_list.append(year)
            else:
                print("vous devez entrer une année à 4 chiffres")
        return f"{tournament_date_list[0]}/{tournament_date_list[1]}/{tournament_date_list[2]}"


    def choice_tournament_date(self):
        informed_choice_date = False
        choice_date = None
        while not informed_choice_date:
            choice_date = input("si vous choisissez la date d'aujourd'hui pour le tournoi tapez 1, \n "
                                "si vous souhaitez renseigner la date tapez 2 ---Choisissez : ")
            if choice_date == "1":
                informed_choice_date = True
                today = date.today()
                date_tournoi = str(today.strftime("%A %d %B %Y"))
                print("vous venez de valider la date d'aujourd'hui qui est : " + str(today.strftime("%A %d %B %Y")))
            elif choice_date == "2":
                print("vous allez entrer manuellement la date du tournoi")
                date_tournoi = self.add_tournament_date()
                print("la date du tournoi est : " + date_tournoi)
                informed_choice_date = True
            else:
                print("tapez 1 ou 2")
        return date_tournoi

    def add_number_of_rounds(self):
        number_of_rounds = 4
        print("Le nombre de rounds est de 4 par défaut\n"
          "Souhaitez-vous changer ce nombre ?")

        valid_number = False
        while not valid_number:
            print("Entrer 'Y' pour changer, ou 'N' pour continuer")
            choice = input("--> ")
            if choice == "Y":
                number_of_rounds = input("Entrez le nombre de rounds :")
                if number_of_rounds.isdigit():
                    valid_number = True
                else:
                    print("Vous devez entrer un nombre entier")
            if choice == "N":
                valid_number = True
        return number_of_rounds

    def add_time_control(self):
        print("Choisissez le contrôle du temps:")
        time_control = None
        entry = input(f"taper 1 s'il s'agit d'une partie de type Bullet \n"
                      "taper 2 s'il s'agit d'une partie de type Blitz \n"
                      "taper 3 s'il s'agit d'une partie de type rapide \n"
                      "Entrez votre type de controle ------>: "
                      )
        if entry == "1":
            time_control = "Bullet"
        if entry == "2":
            time_control = "Blitz"
        if entry == "3":
            time_control = "Coup rapide"
        return time_control

    def add_description(self):
        description = input("Entrer une description au tournoi :\n"
                            "-->")
        return description


