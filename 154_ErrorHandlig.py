# # Error Handling

# while True:
#   try:
#     age = int(input('what is your age?'))
#   except ValueError:
#     print ('enter a number')
#   except ZeroDivisionError:
#     print ('enter a number greater than 0')
#   else:
#     print('thank you!')
#     break
#   finally:
#     print('i am finally done')


# def sum(num1, num2):
#   try:
#     return num1+num2
#   except TypeError as err:
#     # Così mi crea l'eccezione
#       print ('enter a number' + err)
#     # Così mi da solo il messaggio di errore  
#       print (f'enter a number beacause {err}')


# print (sum(1,'2'))

# def sum(num1, num2):
#   try:
#     return num1/num2

#   except (TypeError, ZeroDivisionError) as err:
#     # Così mi da solo il messaggio di errore  
#       print ( err)


# print (sum(1,'2'))



# Creare Errori:

while True:
  try:
    age = int(input('what is your age?'))
    raise ValueError ('hey cut it out')
    
  except ZeroDivisionError:
    print ('enter a number greater than 0')
  else:
    print('thank you!')
    break
  finally:
    print('i am finally done')




# Creare Eccezioni:

while True:
  try:
    age = int(input('what is your age?'))
    raise Exception ('hey cut it out')
    
  except ZeroDivisionError:
    print ('enter a number greater than 0')
  else:
    print('thank you!')
    break
  finally:
    print('i am finally done')

