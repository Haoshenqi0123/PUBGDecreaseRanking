import time
import win32api
import win32gui
import win32con
from ctypes import *
def moveCurPos(x,y):
    windll.user32.SetCursorPos(x, y)
def clickLeftCur():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP, 0, 0)
#moveCurPos(0,0)

def getCurPos():
    return win32gui.GetCursorPos()
print (getCurPos())

moveCurPos(33,728)
clickLeftCur()
