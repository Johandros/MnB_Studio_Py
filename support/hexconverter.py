# This Python file uses the following encoding: utf-8

from PySide2.QtWidgets import QMessageBox
import string

# Consts

# MAX_NUM_OF_BITS = 96
# TWO_TO_THE_49TH_POWER = 562949953421312


# Hex Methods

# returns hex string
def Dec2Hex(decimalIn, use16Chars=False):
    hexs = ""

    hex_length = 8
    if use16Chars:
        hex_length *= 2  # 16

    try:
        valx = int(decimalIn)
        hexs = "{0:0{1}x}".format(valx, hex_length)
    except:
        errorMsg = "ERROR #111222 -> HEX_CONVERTER_WRONG_FORMAT: "
        errorMsg += str(decimalIn)
        ERROR_HEX(errorMsg)

    return hexs


def Hex2Dec(hexString, use16Char=False):
    dexc = 0
    try:
        decx = int(hexString, 16)
    except:
        errorMsg = "ERROR #333444 -> HEX_CONVERTER_WRONG_FORMAT: "
        errorMsg += str(decimalIn)
        ERROR_HEX(errorMsg)
    return decx


def ConvertSingleHexCodeToIntArray(hexCode):
    array = []
    for ch in hexCode:
        i = ReplaceHexToInt(ch)
        array.append(i)
    return array


def ReplaceHexToInt(hexChar):
    return int(hexChar, 16)


def ReplaceHexToIntString(hexChar):
    return str(ReplaceHexToInt(hexChar))


# region Helper Methods

def ERROR_HEX(errorMsg):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setWindowTitle("ERROR")  # Application.ProductName
    msg.setStandardButtons(QMessageBox.Ok)
    # msg.buttonClicked.connect(msgbtn)

    msg.setText(errorMsg)
    msg.exec_()


def Dec2Hex_16CHARS(decimalIn):
    return Dec2Hex(decimalIn, True)

def Hex2Dec_16CHARS(hexString):
    return Hex2Dec(hexString, True)
