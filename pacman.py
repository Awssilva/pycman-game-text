#Our hero
#G -> ghosts
#P -> Pills
#. -> empty spaces
# | and - -> walls  

map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G...@.|.|",
    "|........|",
    "|--------|"

]

def find_pacman(map):
    pacman_x = -1
    pacman_y = -1
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '@':
                pacman_x = x
                pacman_y = y 

    return pacman_x, pacman_y


def move_pacman(map, next_pacman_x, next_pacman_y):

     pacman_x, pacman_y = find_pacman(map)
    
    #pacman to dot
     everything_to_the_left = map[pacman_x][0:pacman_y]
     everything_to_the_right = map[pacman_x][pacman_y+1:]
     map[pacman_x] = everything_to_the_left + "." + everything_to_the_right
    
    #dot to pacman
     everything_to_the_left = map[next_pacman_x][0:next_pacman_y]
     everything_to_the_right = map[next_pacman_x][next_pacman_y+1:]
     map[next_pacman_x] = everything_to_the_left + "@" + everything_to_the_right
