

class MainDisplay:
    """Docstring"""
    @staticmethod
    def menu_home_display():
        """Display the main menu"""
        print("--------------------------------------------------------------\n"
              "-------------- Bienvenue sur le gestionnaire -----------------\n"
              "-------------------pour le tournoi d'echecs-------------------\n"
              "--------------------------------------------------------------\n"
              "--------Menu tournoi : Choisir une des 4 options--------------\n"
              "--------------------------------------------------------------\n"
              )
    @staticmethod
    def tournament_menu_display():
        print("--------------------------------------------------------------\n"
              "--------Commencer un nouveau tournoi : Tapez 1----------------\n"
              "--------Reprendre un tournoi________ : Tapez 2----------------\n"
              "--------Visualiser les rapports_____ : Tapez 3----------------\n"
              "--------Quitter l'application_______ : Tapez 4----------------\n"
              "--------------------------------------------------------------\n"
              )


class SubMenusDisplay:
    """Display the sub-menus"""
    @staticmethod
    def tournament_menu_display():
        print("-------------------------------------------------------------------------\n"
              "--------Lister les nouveau(x) joueur(s)________ : Tapez 1----------------\n"
              "--------Mettre à jour le classement des joueur  : Tapez 2----------------\n"
              "--------Afficher un rapport____________________ : Tapez 3----------------\n"
              "--------Retourner au menu principal____________ : Tapez 4----------------\n"
              )

    @staticmethod
    def time_control_menu_display():
        print("------------------------------------------------------------------------\n"
             "---Type de Controle du Temps du tournoi -->     -------------------------\n"
             "---------------------------Bullet_____ : Tapez 1-------------------------\n"
             "---------------------------Blitz______ : Tapez 2-------------------------\n"
             "---------------------------Coup rapide : Tapez 3-------------------------\n"
             )

    @staticmethod
    def player_report_menu():
        print("------------------------------------------------------------------------\n"
             "---Rapport sur les joueurs -->          ---------------------------------\n"
             "---Afficher les joueurs Par ordre de classement : Tapez 1----------------\n"
             "---Afficher les joueurs Par ordre alphabétique  : Tapez 2----------------\n"
             "---Retourner au menu principal________________  : Tapez 3----------------\n"
             )

    @staticmethod
    def tournament_report_menu():
        print("------------------------------------------------------------------------\n"
             "---Rapport sur les tournois-->          ---------------------------------\n"
             "---------Afficher tous les tournois___ : Tapez 1-------------------------\n"
             "---------choisir un tournoi spécifique : Tapez 2-------------------------\n"
             "---------Retourner au menu principal__ : Tapez 3-------------------------\n"
             )

    @staticmethod
    def specific_tournament_report_menu():
        print("------------------------------------------------------------------------\n"
             "---Rapport sur les tournois-->          ---------------------------------\n"
             "---------Afficher les joueurs_________ : Tapez 2-------------------------\n" 
             "---------Afficher tous les tours______ : Tapez 1-------------------------\n"
             "---------Afficher les matchs__________ : Tapez 2-------------------------\n"
             "---------Retourner au menu principal__ : Tapez 3-------------------------\n"
             )







