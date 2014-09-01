def character_init():
        player_race = raw_input("Please select your race: (d)warf, (e)lf, or (h)uman.\t").lower()[:1]
        if player_race in ('d','e','h'):
            races = {'d':'Dwarf', 'e':'Elf', 'h':'Human'}
            print("So you want to play a %s? A fine choice, indeed!") % races[player_race]
        else:
            print("Invalid input. Restarting.")
            character_init()

def stat_init():
    	player_stats = raw_input("Please select an attribute template.\t").lower()[:1]
	if player_stats in ('k','m','t'):
	    init_stats = {'k':'Knight', 'm':'Mage', 't':'Thief'}
	    print("There are plenty of opportunities for a %s in the land of etoris!") % init_stats[player_stats]
	    #continue_game_function()
	else:
	    print("Please select either the (K)night, (M)age, or (T)hief stat templates")
	    stat_init()
