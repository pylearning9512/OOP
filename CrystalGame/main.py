import time 
from gems import * 



for k, v in gems.items():
    print(gems[v])


print(f'{jasper.attack(amethyst)}')
time.sleep(5)

print(f'{jasper.attack(amethyst)}')
time.sleep(5)

print(f'{amethyst.attack(jasper)}')


print(f'\n{pearl.fuse(amethyst.name)}\n')
time.sleep(5)
