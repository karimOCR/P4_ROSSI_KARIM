from tinydb import TinyDB


class Player:
    """initialization of player datas"""
    def __init__(self, firstname=None, nickname=None, birthdate=None, gender=None, ranking=None, score=0, player_id=0):
        self.firstname = firstname
        self.nickname = nickname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.score = score
        self.player_id = player_id

    def serialized(self):
        serialized_players_datas = {}
        serialized_players_datas['Nom'] = self.firstname
        serialized_players_datas['Prenom'] = self.nickname
        serialized_players_datas['date_de_naissance'] = self.birthdate
        serialized_players_datas['Sexe'] = self.gender
        serialized_players_datas['Classement'] = self.ranking
        serialized_players_datas['Score'] = self.score
        serialized_players_datas['id_du_joueur'] = self.player_id
        return serialized_players_datas

    def unserialized(self, serialized_player):
        firstname = serialized_player["Nom"]
        nickname = serialized_player["Prenom"]
        birthdate = serialized_player["date_de_naissance"]
        gender = serialized_player["Sexe"]
        ranking = serialized_player["Classement"]
        score = serialized_player["Score"]
        player_id = serialized_player["Id_du_joueur"]
        return Player(firstname,
                      nickname,
                      birthdate,
                      gender,
                      ranking,
                      score,
                      player_id
                      )

    def __str__(self):
        return f"{self.firstname} {self.nickname}"

    def __repr__(self):
        return f"{self.firstname} {self.nickname}, classement : {self.ranking}"

    def add_undefined_firstname(self):
        # fonction pour contraindre d'entrer un nom de famille pour l'inscription
        firstname = False
        informed_firstname = False
        while not informed_firstname:
            firstname = input(f"Veuillez donner le nom de famille du joueur: ")
            if firstname != "":
                informed_firstname = True
            else:
                print(f"vous devez entrer le nom de famille du joueur")
        return firstname

    def add_undefined_nickname(self):
        nickname = False
        informed_nickname = False
        while not informed_nickname:
            nickname = input(f"Veuillez donner le prénom du joueur: ")
            if nickname != "":
                informed_nickname = True
            else:
                print(f"vous devez entrer le prénom du joueur")
        return nickname


    def add_undefined_gender(self):
        informed_gender = False
        defined_gender = None
        while not informed_gender:
            gender = input(f"Veuillez saisir le genre du joueur M pour masculin ou F pour feminin: ")
            if (gender == "M") or (gender =="m"):
                informed_gender = True
                defined_gender = "Homme"
                print("vous êtes un Homme")
            elif (gender == "F") or (gender =="f"):
                informed_gender = True
                defined_gender = "Femme"
                print("vous êtes une Femme")
            else:
                print("Veuillez SVP taper H ou F")
        return defined_gender


    def add_undefined_ranking(self):
        ranking = -1
        informed_ranking = False
        while not informed_ranking:
            ranking = input("veuillez entrer votre classement ELO : ")
            ranking = int(ranking)
            if ranking >= 0:
                informed_ranking = True
            else:
                print(f"Veuillez entrer un classement ELO correcte SVP")
        return ranking


    def add_undefined_birthdate(self):
        birthdate_list = []

        informed_birthday = False
        while not informed_birthday:
            birthday = input("entrer votre jour de naissance: ")
            #birthday = int(birthday)
            if (birthday.isdigit()) and (len(birthday) == 2) and (int(birthday) < 32):
                informed_birthday = True
                birthdate_list.append(birthday)
            else:
                print("vous devez entrer un chiffre inférieur ou égal à 31")

        informed_birthmonth = False
        while not informed_birthmonth:
            birthmonth = input("entrer votre mois de naissance: ")
            #birthmonth = int(birthmonth)
            if birthmonth.isdigit() and len(birthmonth) == 2 and int(birthmonth) < 13:
                informed_birthmonth = True
                birthdate_list.append(birthmonth)
            else:
                print("vous devez entrer un chiffre inférieur ou égal à 12")

        informed_birthyear = False
        while not informed_birthyear:
            birthyear = input("entrer votre année de naissance: ")
            #birthyear = int(birthyear)
            if birthyear.isdigit() and len(birthyear) == 4:
                informed_birthyear = True
                birthdate_list.append(birthyear)
            else:
                print("vous devez entrer une année à 4 chiffres")
        return f"{birthdate_list[0]}/{birthdate_list[1]}/{birthdate_list[2]}"

    # def add_score_player(self):
    #     informed_score_player = False
    #     while not informe_score_player:
    #         try:
    #             score_player_1 = input(f"Entrez le score de {match.player_1} :")
    #             float(score_player_1)
    #         except Exception:
    #             print("Vous devez entrer 0, 0.5, ou 1")
    #         else:
    #             match.score_player_1 = float(score_player_1)
    #             match.player_1.tournament_score += float(score_player_1)
    #             informed_score_player_1 = True


    # def add_player_id(self):
    #     """Recuperer id au joueur venant du document de TinyDB"""
    #     #database = TinyDB('db.json', indent=4)
    #     players_table = database.table('players')
    #     informed_player_id = False
    #     while not informed_player_id:
    #         for player in players_table.all():
    #             player_id = player.doc_id
    #             informed_player_id = True
    #     return

    # @staticmethod
    # def modify_player_ranking(cls: "Player"):
    #     """To modify manually the player ranking"""
    #     player_id = check.request_id(PLAYERS)
    #     player_data = PLAYERS.get(doc_id=player_id)
    #     print(str(player_id))
    #     player = Player.deserialize_player(Player, player_id)
    #     print(f"The general score of this player is {str(player.ranking)}")
    #     print("Enter the new general score : ")
    #     new_player_score = check.request_only_numbers()
    #     PLAYERS.update(
    #         {"ranking": new_player_score},
    #         where("ranking") == player_data.get("ranking"))
    #     print(f"The general score of {player.first_name} is now at {str(new_player_score)}")
    #     utils.display_enter_to_continue()



