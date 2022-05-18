from tinydb import TinyDB

from tours_and_matches_model import Tour
from tours_and_matches_model import Match

database = TinyDB('db.json', indent=4)
round_matches_table = database.table('rounds_matches')
round_matches_table.truncate() # clear the table first

match = Match()
round_1 = match.get_match_score()


"""creation de la premiere instance de la classe Tour composée de 4 matchs"""
"""on recupere 4 listes de 2 tuples chacune"""
round_1 = round_matches_table.insert(first_round_matches_list)

"""on insert id_du_joueur par rapport au joueur_1 et joueur_2"""






# first_round_matches_table.insert({"joueur_1": first_round_match[0][0]})
# first_round_matches_table.insert({"joueur_2": first_round_match[1][0]})
# first_round_matches_table.insert({"joueur_1": first_round_match[2][0]})
# first_round_matches_table.insert({"joueur_1": first_round_match[3][0]})








