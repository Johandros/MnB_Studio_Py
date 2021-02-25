# This Python file uses the following encoding: utf-8

import hexconverter as hexc


class FaceFinder:
    FaceCodes = ["", ""]

    # -- Face1
    @property
    def Face1(self):
        return self.FaceCodes[0]

    @Face1.setter
    def Face1(self, value):
        self.FaceCodes[0] = value

    # -- Face2
    @property
    def Face2(self):
        return self.FaceCodes[1]

    @Face2.setter
    def Face2(self, value):
        self.FaceCodes[1] = value


    def __init__(self):
        pass

    def ReadFaceCode(self, faceCodeLine):
        sp = faceCodeLine.strip().split()

        Face1 = "0x"
        Face1 += hexc.Dec2Hex_16CHARS(sp[0])
        Face1 += hexc.Dec2Hex_16CHARS(sp[1])
        Face1 += hexc.Dec2Hex_16CHARS(sp[2])
        Face1 += hexc.Dec2Hex_16CHARS(sp[3])

        Face2 = "0x"
        Face2 += hexc.Dec2Hex_16CHARS(sp[4])
        Face2 += hexc.Dec2Hex_16CHARS(sp[5])
        Face2 += hexc.Dec2Hex_16CHARS(sp[6])
        Face2 += hexc.Dec2Hex_16CHARS(sp[7])

    def GetFaceCode(self, face1, face2):
        space = ' '
        facecode = " "

        ff = hexc.Hex2Dec(face2[19:16])

        fx2 = int(ff)  # long
        if fx2 > 0:
            ff = str(fx2 - 1)

        facecode += " "
        facecode += " {}".format(hexc.Hex2Dec(face1[3:16]))
        facecode += " {}".format(hexc.Hex2Dec(face1[19:16]))
        facecode += " {}".format(hexc.Hex2Dec(face1[35:16]))
        facecode += " {}".format(hexc.Hex2Dec(face1[51:16]))
        facecode += " {}".format(hexc.Hex2Dec(face2[3:16]))
        facecode += " " + ff  # 19:16
        facecode += " {}".format(hexc.Hex2Dec(face2[35:16]))
        facecode += " {}".format(hexc.Hex2Dec(face2[51:16]))
        facecode += " "

        return facecode
