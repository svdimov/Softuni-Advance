from project import Player


class Team:
    def __init__(self,name:str,rating:int):
        self.__rating = rating
        self.__name = name
        self.__players:list[Player] = []

    def add_player(self,player:Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"


    def remove_player(self,player_name: str):
        c_player = next((p for p in self.__players if p.name == player_name),None)
        if c_player:
            self.__players.remove(c_player)
            return c_player
        return  f"Player {player_name} not found"




