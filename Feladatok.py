#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Feladatok():

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

    def aku(self):
        # akkumulátor töltése
        #konzol ablakba kiírás
        print("akumulátor tölttöttségi szintje: "+str(int(self.ev3.battery.voltage())/1000)+" V")
        #robot képernyőre
        akuErtek = "akumulátor tölttöttségi  \nszintje: "+str(int(self.ev3.battery.voltage())/1000)+"V"
        self.ev3.screen.print(akuErtek)
        wait(1000)

    def csipog(self):
        self.ev3.speaker.beep()

    def feladat1(self):
        #Haladjon az asztal széle fele a robot majd álljon meg a szélén.
        #asztallap 63
        #fekete vonal 10
        #lelóg 0
        #fele-fele 20

        while(self.cs.reflection()>30):
            self.robot.drive(100,0)
            #print("Szín:"+str(self.cs.reflection()))
        self.robot.stop(Stop.BRAKE)

    def feladat2(self):
        #elindulok ha asztal szélét vagy fekete vonalat látok tolassak vissza a kezdőhelyre.
        self.ido.reset() # elinditom a stoppert
        while(self.cs.reflection()>30):
            self.robot.drive(100,0)
        self.robot.stop(Stop.BRAKE)
        elteltIdo = self.ido.time() # stopper óra aktuális ideje
        self.ido.pause() # stopper megállítása 
        #hátra fele vissza indulás
        self.robot.drive(-100,0)
        wait(elteltIdo)
        self.robot.stop(Stop.BRAKE)

    def feladat3(self):
        while(self.us.distance()>100):
            self.robot.drive(self.us.distance(),0)
            print("Távolság: "+ str(self.us.distance()))
        self.robot.stop(Stop.BRAKE)

    def feladat03202(self):
        self.robot.drive(100,0)
        self.ido.reset()
        hol = 0
        while self.ido.time()<3000:
            if self.cs.reflection()<30:
                self.ev3.screen.draw_line(hol,0,hol,127)
            hol += 1
            wait(3000/170)
        self.robot.stop(Stop.BRAKE)
        wait(1000)

    def feladat_1a(self):
        while(self.cs.reflection()>10):
            self.robot.drive(100,0)
        while self.cs.reflection()<10:
            self.robot.drive(100,0)
        self.robot.stop(Stop.BRAKE)

    def feladat_1a2(self):
        vege = False
        fekete = False
        self.robot.drive(100,0)
        while not vege:
            if self.cs.reflection() < 30:
                fekete = True
            if fekete and self.cs.reflection() > 30:
                vege = True
        self.robot.stop(stop.BRAKE)

    def hanyvonal(self, db, seb, hatar):
        #több vonalam van
        for vonalaink in range(db):
            vege = False
            fekete = False
            self.robot.drive(seb,0)
            while not vege:
                if self.cs.reflection() < hatar:
                    fekete = True
                if fekete and self.cs.reflection() > hatar+5:
                    vege = True
            self.robot.stop(Stop.BRAKE)

    def feladat_1b(self):
        self.hanyvonal(4,100,30)

    def feladat_1c(self):
        self.hanyvonal(4,-100,30)

    def feladat_1d(self):
        hosszak = []
        for vonalaink in range(5):
            vege = False
            fekete = False
            self.robot.drive(100,0)
            while not vege:
                if self.cs.reflection() < 30 and not fekete:
                    fekete = True
                    #időmérés elinditása
                    self.ido.reset()
                if fekete and self.cs.reflection() > 35:
                    vege = True
                    #időmérés leállítása
                    hossz = self.ido.time()
                    hosszak.append(hossz)
        self.robot.stop(Stop.BRAKE)
        print(hosszak)
        return hosszak

    def feladat_1e(self):
        hosszak = self.feladat_1d()
        #szélsőérték 
        max = 0
        min = 0
        for index in range(len(hosszak)):
            if hosszak[index]< hosszak[min]:
                min = index
            if hosszak[index]< hosszak[max]:
                max = index

        #csipogás
        for cispog in range(max+1):
            self.ev3.speaker.beep()
            wait(100)

    def feladat_1f(self):
        hosszak = self.feladat_1d()
        max = 0
        min = 0
        for index in range (len(hosszak)):
            if hosszak[index]< hosszak[min]:
                min = index
            if hosszak[index]> hosszak[max]:
                max = index

        kozepertek =(hosszak[min]+ hosszak[max])/2
        for index in range(len(hosszak)):
            if hosszak[index]<kozepertek:
                self.ev3.speaker.beep(440,100)
            else:
                self.ev3.speaker.beep(440,200)
            wait(100)
        
        
            