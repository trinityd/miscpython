import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math
import numpy as np

# Matrix Stuff
def IdentityMat44(): return np.matrix(np.identity(4), copy=False, dtype='float32')

# Helpful Functions
def constrain(num, a, b):
    if num > b: return b
    elif num < a: return a
    else: return num

# Vertex Stuff
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
)

def Cube():
    glBegin(GL_QUADS)

    for surface in surfaces:
        coloridx = 0
        for vertex in surface:
            coloridx += 1
            glColor3fv(colors[coloridx])
            glVertex3fv(vertices[vertex])

    glEnd()

    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()

def main():
    # Variables
    playerSpeed = -.2
    playerPos = [0, 0, -10] # Also camera pos

    cameraSpeed = (.5, .5)
    cameraAngleZ = 0

    displayW = 800
    displayH = 600

    pygame.init()
    display = (displayW, displayH)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    # Starting Camera
    viewMat = IdentityMat44()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(playerPos[0], playerPos[1], playerPos[2])
    glGetFloatv(GL_MODELVIEW_MATRIX, viewMat)
    glLoadIdentity()
    glRotatef(180, 0, 1, 0)
    pygame.mouse.set_pos(displayW/2, displayH/2)
    # pygame.mouse.set_visible(False)

    while True:
        glPushMatrix()
        glLoadIdentity()

        # PyGame Events
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                quit()

        # Key Holding
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            glTranslatef(-playerSpeed, 0, 0)
            playerPos[0] += -playerSpeed
        if keys[K_d]:
            glTranslatef(playerSpeed, 0, 0)
            playerPos[0] += playerSpeed
        if keys[K_w]:
            glTranslatef(0, 0, -playerSpeed)
            playerPos[2] += -playerSpeed
        if keys[K_s]:
            glTranslatef(0, 0, playerSpeed)
            playerPos[2] += playerSpeed
        if keys[K_SPACE]:
            glRotatef(-cameraAngleZ, 1, 0, 0)
            glTranslatef(0, playerSpeed, 0)
            playerPos[1] += playerSpeed
            glRotatef(cameraAngleZ, 1, 0, 0)
        if keys[K_LSHIFT]:
            glRotatef(-cameraAngleZ, 1, 0, 0)
            glTranslatef(0, -playerSpeed, 0)
            playerPos[1] += -playerSpeed
            glRotatef(cameraAngleZ, 1, 0, 0)

        # print(f"{playerPos[0]:.2f}, {playerPos[1]:.2f}, {playerPos[2]:.2f}")
        # t = pygame.time.get_ticks()
        # tsec = t/1000
        # glTranslatef(math.sin(tsec)/10, 0, 0)


        # Camera Updating
        # pygame.mouse.get_rel()
        mouseMovement = pygame.mouse.get_rel()  # (x, y)

        # pygame.mouse.set_pos(displayW / 2, displayH / 2)
        dx = mouseMovement[0] * cameraSpeed[0]
        glRotatef(dx, 0, 0, 1)
        dy = mouseMovement[1] * cameraSpeed[1]
        if(cameraAngleZ - dy > -90 and cameraAngleZ - dy < 90):
            # glRotatef(dy, 1, 0, 0)
            cameraAngleZ -= dy
        cameraAngleZ = constrain(cameraAngleZ, -90, 90)

        glMultMatrixf(viewMat)
        glGetFloatv(GL_MODELVIEW_MATRIX, viewMat)

        # Drawing
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()