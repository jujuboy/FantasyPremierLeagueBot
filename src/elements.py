"""
Module containing basic elements for the environment.
"""
import numpy as np

class Player():
    """
    Class for real football players.
    """

    def __init__(self, price: float,
                 team: str, pos: str,
                 name: str):

        if not (isinstance(price, float) or isinstance(price, int)):
            raise TypeError("Price argument must be a float or int.")

        if price <= 0:
            raise ValueError("Price argument must be greater than 0.0.")

        if not isinstance(pos, str):
            raise TypeError("Position argument must be a string.")

        if not isinstance(team, str):
            raise TypeError("Team argument must be a string.")

        if not isinstance(name, str):
            raise TypeError("Name argument must be a string.")

        self.__price = np.float_(price)
        self.__team = team
        self.__pos = pos
        self.__name = name

    def price(self):
        """
        Returns the FPL price of the player.
        """
        return self.__price

    def name(self):
        """
        Returns the FPL name of the player.
        """
        return self.__name

    def pos(self):
        """
        Returns the FPL position of the player.
        """
        return self.__pos

    def team(self):
        """
        Returns the FPL team of the player.
        """
        return self.__team

    def set_team(self, new_team:str):
        """
        Method to set new team of player.
        """
        if not isinstance(new_team, str):
            raise TypeError("New team argument must be a string.")
        self.__team = str(new_team)

    def price_change(self, value:float):
        """
        Method to implement price change of a player.
        """
        if not (isinstance(value, float) or isinstance(value, int)):
            raise TypeError("Value argument must be a float or int.")
        self.__price += value

class Fpl_Team():
    """
    Class for FPL team.
    """
    def __init__(self, player_prices:list,
                 player_names:list, player_positions:list,
                 player_teams:list):
        self.__players = [Player(price=player_prices[i],
                                 name=player_names[i],
                                 team=player_teams[i],
                                 pos=player_positions[i]) for i in range(len(player_names))]
    
    def players(self):
        """
        Method to return player names.
        """
        return self.__players

def main():

    player_names = ['James', 'John']
    player_teams = ['LIV', 'MNC']
    player_positions = ['GKP', 'DEF']
    player_prices = [8.0, 5.0]

    my_team = Fpl_Team(player_positions=player_positions,
                    player_names=player_names,
                    player_teams=player_teams,
                    player_prices=player_prices)

if __name__ == main():
    main()
