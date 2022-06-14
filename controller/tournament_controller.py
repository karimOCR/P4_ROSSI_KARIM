from tinydb import TinyDB
import json
from models.player_model import Player
from models.tournament_model import Tournament
#from tournament_model import Round
#import datetime

def start_tournament():
    database = TinyDB('db.json', indent=4)
    tournament_table = database.table('tournoi_infos')
    tournament_table.truncate() # clear the table first

    #db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '))

    """Creation de l'instance de l'objet tournament"""
    tournament = Tournament()
    nom_du_tournoi = tournament.add_undefined_tournament_name()
    tournament.tournament_name = nom_du_tournoi
    lieu = tournament.add_undefined_location()
    tournament.location = lieu
    date = tournament.choice_tournament_date()
    tournament.tournament_date = date
    nombre_de_tours = tournament.add_number_of_rounds()
    tournament.number_of_tours = nombre_de_tours
    controle_de_temps = tournament.add_time_control()
    tournament.time_control = controle_de_temps
    description = tournament.add_description()
    tournament.description = description




    serialized_tournament = tournament.serialized()
    tournament_table.insert(serialized_tournament)

    print(f"""
                 **************RECAPITULATIF DU TOURNOI   *********************
                 Le tournoi s'appellant {nom_du_tournoi} se déroulant à {lieu} à la date du {date}, avec un nombre 
                 de {nombre_de_tours} tours  et ayant comme type de controle du temps {controle_de_temps}
                 vient d'être enregistré avec cette description--> {description}
                 **************************************************************
                 """)

