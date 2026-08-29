import pygame

# game settings
columns = 10
rows = 20
cellSize = 40
gameWidth = columns * cellSize
gameHeight = rows * cellSize

# display settings
sideBarWidth = 200
previewHeightFraction = 0.7
scoreHeightFraction = 1 - previewHeightFraction

# window settings
padding = 20
windowWidth = gameWidth + sideBarWidth + padding * 3
windowHeight = gameHeight + padding * 2

# gameplay settings
updateStartSpeed = 800
moveWaitTime = 200
rotateWaitTime = 200
blockOffset = pygame.Vector2(columns // 2, -1)

# scoring bonuses for manual drops (points per row dropped)
softDropPoints = 1
hardDropPoints = 2

# colors
yellow = '#f1e68d'
red = '#e51b20'
blue = '#204b9b'
green = '#65b32e'
purple = '#7b217f'
cyan = '#6cc6d9'
orange = '#e07b1f'
gray = '#1C1C1C'
lineColor = '#FFFFFF'

# shapes
tetrominoShapes = {
    'T': {'shape': [(0,0),(-1,0),(1,0),(0,-1)], 'color': purple},
    'O': {'shape': [(0,0),(1,0),(0,-1),(1,-1)], 'color': yellow},
    'J': {'shape': [(0,0),(-1,0),(1,0),(1,-1)], 'color': blue},
    'L': {'shape': [(0,0),(-1,0),(1,0),(-1,-1)], 'color': orange},
    'I': {'shape': [(0,0),(-1,0),(1,0),(2,0)], 'color': cyan},
    'S': {'shape': [(0,0),(-1,0),(0,-1),(1,-1)], 'color': green},
    'Z': {'shape': [(0,0),(1,0),(0,-1),(-1,-1)], 'color': red},
}

# 1 line = single, 2 = double, 3 = triple, 4 = tetris
scoreData = {
    1: 100,
    2: 300,
    3: 500,
    4: 1200
}
