from collections import namedtuple
from typing import NoReturn

print('welcome to MadLib!')
print('')
print('Madlib is a game that allows you to input the desired category of words. Madlib is a two player game, one player will have the story in hand and will not let the other person see it. They will ask for whatever category of word that is required at that time. They will annotate the word in that desired spot, At the end of the story and all place holders are filled, then the story reader will read the whole story at loud. Enjoy the game!')
print('')
print('Past Tense Verb - Past tense verbs refer to actions or events in the past.')
print('')
print('Plural noun - is a word that indicates that there is more than one person, animal place, thing, or idea.')
print('')
print('Adjective - a word or phrase naming an attribute.')
print('')
print('Please input the required fields and enjoy the story at the end! Enjoy!')


adj_1 = input("Adjective: ")
adj_2 = input("Adjective: ")
adj_3 = input("Adjective: ")
adj_4 = input("Adjective: ")
adj_5 = input("Adjective: ")
adj_6 = input("Adjective: ")
firstName_1 = input("First Name: ")
firstName_2 = input("First Name: ")
firstName_3 = input("First Name: ")
girlName = input("Girl's name: ")
pluralNoun_1 = input("Plural noun: ")
pluralNoun_2 = input("Plural noun: ")
pluralNoun_3 = input("Plural noun: ")
pluralNoun_4 = input("Plural noun: ")
pluralNoun_5 = input("Plural noun: ")
pastTenseVerb = input("Past Tense verb: ")
lgAnimal = input("large animial: ")
smAnimal = input("small animial: ")
numbers = input("number between 1 and 50: ")
number_1 = input("Input a number: ")
number_2 = input("Random number: ")

print('')

mad_lib_story = "I the %s and %s %s have %s %s's %s sister and plan to steal her %s %s! What are a %s and backpacking %s to do? Before you can help %s, you'll have to collect the %s %s and %s %s that open up the %s worlds connected to A %s Lair. There are %s %s and %s %s in the game, along with hundreds of other goodies for you to find."

print(
    mad_lib_story
    % (
        adj_1,
        adj_2,
        firstName_1,
        pastTenseVerb,
        firstName_2,
        adj_3,
        adj_4,
        pluralNoun_1,
        lgAnimal,
        smAnimal,
        girlName,
        adj_5,
        pluralNoun_2,
        adj_6,
        pluralNoun_3,
        numbers,
        firstName_3,
        number_1,
        pluralNoun_4,
        number_2,
        pluralNoun_5,
    )
)