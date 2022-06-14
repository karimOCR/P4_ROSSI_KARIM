from models.player_model import Player

from tinydb import TinyDB

def start_player_registration():
    database = TinyDB('db.json', indent=4)
    players_table = database.table('players')
    players_table.truncate() # clear the table first

    """"creation d'une instance de l'objet Player"""
    for i in range(8):
        i+=1
        player = Player()
        nom = player.add_undefined_firstname()
        player.firstname = nom
        prenom = player.add_undefined_nickname()
        player.nickname = prenom
        date_de_naissance = player.add_undefined_birthdate()
        player.birthdate = date_de_naissance
        genre = player.add_undefined_gender()
        player.gender = genre
        classement = player.add_undefined_ranking()
        player.ranking = classement



        print(f"""
                     **************RECAPITULATIF DU JOUEUR {i}  *********************
                     Le Joueur {nom} {prenom} né(e) le {date_de_naissance}, de genre {genre} avec un classement ELO de {classement}
                     vient d'être enregistré pour le tournoi
                     **************************************************************
                     """)

        #on appelle la methode
        serialized_player = player.serialized()
        #recupere id du joueur
        id_du_joueur = players_table.insert(serialized_player)
        player.player_id = id_du_joueur
        players_table.update({"id_du_joueur": id_du_joueur}, doc_ids=[id_du_joueur])
        print(player.serialized())


