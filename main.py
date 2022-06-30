#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Felipe Mendoza Giraldo
# Created Date: 29/06/2022
# version ='1.0'
# ---------------------------------------------------------------------------
"""A one-line description or name.
A longer description that spans multiple lines.  Explain the purpose of the
file and provide a short list of the key classes/functions it contains.  This
is the docstring shown when some does 'import foo;foo?' in IPython, so it
should be reasonably useful and informative.
"""
# -----------------------------------------------------------------------------
# Copyright (c) 2015, the IPython Development Team and José Fonseca.
#
# Distributed under the terms of the Creative Commons License.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#
#
# REFERENCES:
#
# -----------------------------------------------------------------------------
'''
OPTIONS ------------------------------------------------------------------
A description of each option that can be passed to this script
ARGUMENTS -------------------------------------------------------------
A description of each argument that can or must be passed to this script
'''


# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from utils import TimeAxisItem, timestamp, timestamp1
import numpy as np
import serial
import struct
import datetime
# stdlib imports -------------------------------------------------------

# Third-party imports -----------------------------------------------

# Our own imports ---------------------------------------------------


# -----------------------------------------------------------------------------
# GLOBALS
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# CONSTANTS
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# LOCAL UTILITIES
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Mag_plot = timePlot(self.centralwidget)
        self.Mag_plot.setObjectName("Mag_plot")
        self.gridLayout.addWidget(self.Mag_plot, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 3, 1)
        self.Accel_plot = timePlot(self.centralwidget)
        self.Accel_plot.setObjectName("Accel_plot")
        self.gridLayout.addWidget(self.Accel_plot, 0, 1, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.yAccel = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yAccel.sizePolicy().hasHeightForWidth())
        self.yAccel.setSizePolicy(sizePolicy)
        self.yAccel.setObjectName("yAccel")
        self.gridLayout_2.addWidget(self.yAccel, 1, 0, 1, 1)
        self.xAccel1 = QtWidgets.QLabel(self.widget_4)
        self.xAccel1.setMinimumSize(QtCore.QSize(20, 0))
        self.xAccel1.setMaximumSize(QtCore.QSize(20, 16777215))
        self.xAccel1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.xAccel1.setText("")
        self.xAccel1.setObjectName("xAccel1")
        self.gridLayout_2.addWidget(self.xAccel1, 0, 1, 1, 1)
        self.xAccel = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xAccel.sizePolicy().hasHeightForWidth())
        self.xAccel.setSizePolicy(sizePolicy)
        self.xAccel.setObjectName("xAccel")
        self.gridLayout_2.addWidget(self.xAccel, 0, 0, 1, 1)
        self.zAccel = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zAccel.sizePolicy().hasHeightForWidth())
        self.zAccel.setSizePolicy(sizePolicy)
        self.zAccel.setObjectName("zAccel")
        self.gridLayout_2.addWidget(self.zAccel, 2, 0, 1, 1)
        self.yAccel1 = QtWidgets.QLabel(self.widget_4)
        self.yAccel1.setMinimumSize(QtCore.QSize(20, 0))
        self.yAccel1.setMaximumSize(QtCore.QSize(20, 16777215))
        self.yAccel1.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.yAccel1.setText("")
        self.yAccel1.setObjectName("yAccel1")
        self.gridLayout_2.addWidget(self.yAccel1, 1, 1, 1, 1)
        self.zAccel1 = QtWidgets.QLabel(self.widget_4)
        self.zAccel1.setMinimumSize(QtCore.QSize(20, 0))
        self.zAccel1.setMaximumSize(QtCore.QSize(20, 16777215))
        self.zAccel1.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.zAccel1.setText("")
        self.zAccel1.setObjectName("zAccel1")
        self.gridLayout_2.addWidget(self.zAccel1, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.widget_4, 0, 2, 1, 1)
        self.Rate_plot = timePlot(self.centralwidget)
        self.Rate_plot.setObjectName("Rate_plot")
        self.gridLayout.addWidget(self.Rate_plot, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.yRate = QtWidgets.QLabel(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yRate.sizePolicy().hasHeightForWidth())
        self.yRate.setSizePolicy(sizePolicy)
        self.yRate.setObjectName("yRate")
        self.gridLayout_3.addWidget(self.yRate, 1, 0, 1, 1)
        self.xRate1 = QtWidgets.QLabel(self.widget_5)
        self.xRate1.setMinimumSize(QtCore.QSize(20, 0))
        self.xRate1.setMaximumSize(QtCore.QSize(20, 16777215))
        self.xRate1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.xRate1.setText("")
        self.xRate1.setObjectName("xRate1")
        self.gridLayout_3.addWidget(self.xRate1, 0, 1, 1, 1)
        self.xRate = QtWidgets.QLabel(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xRate.sizePolicy().hasHeightForWidth())
        self.xRate.setSizePolicy(sizePolicy)
        self.xRate.setObjectName("xRate")
        self.gridLayout_3.addWidget(self.xRate, 0, 0, 1, 1)
        self.zRate = QtWidgets.QLabel(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zRate.sizePolicy().hasHeightForWidth())
        self.zRate.setSizePolicy(sizePolicy)
        self.zRate.setObjectName("zRate")
        self.gridLayout_3.addWidget(self.zRate, 2, 0, 1, 1)
        self.yRate1 = QtWidgets.QLabel(self.widget_5)
        self.yRate1.setMinimumSize(QtCore.QSize(20, 0))
        self.yRate1.setMaximumSize(QtCore.QSize(20, 16777215))
        self.yRate1.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.yRate1.setText("")
        self.yRate1.setObjectName("yRate1")
        self.gridLayout_3.addWidget(self.yRate1, 1, 1, 1, 1)
        self.zRate1 = QtWidgets.QLabel(self.widget_5)
        self.zRate1.setMinimumSize(QtCore.QSize(20, 0))
        self.zRate1.setMaximumSize(QtCore.QSize(20, 16777215))
        self.zRate1.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.zRate1.setText("")
        self.zRate1.setObjectName("zRate1")
        self.gridLayout_3.addWidget(self.zRate1, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.widget_5, 1, 2, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.yMag = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yMag.sizePolicy().hasHeightForWidth())
        self.yMag.setSizePolicy(sizePolicy)
        self.yMag.setObjectName("yMag")
        self.gridLayout_4.addWidget(self.yMag, 1, 0, 1, 1)
        self.xMag1 = QtWidgets.QLabel(self.widget_6)
        self.xMag1.setMinimumSize(QtCore.QSize(20, 0))
        self.xMag1.setMaximumSize(QtCore.QSize(20, 16777215))
        self.xMag1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.xMag1.setText("")
        self.xMag1.setObjectName("xMag1")
        self.gridLayout_4.addWidget(self.xMag1, 0, 1, 1, 1)
        self.xMag = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xMag.sizePolicy().hasHeightForWidth())
        self.xMag.setSizePolicy(sizePolicy)
        self.xMag.setObjectName("xMag")
        self.gridLayout_4.addWidget(self.xMag, 0, 0, 1, 1)
        self.zMag = QtWidgets.QLabel(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zMag.sizePolicy().hasHeightForWidth())
        self.zMag.setSizePolicy(sizePolicy)
        self.zMag.setObjectName("zMag")
        self.gridLayout_4.addWidget(self.zMag, 2, 0, 1, 1)
        self.yMag1 = QtWidgets.QLabel(self.widget_6)
        self.yMag1.setMinimumSize(QtCore.QSize(20, 0))
        self.yMag1.setMaximumSize(QtCore.QSize(20, 16777215))
        self.yMag1.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.yMag1.setText("")
        self.yMag1.setObjectName("yMag1")
        self.gridLayout_4.addWidget(self.yMag1, 1, 1, 1, 1)
        self.zMag1 = QtWidgets.QLabel(self.widget_6)
        self.zMag1.setMinimumSize(QtCore.QSize(20, 0))
        self.zMag1.setMaximumSize(QtCore.QSize(20, 16777215))
        self.zMag1.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.zMag1.setText("")
        self.zMag1.setObjectName("zMag1")
        self.gridLayout_4.addWidget(self.zMag1, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.widget_6, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.yAccel.setText(_translate("MainWindow", "yAccel"))
        self.xAccel.setText(_translate("MainWindow", "xAccel"))
        self.zAccel.setText(_translate("MainWindow", "zAccel"))
        self.yRate.setText(_translate("MainWindow", "yRate"))
        self.xRate.setText(_translate("MainWindow", "xRate"))
        self.zRate.setText(_translate("MainWindow", "zRate"))
        self.yMag.setText(_translate("MainWindow", "yMag"))
        self.xMag.setText(_translate("MainWindow", "xMag"))
        self.zMag.setText(_translate("MainWindow", "zMag"))

        # still here
        self.Accel_plot.plot.setBackground('w')
        self.Rate_plot.plot.setBackground('w')
        self.Mag_plot.plot.setBackground('w')
        self.IMU = {
            'time': 0,
            'xAccel': 0.0,
            'yAccel': 0.0,
            'zAccel': 0.0,
            'xRate': 0.0,
            'yRate': 0.0,
            'zRate': 0.0,
            'xMag': 0.0,
            'yMag': 0.0,
            'zMag': 0.0,
        }
        self.serialPort = serial.Serial('COM5', 115200)


class timePlot(QWidget):
    def __init__(self, parent=None, yname='Reading / mV'):
        QWidget.__init__(self, parent)
        self.plot = pg.PlotWidget(
            title="Example plot",
            labels={'left': yname},
            axisItems={'bottom': TimeAxisItem(orientation='bottom')}
        )
        self.plot.setYRange(0, 5000)
        self.plot.setXRange(timestamp(), timestamp() + 20)
        self.plot.showGrid(x=True, y=True)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.plot, 0, 0)

        self.plotCurve = self.plot.plot()
        self.plotCurve1 = self.plot.plot()
        self.plotCurve2 = self.plot.plot()

        self.plotData = {'x': [], 'y': [], 'z': [], 'z1': []}

    def updatePlot(self, newValue, newValue1, newValue2):
        self.plotData['y'].append(newValue)
        self.plotData['z'].append(newValue1)
        self.plotData['z1'].append(newValue2)
        self.plotData['x'].append(timestamp1())
        self.plot.setYRange(min(self.plotData['y'][-150:] + self.plotData['z'][-150:] + self.plotData['z1'][-150:]),
                            max(self.plotData['y'][-150:] + self.plotData['z'][-150:] + self.plotData['z1'][-150:]))
        self.plot.setXRange(timestamp() - 15, timestamp() + 5)
        self.plotCurve.setData(self.plotData['x'], self.plotData['y'], pen=pg.mkPen(color=(255, 0, 0)))
        self.plotCurve1.setData(self.plotData['x'], self.plotData['z'], pen=pg.mkPen(color=(0, 0, 255)))
        self.plotCurve2.setData(self.plotData['x'], self.plotData['z1'], pen=pg.mkPen(color=(0, 255, 0)))




# -----------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------

# FUNCTION CATEGORY 1 -----------------------------------------
from guiLoop import guiLoop # https://gist.github.com/niccokunzmann/8673951


@guiLoop
def Main_loop():
    data = b''
    while True:
        if ui.serialPort.isOpen():
            if ui.serialPort.in_waiting:
                dr = ui.serialPort.read()
                data += dr
                try:
                    if data[-2:] == b'UU':
                        z1 = data.find(b'z1') + 3
                        UU = data.find(b'UU')
                        datos = data[z1:UU]
                        data = b''
                        i = 0
                        for key in ui.IMU:
                            if key == 'time':
                                ui.IMU[key] = int.from_bytes(datos[4 * i:(4 * i + 4)], byteorder='little',
                                                          signed=False)
                            else:
                                [x] = struct.unpack('f', datos[4 * i:(4 * i + 4)])
                                ui.IMU[key] = x
                            i += 1
                        print()
                        ui.Accel_plot.updatePlot(ui.IMU['xAccel'], ui.IMU['yAccel'], ui.IMU['zAccel'])
                        ui.Rate_plot.updatePlot(ui.IMU['xRate'], ui.IMU['yRate'], ui.IMU['zRate'])
                        ui.Mag_plot.updatePlot(ui.IMU['xMag'], ui.IMU['yMag'], ui.IMU['zMag'])
                except:
                    pass

        yield 0.00001


# FUNCTION CATEGORY 2 -----------------------------------------


# FUNCTION CATEGORY n -----------------------------------------


# -----------------------------------------------------------------------------
# RUNTIME PROCEDURE
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    Main_loop(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
