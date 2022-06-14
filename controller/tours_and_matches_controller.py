from tinydb import TinyDB

from models.tours_and_matches_model import Tour
from models.tours_and_matches_model import Match
from models.player_model import Player

def start_matches_by_round():
    database = TinyDB('db.json', indent=4)
    round_matches_table = database.table('rounds_matches')
    round_matches_table.truncate() # clear the table first

    players_table = database.table('players')

    """Creation d'une instance de l'objet de classe Match"""
    instance_match = Match()


    """Execution de la methode du premier tour """
    liste_du_premier_pool, liste_du_second_pool = instance_match.listing_of_players()
    print(liste_du_premier_pool, liste_du_second_pool)


    """Enregistrement des matchs du premier tour"""
    first_round_matches_dict, liste_des_matchs_premier_tour = instance_match.add_match_score_first_round(liste_du_premier_pool, liste_du_second_pool)
    resultant_instance_round_1 = instance_match.first_round_list_sliced_by_match(liste_des_matchs_premier_tour)
    print(f"le resultat de chaque match en liste de dictionnaire {resultant_instance_round_1}")

    round_matches_table.insert({"match": resultant_instance_round_1})

#def start_display_first_round_by_score revoit vers le main pour le display
    """Appel de la Methode pour le classement des joueurs du premier round"""
    first_round_classement = Match()
    dict_des_matches_premier_round = first_round_classement.sorted_players_after_first_round(first_round_matches_dict)


    """Update du score de chaque Joueur en utilisant l'id de chaque joueur"""
    liste_joueurs_par_id_premier_round = Match()
    liste_joueurs_par_id_premier_round = liste_joueurs_par_id_premier_round.sorted_players_by_id_after_first_round(dict_des_matches_premier_round)

    """Mise à jour du score des joueurs apres le premier round en utilisant l'id de chaque joueur"""
    dict_des_joueurs_id_tries = Match()
    dict_des_joueurs_id_tries = dict_des_joueurs_id_tries.dict_sorted_players_by_id_after_first_round(liste_joueurs_par_id_premier_round)


    for key, value in dict_des_joueurs_id_tries.items():
        print(key, value)
        print(players_table.get(doc_id= key)["Score"])
        players_table.update({"Score": value}, doc_ids=[key])


    """methode du scond tour"""
    instance_2_match = Match()
    second_round_matches = add_match_score_second_round()







# Enregistrement du classement du premier tour dans db.json
# round_matches_table.insert(first_round_classement)



# Execution de la methode du second tour
#
#
# second_round_resultat = Match()
# second_round_resultat.add_match_score_second_round(first_round_classement)









"""creation de la premiere instance de la classe Tour composée de 4 matchs"""
"""on recupere 4 listes de 2 tuples chacune"""
#round_1 = round_matches_table.insert(first_round_matches_list)

"""on insert id_du_joueur par rapport au joueur_1 et joueur_2"""






# first_round_matches_table.insert({"joueur_1": first_round_match[0][0]})
# first_round_matches_table.insert({"joueur_2": first_round_match[1][0]})
# first_round_matches_table.insert({"joueur_1": first_round_match[2][0]})
# first_round_matches_table.insert({"joueur_1": first_round_match[3][0]})








