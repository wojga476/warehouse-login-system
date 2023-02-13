# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 18:58:03 2023

@author: Wojtek
"""
import sys

class Warehouse:
    
    def __init__(self, list_prod):
        self.list_prod = list_prod
        
    def show_items(self):
        print('Available products: ')
        for product in self.list_prod:
            print(product)
    
    def add(self):
        self.name_prod = input('Enter the product name: >>>>')
        if self.name_prod not in self.list_prod:
             self.list_prod.append(self.name_prod)
             print(f'Product {self.name_prod} has been added to warehouse.')
        
    def remove(self):
        self.name_prod = input('Enter name of product you want to remove: >>>>')
        if self.name_prod in self.list_prod:
            self.list_prod.remove(self.name_prod)
            print(f'Product {self.name_prod} has been removed from warehouse.')
        else:
            print(f'Product {self.name_prod} is out of stock.')
            
# %%
warehouse = Warehouse(['milk', 'water', 'eggs'])
CODE_PIN = '1234'
counter = 0
NICK = 'benjami'
nick = ''
pin = ''

print('Welcome to warehouse login system.')
print('*' * 30)

while  pin != CODE_PIN and nick != NICK and counter < 3 :
    
    nick = input('Enter your nick: ')
    pin = input(f'Enter your code pin, {nick}: ')
    if len(pin) == 4 and pin in '0123456789':
        print('*' * 30)
        print('*' * 30)
        print('CODE PIN CORRECT.')
        print('SUCCESSFULLY LOGGED INTO THE SYSTEM.')
        while True:
            print('*' * 30)
            print('Enter 1 to show stock status.')
            print('Enter 2, to add new product.')
            print('Enter 3, to remove product.')
            print('Enter 4, to quit.')
            print('*' * 30)
            choice_user = int(input('>>>> '))
            if choice_user == 1:
                print('*' * 30)
                warehouse.show_items()
            elif choice_user == 2:
                print('*' * 30)
                warehouse.add()
            elif choice_user == 3:
                print('*' * 30)
                warehouse.remove()
            elif choice_user == 4:
                sys.exit()
    counter += 1
    print('*' * 30)
    print('NICK OR PIN IS INCORRECT.')
else:
    print('Too many login attempts.')
