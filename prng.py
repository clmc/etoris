# prng module, for all random needs
import random
import os

# seed the RNG with /dev/urandom
def rngSeed():
    random.seed(os.urandom(256))
    os_rand = random.getrandbits(1024)
    random.seed(os_rand)

# print 100 random numbers
def randomNum():
    loopCount = 0
    while loopCount < 100:
	random_number = random.randint(0,100)
	print random_number
	loopCount += 1
