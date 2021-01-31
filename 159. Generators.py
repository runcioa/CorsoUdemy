# # Generators

# def generator_function(num):
#   for i in range(num):
#     yield i * 2

# g = generator_function(100)

# print (next (g))
# print  (next(g))

# print(next(g))

# #Ciclo FOR

# def special_for(iterable):
#   iterator = iter(iterable)
#   while True:
#     try:
#       print(iterator)
#       print(next (iterator))
#     except StopIteration:
#       break


# special_for([1,2,3,4,5])

#  Creare un generator

# class Mygen:
#   """
#   docstring
#   """
#   current = 0

#   def __init__(self, first, last):
#     self.first = first
#     self.last = last
#     Mygen.current = self.first

#   def __iter__(self):
#     return self

#   def __next__(self):
#     if Mygen.current < self.last:
#       num = Mygen.current
#       Mygen.current += 1
#       return num
#     raise StopIteration

# gen = Mygen(1,1000)

# for i in gen:
#   print(i)


#  Fibonacci number

def fib(number):
  primo = 0
  secondo = 1
  for i in range(number):
    yield primo
    temp = primo
    primo = secondo
    secondo = temp + primo

# for x in fib(10000):
#   print (x)


def fib2(number):
  primo = 0
  secondo = 1
  result = []
  for i in range(number):
    result.append(primo)
    temp = primo
    primo = secondo
    secondo = temp + secondo
  return result

print(fib2(1000))
