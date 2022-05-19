import time
# from tinydb import TinyDB, Query, where
# db = TinyDB("db.json")
#
# # definition d'une classe d'objet "Player"
# class Player:
#     def _init_(self, last_name = None , first_name = None, birthdate = None, gender= None, ranking_elo = None, tournament_score= None):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.birthdate = birthdate
#         self.gender = gender
#         self.ranking_elo= ranking_elo
#         self.tournament_score = tournament_score
#
# """
# player1 = player("Z" ,"Tom" ,"15/01:/980", "masculin", 198 )
# player2 = player("Y" ,"Charles" ,"15/01/1975", "masculin", 56 )
# player3 = player("X" ,"Pierre" ,"31/03/1993", "masculin", 198 )
# player4 = player("W" ,"Justine" ,"09/09/2003", "feminin", 74 )
# player5 = player("V" ,"Julie", "10/10/2006", "feminin", 30 )
# player6 = player("U" ,"Sandra" ,"09/09/2003", "feminin", 74 )
# player7 = player("T" ,"Walid" ,"23/11/1980", "masculin", 198 )
# player8 = player("S" ,"Steve" ,"04/012/1963", "masculin", 198 )
# """
#
# #Pour stocker une instance de joueur, on doit d'abord la convertir en dictionnaire (cad sérialiser)
#
# serialized_player = {
#     "nom" : joueur.nom,
#     "prenom" : joueur.prenom,
#     "date_de_naissance" : joueur.date_de_naissance,
#     "sexe" : joueur.sexe,
#     "classement_elo" : joueur.classement_elo,
#     "score_au_tournoi" : joueur.score
# }
#
#
# players_table = db.table("players")
# players_table.truncate()	# clear the table first pourquoi NE PAS UTILISER db.purge()
# players_table.insert_multiple(serialized_players)
#
#
#
# #Pour recharger les joueurs sérialisés, tu peux faire ceci :
#
# serialized_players = players_table.all()
#
#
# class Tournoi:
#     def _init_(self, ):
#################################################################################################################
from datetime import date
from datetime import datetime
#
# def add_tournament_date():
#         tournament_date_list = []
#
#         informed_tournament_day = False
#         while not informed_tournament_day:
#                 day = input("entrer votre jour du tournoi: ")
#                 # birthday = int(birthday)
#                 if (day.isdigit()) and (len(day) == 2) and (int(day) < 32):
#                         informed_tournament_day = True
#                         tournament_date_list.append(day)
#                 else:
#                         print("vous devez entrer un chiffre inférieur ou égal à 31")
#
#         informed_tournament_month = False
#         while not informed_tournament_month:
#                 month = input("entrer votre mois : ")
#                 if month.isdigit() and len(month) == 2 and int(month) < 13:
#                         informed_tournament_month = True
#                         tournament_date_list.append(month)
#                 else:
#                         print("vous devez entrer un chiffre inférieur ou égal à 12")
#
#         informed_tournament_year = False
#         while not informed_tournament_year:
#                 year = input("entrer l'année duournoi: ")
#                 # birthyear = int(birthyear)
#                 if year.isdigit() and len(year) == 4:
#                         informed_tournament_year = True
#                         tournament_date_list.append(year)
#                 else:
#                         print("vous devez entrer une année à 4 chiffres")
#         return f"{tournament_date_list[0]}/{tournament_date_list[1]}/{tournament_date_list[2]}"
#
#
# def choice_tournament_date():
#     informed_choice_date = False
#     choice_date = None
#     while not informed_choice_date:
#         choice_date = input("si vous choisissez la date d'aujourd'hui pour le tournoi tapez 1, \n "
#                                 "si vous souhaitez renseigner la date tapez 2 ---Choisissez : ")
#         if choice_date =="1":
#                 informed_choice_date = True
#                 today = date.today()
#                 print("vous venez de valider la date d'aujourd'hui qui est : " + str(today.strftime("%A %d %B %Y")))
#         elif choice_date =="2":
#                 print("vous allez entrer manuellement la date du tournoi")
#                 date_tournoi = add_tournament_date()
#                 print("la date du tournoi est : "+ date_tournoi)
#                 informed_choice_date = True
#         else:
#                 print("tapez 1 ou 2")
#     return choice_date
#
# choice_tournament_date()


# def add_tour_name():
#     # methode pour definir le nom du tour qui sera par defaut Round 1, Round 2 ...
#     informed_tour_name = False
#     while not informed_tour_name:
#         tour_name = input("Veuillez entrer le nom du tour (Round 1, Round 2, etc) : ")
#         if tour_name == "Round 1":
#             informed_tour_name = True
#         elif tour_name == "Round 2":
#             informed_tour_name = True
#         elif tour_name == "Round 3":
#             informed_tour_name = True
#         elif tour_name == "Round 4":
#             informed_tour_name = True
#         else:
#             print("Vous avez mal renseigné le nom du tour, veuillez re-essayer")
#         print(f"le nom du tour est :" + tour_name)
#     return informed_tour_name
#
# add_tour_name()
#
# def add_manually_begin_time(self):
#     manually_begin_time_list = []
#
#     informed_manually_begin_day = False
#     while not informed_manually_begin_day:
#         begin_round_day = input("entrer le jour du tour ")
#         if (day.isdigit()) and (len(day) == 2) and (int(day) < 32):
#             informed_manually_begin_day = True
#             manually_begin_time_list.append(begin_round_day)
#         else:
#             print("vous devez entrer un chiffre inférieur ou égal à 31")
#
#     informed_manually_begin_month = False
#     while not informed_manually_begin_month:
#         begin_round_month = input("entrer le mois du tour : ")
#         if month.isdigit() and len(month) == 2 and int(month) < 13:
#             informed_manually_begin_month = True
#             manually_begin_time_list.append(begin_round_month)
#         else:
#             print("vous devez entrer un chiffre inférieur ou égal à 12")
#
#     informed_manually_begin_year = False
#     while not informed_manually_begin_year:
#         begin_round_year = input("entrer l'année du tour: ")
#         if year.isdigit() and len(year) == 4:
#             informed_tournament_year = True
#             manually_begin_time_list.append(begin_round_year)
#         else:
#             print("vous devez entrer une année à 4 chiffres")
#     return f"{manually_begin_time_list[0]}/{manually_begin_time_list[1]}/{manually_begin_time_list[2]}"

#
# def add_begin_time():
#     # methode pour ajouter date et heure de debut du round
#     informed_begin_time = False
#     while not informed_begin_time:
#         choice_begin_time = input("si vous souhaitez entrer automatiquement la date et l'heure du début du Round \n"
#                            " ----> TAPER entrer sinon taper une touche: ")
#         if choice_begin_time == "":
#             informed_begin_time = True
#             now = datetime.now()  # current date and time
#             begin_time = str(now.strftime("%A %d %B %Y, %H:%M:%S"))
#             print("Date et Heure du début du tour est : " + str(now.strftime("%A %d %B %Y, %H:%M:%S")))
#         else:
#             print("vous avez refuser de le faire automatiquement")
#     return informed_begin_time
#
# add_begin_time()


# def add_end_time():
#     # methode pour ajouter date et heure de fin du round
#     informed_end_time = False
#     while not informed_end_time:
#         choice_end_time = input("si vous souhaitez entrer automatiquement la date et l'heure du début du Round \n"
#                                 " ----> TAPER entrer sinon taper une touche puis entrer: ")
#         if choice_end_time == "":
#             informed_end_time = True
#             now = datetime.now()  # current date and time
#             end_time = str(now.strftime("%A %d %B %Y, %H:%M:%S"))
#             print("Le début du tour est : " + str(now.strftime("%A %d %B %Y, %H:%M:%S")))
#         else:
#             print("vous avez refusé d'entrer automatiquement la date et heure du début du tour")
#     return informed_end_time
#
# add_end_time()

# def add_score_player():
#         informed_score_player = False
#         while not informed_score_player:
#             score_player = input(f"Entrez le score de {match.player_1} :")
#                 float(score_player_1)
#             except Exception:
#                 print("Vous devez entrer 0, 0.5, ou 1")
#             else:
#                 match.score_player_1 = float(score_player_1)
#                 match.player_1.tournament_score += float(score_player_1)
#                 informed_score_player_1 = True
#         return
# add_score_player()
#
# from tinydb import TinyDB
#
# database = TinyDB('db.json', indent=4)
# players_table = database.table('players')
#
# print(players_table.all())
# print(players_table.all()[0])


# for player in players_table.all():
#     player_id = player.doc_id
#     print(player)
#     print(player.doc_id)
#     print(type(player))
#     print(player_id)
#
#
# def add_player_id():
#     informed_player_id = False
#     while not informed_player_id:
#         for player in players_table.all():
#             players_table.update({"Id du joueur": player_id}, doc_ids=[player_id])
#             #player_id = player.doc_id
#             informed_player_id = True
#             print(player)
#     return
# add_player_id()
#

# def add_undefined_player_id():
#     """Ajouter un id au joueur venant de l'id du document de TinyDB"""
#     database = TinyDB('db.json', indent=4)
#     players_table = database.table('players')
#     informed_player_id = False
#     while not informed_player_id:
#         for player in players_table.all():
#             player_id = player.doc_id
#             informed_player_id = True
#             print(player)
#     return
# add_undefined_player_id()


