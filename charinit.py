def character_init():
    while True:
        player_race = raw_input("Please select your race: (d)warf, (e)lf, or (h)uman.\t").lower()[:1]
        if player_race in ('d','e','h'):
            races = {'d':'Dwarf', 'e':'Elf', 'h':'Human'}
            print("So you want to play a %s? A fine choice, indeed!") % races[player_race]
            #goToNextPartOfGame()
        else:
            print("Invalid input. Restarting.")
            character_init()
