#!/usr/bin/env python3
from colorama import Fore as FORE, Back as BACK, Style as STYLE, init
init()
x = True
moves = []
def color(a):
    if a == 'W':
        return FORE.LIGHTWHITE_EX + a
    if a == 'Y':
        return FORE.LIGHTYELLOW_EX + a
    if a == 'O':
        return FORE.YELLOW + a
    if a == 'R':
        return FORE.LIGHTRED_EX + a
    if a == 'B':
        return FORE.LIGHTBLUE_EX + a
    if a == 'G':
        return FORE.LIGHTGREEN_EX + a
    else:
        return FORE.LIGHTWHITE_EX + a
def shift(face):
    face.insert(0, face[2])
    face.pop(3)
    face.insert(2, face[3])
    face.pop(4)
def colorize(face):
    for c in face:
        color(c)
def net():
    print(' ' * 4 + color(Above[0]) + color('|') + color(Above[1]))
    print(' ' * 4 + color(Above[2]) + color('|') + color(Above[3]))
    print(color(Left[0]) + color('|') + color(Left[1]) + color('|') + color(Front[0]) + color('|') + color(Front[1]) + color('|') + color(Right[0]) + color('|') + color((Right[1])))
    print(color(Left[2]) + color('|') + color(Left[3]) + color('|') + color(Front[2]) + color('|') + color(Front[3]) + color('|') + color(Right[2]) + color('|') + color((Right[3])))
    print(' ' * 4 + color(Under[0]) + color('|') + color(Under[1]))
    print(' ' * 4 + color(Under[2]) + color('|') + color(Under[3]))
    print(' ' * 4 + color(Back[0]) + color('|') + color(Back[1]))
    print(' ' * 4 + color(Back[2]) + color('|') + color(Back[3]))
    print(color(' '))
def above(a = None):
    if a:
        pass
    else:
        moves.append('A')
    Right.insert(0,Front[0])
    Right.insert(1,Front[1])
    Back.insert(2,Right[2])
    Back.insert(2,Right[3])
    Left.insert(2,Back[4])
    Left.insert(2,Back[5])
    Front.insert(0,Left[0])
    Front.insert(1,Left[1])
    Front.pop(2)
    Front.pop(2)
    Right.pop(2)
    Right.pop(2)
    Back.pop(4)
    Back.pop(4)
    Left.pop(0)
    Left.pop(0)
    for i in range(3):
        shift(Above)
def under(a = None):
    if a:
        pass
    else:
        moves.append('U')
    Right.insert(2,Front[2])
    Right.insert(3,Front[3])
    Back.insert(0,Right[5])
    Back.insert(1,Right[4])
    Left.insert(2,Back[2])
    Left.insert(2,Back[3])
    Front.insert(2,Left[4])
    Front.insert(3,Left[5])
    Front.pop(4)
    Front.pop(4)
    Right.pop(4)
    Right.pop(4)
    Back.pop(2)
    Back.pop(2)
    Left.pop(4)
    Left.pop(4)
    shift(Under)
def right(a = None):
    if a:
        pass
    else:
        moves.append('R')
    Above.insert(2,Front[1])
    Above.insert(4,Front[3])
    Back.insert(2,Above[1])
    Back.insert(4,Above[5])
    Under.insert(2,Back[1])
    Under.insert(4,Back[5])
    Front.insert(2,Under[1])
    Front.insert(4,Under[5])
    Front.pop(1)
    Front.pop(4)
    Above.pop(1)
    Above.pop(4)
    Back.pop(1)
    Back.pop(4)
    Under.pop(1)
    Under.pop(4)
    shift(Right)
def left(a = None):
    if a:
        pass
    else:
        moves.append('L')
    Above.insert(1, Front[0])
    Above.insert(3, Front[2])
    Back.insert(1, Above[0])
    Back.insert(3, Above[4])
    Under.insert(1, Back[0])
    Under.insert(3, Back[4])
    Front.insert(1, Under[0])
    Front.insert(3, Under[4])
    Front.pop(0)
    Front.pop(3)
    Above.pop(0)
    Above.pop(3)
    Back.pop(0)
    Back.pop(3)
    Under.pop(0)
    Under.pop(3)
    for i in range(3):
        shift(Left)
def front(a = None):
    if a:
        pass
    else:
        moves.append('F')
    Above.insert(2, Left[1])
    Above.insert(2, Left[3])
    Right.insert(0, Above[4])
    Right.insert(3, Above[5])
    Under.insert(0, Right[1])
    Under.insert(0, Right[4])
    Left.insert(2, Under[2])
    Left.insert(5, Under[3])
    Left.pop(1)
    Left.pop(3)
    Above.pop(4)
    Above.pop(4)
    Right.pop(1)
    Right.pop(3)
    Under.pop(2)
    Under.pop(2)
    shift(Front)
def back(a = None):
    if a:
        pass
    else:
        moves.append('B')
    Above.insert(1, Left[0])
    Above.insert(0, Left[2])
    Right.insert(1, Above[1])
    Right.insert(4, Above[3])
    Under.insert(3, Right[2])
    Under.insert(2, Right[5])
    Left.insert(0, Under[3])
    Left.insert(3, Under[5])
    Left.pop(1)
    Left.pop(3)
    Above.pop(1)
    Above.pop(2)
    Right.pop(2)
    Right.pop(4)
    Under.pop(3)
    Under.pop(4)
    for i in range(3):
        shift(Back)
def a():
    for i in range(3):
        above(True)
    moves.append("A'")
def r():
    for i in range(3):
        right(True)
    moves.append("R'")
def l():
    for i in range(3):
        left(True)
    moves.append("L'")
def bprime():
    for i in range(3):
        back(True)
    moves.append("B'")
def u():
    for i in range(3):
        under(True)
    moves.append("U'")
def f():
    for i in range(3):
        front(True)
    moves.append("F'")
def score(c, d):
    global b
    b = 0
    for index in c:
        if index == '{}'.format(d):
            b += 1
    return b
def locate(a):
    b = 0
    for piece in a:
        if piece == 'W':
            return b
        else:
            b += 1
def cornerplacer():
    bprime()
    right()
    back()
def cornerplacel():
    back()
    left()
    bprime()
def backgorithim():
    under()
    l()
    l()
    u()
def whiteside():
    while 'R' in Front or 'Y' in Front or 'B' in Front or 'O' in Front or 'G' in Front:
        ls = score(Left, 'W')
        us = score(Under, 'W')
        abs = score(Above, 'W')
        rs = score(Right, 'W')
        bs = score(Back, 'W')
        if ls > 0:
            p = locate(Left)
            if p == 0:
                while Front[p] == 'W':
                    front()
                r()
                above()
                right()
            if p == 1:
                r()
                above()
                right()
            if p == 2:
                while Front[2] == 'W':
                    front()
                right()
                under()
                r()
            if p == 3:
                right()
                under()
                r()
        if rs > 0:
            p = locate(Right)
            if p == 0:
                l()
                a()
                left()
            if p == 1:
                while Front[1] == 'W':
                    front()
                l()
                a()
                left()
            if p == 2:
                left()
                u()
                l()
            if p == 3:
                while Front[3] == 'W':
                    front()
                left()
                u()
                l()
        if abs > 0:
            p = locate(Above)
            if p == 0:
                while Front[0] == 'W':
                    front()
                under()
                l()
                u()
            if p == 1:
                while Front[1] == 'W':
                    front()
                u()
                r()
                under()
            if p == 2:
                under()
                l()
                u()
            if p == 3:
                u()
                r()
                under()
        if us > 0:
            p = locate(Under)
            if p == 0:
                above()
                left()
                a()
            if p == 1:
                a()
                right()
                above()
            if p == 2:
                while Front[2] == 'W':
                    front()
                above()
                left()
                a()
            if p == 3:
                while Front[3] == 'W':
                    front()
                a()
                right()
                above()
        if bs > 0:
            g = locate(Back)
            while Front[0] == 'W':
                front()
            if g == 0:
                back()
                backgorithim()
            if g == 1:
                back()
                back()
                backgorithim()
            if g == 2:
                bprime()
                backgorithim()
            if g == 3:
                backgorithim()
def firstlayer():
    gs = 0
    bs = 0
    rs = 0
    os = 0
    while rs != 1 and os != 1 and bs != 1 and gs != 1:
        if Above[2] == Above[3] and Right[0] == Right[2]:
            return
        elif Left[1] == Left[3]:
            above()
            back()
            a()
            a()
            right()
            above()
            u()
            r()
            under()
            gs = 1
            bs = 1
            rs = 1
            os = 1
            continue
        elif Right[0] == Right[2]:
            u()
            back()
            under()
            under()
            l()
            u()
            above()
            left()
            a()
            gs = 1
            bs = 1
            rs = 1
            os = 1
            continue
        elif Under[0] == Under[1]:
            left()
            back()
            l()
            l()
            a()
            left()
            r()
            above()
            right()
            gs = 1
            bs = 1
            rs = 1
            os = 1
            continue
        elif Above[2] == Above[3]:
            r()
            bprime()
            right()
            right()
            under()
            r()
            left()
            u()
            l()
            gs = 1
            bs = 1
            rs = 1
            os = 1
            continue
        else:
            r()
            back()
            right()
            right()
            under()
            r()
            left()
            u()
            l()
            left()
            back()
            l()
            l()
            a()
            left()
            r()
            above()
            right()
            return
def Ysidecode():
    right()
    bprime()
    r()
    bprime()
    right()
    bprime()
    bprime()
    r()
def Yside():
    while 'R' in Back or 'W' in Back or 'B' in Back or 'O' in Back or 'G' in Back:
        s = score(Back, 'Y')
        if s >= 2:
            if (Back[0] == 'Y' and Back[3] == 'Y') or (Back[1] == 'Y' and Back[2] == 'Y'):
                while Back[2] != 'Y':
                    back()
                Ysidecode()
            else:
                while Back[1] != 'Y' or Back[3] != 'Y':
                    bprime()
                Ysidecode()
        elif s == 1:
            while Back[2] != 'Y':
                bprime()
            Ysidecode()
        else:
            Ysidecode()
def final():
    bs = score(Left, 'B')
    gs = score(Right, 'G')
    os = score(Under, 'O')
    rs = score(Above, 'R')
    while bs < 2 and gs < 2 and os < 2 and rs < 2:
        front()
        bs = score(Left, 'B')
        gs = score(Right, 'G')
        os = score(Under, 'O')
        rs = score(Above, 'R')
    while bs != 4 and gs != 4 and os != 4 and rs != 4:
        for i in range(4):
            back()
            bs = score(Left, 'B')
            gs = score(Right, 'G')
            os = score(Under, 'O')
            rs = score(Above, 'R')
            if (gs == 4 and rs == 4 and bs == 4 and os == 4) or (gs == 0 and rs == 0 and bs == 0 and os == 0):
                return
            if gs == 4:
                above()
                l()
                above()
                right()
                right()
                a()
                left()
                a()
                right()
                right()
                a()
                a()
                right()
                right()
                return
            elif bs == 4:
                u()
                right()
                u()
                l()
                l()
                under()
                r()
                under()
                l()
                l()
                under()
                under()
                l()
                l()
                return
            elif rs == 4:
                left()
                under()
                left()
                a()
                a()
                l()
                u()
                l()
                a()
                a()
                l()
                l()
                a()
                a()
                return
            elif os == 4:
                r()
                a()
                r()
                u()
                u()
                right()
                above()
                right()
                a()
                a()
                l()
                l()
                a()
                a()
                return
        r()
        a()
        r()
        u()
        u()
        right()
        above()
        right()
        a()
        a()
        l()
        l()
        a()
        a()
def complete():
    while Left[0] != Left[3]:
        front()
print('Help or Troubleshooting: https://github.com/Mrplip123/2x2-Rubik-s-Cube-Solver---Adi-R/edit/main/README.md')
Front = (input('Front'))
Back = (input('Back'))
Right = (input('Right'))
Left = (input('Left'))
Above = (input('Above'))
Under = (input('Under'))
Front = list(Front)
Back = list(Back)
Right = list(Right)
Left = list(Left)
Above = list(Above)
Under = list(Under)
fr = Front.copy()
ba = Back.copy()
ri = Right.copy()
le = Left.copy()
ab = Above.copy()
un = Under.copy()
whiteside()
moves.append('White Side Solved')
firstlayer()
moves.append('First Layer Solved')
Yside()
moves.append('Yellow Side Solved')
final()
moves.append('Cube almost Solved')
complete()
moves.append('Cube Solved')
Front = fr.copy()
Back = ba.copy()
Right = ri.copy()
Left = le.copy()
Above = ab.copy()
Under = un.copy()
for move in moves:
        i = input(move)
        if i == 'help':
            print('https://github.com/Mrplip123/2x2-Rubik-s-Cube-Solver---Adi-R/edit/main/README.md')
        if move == 'R':
            right()
        if move == 'L':
            left()
        if move == 'F':
            front()
        if move == 'B':
            back()
        if move == 'A':
            above()
        if move == 'U':
            under()
        if move == "R'":
            r()
        if move == "L'":
            l()
        if move == "F'":
            f()
        if move == "B'":
            bprime()
        if move == "A'":
            a()
        if move == "U'":
            u()
        elif i != '':
            net()
print(len(moves))


