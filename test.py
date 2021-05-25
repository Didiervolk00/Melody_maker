import random
import json

musicBlock = open('blocks.json',)
data = json.load(musicBlock)

musicBlocks = data['musicBlocks']

music_blocks = []

# print(musicBlocks['0']['input'])

for i in range(len(musicBlocks)):

    music = musicBlocks[f'{random.randint(0,7)}']['input']

    #Insert the input in the array to be shuffeld
    for j in range(8):
        music_blocks.append(music[j])
        print(random.randint(0, 7))

print('')
print('muziek stukken achter elkaar')
print('============================')
print(music_blocks)

# shuffeld_blocks = (random.sample(music_blocks, len(music_blocks)))

# print('')
# print('muziek stukken door elkaar')
# print('============================')
# print(shuffeld_blocks)
# print('')
