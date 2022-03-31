# choosing what fortune to show (random.randint() and "if")
import random

fortune_number = random.randint(1, 3)

fortune_text = ''

if fortune_number == 1:
  fortune_text = 'You will have a great day!'
if fortune_number == 2:
  fortune_text = 'Today will be tough...but worth it.'
if fortune_number == 3:
  fortune_text = 'You will get married this year!'
  
lucky_number = random.randint(1, 100)
print(f'{fortune_text} Yout Lucky Nomber is: {lucky_number}')
