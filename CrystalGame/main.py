import time 
from gems import * 

#text game in development, no game loop yet, this is basic testing of the gem objects and the attack/fuse methods


print(f'{jasper.attack(amethyst)}')
time.sleep(5)

print(f'{jasper.attack(amethyst)}')
time.sleep(5)

print(f'{amethyst.attack(jasper)}')


print(f'\n{pearl.fuse(amethyst.name)}\n')
time.sleep(5)
