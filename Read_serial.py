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
IMU = {
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

# -----------------------------------------------------------------------------
# LOCAL UTILITIES
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------

# FUNCTION CATEGORY 1 -----------------------------------------


# FUNCTION CATEGORY 2 -----------------------------------------


# FUNCTION CATEGORY n -----------------------------------------


# -----------------------------------------------------------------------------
# RUNTIME PROCEDURE
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    serialPort = serial.Serial('COM5', 115200)
    try:
        data = b''
        while True:
            if serialPort.isOpen():
                if serialPort.in_waiting:
                    dr = serialPort.read()
                    data += dr
                    try:
                        if data[-2:] == b'UU':
                            z1 = data.find(b'z1')+3
                            UU = data.find(b'UU')
                            datos = data[z1:UU]
                            data = b''
                            i = 0
                            for key in IMU:
                                if key == 'time':
                                    IMU[key] = int.from_bytes(datos[4*i:(4*i+4)], byteorder='little', signed=False)
                                else:
                                    [x] = struct.unpack('f', datos[4*i:(4*i+4)])
                                    IMU[key] = x
                                i += 1
                            print(IMU)
                    except:
                        pass
    except:
        print('End program')
