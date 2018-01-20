

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np
from scipy.integrate import *
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np

import numpy as np
from vispy import app, gloo, visuals
from vispy.geometry import create_sphere
from vispy.visuals.transforms import (STTransform, AffineTransform,
                                      ChainTransform)




class impulse3(QWidget):
    def __init__(self):
        super(impulse3, self).__init__()
        layout = QFormLayout()
        self.setLayout(layout)
        self.setWindowTitle("3 impulse manever ")
        self.setGeometry(10, 10, 500, 500)

        self.btn3 = QPushButton("V1")
        self.btn3.clicked.connect(self.clicked)
        self.vec = []
        layout.addWidget(self.btn3)

        self.btn4 = QPushButton("theta1")
        self.btn4.clicked.connect(self.clicked2)
        layout.addWidget(self.btn4)
        self.btn2 = QPushButton("phi1")
        self.btn2.clicked.connect(self.clicked3)

        layout.addWidget(self.btn2)
        self.btn5 = QPushButton("V2")
        self.btn5.clicked.connect(self.clicked4)
        layout.addWidget(self.btn5)
        self.btn6 = QPushButton("theta2")
        self.btn6.clicked.connect(self.clicked5)
        layout.addWidget(self.btn6)


        self.btn7 = QPushButton("phi2")
        self.btn7.clicked.connect(self.clicked6)
        layout.addWidget(self.btn7)

        self.btn8 = QPushButton("V3")
        self.btn8.clicked.connect(self.clicked7)
        layout.addWidget(self.btn8)

        self.btn9 = QPushButton("theta3")
        self.btn9.clicked.connect(self.clicked8)
        layout.addWidget(self.btn9)

        self.btn10 = QPushButton("phi3")
        self.btn10.clicked.connect(self.clicked9)
        layout.addWidget(self.btn10)

        self.btn11 = QPushButton("TOF1")
        self.btn11.clicked.connect(self.clicked10)
        layout.addWidget(self.btn11)

        self.btn12 = QPushButton("TOF2")
        self.btn12.clicked.connect(self.clicked11)
        layout.addWidget(self.btn12)

        self.btn13 = QPushButton("ENTER")
        self.btn13.clicked.connect(self.check4fv)
        layout.addWidget(self.btn13)

    def clicked(self):
        if (self.btn3.clicked):
            V1X, ok = QInputDialog.getDouble(self, "V1 ENTRY", "ENTER AN INTEGR ")
            if (ok and V1X):
                self.vec.append(V1X)
            if (not ok or not V1X):
                self.vec.append(10 ** 6)

    def clicked2(self):
        if (self.btn2.clicked):
            V1Y, ok = QInputDialog.getDouble(self, "theta1 ENTRY", "ENTER AN INTEGR ")
            if (ok and V1Y):
                self.vec.append(V1Y)
            if (not ok or not V1Y):
                self.vec.append(10 ** 6)

    def clicked3(self):
        if (self.btn4.clicked):
            V1Z, ok = QInputDialog.getDouble(self, "phi1 ENTRY", "ENTER AN INTEGR ")
            if (ok and V1Z):
                self.vec.append(V1Z)
            if (not ok or not V1Z):
                self.vec.append(10 ** 6)

    def clicked4(self):
        if (self.btn5.clicked):
            V2X, ok = QInputDialog.getDouble(self, "V2 ENTRY", "ENTER AN INTEGR ")
            if (ok and V2X):
                self.vec.append(V2X)
            if (not ok or not V2X):
                self.vec.append(10 ** 6)

    def clicked5(self):
        if (self.btn6.clicked):
            V2Y, ok = QInputDialog.getDouble(self, "theta2 ENTRY", "ENTER AN INTEGR ")
            if (ok and V2Y):
                self.vec.append(V2Y)
            if (not ok or not V2Y):
                self.vec.append(10 ** 6)

    def clicked6(self):
        if (self.btn7.clicked):
            V2Z, ok = QInputDialog.getDouble(self, "phi2 ENTRY", "ENTER AN INTEGR ")
            if (ok and V2Z):
                self.vec.append(V2Z)
            if (not ok or not V2Z):
                self.vec.append(10 ** 6)

    def clicked7(self):
        if (self.btn8.clicked):
            V3X, ok = QInputDialog.getDouble(self, "V3 ENTRY", "ENTER AN INTEGR ")
            if (ok and V3X):
                self.vec.append(V3X)
            if (not ok or not V3X):
                self.vec.append(10 ** 6)

    def clicked8(self):
        if (self.btn9.clicked):
            V3Y, ok = QInputDialog.getDouble(self, "theta3 ENTRY", "ENTER AN INTEGR ")
            if (ok and V3Y):
                self.vec.append(V3Y)
            if (not ok or not V3Y):
                self.vec.append(10 ** 6)

    def clicked9(self):
        if (self.btn10.clicked):
            V3Z, ok = QInputDialog.getDouble(self, "phi3 ENTRY", "ENTER AN INTEGR ")
            if (ok and V3Z):
                self.vec.append(V3Z)
            if (not ok or not V3Z):
                self.vec.append(10 ** 6)

    def clicked10(self):
        if (self.btn11.clicked):
            TOF1, ok = QInputDialog.getDouble(self, "TOF1 ENTRY", "ENTER AN INTEGR ")
            if (ok and TOF1):
                self.vec.append(TOF1)
            if (not ok or not TOF1):
                self.vec.append(10 ** 6)

    def clicked11(self):
        if (self.btn12.clicked):
            TOF2, ok = QInputDialog.getDouble(self, "TOF2 ENTRY", "ENTER AN INTEGR ")
            if (ok and TOF2):
                self.vec.append(TOF2)
            if (not ok or not TOF2):
                self.vec.append(10 ** 6)

    def check4fv(self):

        return self.vec


class impulse2(QWidget):
    def __init__(self):
        super(impulse2, self).__init__()
        layout = QFormLayout()
        self.setLayout(layout)
        self.setWindowTitle("2 impulse manever ")
        self.setGeometry(10, 10, 500, 500)

        self.btn3 = QPushButton("V1")
        self.btn3.clicked.connect(self.clicked)
        self.vec = []

        self.btn4 = QPushButton("phi1")
        self.btn4.clicked.connect(self.clicked2)
        layout.addRow(self.btn4, self.btn3)
        self.btn2 = QPushButton("theta1")
        self.btn2.clicked.connect(self.clicked3)
        layout.addWidget(self.btn2)


        self.btn5 = QPushButton("V2")
        self.btn5.clicked.connect(self.clicked4)

        self.btn6 = QPushButton("phi2")
        self.btn6.clicked.connect(self.clicked5)
        layout.addRow(self.btn5, self.btn6)
        self.btn7 = QPushButton("theta2")
        self.btn7.clicked.connect(self.clicked6)
        layout.addWidget(self.btn7)



        self.btn11 = QPushButton("TOF1")
        self.btn11.clicked.connect(self.clicked10)
        layout.addWidget(self.btn11)

        self.btn13 = QPushButton("ENTER")
        self.btn13.clicked.connect(self.check4fv)
        layout.addWidget(self.btn13)

    def clicked(self):
        if (self.btn3.clicked):
            V1X, ok = QInputDialog.getDouble(self, "V1 ENTRY", "ENTER AN INTEGR ")
            if (ok and V1X):
                self.vec.append(V1X)
            if (not ok or not V1X):
                self.vec.append(10 ** 6)

    def clicked2(self):
        if (self.btn2.clicked):
            V1Y, ok = QInputDialog.getDouble(self, "tehta1 ENTRY", "ENTER AN INTEGR ")
            if (ok and V1Y):
                self.vec.append(V1Y)
            if (not ok or not V1Y):
                self.vec.append(10 ** 6)

    def clicked3(self):
        if (self.btn4.clicked):
            V1Z, ok = QInputDialog.getDouble(self, "phi1 ENTRY", "ENTER AN INTEGR ")
            if (ok and V1Z):
                self.vec.append(V1Z)
            if (not ok or not V1Z):
                self.vec.append(10 ** 6)

    def clicked4(self):
        if (self.btn5.clicked):
            V2X, ok = QInputDialog.getDouble(self, "V2 ENTRY", "ENTER AN INTEGR ")
            if (ok and V2X):
                self.vec.append(V2X)
            if (not ok or not V2X):
                self.vec.append(10 ** 6)

    def clicked5(self):
        if (self.btn6.clicked):
            V2Y, ok = QInputDialog.getDouble(self, "theta2 ENTRY", "ENTER AN INTEGR ")
            if (ok and V2Y):
                self.vec.append(V2Y)
            if (not ok or not V2Y):
                self.vec.append(10 ** 6)

    def clicked6(self):
        if (self.btn7.clicked):
            V2Z, ok = QInputDialog.getDouble(self, "phi2 ENTRY", "ENTER AN INTEGR ")
            if (ok and V2Z):
                self.vec.append(V2Z)
            if (not ok or not V2Z):
                self.vec.append(10 ** 6)

    def clicked10(self):
        if (self.btn11.clicked):
            TOF1, ok = QInputDialog.getDouble(self, "TOF2 ENTRY", "ENTER AN INTEGR ")
            if (ok and TOF1):
                self.vec.append(TOF1)
            if (not ok or not TOF1):
                self.vec.append(10 ** 6)

    def check4fv(self):

        return self.vec


class impulse1(QWidget):
    def __init__(self):
        super(impulse1, self).__init__()
        layout = QFormLayout()
        self.setLayout(layout)
        self.setWindowTitle("1 impulse manever ")
        self.setGeometry(10, 10, 500, 500)

        self.btn3 = QPushButton("V1")
        self.btn3.clicked.connect(self.clicked)
        self.vec = []
        layout.addWidget(self.btn3)

        self.btn4 = QPushButton("theta")
        self.btn4.clicked.connect(self.clicked2)
        layout.addWidget(self.btn4)

        self.btn2 = QPushButton("phi")
        self.btn2.clicked.connect(self.clicked3)
        layout.addWidget(self.btn2)

        self.btn11 = QPushButton("TOF1")
        self.btn11.clicked.connect(self.clicked10)
        layout.addWidget(self.btn11)

        self.btn13 = QPushButton("ENTER")
        self.btn13.clicked.connect(self.check4fv)
        layout.addWidget(self.btn13)

    def clicked(self):
        if (self.btn3.clicked):
            V1X, ok = QInputDialog.getDouble(self, "V1 ENTRY", "ENTER AN INTEGR ")
            if (ok and V1X):
                self.vec.append(V1X)
            if (not ok or not V1X):
                self.vec.append(10 ** 6)

    def clicked2(self):
        if (self.btn2.clicked):
            V1Y, ok = QInputDialog.getDouble(self, "theta ENTRY", "ENTER AN INTEGR ")
            if (ok and V1Y):
                self.vec.append(V1Y)
            if (not ok or not V1Y):
                self.vec.append(10 ** 6)

    def clicked3(self):
        if (self.btn4.clicked):
            V1Z, ok = QInputDialog.getDouble(self, "phi ENTRY", "ENTER AN INTEGR ")
            if (ok and V1Z):
                self.vec.append(V1Z)
            if (not ok or not V1Z):
                self.vec.append(10 ** 6)

    def clicked10(self):
        if (self.btn11.clicked):
            TOF1, ok = QInputDialog.getDouble(self, "TOF2 ENTRY", "ENTER AN INTEGR ")
            if (ok and TOF1):
                self.vec.append(TOF1)
            if (not ok or not TOF1):
                self.vec.append(10 ** 6)

    def check4fv(self):

        return self.vec


class BC3(QWidget):
    def __init__(self):
        super(BC3, self).__init__()
        layout = QFormLayout()
        self.setLayout(layout)
        self.setWindowTitle("BC FOR 3 impulse manever ")
        self.setGeometry(10, 10, 500, 500)

        self.btn3 = QPushButton("e1")
        self.btn3.clicked.connect(self.clicked)
        self.vec = []
        self.vec2 = []

        self.btn4 = QPushButton("e2")
        self.btn4.clicked.connect(self.clicked2)
        layout.addRow(self.btn3, self.btn4)

        self.btn2 = QPushButton("i1")
        self.btn2.clicked.connect(self.clicked3)

        self.btn5 = QPushButton("i2")
        self.btn5.clicked.connect(self.clicked4)
        layout.addRow(self.btn2, self.btn5)
        self.btn6 = QPushButton("v1")
        self.btn6.clicked.connect(self.clicked5)

        self.btn7 = QPushButton("v2")
        self.btn7.clicked.connect(self.clicked6)


        layout.addRow(self.btn6, self.btn7)

        self.btn8 = QPushButton("r1")
        self.btn8.clicked.connect(self.clicked7)

        self.btn9 = QPushButton("r2")
        self.btn9.clicked.connect(self.clicked8)

        layout.addRow(self.btn8, self.btn9)

        self.btn10 = QPushButton("E1")
        self.btn10.clicked.connect(self.clicked9)

        self.btn11 = QPushButton("E2")
        self.btn11.clicked.connect(self.clicked10)
        layout.addRow(self.btn10, self.btn11)

        self.btn12 = QPushButton("a1")
        self.btn12.clicked.connect(self.clicked11)


        self.btn14 = QPushButton("a2")
        self.btn14.clicked.connect(self.clicked12)

        layout.addRow(self.btn12, self.btn14)

        self.btn15 = QPushButton("TP1")
        self.btn15.clicked.connect(self.clicked13)

        self.btn16 = QPushButton("TP2")
        self.btn16.clicked.connect(self.clicked14)

        layout.addRow(self.btn15, self.btn16)

        self.btn13 = QPushButton("ENTER")
        self.btn13.clicked.connect(self.check4fv)

        layout.addWidget(self.btn13)

    def clicked(self):
        if (self.btn3.clicked):
            e1, ok = QInputDialog.getDouble(self, "e1 ENTRY", "ENTER AN INTEGR ")
            if (ok and e1):
                self.vec.append(e1)
            if (not ok or not e1):
                self.vec.append(10 ** 6)

    def clicked2(self):
        if (self.btn2.clicked):
            e2, ok = QInputDialog.getDouble(self, "e2 ENTRY", "ENTER AN INTEGR ")
            if (ok and e2):
                self.vec2.append(e2)
            if (not ok or not e2):
                self.vec2.append(10 ** 6)

    def clicked3(self):
        if (self.btn4.clicked):
            I1, ok = QInputDialog.getDouble(self, "I1 ENTRY", "ENTER AN INTEGR ")
            if (ok and I1):
                self.vec.append(I1)
            if (not ok or not I1):
                self.vec.append(10 ** 6)

    def clicked4(self):
        if (self.btn5.clicked):
            I2, ok = QInputDialog.getDouble(self, "I2 ENTRY", "ENTER AN INTEGR ")
            if (ok and I2):
                self.vec2.append(I2)
            if (not ok or not I2):
                self.vec2.append(10 ** 6)

    def clicked5(self):
        if (self.btn6.clicked):
            V1, ok = QInputDialog.getDouble(self, "V1 ENTRY", "ENTER AN INTEGR ")
            if (ok and V1):
                self.vec.append(V1)
            if (not ok or not V1):
                self.vec.append(10 ** 6)

    def clicked6(self):
        if (self.btn7.clicked):
            V2, ok = QInputDialog.getDouble(self, "V2 ENTRY", "ENTER AN INTEGR ")
            if (ok and V2):
                self.vec2.append(V2)
            if (not ok or not V2):
                self.vec2.append(10 ** 6)

    def clicked7(self):
        if (self.btn8.clicked):
            R1, ok = QInputDialog.getDouble(self, "R1 ENTRY", "ENTER AN INTEGR ")
            if (ok and R1):
                self.vec.append(R1)
            if (not ok or not R1):
                self.vec.append(10 ** 6)

    def clicked8(self):
        if (self.btn9.clicked):
            R2, ok = QInputDialog.getDouble(self, "R2 ENTRY", "ENTER AN INTEGR ")
            if (ok and R2):
                self.vec2.append(R2)
            if (not ok or not R2):
                self.vec2.append(10 ** 6)

    def clicked9(self):
        if (self.btn10.clicked):
            E1, ok = QInputDialog.getDouble(self, "E1 ENTRY", "ENTER AN INTEGR ")
            if (ok and E1):
                self.vec.append(E1)
            if (not ok or not E1):
                self.vec.append(10 ** 6)

    def clicked10(self):
        if (self.btn11.clicked):
            E2, ok = QInputDialog.getDouble(self, "E2 ENTRY", "ENTER AN INTEGR ")
            if (ok and E2):
                self.vec2.append(E2)
            if (not ok or not E2):
                self.vec2.append(10 ** 6)

    def clicked11(self):
        if (self.btn12.clicked):
            a1, ok = QInputDialog.getDouble(self, "a1 ENTRY", "ENTER AN INTEGR ")
            if (ok and a1):
                self.vec.append(a1)
            if (not ok or not a1):
                self.vec.append(10 ** 6)

    def clicked12(self):
        if (self.btn14.clicked):
            a2, ok = QInputDialog.getDouble(self, "a2 ENTRY", "ENTER A NUMBER ")
            if (ok and a2):
                self.vec2.append(a2)
            if (not ok or not a2):
                self.vec2.append(10 ** 6)

    def clicked13(self):
        if (self.btn15.clicked):
            TP1, ok = QInputDialog.getDouble(self, "TOF2 ENTRY", "ENTER A NUMBER ")
            if (ok and TP1):
                self.vec.append(TP1)
            if (not ok or not TP1):
                self.vec.append(10 ** 6)

    def clicked14(self):
        if (self.btn16.clicked):
            TP2, ok = QInputDialog.getDouble(self, "TP2 ENTRY", "ENTER A NUMBER ")
            if (ok and TP2):
                self.vec2.append(TP2)
            if (not ok or not TP2):
                self.vec2.append(10 ** 6)

    def check4fv(self):
        self.check4vec2()

        return self.vec

    def check4vec2(self):
        return self.vec2


class BC2(QWidget):
    def __init__(self):
        super(BC2, self).__init__()
        layout = QFormLayout()
        self.setLayout(layout)
        self.setWindowTitle("BC FOR 2 impulse manever ")
        self.setGeometry(10, 10, 500, 500)

        self.btn3 = QPushButton("e1")
        self.btn3.clicked.connect(self.clicked)
        layout.addWidget(self.btn3)
        self.vec = []

        self.btn2 = QPushButton("i1")
        self.btn2.clicked.connect(self.clicked3)
        layout.addWidget(self.btn2)

        self.btn6 = QPushButton("v1")
        self.btn6.clicked.connect(self.clicked5)
        layout.addWidget(self.btn6)

        self.btn8 = QPushButton("r1")
        self.btn8.clicked.connect(self.clicked7)
        layout.addWidget(self.btn8)

        self.btn10 = QPushButton("E1")
        self.btn10.clicked.connect(self.clicked9)
        layout.addWidget(self.btn10)

        self.btn12 = QPushButton("a1")
        self.btn12.clicked.connect(self.clicked11)
        layout.addWidget(self.btn12)

        self.btn15 = QPushButton("TP1")
        self.btn15.clicked.connect(self.clicked13)

        layout.addWidget(self.btn15)


        self.btn20 = QPushButton("AOP")
        self.btn20.clicked.connect(self.clicked14)

        layout.addWidget(self.btn20)

        self.btn21 = QPushButton("ASENTION")
        self.btn21.clicked.connect(self.clicked15)

        layout.addWidget(self.btn21)
        self.btn22 = QPushButton("TRUE ANOMLY")
        self.btn22.clicked.connect(self.clicked16)

        layout.addWidget(self.btn22)

        self.btn13 = QPushButton("ENTER")
        self.btn13.clicked.connect(self.check4fv)

        layout.addWidget(self.btn13)

    def clicked(self):
        if (self.btn3.clicked):
            e1, ok = QInputDialog.getDouble(self, "e1 ENTRY", "ENTER AN INTEGR ")
            if (ok and e1):
                self.vec.append(e1)
            if (not ok or not e1):
                self.vec.append(10 ** 6)

    def clicked3(self):
        if (self.btn2.clicked):
            I1, ok = QInputDialog.getDouble(self, "I1 ENTRY", "ENTER AN INTEGR ")
            if (ok and I1):
                self.vec.append(I1)
            if (not ok or not I1):
                self.vec.append(10 ** 6)

    def clicked5(self):
        if (self.btn6.clicked):
            V1, ok = QInputDialog.getDouble(self, "V1 ENTRY", "ENTER AN INTEGR ")
            if (ok and V1):
                self.vec.append(V1)
            if (not ok or not V1):
                self.vec.append(10 ** 6)

    def clicked7(self):
        if (self.btn8.clicked):
            R1, ok = QInputDialog.getDouble(self, "R1 ENTRY", "ENTER AN INTEGR ")
            if (ok and R1):
                self.vec.append(R1)
            if (not ok or not R1):
                self.vec.append(10 ** 6)

    def clicked9(self):
        if (self.btn10.clicked):
            E1, ok = QInputDialog.getDouble(self, "E1 ENTRY", "ENTER AN INTEGR ")
            if (ok and E1):
                self.vec.append(E1)
            if (not ok or not E1):
                self.vec.append(10 ** 6)

    def clicked11(self):
        if (self.btn12.clicked):
            a1, ok = QInputDialog.getDouble(self, "a1 ENTRY", "ENTER AN INTEGR ")
            if (ok and a1):
                self.vec.append(a1)
            if (not ok or not a1):
                self.vec.append(10 ** 6)

    def clicked13(self):

        if (self.btn15.clicked):

            TP1, ok = QInputDialog.getDouble(self, "TOF2 ENTRY", "ENTER A NUMBER ")
            if (ok and TP1):
                self.vec.append(TP1)
            if (not ok or not TP1):
                self.vec.append(10 ** 6)

    def clicked14(self):

        if (self.btn20.clicked):

            AOP, ok = QInputDialog.getDouble(self, "AOP ENTRY", "ENTER A NUMBER ")
            if (ok and AOP):
                self.vec.append(AOP)
            if (not ok or not AOP):
                self.vec.append(10 ** 6)



    def clicked15(self):

        if (self.btn21.clicked):

            ASENT, ok = QInputDialog.getDouble(self, "RIGHT ASCENSION ENTRY", "ENTER A NUMBER ")
            if (ok and ASENT):
                self.vec.append(ASENT)
            if (not ok or not ASENT):
                self.vec.append(10 ** 6)



    def clicked16(self):

        if (self.btn22.clicked):

            anomly, ok = QInputDialog.getDouble(self, "TRUE ANOMLY ENTRY", "ENTER A NUMBER ")
            if (ok and anomly):
                self.vec.append(anomly)
            if (not ok or not anomly):
                self.vec.append(10 ** 6)



    def check4fv(self):
        #WHEN I PRESS ENTER IN THE GUI BUTTON

        return self.vec








class RV(QWidget):
    def __init__(self, parent=None):
        super(RV, self).__init__(parent)
        self.RV_VECTOR=[]
        self.V_VECTOR=[]

        layout = QFormLayout()
        self.setLayout(layout)
        self.setWindowTitle("INPUT STATE VECTOR OF INTIAL ORBIT ")
        self.setGeometry(10,10,500,500)





        self.btn = QPushButton("ENTER R VECTOR")
        self.btn.clicked.connect(self.getRCOMP)


        layout.addWidget(self.btn)







        self.btn1 = QPushButton("ENTER V VECTOR")
        self.btn1.clicked.connect(self.getVCOMP)
        self.le1 = QLineEdit()
        layout.addWidget(self.btn1)

    def getRCOMP(self):

        for i in range(3):
            num, ok = QInputDialog.getDouble(self, "rcomponent input", "enter r ")


            if ok:

                self.Rv_VECTOR.append(num)
        return







    def getVCOMP(self):
        for i in range(3):

            num, ok = QInputDialog.getDouble(self, "Vcomponent input", "enter V ")
            if ok:
                self.V_VECTOR.append(num)



        return









class OE(QWidget):
    def __init__(self, parent=None):
        super(OE, self).__init__(parent)
        self.ORBITAL_ELEMENTS=[]

        layout = QFormLayout()
        self.setLayout(layout)
        self.setWindowTitle("ORBITAL ELEMENTS OF INTIAL ORBIT")

        self.btn = QPushButton("ENTER ECENTRICTY")
        self.btn.clicked.connect(self.getECEN)
        layout.addWidget(self.btn)



        self.btn1 = QPushButton("ENTER AOP")
        self.btn1.clicked.connect(self.getAOP)
        layout.addWidget(self.btn1)

        self.setGeometry(0, 0, 500, 500)


        self.btn4 = QPushButton("RIGHT ASENSION")
        self.btn4.clicked.connect(self.getASENT)
        layout.addWidget(self.btn4)




        self.btn5 = QPushButton("ENTER SEMI MAJOR AXIS")
        self.btn5.clicked.connect(self.getSAXIS)
        layout.addWidget(self.btn5)



        self.btn6 = QPushButton("ENTER THE INCLINATION")
        self.btn6.clicked.connect(self.getINC)
        layout.addWidget(self.btn6)

        self.btn7 = QPushButton("ENTER intial anomly")
        self.btn7.clicked.connect(self.getanom)
        layout.addWidget(self.btn7)

    def getECEN(self):
        ECEN, ok = QInputDialog.getDouble(self, "input elemnt", "enter  ecentricty")

        if ok:
            self.ORBITAL_ELEMENTS.append(ECEN)
            return ECEN

    def getAOP(self):
        AOP, ok = QInputDialog.getDouble(self, "input elemnt", "enter AOP")

        if ok:
            self.ORBITAL_ELEMENTS.append(AOP)
            return AOP



    def getASENT(self):
        ASENT, ok = QInputDialog.getDouble(self, "input elemnt", " ENTER ASENT")

        if ok:
            self.ORBITAL_ELEMENTS.append(ASENT)
            return  ASENT

    def getSAXIS(self):
        MAJOR_AXIS, ok = QInputDialog.getDouble(self, "input elemnt", "ENTER a")

        if ok:
            self.ORBITAL_ELEMENTS.append(MAJOR_AXIS)
            return  MAJOR_AXIS

    def getINC(self):
        INC, ok = QInputDialog.getDouble(self, "input elemnt", "ENTER INCLINATION")

        if ok:
            self.ORBITAL_ELEMENTS.append(INC)
            return INC



    def getanom(self):
        anom, ok = QInputDialog.getDouble(self, "input elemnt", "ENTER itial anomly")
        if ok:
            self.ORBITAL_ELEMENTS.append(anom)
            return anom











#y should be n*3 whrere n is the number of data points
class NUMERCAL_INTEGRATION(RV):

    def __init__(self):

        super(NUMERCAL_INTEGRATION,self).__init__()





    def state_vec(self,t0, u_, k, ad):
        ax, ay, az = ad(t0, u_, k)

        x, y, z, vx, vy, vz = u_
        r3 = (x ** 2 + y ** 2 + z ** 2) ** 1.5

        du = np.array([
            vx,
            vy,
            vz,
            -k * x / r3 + ax,
            -k * y / r3 + ay,
            -k * z / r3 + az ])
        return du

    def get_initals(self):
        tof=1000
        r0=[]
        v0=[]
#we can change it ba3deen
        r0=self.RV_VECTOR
        v0=self.V_VECTOR
        return r0,v0,tof


    def form_segment(self):

        global k
        k=398600
        r0 = []
        v0 = []


        r0, v0,tof=self.get_initals()


        rtol = 1e-10
        ad = None
        callback = None
        nsteps = 10000
        x=[]
        y=[]
        z=[]
        vx=[]
        vy=[]
        vz=[]
        x, y, z = r0
        vx, vy, vz = v0
        u0 = np.array([x, y, z, vx, vy, vz])

        # Set the non Keplerian acceleration
        if ad is None:
            ad = lambda t0, u_, k_: (0, 0, 0)

        # Set the integrator
        rr = ode(self.state_vec).set_integrator('dop853', rtol=rtol, nsteps=nsteps)
        rr.set_initial_value(u0)  # Initial time equal to 0.0
        rr.set_f_params(k, ad)  # Parameters of the integration
        if callback:
            rr.set_solout(callback)

        # Make integration step
        rr.integrate(tof)

        if rr.successful():
            r, v = rr.y[:3], rr.y[3:]
        else:
            raise RuntimeError("Integration failed")

        return r, v

class GRAPHICS(gl.GLViewWidget):

    def __init__(self):
        super(GRAPHICS, self).__init__()

    def createWINDOW_PLOT(self):

        self.NUM_INTG=NUMERCAL_INTEGRATION()


        [y, v] = self.NUM_INTG.form_segment()
#WINDOW PLOT BY PYGRAPH QT

        self.setWindowTitle('3D GRAPH')
        self.setCameraPosition(5000)
        g = gl.GLGridItem()

        g.scale(10000, 10000, 10000)
        g.setDepthValue(10000)
        self.addItem(g)
        color_graph = np.ones([1000, 4])

        md = gl.MeshData.sphere(rows=100, cols=200, radius=5000)

        # colors = np.random.random(size=(md.faceCount(), 4))
        # colors[:,3] = 0.3
        # colors[100:] = 0.0
        colors = np.ones((md.faceCount(), 4), dtype=float)
        colors[::2, 0] = 0
        colors[:, 1] = np.linspace(0, 1, colors.shape[0])
        md.setFaceColors(colors)

        m3 = gl.GLMeshItem(meshdata=md, smooth=False, shader='balloon')

        m3.translate(0, 0, 0)
        self.addItem(m3)
        # drwaing part

        pos = y

        p4 = gl.GLLinePlotItem(pos=pos, color=color_graph, width=10, mode='lines')
        p4.translate(1, 1, 0)
        self.addItem(p4)
        self.show()

#if iwant to call the plotting function without integration just to plot i inherit from the class and call it as member function
















class BAZAWIN(QWidget):
    def __init__(self):
        super(BAZAWIN,self).__init__()
        self.G_BAZA=GRAPHICS()
        self.RV1=RV()
        self.OE1=OE()


        layout = QFormLayout()
        self.setLayout(layout)
        self.setWindowTitle("baza window")
        self.setGeometry(10, 10, 500, 500)




        self.btn3 = QPushButton("NUMBER OF MANEVERS")
        self.btn3.clicked.connect(self.getimpnumber)
        layout.addWidget(self.btn3)



        self.btn4 = QPushButton("ENTER BOUNDRY CONDTIONS")
        self.btn4.clicked.connect(self.getBCS)
        layout.addWidget(self.btn4)

        self.btn2 = QPushButton("SET FREE VARIBALES")
        self.btn2.clicked.connect(self.getItem)
        layout.addWidget(self.btn2)

        self.btns = QPushButton("SIMULATE THE PROBLEM")
        self.btns.clicked.connect(self.SIMULATE)
        layout.addWidget(self.btns)

    def getItem(self):

        impulsenum=self.getimpnumber()
        if (impulsenum==3):

            self.win43 = impulse3()
            self.win43.show()
        if (impulsenum==2):
            self.win42 = impulse2()
            self.win42.show()
        if (impulsenum==1):
            self.win41 = impulse1()
            self.win41.show()
        return



    def getimpnumber(self):
        num, ok = QInputDialog.getInt(self, "NUMBER OF IMPULSE MANUVERS", "ENTER AN INTEGR ")
        if ok:
            return num


    def getBCS(self):
        impulsenum=self.getimpnumber()
        if (impulsenum==3):
            self.winBC3 = BC3()
            self.winBC3.show()
        if (impulsenum==2):
            self.winBC2 = BC2()
            self.winBC2.show()
        if (impulsenum==1):
            self.winBC1 = BC2()
            self.winBC1.show()


    def SIMULATE(self):
        self.G_BAZA.createWINDOW_PLOT()





class menahWIN(QWidget):
    def __init__(self):
        super(menahWIN, self).__init__()


        self.RV2 = RV()
        self.OE2 = OE()

        layout = QFormLayout()
        self.setLayout(layout)
        self.setWindowTitle("baza window")
        self.setGeometry(10, 10, 500, 500)

        self.btn3 = QPushButton("NUMBER OF MANEVERS")
        self.btn3.clicked.connect(self.getimpnumber)
        layout.addWidget(self.btn3)

        self.btn4 = QPushButton("ENTER BOUNDRY CONDTIONS")
        self.btn4.clicked.connect(self.getBCS)
        layout.addWidget(self.btn4)

        self.btn10 = QPushButton("SOLVE")
        #self.btn10.clicked.connect(self.CALL_OPTIMSER)
        layout.addWidget(self.btn10)



        self.btn11 = QPushButton("PLOT ")
        self.btn4.clicked.connect(self.CALLPLOTS)
        layout.addWidget(self.btn11)

    def getimpnumber(self):
        num, ok = QInputDialog.getInt(self, "NUMBER OF IMPULSE MANUVERS", "ENTER AN INTEGR ")
        if ok:
            return num

    def impbutton(self):

        dv_vec = np.zeros([1, 3])

        for i in range(3):
            num, ok = QInputDialog.getDouble(self, "IMPULSIVE MANEUVER INPUT", "enter impulse value ")

            if ok:
                dv_vec[:, i] = num
        return dv_vec

    def getimp(self):
        impulse_num = self.getimpnumber()

        for i in range(impulse_num):
            self.impbutton()

        return

    def getBCS(self):
        num, ok = QInputDialog.getDouble(self, "ENCENTRICTY BC", "enter e value ")
        num1, ok = QInputDialog.getDouble(self, "SEMI MAJOR AXIS BC", "enter a value ")
        num2, ok = QInputDialog.getDouble(self, "VMAG BC", "enter V value ")
        num3, ok = QInputDialog.getDouble(self, "RMAG B", "enter R value ")
        if (ok and (num, num1, num2, num3)):
            return num, num1, num2, num3

    def CALLPLOTS(self):
        self.plot = GRAPHICS()
        self.plot.show()
        self.plot.createWINDOW_PLOT()
        return


                #def CALL_OPTIMSER(self):

    #   self.menah_opt=menahOPTMIZE()
    #   self.menah_opt.show()

    #   return


    # menahOPTMIZE() IS A CLASS THAT WILL HAVE MENAH FUNCTIONS AND WILL CALL THE SOLVER OF MENAH AND RETURNVALUES TO BE PLOTED






class window55(QMainWindow):
    def __init__(self):
        super(window55, self).__init__()

        self.w1 = BAZAWIN()
        self.setCentralWidget(self.w1)
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("WELCOME BAZA")
        oImage = QImage("/home/bora3i/e3.jpg")

        sImage = oImage.scaled(QSize(500, 500))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.label = QLabel('Test', self)
        self.label.setGeometry(50, 50, 200, 50)




class window22(QMainWindow):
    def __init__(self):
        super(window22, self).__init__()

        self.w1 =menahWIN()
        self.setCentralWidget(self.w1)
        self.setGeometry(0, 0, 600, 600)
        self.setWindowTitle("WELCOME MENAH (etfo aleko kolko) :D")
        oImage = QImage("/home/bora3i/m1.jpg")

        sImage = oImage.scaled(QSize(600, 600))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.label = QLabel('Test', self)
        self.label.setGeometry(50, 50, 200, 50)











class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()

        self.w1=RV()
        self.setCentralWidget(self.w1)
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("SAMA3NI SLAM EL MOOT 3ALENA 7A2")
        oImage = QImage("/home/bora3i/p1.jpg")

        sImage = oImage.scaled(QSize(500, 500))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.label = QLabel('Test', self)
        self.label.setGeometry(50, 50, 200, 50)

class window2(QMainWindow):
    def __init__(self):
        super(window2, self).__init__()

        self.w2=OE()
        self.setCentralWidget(self.w2)
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("SAMA3NI SLAM EL MOOT 3ALENA 7A2")
        oImage = QImage("/home/bora3i/p1.jpg")

        sImage = oImage.scaled(QSize(500, 500))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.label = QLabel('Test', self)
        self.label.setGeometry(50, 50, 200, 50)





class choose(QMainWindow):
    def __init__(self, parent=None):
        super(choose, self).__init__(parent)

        widget=QWidget()
        self.setCentralWidget(widget)
        self.setGeometry(0,0,800,800)




        layout=QFormLayout()
        widget.setLayout(layout)
        widget.setGeometry(0,0,800,800)
        self.setWindowTitle("ENTERY WINDOW")

        self.btn = QPushButton("USE ORBITAL ELEMENTS")
        self.btn.clicked.connect(self.callOE)
        oImage=QImage("/home/bora3i/space.jpg")

        sImage = oImage.scaled(QSize(800, 800))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.label = QLabel('Test', self)
        self.label.setGeometry(50, 50, 200, 50)

        self.btn1 = QPushButton("USE STATE VECTOR")
        self.btn1.clicked.connect(self.callRV)
        layout.addWidget(self.btn1)


        self.btn1.setGeometry(10,10,200,200)
        self.btn.setGeometry(0,0,200,200)
        layout.addRow(self.btn,self.btn1)


    def callOE(self):

        self.oe=window2()
        self.oe.show()





    def callRV(self):
        self.rv=window()


        self.rv.show()










class windowBIG(QMainWindow):
    def __init__(self):
        super(windowBIG, self).__init__()

        MAYmain=QWidget()

        layout = QFormLayout()
        MAYmain.setLayout(layout)
        self.setGeometry(0,0,800,800)
        MAYmain.setGeometry(0, 0, 800, 800)
        self.setCentralWidget(MAYmain)
        self.setWindowTitle("7ASBYA ALLAH W N3M EL WAKEEL FEEK YA SHE5")

        self.btn = QPushButton("CALL BAZA")
        self.btn.clicked.connect(self.callBAZA)
        self.btn.setGeometry(0,0,200,200)
        layout.addWidget(self.btn)
        self.btn.setGeometry(30, 30, 200, 200)




        self.btn1 = QPushButton("CALL MENAH")
        self.btn1.clicked.connect(self.callMENAH)
        self.btn1.setGeometry(10,10,200,200)
        layout.addWidget(self.btn1)




        self.btn2 = QPushButton("CALL ENTRY MENU OF INTIAL ORBIT ELEMENTS")
        self.btn2.clicked.connect(self.callchoose)
        self.btn2.setGeometry(20,20,200,200)
        layout.addWidget(self.btn2)


        oImage = QImage("/home/bora3i/an.jpg")

        sImage = oImage.scaled(QSize(800, 800))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.label = QLabel('Test', self)
        self.label.setGeometry(50, 50, 200, 50)



    def callMENAH(self):
        self.oe = window22()
        self.oe.show()

    def callBAZA(self):
        self.oe55 = window55()
        self.oe55.show()
    def callchoose(self):
        self.choose1=choose()
        self.choose1.show()




def main():
    app = QApplication(sys.argv)
    MAY_BIG_WINDOW=windowBIG()
    MAY_BIG_WINDOW.show()


    sys.exit(app.exec_())


if __name__ == '__main__':
   main()

