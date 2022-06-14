

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
    def sub_menu_display():
        print("-------------------------------------------------------------------------\n"
              "--------Renseigner les infos sur le tournoi____ : Tapez 1----------------\n"
              "--------Lister les nouveau(x) joueur(s)________ : Tapez 2----------------\n"
              "--------Mettre à jour le classement des joueur  : Tapez 3----------------\n"
              "--------Afficher un rapport____________________ : Tapez 4----------------\n"
              "--------Retourner au menu principal____________ : Tapez 5----------------\n"
              )

    @staticmethod
    def menu_display_explanation():
        print("------------------------------------------------------------------------\n"
              "---Les infos que vous allez renseigner pour le tournoi sont  --> -------\n"
             "------Le Nom du Tournoi   /  Le Lieu du Tournoi -------------------------\n"
             "-------------------------------------------------------------------------\n"
             "------La date du Tournoi  /  Le Nombre de Round -------------------------\n"
             "-------------------------------------------------------------------------\n" 
             "--Type de Controle du Temps du tournoi --> Bullet ou Bitz ou coup rapide-\n"
             "-------------------------------------------------------------------------\n"
             )

    @staticmethod
    def specific_tournament_report_menu():
        print("------------------------------------------------------------------------\n"
             "---Rapport sur les tournois-->          ---------------------------------\n"
             "---------Afficher tous les tours______ : Tapez 1-------------------------\n"
             "---------Afficher les joueurs_________ : Tapez 2-------------------------\n" 
             "---------Afficher les matchs__________ : Tapez 2-------------------------\n"
             "---------Retourner au menu principal__ : Tapez 3-------------------------\n"
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









