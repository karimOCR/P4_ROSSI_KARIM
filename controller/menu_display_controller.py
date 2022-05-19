



class ClearScreen:
    """Clear the terminal"""
    def __call__(self):
        # for windows
        if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
        _ = system('clear')



    @staticmethod
    def menu_home_check(self, message):
        """ check if the input number is correct"""
        user_choice = input("----choisissez ici : ")
        while user_choice not in ["1", "2", "3", "4"]:
            user_choice = input(f"Error : {message}")
            return user_choice

    def get_user_input(message):
        user_choice = input(message)
        return user_choice

    @staticmethod
    def menu_home_check(self):
        menu = menu_home_display(self)
        print()
        chosen_option = self.menu_home_check(menu)
        if chosen_option == "1":
            self.controller.run_new_tournament()
        elif chosen_option == "2":
            self.controller.run_reload_tournament()
        elif chosen_option == "3":
            print("Rapport")
        else:
            exit()