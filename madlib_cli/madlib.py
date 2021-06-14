from collections import namedtuple
from typing import NoReturn


print('welcome to MadLib!')
print('Madlib is a game that allows you to input the desired category of words. Madlib is a two player game, one player will have the story in hand and will not let the other person see it. They will ask for whatever category of word that is required at that time. They will annotate the word in that desired spot, At the end of the story and all place holders are filled, then the story reader will read the whole story at loud. Enjoy the game!')

print_fName = print('First Name'
# Do all of these in order of the story and name them corresponding to how many there are.
firstName = input()

print_LaAnimal = print('Large Animal')

print_SmAnimal = print('Small Animal')

print_giName = print('Girl Name')

print_Numbers = print('Numbers 1 - 50')

print_number = print('Number')

print_pastTenseVerb = print('Past Tense Verb - Past tense verbs refer to actions or events in the past.')

print_pluralNoun = print('Plural noun - is a word that indicates that there is more than one person, animal place, thing, or idea.')

print_adj = print('Adjective - a word or phrase naming an attribute.')

adjective = input()
giName = input()
LaAnimal = input()
SmAnimal = input()
Numbers = input()
number = input()
pastTenseVerb = input()
pluralNoun = input()

# # Adjective X 6
# fName = ['', '', '']
# # a first Name X3
# pastTenseVerb = '' 
# # Past tense verb
# pluralNoun = ['', '', '', '', '']
# # plural noun X5
# largeAnimal = []
# # Large Animal 
# smallAnimal = []
# # Small animal
# girlsName = ''
# # a Girls name
# numbers =  1 - 50
# # Number 1 - 50
# number = [1, 2]
# # number X2

# Adjective -X 
# Adjective
# First name - X
# Past tense Verb
# A first name
# Adjective
# Adjective
# Plural Noun
# Large Animal
# Small Animal
# A girls name
# adjective
# plural Noun
# number
# plural Noun

Story = print('Once apon a time, in a far far land. A young lad named' + (print_fName) + (firstName) + 'He/she is' + (print_adj) + (adjective) + '.  ')

print(Story)