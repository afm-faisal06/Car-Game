from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random

moveX, moveY, down, down2, down3, down4, down5, down6, down7, distance = [0]*10
power_up_active = False
power_up_duration = 1000

speed = .3
play = "stop"
r1 = random.randint(0, 440)
r2 = random.randint(0, 440)
r3 = random.randint(0, 440)
r4 = random.randint(0, 440)
r5 = random.randint(0, 440)
r6 = random.randint(0, 440)
r7 = random.randint(0, 440)
start = "running"
carTire = []
leftTopX = 235
leftTopY = 45
carTire.append([leftTopX, leftTopY, 7])
bottomLeftX = 235
bottomLeftY = 25
carTire.append([bottomLeftX, bottomLeftY, 7])
rightLeftX = 265
rightLeftY = 45
carTire.append([rightLeftX, rightLeftY, 7])
rightBottomX = 265
rightBottomY = 25
carTire.append([rightBottomX, rightBottomY, 7])


class AABB:
    x = 0
    y = 0
    w = 0
    h = 0

    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

    def collides_with(self, other):
        return (self.x < other.x + other.w and  # x_min_1 < x_max_2
                self.x + self.w > other.x and  # x_max_1 > m_min_2
                self.y < other.y + other.h and  # y_min_1 < y_max_2
                self.y + self.h > other.y)     # y_max_1 > y_min_2


# car
car = AABB(230, 16, 42, 38)
# rock
rock1 = AABB(10+r2, 612, 23, 24)
rock2 = AABB(10+r3, 712, 23, 24)
rock3 = AABB(10+r5, 812, 23, 24)
rock4 = AABB(10+r4, 912, 23, 24)
rock5 = AABB(10+r6, 1012, 23, 24)
rock6 = AABB(10+r7, 1112, 23, 24)
rocks = [rock1, rock2, rock3, rock4, rock5, rock6]
rockSpeed = 7
collision = False


def show_score():
    glRasterPos2f(505, 600 - 40)
    distance_text = f"Distance: {distance}"
    power_text = f"Power Time: {power_up_duration}"

    for char in distance_text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))

    glRasterPos2f(505, 600 - 80)  # Set new position for the second line
    for char in power_text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))


def draw_circle_points(x,y,x0,y0):
    glVertex2f(x + x0, y + y0)
    glVertex2f(-x + x0, y + y0)
    glVertex2f(x + x0, -y + y0)
    glVertex2f(-x + x0, -y + y0)
    glVertex2f(y + x0, x + y0)
    glVertex2f(-y + x0, x + y0)
    glVertex2f(y + x0, -x + y0)
    glVertex2f(-y + x0, -x + y0)


# Mid Point Circle Algorithm
def Mid_Point_Circle(x0,y0,radius):
    d=1-radius
    x=0
    y=radius
    draw_circle_points(x,y,x0,y0)

    while x<y:
        if d<0:
            d=d+2*x+3
            x=x+1
        else:
            d=d+2*x-2*y+5
            x=x+1
            y=y-1

        draw_circle_points(x,y,x0,y0)


def draw_lines(circle):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POINTS)
    Mid_Point_Circle(circle[0], circle[1], circle[2])
    glEnd()


def draw_circles():
    for circle in carTire:
        draw_lines(circle)


def draw_box(box):
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(box.x, box.y)
    glVertex2f(box.x + box.w, box.y)

    glVertex2f(box.x + box.w, box.y)
    glVertex2f(box.x + box.w, box.y + box.h)

    glVertex2f(box.x + box.w, box.y + box.h)
    glVertex2f(box.x, box.y + box.h)

    glVertex2f(box.x, box.y + box.h)
    glVertex2f(box.x, box.y)
    glEnd()


def check_collision():
    global car, rock1, rock2, rock3, rock4, rock5, rock6, collision, rocks, carTire, down, down2, down3, down4, down5, r1, r4, r5, r2, r3, r6, r7, power_up_active, start
    if start == "running":
        if not power_up_active:
            if car.collides_with(rock5) or car.collides_with(rock1) or car.collides_with(rock2) or car.collides_with(rock3) or car.collides_with(rock4) or car.collides_with(rock6):
                collision = True
            else:
                collision = False


def mouse_click(button, state, x, y):
    global carTire, play, power_up_active, power_up_duration
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if play == "stop":
            play = "resume"
        else:
            play = "stop"
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        power_up_active = True
        power_up_duration = 1000


def initialize():
    glViewport(0, 0, 700, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 700, 0.0, 600, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# Mid Point Line Algorithm
def MidpointLine(x1,y1,x2,y2,zone):
    dx = x2-x1
    dy = y2-y1
    d = (2*dy) - dx
    dE = 2*dy
    dNE = 2*(dy-dx)
    x= x1
    y= y2
    while (x<x2):
        if d<=0:
            d=d+dE
            x=x+1
        else:
            d=d+dNE
            x=x+1
            y=y+1
        cx,cy = Convert_to_Original_Zone(x,y,zone)
        glVertex2f(cx,cy)


def FindZone(x1, y1, x2, y2):
    zone = 0
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx <= 0 and dy >= 0:
            zone = 3
        elif dx <= 0 and dy <= 0:
            zone = 4
        elif dx >= 0 and dy <= 0:
            zone = 7
    else:
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx <= 0 and dy >= 0:
            zone = 2
        elif dx <= 0 and dy <= 0:
            zone = 5
        elif dx >= 0 and dy <= 0:
            zone = 6
    return zone    


def convertZone(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        x, y = y, x
        return x, y
    elif zone == 2:
        x, y = y, -x
        return x, y
    elif zone == 3:
        x, y = -x, y
        return x, y
    elif zone == 4:
        x, y = -x, -y
        return x, y
    elif zone == 5:
        x, y = -y, -x
        return x, y
    elif zone == 6:
        x, y = -y, x
        return x, y
    else:
        x, y = x, -y
        return x, y


def Convert_to_Original_Zone(x,y,zone):
    if zone == 0:
        return x, y
    if zone == 1:
        return y, x
    if zone == 2:
        return -y, -x
    if zone == 3:
        return -x, y
    if zone == 4:
        return -x, -y
    if zone == 5:
        return -y, -x
    if zone == 6:
        return y, -x
    if zone == 7:
        return x, -y


def drawLine(x1, y1, x2, y2):
    if x1 > x2:
        x1, x2, y1, y2 = x2, x1, y2, y1
    zone = FindZone(x1, y1, x2, y2)
    x1, y1 = convertZone(x1, y1, zone)
    x2, y2 = convertZone(x2, y2, zone)
    glBegin(GL_POINTS)
    MidpointLine(x1, y1, x2, y2, zone)
    glEnd()


def show_screen():
    global moveX, down, down2, down3, down4, down5, speed, direction, r1, r2, r3, r5, r4, moveY
    # clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1, 1, 1)

    # rock
    drawLine(10 + r2, 615 + down2,
             30 + r2, 615 + down2)
    drawLine(10 + r2, 635 + down2,
             30 + r2, 635 + down2)
    drawLine(10 + r2, 615 + down2,
             10 + r2, 635 + down2)
    drawLine(30 + r2, 635 + down2,
             30 + r2, 615 + down2)

    # rock
    drawLine(10 + r3, 715 + down3,
             30 + r3, 715 + down3)
    drawLine(10 + r3, 735 + down3,
             30 + r3, 735 + down3)
    drawLine(10 + r3, 715 + down3,
             10 + r3, 735 + down3)
    drawLine(30 + r3, 735 + down3,
             30 + r3, 715 + down3)

    # rock
    drawLine(10 + r5, 815 + down4,
             30 + r5, 815 + down4)
    drawLine(10 + r5, 835 + down4,
             30 + r5, 835 + down4)
    drawLine(10 + r5, 815 + down4,
             10 + r5, 835 + down4)
    drawLine(30 + r5, 835 + down4,
             30 + r5, 815 + down4)

    # rock
    drawLine(10 + r4, 915 + down5,
             30 + r4, 915 + down5)
    drawLine(10 + r4, 935 + down5,
             30 + r4, 935 + down5)
    drawLine(10 + r4, 915 + down5,
             10 + r4, 935 + down5)
    drawLine(30 + r4, 935 + down5,
             30 + r4, 915 + down5)

    # rock
    drawLine(10 + r6, 1015 + down6,
             30 + r6, 1015 + down6)
    drawLine(10 + r6, 1035 + down6,
             30 + r6, 1035 + down6)
    drawLine(10 + r6, 1015 + down6,
             10 + r6, 1035 + down6)
    drawLine(30 + r6, 1035 + down6,
             30 + r6, 1015 + down6)

    # rock
    drawLine(10 + r7, 1115 + down7,
             30 + r7, 1115 + down7)
    drawLine(10 + r7, 1135 + down7,
             30 + r7, 1135 + down7)
    drawLine(10 + r7, 1115 + down7,
             10 + r7, 1135 + down7)
    drawLine(30 + r7, 1135 + down7,
             30 + r7, 1115 + down7)

    # car
    drawLine(240+moveX, 25+moveY, 260+moveX, 25+moveY)
    drawLine(240+moveX, 45+moveY, 260+moveX, 45+moveY)
    drawLine(240+moveX, 25+moveY, 240+moveX, 45+moveY)
    drawLine(260+moveX, 45+moveY, 260+moveX, 25+moveY)

    drawLine(500, 0, 500, 600)

    show_score()

    draw_box(car)
    draw_box(rock1)
    draw_box(rock2)
    draw_box(rock3)
    draw_box(rock4)
    draw_box(rock5)
    draw_box(rock6)

    draw_circles()

    glutSwapBuffers()


def keyboard_click(key, x, y):
    global moveX, car, carTire, moveY, start
    if play == "stop":
        if start == "running":
            if key == GLUT_KEY_LEFT:
                if moveX != -224:
                    car.x -= rockSpeed
                    moveX -= 7
                    for circle in carTire:
                        circle[0] -= 7
            elif key == GLUT_KEY_RIGHT:
                if moveX != 224:
                    car.x += rockSpeed
                    moveX += 7
                    for circle in carTire:
                        circle[0] += 7
            elif key == GLUT_KEY_UP:
                if moveY != 532:
                    car.y += rockSpeed
                    moveY += 7
                    for circle in carTire:
                        circle[1] += 7
            elif key == GLUT_KEY_DOWN:
                if moveY != -7:
                    car.y -= rockSpeed
                    moveY -= 7
                    for circle in carTire:
                        circle[1] -= 7

    glutPostRedisplay()


def animation():
    global down, r1, car, collision, speed, play, r2, r4, r5, r3, down2, down3, down4, down5, down6, down7, carTire, distance, r6, r7, power_up_active, power_up_duration, start
    check_collision()
    if play == "stop":
        if start == "running":
            if power_up_active:
                power_up_duration -= 1
                if power_up_duration <= 0:
                    power_up_active = False
                    power_up_duration = 1000
            distance += 1
            down -= speed
            down2 -= speed
            down3 -= speed
            down4 -= speed
            down5 -= speed
            down6 -= speed
            down7 -= speed
            rock1.y -= speed
            rock2.y -= speed
            rock3.y -= speed
            rock4.y -= speed
            rock5.y -= speed
            rock6.y -= speed
            if collision:
                print(f"Game Over! Total Distance covered: {distance}")
                start = "end"
            elif down2 < -651:
                down2 = 0
                r2 = random.randint(0, 440)
                rock1.y = 612
                rock1.x = r2+10
            elif down3 < -751:
                down3 = 0
                r3 = random.randint(0, 440)
                rock2.y = 712
                rock2.x = r3+10
            elif down4 < -851:
                down4 = 0
                r5 = random.randint(0, 440)
                rock3.y = 812
                rock3.x = r5+10
            elif down5 < -951:
                down5 = 0
                r4 = random.randint(0, 440)
                rock4.y = 912
                rock4.x = r4+10
            elif down6 < -1051:
                down6 = 0
                r6 = random.randint(0, 440)
                rock5.y = 1012
                rock5.x = r6+10
            elif down7 < -1151:
                down7 = 0
                r7 = random.randint(0, 440)
                rock6.y = 1112
                rock6.x = r7+10

    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(700, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Car Game")
glutDisplayFunc(show_screen)
glutIdleFunc(animation)
glutMouseFunc(mouse_click)
glutSpecialFunc(keyboard_click)
glEnable(GL_DEPTH_TEST)
initialize()
glutMainLoop()
