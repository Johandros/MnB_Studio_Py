# This Python file uses the following encoding: utf-8

import hexconverter as hexc


class FaceFinder:
    FaceCodes = []

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
        self.FaceCodes = ["", ""]

    def ReadFaceCode(self, faceCodeLine):
        sp = faceCodeLine.strip().split()

        face1 = "0x"
        face1 += hexc.Dec2Hex_16CHARS(sp[0])
        face1 += hexc.Dec2Hex_16CHARS(sp[1])
        face1 += hexc.Dec2Hex_16CHARS(sp[2])
        face1 += hexc.Dec2Hex_16CHARS(sp[3])
        self.Face1 = face1

        face2 = "0x"
        face2 += hexc.Dec2Hex_16CHARS(sp[4])
        face2 += hexc.Dec2Hex_16CHARS(sp[5])
        face2 += hexc.Dec2Hex_16CHARS(sp[6])
        face2 += hexc.Dec2Hex_16CHARS(sp[7])
        self.Face2 = face2

    def GetFaceCode(self, face1, face2):
        ff = hexc.Hex2Dec(face2[19:16])

        fx2 = int(ff)  # long
        if fx2 > 0:
            ff = str(fx2 - 1)

        facecode = "  "
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
