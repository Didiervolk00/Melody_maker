import muser as ms
import random as rnd
import json
from playsound import playsound
import os
genId = 0

musicBlock = open('blocks.json')
data = json.load(musicBlock)

musicBlocks = data['musicBlocks']

music_blocks = []
for i in range(len(musicBlocks)):
    music = musicBlocks[f'{i}']['input']
    music_blocks.append(music)

generations = {}

def saveGenerations():
    with open('generations.json', 'w', encoding ='utf8') as genFile:
        json.dump(generations, genFile, indent=4)

def createFirstGeneration():
    if not os.path.exists(f'generations/generation_{genId}'):
        os.makedirs(f'generations/generation_{genId}')

    generations[f'generation_{genId}'] = {}
    for i in range(3):
        generated_blocks = [rnd.choice(music_blocks) for j in range(8)]

        generations[f'generation_{genId}'][f'{i}'] = {}
        generations[f'generation_{genId}'][f'{i}']['input'] = generated_blocks
        
        song = [[]]
        for block in generated_blocks:
            for note in block:
                song[0].append(note)

        muser = ms.Muser()
        muser.generate(song, i, genId)

        playsound(f'generations/generation_{genId}/track_00{i}.wav')       
        
        generations[f'generation_{genId}'][f'{i}']['rating'] = int(input("Enter rating:"))
    saveGenerations()



def createNewGeneration():
    prevGeneration = open('generations.json')
    dataPrevGeneration = json.load(prevGeneration)
    for i in range(3):
        building_Blocks = dataPrevGeneration[f'generation_{genId}'][f'{i}']['input']
        rating = dataPrevGeneration[f'generation_{genId}'][f'{i}']['rating']

        pickBlocks = rating - 5

    for block in range(pickBlocks):
        randomBlock = rnd.randint(0,7)
        building_Blocks[randomBlock]

        song = [[]]
        for block in building_Blocks:
            for note in block:
                song[0].append(note)


        genId = genId + 1         
        muser = ms.Muser()
        muser.generate(song, i, genId)

        playsound(f'generations/generation_{genId}/track_00{i}.wav')       
        
        generations[f'generation_{genId}'][f'{i}']['rating'] = int(input("Enter rating:"))

        

#createFirstGeneration()
createNewGeneration()