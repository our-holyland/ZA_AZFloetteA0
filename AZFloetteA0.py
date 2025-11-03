from Commands.PythonCommandBase import ImageProcPythonCommand
from Commands.Keys import Button, Hat, Direction, Stick
import cv2

#####################################################
#ファイルの配置
##ぽけこん(Modified版 or Extension版)
##|-SerialController/
##  |-Template/
##    |-ZA/
##      |-AZFloette/     ・・・画像ファイルフォルダ
##  |-Commands/
##    |-PythonCommands/
##      |-ImageProcessingOnly/
##        |-AZFloette.py ・・・プログラム本体
#使い方
##手持ちを一体にしておくこと
##メインミッション39のAZフラエッテ受け取り直前までシナリオを進めておくこと
##Switch2の場合は厳選するアカウントを左端に配置しておくこと
##20番ワイルドゾーン北のポケセンで回復した時点で本プログラムを起動すること
#プログラムの概要
##ポケセンからクエーサー社へ行ってイベントを見る
##もらったフラエッテがA0(実数値88)なら終了、そうでなければリセット
##バックアップデータでポケセンから再開してやり直し
##厳選完了時にDiscord通知します
#####################################################
class AZFloette(ImageProcPythonCommand):
    NAME = 'ZA_AZフラエッテA0厳選_ver1.0'

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
            ret = self.isContainTemplate('ZA/AZFloette/pos2.png', 0.80,
                                         crop=[100, 102, 140, 142],
                                         use_gray=False)
            if ret:
                break
            self.press(Button.A, 0.1, 0.2)
        self.pressRep(Button.B, wait=0.1, repeat=3, duration=0.2, interval=0.1)

    def chkFloetteA0(self):
        self.press(Button.X, 0.1, 1.0)
        self.press(Button.A, 0.1, 2.0)
        self.press(Hat.TOP, 0.1, 1.0)
        self.press(Hat.RIGHT, 0.1, 1.0)
        ret = self.isContainTemplate('ZA/AZFloette/FloetteA0.png',
                                     0.90, crop=[1085, 239, 1135, 275],
                                     use_gray=False)
        return ret

    def backupRestart(self):
        self.press(Button.HOME, 0.1, 1.0)
        self.press(Button.Y, 0.1, 1.0)
        self.press(Button.A, 0.1, 2.0)
        self.press(Button.A, 0.1, 2.0)
        while True:
            ret = self.isContainTemplate('ZA/AZFloette/zaStart.png', 0.80,
                                         crop=[465, 567, 815, 607],
                                         use_gray=False)
            if ret:
                break
            self.wait(1.0)
        self.press([Hat.TOP, Button.X, Button.B], 0.2, 1.0)
        self.pressRep(Button.A, wait=0.1, repeat=10, duration=0.2, interval=0.1)
        while True:
            ret = self.isContainTemplate('ZA/AZFloette/pos1.png', 0.80,
                                         crop=[100, 102, 140, 142],
                                         use_gray=False)
            if ret:
                break
            self.wait(1.0)
