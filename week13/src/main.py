from aggregation import Player
from aggregation import Team


smith = Player("Smith", "Goalie")
smith2 = Player("Smith", "Goalie")

print(smith == smith2)


print(type(smith))
gert = Player("Gert", "Forward")

wet_tissues = Team("The Wet Tissues")

wet_tissues.add_player(smith)
wet_tissues.add_player(gert)

print(wet_tissues.players)
# here

wet_tissues.remove_player(smith2)

print(wet_tissues.players)
