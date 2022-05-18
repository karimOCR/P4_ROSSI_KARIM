from datetime import date
from datetime import datetime
from tinydb import TinyDB
from player_model import Player

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




# class Tour:
#     """each tour is a list of matches, each match is a tuple, pair of players with a result for each player"""
#     def __init__(self, tour_name=None, begin_time=None, end_time=None, round_instances_list=None):
#         self.tour_name = tour_name
#         self.begin_time = begin_time
#         self.end_time = end_time
#         self.round_instances_list= round_instances_list
#
#     def serialized (self):
#         serialized_tour_datas = {}
#         serialized_tour_datas["nom_du_tour"] = self.tour_name
#         serialized_tour_datas["date_et_heure_de_début_de_la_partie"] = self.begin_time
#         serialized_tour_datas["date_et_heure_de_fin_de_la_partie"] = self.end_time
#         serialized_tour_datas["liste_des_instances_de_round"] = self.round_instances_list
#
#     def unserialized(self, serialized_tour):
#         tour_name = serialized_tour["nom_du_tour"]
#         begin_time = serialized_tour["date_et_heure_de_début_de_la_partie"]
#         end_time = serialized_tour["date_et_heure_de_fin_de_partie"]
#         round_instances_list = serialized_tour["liste_des_instances_de_round"]
#         return Tour(tour_name, begin_time, end_time, round_instances_list)
#
#
#     def add_tour_name(self):
#         """Creation of method for Tour Class"""
#         # methode pour definir le nom du tour qui sera par defaut Round 1, Round 2 ...
#         informed_tour_name = False
#         while not informed_tour_name:
#             tour_name = input("Veuillez entrer le nom du tour (Round 1, Round 2, etc) : ")
#             if tour_name == "Round 1":
#                 informed_tour_name = True
#             elif tour_name == "Round 2":
#                 informed_tour_name = True
#             elif tour_name == "Round 3":
#                 informed_tour_name = True
#             elif tour_name == "Round 4":
#                 informed_tour_name = True
#             else:
#                 print("Vous avez mal renseigné le nom du tour, veuillez re-essayer")
#             print(f"le nom du tour est :" + tour_name)
#         return informed_tour_name
#
#     def add_begin_time(self):
#         # methode pour ajouter date et heure de debut du round
#         informed_begin_time = False
#         while not informed_begin_time:
#             choice_begin_time = input("si vous souhaitez entrer automatiquement la date et l'heure du début du Round \n"
#                                " ----> TAPER entrer sinon taper une touche puis entrer: ")
#             if choice_begin_time == "":
#                 informed_begin_time = True
#                 now = datetime.now() #current date and time
#                 begin_time = str(now.strftime("%A %d %B %Y, %H:%M:%S"))
#                 print("Le début du tour est : " + str(now.strftime("%A %d %B %Y, %H:%M:%S")))
#             else:
#                 print("vous avez refusé d'entrer automatiquement la date et heure du début du tour")
#         return informed_begin_time
#
#     def add_end_time(self):
#         # methode pour ajouter date et heure de fin du round
#         informed_end_time = False
#         while not informed_end_time:
#             choice_end_time = input("si vous souhaitez entrer automatiquement la date et l'heure de FIN du Round \n"
#                             " ----> TAPER entrer sinon taper une touche puis entrer: ")
#             if choice_end_time == "":
#                 informed_end_time = True
#                 now = datetime.now()  # current date and time
#                 end_time = str(now.strftime("%A %d %B %Y, %H:%M:%S"))
#                 print("Le début du tour est : " + str(now.strftime("%A %d %B %Y, %H:%M:%S")))
#             else:
#                 print("vous avez refusé d'entrer automatiquement la date et heure de FIN du tour")
#         return informed_end_time
#
#     def add_round_instances_list(self):
#         # les intances de rounds seront stockées dans une liste sur l'instance du tournoi
#
#
#     def sorted_players_by_ranking(self):
#         # it returns a dictionnary d’instance d’objet player initialement renseigner par l’organisateur.
#         players_initial_dict = player.serialized()
#         print(players_initial_dict)
#
#         # sorted of dictionnary, in result we have a list of compley key/value pairs
#         sorted_ranking_of_players_initial_list = sorted(players_initial_dict.item(), key=lambda t: t[1][4])
#         print(sorted_ranking_of_players_initial_list)
#
#         # slicing in 2 lists, upper & lower ranking
#         upper_players_list = sorted_ranking_of_players_initial_list[0:4]
#         lower_players_list = sorted_ranking_of_players_initial_list[4:8]
#         print(upper_players_list)
#         print(lower_players_list)
#         return
#
#
#         MATCH_NUMBER = 1
#
# class Match:
#     # chaque match est definit par un tuple composé de deux listes contenant id du joueur et son score
#     def __init__(self, match_name=None, player_1=None, player_2=None,
#              score_player_1=0, score_player_2=0):
#         self.match_name = "Match" + str(Match.MATCH_NUMBER)
#         self.player_1 = player_1
#         self.player_2 = player_2
#         self.score_player_1 = score_player_1
#         self.score_player_2 = score_player_2
#
#     def serialized(self):
#         serialized_match_datas = {}
#         serialized_match_datas["nom_du_match"] = self.match_name
#         serialized_match_datas["joueur_1"] = self.player_1
#         serialized_match_datas["joueur_2"] = self.player_2
#         serialized_match_datas["score_du_joueur_1"] = self.score_player_1
#         serialized_match_datas["score_du_joueur_2"] = self.score_player_2
#
#     def unserialized(self, serialized_match):
#         match_name = serialized_match["nom_du_match"]
#         player_1 = serialized_match["joueur_1"]
#         player_2 = serialized_match["joueur_2"]
#         score_player_1 = serialized_match["score_du_joueur_1"]
#         score_player_2 = serialized_match["score_du_joueur_2"]
#         return Match(match_name,
#                  player_1,
#                  player_2,
#                  score_player_1,
#                  score_player_2)
#
#     def __str__(self):
#         return f"{self.match_name} : Le {self.player_1} joue contre le {self.player_2}."
#
#     def __rep__(self):
#         return f"{self.match_name}  - Debut : {self.begin_time}  - Fin : {self.end_time}"
#
#
#     def dict(self):
#         database = TinyDB('db.json', indent=4)
#         players_table = database.table('players')
#         print(players_table.all())
#
#
#     def get_match_score(self):
#         # puisque le gestionnaire saisit tous les resultats de match en fin de tour, on utilise une boucle for pour incrémentation
#         first_round_matches_list = []
#
#         match_1_vs_5 = ([upper_lower_list[0][4], score_player_1],
#                                     [lower_player_list[0][4], score_player_2])
#         informed_match_1_vs_5  = False
#         while not informed_match_1_vs_5:
#             score_player_1 = input(f"veuillez enter le score du joueur 1 : ")
#             score_player_2 = input(f"veuillez enter le score du joueur 2 : ")
#             if (score_player_1 == 0) and (score_player_2 == 1):
#                 print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
#                 informed_match = True
#                 first_round_matches_list.append(match_1_vs_5)
#             elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
#                 print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
#                 informed_match = True
#                 first_round_matches_list.append(match_1_vs_5)
#             elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
#                 print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
#                 informed_match = True
#                 first_round_matches_list.append(match_1_vs_5)
#             else:
#                 print(f'il y a une erreur dans le résultat, veuillez recommencer')
#         return
#
#         match_2_vs_6 = ([upper_lower_list[1][4], score_player_1],
#                        [lower_player_list[1][4], score_player_2])
#         informed_match_2_vs_6 = False
#         while not informed_match_2_vs_6:
#             score_player_1 = input(f"veuillez enter le score du joueur 1 : ")
#             score_player_2 = input(f"veuillez enter le score du joueur 2 : ")
#             if (score_player_1 == 0) and (score_player_2 == 1):
#                 print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
#                 informed_match = True
#                 first_round_matches.append(match_2_vs_6)
#             elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
#                 print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
#                 informed_match = True
#                 first_round_matches.append(match_2_vs_6)
#             elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
#                 print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
#                 informed_match = True
#                 first_round_matches.append(match_2_vs_6)
#             else:
#                 print(f'il y a une erreur dans le résultat, veuillez recommencer')
#         return
#
#         match_3_vs_7 = ([upper_lower_list[2][4], score_player_1],
#                        [lower_player_list[2][4], score_player_2])
#         informed_match_3_vs_7 = False
#         while not informed_match_3_vs_7:
#             score_player_1 = input(f"veuillez enter le score du joueur 1 : ")
#             score_player_2 = input(f"veuillez enter le score du joueur 2 : ")
#             if (score_player_1 == 0) and (score_player_2 == 1):
#                 print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
#                 informed_match = True
#                 first_round_matches.append(match_3_vs_7)
#             elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
#                 print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
#                 informed_match = True
#                 first_round_matches.append(match_3_vs_7)
#             elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
#                 print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
#                 informed_match = True
#                 first_round_matches.append(match_3_vs_7)
#             else:
#                 print(f'il y a une erreur dans le résultat, veuillez recommencer')
#         return
#
#         match_4_vs_8 = ([upper_lower_list[3][4], score_player_1],
#                        [lower_player_list[3][4], score_player_2])
#         informed_match_4_vs_8 = False
#         while not informed_match_4_vs_8:
#             score_player_1 = input(f"veuillez enter le score du joueur 1 : ")
#             score_player_2 = input(f"veuillez enter le score du joueur 2 : ")
#             if (score_player_1 == 0) and (score_player_2 == 1):
#                 print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
#                 informed_match = True
#                 first_round_matches_list.append(match_4_vs_8)
#             elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
#                 print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
#                 informed_match = True
#                 first_round_matches_list.append(match_4_vs_8)
#             elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
#                 print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
#                 informed_match = True
#                 first_round_matches_list.append(match_4_vs_8)
#             else:
#                 print(f'il y a une erreur dans le résultat, veuillez recommencer')
#         return
#     print("{first_round_matches_list[0]} \n"
#           "{first_round_matches_list[1]} \n"
#           "{first_round_matches_list[2]} \n"
#           "{first_round_matches_list[3]} \n"
#           )
#     return












    def get_match_score(self):
        # puisque le gestionnaire saisit tous les resultats de match en fin de tour, on utilise une boucle for pour incrémentation
        for i in range(4):
            i=+1
            match_({i})_vs_({i}+5) = ([upper_lower_list[i], score_player_1],
                                        [lower_player_list[i][4], score_player_2])
            informed_match = False
            while not informed_match:
                score_player_1 = input(f"veuillez enter le score du joueur 1 : ")
                score_player_2 = input(f"veuillez enter le score du joueur 2 : ")
                if (score_player_1 == 0) and (score_player_2 == 1):
                    print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
                    informed_match = True
                elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
                    print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
                    informed_match = True
                elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
                    print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
                    informed_match = True
                else:
                    print(f'il y a une erreur dans le résultat, veuillez recommencer')
            return













sorted_players_by_ranking(self)

# dict_all_players = {1: 130, 2: 25, 3: 45, 4: 287, 5: 158, 6: 32, 7: 987, 8: 654}
# for key, value in dict_all_players.items():
#     print(key, value)
# liste_sorted_players_by_ranking = sorted(dict_all_players.items(), key=lambda x: x[1], reverse=True)
# print(liste_sorted_players_by_ranking)
# #sorted_by_ranking = di
#
# head_list_players = liste_sorted_players_by_ranking[0:4]
# end_list_players = liste_sorted_players_by_ranking[4:8]
# print(head_list)
# print(end_list)
#
# for i, v in enumerate(head_list):
#     print(i,v)
# for i, v in enumerate(end_list):
#     print(i,v)
#
#
# def player_first_round():
#     player_ranking_1_first_round = head_list_players.index(0)
#     player_ranking_5_first_round = end_list_players.index(0)
#     player_ranking_2_first_round = head_list_players.index(1)
#     player_ranking_6_first_round = end_list_players.index(1)
#     player_ranking_3_first_round = head_list_players.index(2)
#     player_ranking_7_first_round = end_list_players.index(2)
#     player_ranking_4_first_round = head_list_players.index(3)
#     player_ranking_8_first_round = end_list_players.index(3)
#
#
#     players_Match_1 = {head_list_players.index()}
#
# def matches_round_one():
#
#
#
