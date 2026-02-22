class dog:

    species='dog'

    def __init__(self, colour, height):
        self.colour=colour
        self.height=height

Bj=dog('brown',50)
Hawkeye=dog('black',30)

print('\nBj is a {} and is colour {} and is {} centimeters tall'.format(Bj.species, Bj.colour, Bj.height))
print('Hawkeye is a {} and is colour {} and is {} centimeters tall'.format(Hawkeye.species, Bj.colour, Bj.height),'\n')