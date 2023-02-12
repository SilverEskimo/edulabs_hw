from best_bus_ever.src.utils.exceptions import *


class UserInputValidation:

    @staticmethod
    def valid_role_choice(choice: str):
        try:
            role = int(choice)
        except ValueError as e:
            raise WrongUserRoleChoice(f"Error: role should be a number")
        if not 1 <= role <= 3:
            raise WrongUserRoleChoice(f"Error: role has to be 1 or 2 (3 for exit)")
        return role

    @staticmethod
    def valid_manager_action(action: str, delete_action=False):
        try:
            user_action = int(action)
        except ValueError:
            raise WrongManagerAction(f"Error: manager action should be a number")
        if not delete_action:
            if not 1 <= user_action <= 5:
                raise WrongManagerAction(f"Error: manager action has to be 1 or 2 or 3 or 4 or 5")
        else:
            if not 1 <= user_action <= 4:
                raise WrongManagerAction(f"Error: manager action has to be 1 or 2 or 3 or 4")
        return user_action

    @staticmethod
    def valid_update_actions(actions: str):
        update_actions = actions.split(" ")
        res_list = []
        try:
            if len(update_actions) == 1 and update_actions[0] == "4":
                res_list.append(int(actions[0]))
                return res_list
            for action in update_actions:
                res_list.append(int(action))
                if not 1 <= int(action) <= 3:
                    raise WrongUpdateRange(f"Error: update action cannot contain {int(action)}")
            if len(res_list) > 3:
                raise WrongUpdateRange(f"Error: too much options to update. Can be up to 3")
        except ValueError:
            raise WrongManagerAction(f"Error: update action should be a number")
        return res_list

    @staticmethod
    def valid_passenger_action(action: str):
        try:
            user_action = int(action)
        except ValueError as e:
            raise WrongPassengerAction(f"Error: passenger action is incorrect")
        if not 1 <= user_action <= 3:
            raise WrongPassengerAction(f"Error: passenger action has to be 1 or 2")
        return user_action

    @staticmethod
    def valid_line_number(line_numer: str):
        try:
            line = int(line_numer)
        except ValueError as e:
            raise WrongLineNumber(f"Error: line number should be a number")
        return line

    @staticmethod
    def valid_search_term(search_term: str):
        try:
            term = int(search_term)
        except ValueError as e:
            raise WrongSearchTerm("Error: searching option should be a number")
        if not 1 <= term <= 5:
            raise WrongSearchTerm("Error: searching option should be 1, 2, 3 or 4")
        return term







