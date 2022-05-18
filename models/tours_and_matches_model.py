from tinydb import TinyDB
"""definition des classes Tour et Match et de leurs methodes"""

class Tour:
    """each tour is a list of matches, each match is a tuple, pair of players with a result for each player"""
    def __init__(self, tour_name=None, begin_time=None, end_time=None, round_instances_list=None):
        self.tour_name = tour_name
        self.begin_time = begin_time
        self.end_time = end_time
        self.round_instances_list= round_instances_list

    def serialized (self):
        serialized_tour_datas = {}
        serialized_tour_datas["nom_du_tour"] = self.tour_name
        serialized_tour_datas["date_et_heure_de_début_de_la_partie"] = self.begin_time
        serialized_tour_datas["date_et_heure_de_fin_de_la_partie"] = self.end_time
        serialized_tour_datas["liste_des_instances_de_round"] = self.round_instances_list

    def unserialized(self, serialized_tour):
        tour_name = serialized_tour["nom_du_tour"]
        begin_time = serialized_tour["date_et_heure_de_début_de_la_partie"]
        end_time = serialized_tour["date_et_heure_de_fin_de_partie"]
        round_instances_list = serialized_tour["liste_des_instances_de_round"]
        return Tour(tour_name, begin_time, end_time, round_instances_list)


    # def add_tour_name(self):
    #     """Creation of method for Tour Class""" inutile
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

    def add_begin_time(self):
        # methode pour ajouter date et heure de debut du round
        informed_begin_time = False
        while not informed_begin_time:
            choice_begin_time = input("si vous souhaitez entrer automatiquement la date et l'heure du début du Round \n"
                               " ----> TAPER entrer sinon taper une touche puis entrer: ")
            if choice_begin_time == "":
                informed_begin_time = True
                now = datetime.now() #current date and time
                begin_time = str(now.strftime("%A %d %B %Y, %H:%M:%S"))
                print("Le début du tour est : " + str(now.strftime("%A %d %B %Y, %H:%M:%S")))
            else:
                print("vous avez refusé d'entrer automatiquement la date et heure du début du tour")
        return informed_begin_time

    def add_end_time(self):
        # methode pour ajouter date et heure de fin du round
        informed_end_time = False
        while not informed_end_time:
            choice_end_time = input("si vous souhaitez entrer automatiquement la date et l'heure de FIN du Round \n"
                            " ----> TAPER entrer sinon taper une touche puis entrer: ")
            if choice_end_time == "":
                informed_end_time = True
                now = datetime.now()  # current date and time
                end_time = str(now.strftime("%A %d %B %Y, %H:%M:%S"))
                print("Le début du tour est : " + str(now.strftime("%A %d %B %Y, %H:%M:%S")))
            else:
                print("vous avez refusé d'entrer automatiquement la date et heure de FIN du tour")
        return informed_end_time

    def add_round_instances_list(self):
        # les intances de rounds seront stockées dans une liste sur l'instance du tournoi


    def sorted_players_by_ranking(self, player):
        # Retourne un dictionnaire d’instance d’objet player initialement renseigner par l’organisateur.
        database = TinyDB('db.json', indent=4)
        players_table = database.table('players')
        players_initial_dict = players_table.all()
        print(players_initial_dict)

        # sorted of dictionnary, in result we have a list of complex key/value pairs
        sorted_ranking_of_players_initial_list = sorted(players_initial_list, key=lambda t: t["Classement"],
                                                        reverse=True)
        print(sorted_ranking_of_players_initial_list)

        # slicing in 2 lists, upper & lower ranking
        upper_players_list = sorted_ranking_of_players_initial_list[0:4]
        lower_players_list = sorted_ranking_of_players_initial_list[4:8]
        print(upper_players_list)
        print(lower_players_list)
        return




class Match:
    # chaque match est definit par un tuple composé de deux listes contenant id du joueur et son score
    def __init__(self, match_name=None, player_1=None, player_2=None,
             score_player_1=0, score_player_2=0):
        self.match_name = "Match" + str(Match.MATCH_NUMBER)
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def serialized(self):
        serialized_match_datas = {}
        serialized_match_datas["nom_du_match"] = self.match_name
        serialized_match_datas["joueur_1"] = self.player_1
        serialized_match_datas["joueur_2"] = self.player_2
        serialized_match_datas["score_du_joueur_1"] = self.score_player_1
        serialized_match_datas["score_du_joueur_2"] = self.score_player_2

    def unserialized(self, serialized_match):
        match_name = serialized_match["nom_du_match"]
        player_1 = serialized_match["joueur_1"]
        player_2 = serialized_match["joueur_2"]
        score_player_1 = serialized_match["score_du_joueur_1"]
        score_player_2 = serialized_match["score_du_joueur_2"]
        return Match(match_name,
                 player_1,
                 player_2,
                 score_player_1,
                 score_player_2)

    def __str__(self):
        return f"{self.match_name} : Le {self.player_1} joue contre le {self.player_2}."

    def __rep__(self):
        return f"{self.match_name}  - Debut : {self.begin_time}  - Fin : {self.end_time}"


    def dict(self):
        database = TinyDB('db.json', indent=4)
        players_table = database.table('players')
        print(players_table.all())


    def get_match_score(self):
        """Pour recolter le score des matchs du premier round"""

        first_round_matches_list = []
        first_round_matches_dict = {}
        for i, v in enumerate(upper_players_list):
            # print(i,v)
            # print(lower_players_list[i])
            joueur_1 = upper_players_list[i]
            joueur_2 = lower_players_list[i]
            first_round_match = (
            [joueur_1['id_du_joueur'], joueur_1['Score']], [joueur_2['id_du_joueur'], joueur_2['Score']])
            print(f"joueur_1 est : {joueur_1['Nom']} {joueur_1['Prenom']} avec ELO de {joueur_1['Classement']}")
            print(f"joueur_2 est : {joueur_2['Nom']} {joueur_2['Prenom']} avec ELO de {joueur_2['Classement']}")
            print(f"Qui a gagné le match ? \n")
            informed_match_winner = False
            wining_player = None
            while not informed_match_winner:
                match_winner = input(
                    f"si c'est le joueur 1, {joueur_1['Nom']} {joueur_1['Prenom']} qui a gagné, Tapez__1 \n"
                    f"si c'est le joueur 2, {joueur_2['Nom']} {joueur_2['Prenom']} qui a gagné, Tapez__2 \n"
                    f"si c'est un match nul alors ________________Tapez__3 \n"
                    f"Tapez 1 ou 2 ou 3 ___: ")
                print(type(match_winner))
                if match_winner == str(1):
                    informed_match_winner = True
                    print(f"Le joueur 1 {joueur_1['Nom']} {joueur_1['Prenom']} a gagné cette partie\n"
                          "et se voit attribué  1 Point")
                    first_round_match[0][1] += 1
                    print(f" l'id du joueur {first_round_match[0][0]} a {first_round_match[0][1]} point \n"
                          f"l'id du joueur {first_round_match[1][0]} a {first_round_match[1][1]} point \n")

                elif match_winner == str(2):
                    informed_match_winner = True
                    print(f"Le joueur 2 {joueur_2['Nom']} {joueur_2['Prenom']} a gagné cette partie\n"
                          "et se voit attribué  1 Point")
                    first_round_match[1][1] += 1
                    print(f" l'id du joueur {first_round_match[0][0]} a {first_round_match[0][1]} point \n"
                          f"l'id du joueur {first_round_match[1][0]} a {first_round_match[1][1]} point \n")

                elif match_winner == str(3):
                    informed_match_winner = True
                    print(f"Le joueur 1 et le joueur 2 ont fait match nul \n"
                          f"{joueur_1['Nom']} {joueur_1['Prenom']} et joueur 2 {joueur_2['Nom']} {joueur_2['Prenom']}\n"
                          f"se voient chacun(e) attribué  0,5 Point")
                    first_round_match[0][1] += 0.5
                    first_round_match[1][1] += 0.5
                    print(f" l'id du joueur {first_round_match[0][0]} a {first_round_match[0][1]} point \n"
                          f"l'id du joueur {first_round_match[1][0]} a {first_round_match[1][1]} point \n")

                else:
                    print(f"il y a une erreur dans votre saisie, veuillez recommencer")
            first_round_matches_list.append(first_round_match)
            print(first_round_matches_list)
            match_dict = dict(first_round_match)
        print(match_dict)
        first_round_matches_dict.update(match_dict)

    def sorted_players_after_first_round(self,first_round_matches_dict):
        # sorted of dictionnary, in result we have a list of complex key/value pairs
        sorted_players_after_first_round_list = sorted(first_round_matches_dict.items(), key=operator.itemgetter(1),
                                                        reverse=True)
        print(sorted_players_after_first_round_list)

    def save_db_match_first_round(self):















    #     first_round_matches_list = []
    #
    #     """Pour le premier match"""
    #     match_1_vs_5 = ([upper_player_list[0][4], upper_player_list[0][5]],
    #                     [lower_player_list[0][4], lower_player_list[0][5]])
    #     informed_match_1_vs_5  = False
    #     while not informed_match_1_vs_5:
    #         score_player_1 = input(f"veuillez enter le score du joueur 1 : ")
    #         score_player_2 = input(f"veuillez enter le score du joueur 2 : ")
    #         if (score_player_1 == 0) and (score_player_2 == 1):
    #             print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
    #             informed_match = True
    #             first_round_matches_list.append(match_1_vs_5)
    #         elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
    #             print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
    #             informed_match = True
    #             first_round_matches_list.append(match_1_vs_5)
    #         elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
    #             print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
    #             informed_match = True
    #             first_round_matches_list.append(match_1_vs_5)
    #         else:
    #             print(f'il y a une erreur dans le résultat, veuillez recommencer')
    #     return
    #
    #     """Pour le second match"""
    #     match_2_vs_6 = ([upper_player_list[1][4], score_player_1],
    #                    [lower_player_list[1][4], score_player_2])
    #     informed_match_2_vs_6 = False
    #     while not informed_match_2_vs_6:
    #         score_player_1 = input(f"veuillez enter le score du joueur 1 : ")
    #         score_player_2 = input(f"veuillez enter le score du joueur 2 : ")
    #         if (score_player_1 == 0) and (score_player_2 == 1):
    #             print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
    #             informed_match = True
    #             first_round_matches.append(match_2_vs_6)
    #         elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
    #             print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
    #             informed_match = True
    #             first_round_matches.append(match_2_vs_6)
    #         elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
    #             print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
    #             informed_match = True
    #             first_round_matches.append(match_2_vs_6)
    #         else:
    #             print(f'il y a une erreur dans le résultat, veuillez recommencer')
    #     return
    #
    #     """Pour le troisième match"""
    #     match_3_vs_7 = ([upper_player_list[2][4], score_player_1],
    #                    [lower_player_list[2][4], score_player_2])
    #     informed_match_3_vs_7 = False
    #     while not informed_match_3_vs_7:
    #         score_player_1 = input(f"veuillez enter le score du joueur 1 : ")
    #         score_player_2 = input(f"veuillez enter le score du joueur 2 : ")
    #         if (score_player_1 == 0) and (score_player_2 == 1):
    #             print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
    #             informed_match = True
    #             first_round_matches.append(match_3_vs_7)
    #         elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
    #             print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
    #             informed_match = True
    #             first_round_matches.append(match_3_vs_7)
    #         elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
    #             print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
    #             informed_match = True
    #             first_round_matches.append(match_3_vs_7)
    #         else:
    #             print(f'il y a une erreur dans le résultat, veuillez recommencer')
    #     return
    #
    #     """Pour le quatrième match"""
    #     match_4_vs_8 = ([upper_player_list[3][4], score_player_1],
    #                    [lower_player_list[3][4], score_player_2])
    #     informed_match_4_vs_8 = False
    #     while not informed_match_4_vs_8:
    #         score_player_1 = input(f"veuillez enter le score du joueur 1 : ")
    #         score_player_2 = input(f"veuillez enter le score du joueur 2 : ")
    #         if (score_player_1 == 0) and (score_player_2 == 1):
    #             print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
    #             informed_match = True
    #             first_round_matches_list.append(match_4_vs_8)
    #         elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
    #             print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
    #             informed_match = True
    #             first_round_matches_list.append(match_4_vs_8)
    #         elif (score_player_1 == 0.5) and (score_player_2 == 0.5):
    #             print(f"le joueur 1 a  {score_player_1} point et joueur 2 a {score_player_2}")
    #             informed_match = True
    #             first_round_matches_list.append(match_4_vs_8)
    #         else:
    #             print(f'il y a une erreur dans le résultat, veuillez recommencer')
    #     return
    # print("{first_round_matches_list[0]} \n"
    #       "{first_round_matches_list[1]} \n"
    #       "{first_round_matches_list[2]} \n"
    #       "{first_round_matches_list[3]} \n"
    #       )
    #
    # def first_round_players_ranking():
    #     score_by_player_first_round_list = ([upper_player_list[0][4], score_player_1],
    #                                         [lower_player_list[0][4], score_player_2]
    #                                         [upper_player_list[1][4], score_player_1],
    #                                         [lower_player_list[1][4], score_player_2],
    #                                         [upper_player_list[2][4], score_player_1],
    #                                         [lower_player_list[2][4], score_player_2]
    #                                         [upper_player_list[3][4], score_player_1],
    #                                         [lower_player_list[3][4], score_player_2]
    #                                         )


