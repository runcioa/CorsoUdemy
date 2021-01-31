# C:\Users\Antonio\Desktop\pCloud\Programmazione\Python\CorsoUdemy\171_BuildInModule\modulo_sys.py

import sys

# Recupero l'argomento della riga di comando
print(sys.argv)

nome_file = sys.argv[0]
first_argument = sys.argv[1]
second_argument = sys.argv[2]

print(f'hiiiiiiiiiiiii! {first_argument}, {second_argument}')
