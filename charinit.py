# gets initial data about player race choice
# only h (human) is recognized at the moment
def character_init():
    print "Please select your race"
    raceLoop = 0
    while raceLoop == 0:
        player_race = raw_input()
	if player_race == "m":
	    print "(m)ore, (h)uman, (e)lf, (d)warf"
	elif player_race != "h" and "e" and "d":
	    print "%s not recognized, (m)ore?" % player_race
	else:
	    print "So, you want %s as your variable" % player_race
	    break
