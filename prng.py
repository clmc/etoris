## prng module, for all random needs
import random
import math
import os

# [MAIN] seed the RNG with /dev/urandom
def rngInitSeed():
    random.seed(os.urandom(256))
    os_rand = random.getrandbits(40960)
    random.seed(seeded_urand)

# [INIT] seed well and assign stats
def statRoll():
    random.seed(os.urandom(8192))
    stat_roll = random.getrandbits(40960)
    random.seed(stat_roll)
    stat_random = random.randint(1,11)
    print stat_random

# [COMBAT] generate random 1-100 number for combat purposes
def randomAttack():
    while True:
	random.seed(os.urandom(1024))
	os_atk_rand = random.getrandbits(9216)
	random.seed(os_atk_rand)
	atk_random = random.randint(0,100)

# [DEBUG] print 100 random numbers
def randomNum():
    loopCount = 0
    while loopCount < 100:
	random_number = random.randint(0,100)
	print random_number
	loopCount += 1
