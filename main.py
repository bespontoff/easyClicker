# -*- coding: UTF-8 -*-
__author__ = 'bespontoff'

import win32api
import time
import win32con


class EasyClicker:

    def __init__(self, duration=0.1):
        self.duration = duration
        self.x = None
        self.y = None

    def get_and_save_pos_when_wheel_up(self):
        self.x, self.y = win32api.GetCursorPos()

    def run(self):
        while True:
            mbm = win32api.GetAsyncKeyState(win32con.VK_MBUTTON)
            if mbm != 0:
                if self.x is None and self.y is None:
                    self.get_and_save_pos_when_wheel_up()
                    win32api.Beep(1000, 100)
                else:
                    self.x = None
                    self.y = None
                    win32api.Beep(10000, 200)

            self.click_on_pos()

    def lmb_down(self):
        if self.x is not None and self.y is not None:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.x, self.y)

    def lmb_up(self):
        if self.x is not None and self.y is not None:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.x, self.y)

    def click_on_pos(self):
        if self.x is not None and self.y is not None:
            win32api.SetCursorPos((self.x, self.y))
            self.lmb_down()
            time.sleep(self.duration)
            self.lmb_up()
            print(f'Clicking on [{self.x}, {self.y}]')


if __name__ == '__main__':
    ec = EasyClicker()
    ec.run()
