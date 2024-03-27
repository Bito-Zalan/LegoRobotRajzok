#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random

class Darts():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        #self.ir = InfraredSensor(Port.S4)

        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

        self.ido = StopWatch()

    def csipog(self):
        self.ev3.speaker.beep()

    def darts1(self):
        #rajzoljatok ki egy kör alaku céltáblát majd véletlen lövöldözünk rá. irjuk ki a találatok számát!
        rLoves = 2
        self.ev3.screen.clear()
        self.ev3.screen.draw_circle(90,60,50,fill=True, color=Color.BLACK)
        db = 0
        for lovesDb in range(0, 10,1):
            #véletlen helyre látják
            rLoves=2
            x = random.randint(0+rLoves, 177-rLoves)
            y = random.randint(0+rLoves, 127-rLoves)
            if  (90-x)**2+(60-y)**2<=50**2:
                #talált
                self.ev3.screen.draw_circle(x,y,rLoves, fill=True, color=Color.WHITE)
                self.ev3.speaker.beep()
                db += 1
            else:
                #nem talált
                #self.ev3.screen.draw_circle(x,y,rLoves, fill=True, color=Color.BLACK)
                szoveg = "Találat"+str(db)+"."
                self.ev3.screen.draw_text(50,110,szoveg,text_color=Color.BLACK, background_color=Color.WHITE)
            wait(100)
        #self.ev3.screen.print("találat: ",db,".")
        wait(6000)

    def darts2a(self):
        #animáljuk a golyó mozgását, a. letörlés
        #self.ev3.screen.draw_box(172,40,177,80, fill=True, color=Color.BLACK)
        #kezdőhely
        y = random.randint(0,127)
        #self.ev3.screen.draw_box(0,y,2, fill=True, color=Color.BLACK)
        for i in range(184):
            #rajzoljuk ki a táblát
            self.ev3.screen.draw_box(172,40,177,80, fill=True, color=Color.BLACK)
            #golyót
            self.ev3.screen.draw_circle(i,y,4, fill=True, color=Color.BLACK)
            wait(30)
            self.ev3.screen.draw_circle(i,y,4, fill=True, color=Color.WHITE)
        wait(1000)