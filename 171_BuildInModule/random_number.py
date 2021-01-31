# C:\Users\Antonio\Desktop\pCloud\Programmazione\Python\CorsoUdemy\171_BuildInModule\random_number.py

import random

# Se voglio un numero casuale tra 0 e 1
print(random.random())

# Se voglio un random intero
print(random.randint(1,10))

# Se voglio a scelta 
print(random.choice([1,2,3,4,5]))

# Se voglio mischiare casualmente una lista in place 
my_list = [1,2,3,4,5]

random.shuffle(my_list)
print(my_list)



