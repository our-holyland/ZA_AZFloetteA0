from Commands.PythonCommandBase import ImageProcPythonCommand
from Commands.Keys import Button, Hat, Direction, Stick
import cv2

class AZFloetteA0(ImageProcPythonCommand):
    NAME = 'ZA_AZフラエッテA0厳選_ver1.01'

    def __init__(self,cam,gui=None):
        super().__init__(cam)
        self.cam = cam

    def do(self):
        while True:
            self.getFloette()
            ret = self.chkFloetteA0()
            if ret:
                print("AZフラエッテのA0厳選が完了しました。")
                self.discord_image("AZフラエッテのA0厳選が完了しました。")
                self.finish()
            self.backupRestart()

    def getFloette(self):
        self.press(Button.PLUS, 0.1, 1.0)
        self.press(Button.RCLICK, 0.1, 1.0)
        self.press(Direction(Stick.LEFT, 270, 0.8), 0.1, 1.0)
        self.press(Button.A, 0.1, 1.0)
        self.press(Button.A, 0.1, 10.0)
        self.press(Direction(Stick.LEFT, 90), 8.0, 1.0)
        self.press(Button.A,0.1,1.0)
        while True:
            img_list = ['ZA/AZFloetteA0/pos2.png',
                        'ZA/AZFloetteA0/pos3.png']
            _, _, ret_list = self.isContainTemplate_max(
                img_list, 0.80,
                crop=[100, 102, 140, 142],
                use_gray=False)
            if any(ret_list):
                break
            self.press(Button.A, 0.1, 0.2)
        self.pressRep(Button.B, wait=0.1, repeat=3, duration=0.2, interval=0.1)

    def chkFloetteA0(self):
        self.press(Button.X, 0.1, 1.0)
        self.press(Button.A, 0.1, 2.0)
        self.press(Hat.TOP, 0.1, 1.0)
        self.press(Hat.RIGHT, 0.1, 1.0)
        ret = self.isContainTemplate('ZA/AZFloetteA0/FloetteA0.png',
                                     0.90, crop=[1085, 239, 1135, 275],
                                     use_gray=False)
        return ret

    def backupRestart(self):
        self.press(Button.HOME, 0.1, 1.5)
        self.press(Button.Y, 0.1, 1.0)
        self.press(Button.A, 0.1, 3.0)
        self.pressRep(Button.A, repeat=5, duration=0.1, interval=0.5)
        self.wait(15.0)
        self.press([Hat.TOP, Button.X, Button.B], 0.2, 1.0)
        self.pressRep(Button.A, wait=0.1, repeat=10, duration=0.2, interval=0.1)
        while True:
            ret = self.isContainTemplate('ZA/AZFloetteA0/pos1.png', 0.80,
                                         crop=[100, 102, 140, 142],
                                         use_gray=False)
            if ret:
                break
            self.wait(1.0)
