#  C:\Users\Antonio\Desktop\pCloud\Programmazione\Python\CorsoUdemy\168_Packages\main.py

from utility import multiply, divide

# Con il from posso importare anche un package
from shopping.more_shopping import shopping_cart

print (shopping_cart.buy("apple"))


#  Il file che viene eseguito ha la proprietà 
# __name__ == '__main__'

if __name__ == '__main__':
  print ('This is main file')