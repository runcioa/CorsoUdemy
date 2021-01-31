def multiply_by2(item):
  # map restituisce direttamante un oggetto dello stesso tipo passato
  return item*2

# Con map chiamo la funzione senza le parentesi e poi gli passo l'argomento dopo

print(list(map(multiply_by2, [1,2,3])))

# Essendo una pure function non modifica il dato originale


# Funzione per i numeri dispari
def only_odd(item):
  # faccio il modulo 2 e se il resto è diverso da 0 è dispari
  # restituisco vero se dispari e falso se pari
  return (item % 2 != 0)

# La funzione filter restituisce solo quello che la funzione restituisce come vero
print (list(filter(only_odd, [1,2,3])))


my_list = [1,2,3]
your_list  = [10, 20, 30]

# zip copmbina le liste una a una e resituisce: [(1, 10), (2, 20), (3, 30)]
# Devono avere la stesasa lunghezza

print(list(zip(my_list, your_list)))

from functools import reduce

my_list_1 = [1,2,3,4]

def accumulator(acc, item):
  # print (acc, item)
  return acc + item

print (reduce(accumulator, my_list_1,0))

# Restituisce 6 perchè parto con l'accumulatore uguale a zero e passo 1 da my_list
# la funzione restituisce 1 a questo punto acc vale 1 passo 2 da my_list e la funzione restituisce 3
# accumulator vale 3 e io passo 3 quindi mi restituisce 6 che è il valore finale
# se passo da my list 4 ho 6 dall'accumulatore e restituisce 10

