#from controller.tours_and_matches_controller import Match
from views.menu_display_view import MainDisplay
from views.menu_display_view import SubMenusDisplay
from views.menu_display_view import specific_tournament_report_menu
from controller.tournament_controller import start_tournament
from controller.player_controller import start_player_registration
from controller.tours_and_matches_controller import start_matches_by_round


main_display = MainDisplay()
main_display.menu_home_display()

main_display.tournament_menu_display()

sub_menu_display = SubMenusDisplay()

selected_menu = input("Quel menu avez-vous choisi ? : ")
print(type(selected_menu))
if selected_menu == "1":
    sub_menu_display.sub_menu_display()
    sub_selected_menu = input("Quel sous-menu avez-vous choisi ? : ")
    if sub_selected_menu == "1":
        sub_menu_display.menu_display_explanation()  #sous menu affichant le type d'info relatif au tournoi
        start_tournament()
    if sub_selected_menu == "2":
        start_player_registration() #sous menu affichant les listes des joueurs selon l'ordre demandé
    if sub_selected_menu == "3":
        start_matches_by_round()

    if sub_selected_menu == "4":
        specific_tournament_report_menu()
        specific_tournament_report_menu = input("Quel rapport souhaitez-vous afficher ? : ")
        if specific_tournament_report_menu == "1":
            print("Vous avez choisi d'afficher la liste de tous les tours du tournoi")
            start_display_all_rounds_of_tournament() #reserver To be defined

        elif specific_tournament_report_menu == "2":
            print("Vous avez choisi d'afficher la liste de tous les joueurs")
            player_report_menu()  #methode se trouvant dans menu_display_view
            player_report_menu_selected = input("Quel type de liste des joueurs avez vous choisi d'afficher :\n"
                                                " 1--> par score  ou  2--> par ordre alphabethique\n")
            if player_report_menu_selected == "1":
               print("Vous avez choisi d'afficher les joueurs par score")
               start_display_player_by_score()  #resever To be defined

            elif player_report_menu_selected == "2":
                print("Vous avez choisi d'afficher les joueurs par ordre alphabethique")
                start_display_player_by_sorted_name()  #resever To be defined

