import pyautogui as p
import time as t
t.sleep(2)
while True:
    x = (p.position())
    detector = (p.pixel(x[0], x[1]))
    if detector == (83, 83, 83):
        p.press('up')
        print('JUMP')
