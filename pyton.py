print ('haello wrod')

print('🌻 Morning Dharma!')
print('🙋🏽 Evening Sonny!')

print('       1')
print('     2 3')
print('   4 5 6')
print('7 8 9 10')

#alfabet
print('p p p p        p p p p    ')      
print('p       p      p       p  ') 
print('p       p      p       p  ')    
print('p p p p        p p p p    ')    
print('p              p          ')            
print('p              p          ')           
print('p              p          ')    
#pesan
print('02-juni-2006')
print('sangat bimbang ingin yang mana')
print('data analys atau web developer')
print('bagaimana apakah sudah menjadi apa yang kamu mau')
print('😎')
# menghitung suhu atau temperatur
temp_f = -1
temp_c = (temp_f - 32) / 1.8

print(temp_c)

#menghitung bmi
weight = 30
height = 1.70

bmi = weight / (height**2)

print(bmi)

#masungkan pengguna
username = input('Enter your name: ')

print(username)

age = int(input('What is your age? '))

print(age)

#menghitung geometri
a = int(input('sisi pendek '))

print(a)


b = int(input('sisi pendek lainya '))

c = (a**2 + b**2)

print (c)

#tular mata uang
pesos = int(input('what do you left in pesos?'))
soles = int(input('what do you left in soles?'))
reais= int(input('what do you left in reais?'))

total = pesos * 0.0002394  + soles * 0.2688  + reais * 0.1691  

print(total)

#randhom
import random

num = random.randint(0, 1)
             
if num > 0.5: 
  print('Heads')
else:
  print('Tails')  


import random

question = input('question : ')
random_number = random.randint(1, 9)

if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
else:
  answer = 'Error'
  
print('Magic 8 Ball:  ' + answer)

#operaotr logika
height = int(input("berapa tinggi badan anda? "))
credits = int(input("berapa banyak kredit yang anda miliki? "))

if height >= 160  and credits >= 10 :
  print('nikmatiperjalananya')
elif credits < 10 and height > 160 :
  print('anda tidak memiliki cukup tinggi badan untuk berkendara')
elif height > 160 and credits < 10 :
  print('anda tidak memiliki cukup kredit')
else:
  print('anda tidak memenuhi salah satu persyaratan')
  
  # Sorting Hat 🧙‍♂️
# Codédex

gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('===============')
print('The Sorting Hat')
print('===============')

# ~~~~~~~~~~~~~~~ Question 1 ~~~~~~~~~~~~~~~

print('Q1) Do you like Dawn or Dusk?')

print('  1) Dawn')
print('  2) Dusk')

answer = int(input('Enter answer (1-2): '))

if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin +=1
else:
  print('Wrong input.')

# ~~~~~~~~~~~~~~~ Question 2 ~~~~~~~~~~~~~~~

print("\nQ2) When I'm dead, I want people to remember me as:")

print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
  hufflepuff += 2
elif answer == 2:
  slytherin += 2
elif answer == 3:
  ravenclaw += 2
elif answer == 4:
  gryffindor += 2
else:
  print('Wrong input.')

# ~~~~~~~~~~~~~~~ Question 3 ~~~~~~~~~~~~~~~

print('\nQ3) Which kind of instrument most pleases your ear?')

print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
  slytherin += 4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw +=4
elif answer == 4:
  gryffindor += 4
else:
  print('Wrong input.')
  
print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

# Bonus Part

if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print('🦁 Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print('🦅 Ravenclaw!')
elif hufflepuff >= slytherin:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')
  
#array atau list
#array adalah kumpulan data yang memiliki index yang sama
hobi =  "main game, makan, tidur"
print(hobi)

hobby = ["main game", "makan", "tidur"]
print(hobby[2-1])

#looping
#looping adalah perulangan yang digunakan untuk melakukan sesuatu secara berulang-ul
buah = "semabngka"
start = 0
ending = 100

while start < ending:
    print(buah)
    start = start + 1

#fungtion
#fungsi adalah sekumpulan kode yang dapat dipanggil kembali
def tambah(x, y):
  return x + y

print(tambah(20, 25))