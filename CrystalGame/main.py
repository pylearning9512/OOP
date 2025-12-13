import time 
from gems import * 


#testing how to print the available gems, this will be a character selection one day
for k, v in gems.items():
    print(gems[v])

#these print statements are testing the imported "gems.py" file by calling some methods between gems
print(f'{jasper.attack(amethyst)}')
time.sleep(5)

print(f'{jasper.attack(amethyst)}')
time.sleep(5)

print(f'{amethyst.attack(jasper)}')


print(f'\n{pearl.fuse(amethyst.name)}\n')
time.sleep(5)
