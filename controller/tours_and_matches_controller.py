from tinydb import TinyDB

from models.tours_and_matches_model import Tour
from models.tours_and_matches_model import Match


database = TinyDB('db.json', indent=4)
round_matches_table = database.table('rounds_matches')
round_matches_table.truncate() # clear the table first

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

"""Appel de la Methode pour le classement des joueurs du premier round"""
first_round_classement = Match()
dict_des_matches_premier_round = first_round_classement.sorted_players_after_first_round(first_round_matches_dict)


"""Update du score de chaque Joueur en utilisant l'id de chaque joueur"""

liste_joueurs_par_id_premier_round = Match()
liste_joueurs_par_id_premier_round.sorted_players_by_id_after_first_round(dict_des_matches_premier_round)






# for i in range(3):
#     i+=1
#     match = Match()
#     id_joueur_1 = match.upper_players_list[i]
#     match.player_1 = id_joueur_1
#     id_joueur_2 = match.lower_players_list[i]
#     match.player_2 = id_joueur_2
#     score_1 = match.score_player_1
#     match.score_player_1 = score_1
#     score_2 = match.score_player_2
#     match.score_player_2 = score_2




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








