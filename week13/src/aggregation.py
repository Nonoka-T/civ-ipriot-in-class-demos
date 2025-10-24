# player.py
class Player():
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def play(self):
        print(f"{self.name} is tearing up the field!")


    def __str__(self):
        return f"Player: {self.name}, {self.position}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name == other.name and self.position == other.position

# team.py
class Team():
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player_to_remove):
        if player_to_remove in self.players:
            self.players.remove(player_to_remove)
        else:
            print(f"{player_to_remove} was not found")
            # f = format
        # found = -1
        # # print(type(self.players[0]))
        # for index in range(len(self.players)):
        #     # print(type(self.players[index]))
        #     if self.players[index].name == player_to_remove.name:
        #         found = index
        #         break
        # if found != -1:
        #     print(f"Removed player: {self.players.pop(found)}")
        # else:
        #     print("We could not find that player")