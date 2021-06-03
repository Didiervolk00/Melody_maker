# Author:       Ricardo Mokveld || Didier Volk  || Diederik van Linden
# Studentnr:    0971051         || 0973139      || 0970665
# Class:        Tinlab Machine Learning
# Assignment:   Assignment 3 :: Melody maker
 
# Prioritized requirements:
    # - The following things are required:
        # - Use building blocks to generate music
        # - Diversity in the building blocks, this means using music from different songs
    
    # - The usage of Machine learning libraries is prohibited
 
# Main design choices:
    # - We use modules to break down the program into small manageable and organized files.
    # - With the building blocks we generate music (randomly), we then give the song a rating, when a song is given a higher rating the next generation uses more building blocks from the previous generation.
 
    # Module muser
        # - This file was given to convert the generated song in an audio file
 
    #  json blocks
        # - The building blocks for the program are written in this file
        # - These blocks are extracted and used in main
    #  Main
	  # - In this file we generate the music
	  # -
# Test specification:
    # - A song is created
    # - A song is created using previous generations 
    # - The song we all like is the final product

import muser as ms
import random as rnd
import json
from playsound import playsound
import os

global genId
genId = 0

musicBlock = open('blocks.json')
data = json.load(musicBlock)

musicBlocks = data['musicBlocks']

music_blocks = []
for i in range(len(musicBlocks)):
    music = musicBlocks[f'{i}']['input']
    music_blocks.append(music)

generations = {}

# Save the current gen to the json file
def saveGenerations():

    with open('generations.json', 'w', encoding ='utf8') as genFile:
        json.dump(generations, genFile, indent=4)

#Create a first generation of songs from a range of buildingblocks
def createFirstGeneration():
    global genId
    print(genId)
    if not os.path.exists(f'generations/generation_{genId}'):
        os.makedirs(f'generations/generation_{genId}')

    generations[f'generation_{genId}'] = {}
    for i in range(3):
        generated_blocks = [rnd.choice(music_blocks) for j in range(8)]

        generations[f'generation_{genId}'][f'{i}'] = {}
        generations[f'generation_{genId}'][f'{i}']['input'] = generated_blocks
        
        # Weird looking array, is needed to combine all the buildingblocks so the muser.py generates 
        # 1 song, and nog the amount of songs according to the amount of buildingblocks
        song = [[]]
        for block in generated_blocks:
            for note in block:
                song[0].append(note)

        muser = ms.Muser()
        muser.generate(song, i, genId)

        playsound(f'generations/generation_{genId}/track_00{i}.wav')       
        
        generations[f'generation_{genId}'][f'{i}']['rating'] = int(input("Enter rating:"))
    saveGenerations()

#Creates a new generation depending on the previous generations songs
def createNewGeneration():
    global genId
    prevGeneration = open('generations.json')
    dataPrevGeneration = json.load(prevGeneration)
    genId = genId + 1
    print(genId)
    generations[f'generation_{genId}'] = {}
    for i in range(3):
        building_Blocks = dataPrevGeneration[f'generation_{genId-1}'][f'{i}']['input']
        rating = dataPrevGeneration[f'generation_{genId-1}'][f'{i}']['rating']

        pickBlocks = rating - 5
        
        for block in range(pickBlocks):
            randomBlock = rnd.randint(0,7)
            building_Blocks[randomBlock]
            
            # Weird looking array, is needed to combine all the buildingblocks so the muser.py generates 
            # 1 song, and nog the amount of songs according to the amount of buildingblocks
            song = [[]]
            for block in building_Blocks:
                for note in block:
                    song[0].append(note)

            generations[f'generation_{genId}'][f'{i}'] = {}
            generations[f'generation_{genId}'][f'{i}']['input'] = building_Blocks
            saveGenerations()
            
            if not os.path.exists(f'generations/generation_{genId}'):
                os.makedirs(f'generations/generation_{genId}')
            
        
        muser = ms.Muser()
        muser.generate(song, i, genId)

        playsound(f'generations/generation_{genId}/track_00{i}.wav')       
            
            
        generations[f'generation_{genId}'][f'{i}']['rating'] = int(input("Enter rating:"))
    saveGenerations()    
        
#The main function that creates the amount of generations that the users wants, and generating the most likely song
def createSong(amount):
    createFirstGeneration()
    for i in range(amount):
        createNewGeneration()

    global genId
    prevGeneration = open('generations.json')
    dataPrevGeneration = json.load(prevGeneration)
    genId = genId + 1
    generations[f'generation_{genId}'] = {}

    building_Blocks = dataPrevGeneration[f'generation_{genId-1}'][f'{i}']['input']
    rating = dataPrevGeneration[f'generation_{genId-1}'][f'{i}']['rating']

    pickBlocks = rating - 5
            
    for block in range(pickBlocks):
        randomBlock = rnd.randint(0,7)
        building_Blocks[randomBlock]

        # Weird looking array, is needed to combine all the buildingblocks so the muser.py generates 
        # 1 song, and nog the amount of songs according to the amount of buildingblocks
        song = [[]]
        for block in building_Blocks:
            for note in block:
                song[0].append(note)

        generations[f'generation_{genId}'][f'{0}'] = {}
        generations[f'generation_{genId}'][f'{0}']['input'] = building_Blocks
        saveGenerations()
        
        if not os.path.exists(f'generations/generation_{genId}'):
            os.makedirs(f'generations/generation_{genId}')
        
    
    muser = ms.Muser()
    muser.generate(song, i, genId)

    playsound(f'generations/generation_{genId}/track_00{i}.wav')
    
    saveGenerations()


createSong(2)


