# This Python file uses the following encoding: utf-8

import hexconverter as hexc
import msinteract as msin

SKILL_MASK = 0xFFFFFFFF


class SkillHunter:
    Skills = []
    Skillnames = []

    def __init__(self):
        self.InitialiseArrays()
        pass

    def ReadSkills(self, skillLine):
        self.ResetSkillArray()
        skillLine = skillLine.strip()

        # only 24 skills
        # return StartUpDefault(skillLine.Split())

        # all skills (48 - are there more?)
        return self.StartUpAll(skillLine.split())

    def InitialiseArrays(self):
        header_skills = msin.importHeader("skills", "skl_")

        self.Skillnames.clear()
        for skill in header_skills["vars"]:
            self.Skillnames.append(skill.lstrip("skl_"))

        self.ResetSkillArray()

    def ResetSkillArray(self):
        self.Skills.clear()
        for i in range(0, len(self.Skillnames)):
            self.Skills.append(0)  # -1

    def StartupDefault(self, tmpArray):
        # read first set of values (if value is A then set it to 10)
        # self.Skills[0] = tmpArray[0] & 0x0000000F  # persuasion
        # self.Skills[1] = tmpArray[5]) & 0xF  # prisoner_management
        # self.Skills[2] = tmpArray[6] & 0xF  # leadership
        # self.Skills[3] = tmpArray[7] & 0xF  # trade
        hexString = hexc.Dec2Hex(tmpArray[0])
        hexValues = hexc.ConvertSingleHexCodeToIntArray(hexString)
        self.Skills[4] = hexValues[0]   # tactics
        self.Skills[5] = hexValues[5]   # pathfinding
        self.Skills[6] = hexValues[6]   # spotting
        self.Skills[7] = hexValues[7]   # inventory_management

        # read second set of values
        hexString = hexc.Dec2Hex(tmpArray[1])
        hexValues = hexc.ConvertSingleHexCodeToIntArray(hexString)
        self.Skills[4] = hexValues[0]   # tactics
        self.Skills[5] = hexValues[1]   # pathfinding
        self.Skills[6] = hexValues[2]   # spotting
        self.Skills[7] = hexValues[3]   # inventory_management
        self.Skills[8] = hexValues[4]   # wound_treatment
        self.Skills[9] = hexValues[5]   # surgery
        self.Skills[10] = hexValues[6]  # first_aid
        self.Skills[11] = hexValues[7]  # engineer

        # read third set of values
        hexString = hexc.Dec2Hex(tmpArray[2])
        hexValues = hexc.ConvertSingleHexCodeToIntArray(hexString)
        self.Skills[12] = hexValues[0]  # horse_archery
        self.Skills[13] = hexValues[1]  # looting
        self.Skills[14] = hexValues[6]  # trainer
        self.Skills[15] = hexValues[7]  # tracking

        # read fourth set of values
        hexString = hexc.Dec2Hex(tmpArray[3])
        hexValues = hexc.ConvertSingleHexCodeToIntArray(hexString)
        self.Skills[16] = hexValues[4]  # weapon_master
        self.Skills[17] = hexValues[5]  # shield
        self.Skills[18] = hexValues[6]  # athletics
        self.Skills[19] = hexValues[7]  # riding

        # read fifth set of values
        hexString = hexc.Dec2Hex(tmpArray[4])
        hexValues = hexc.ConvertSingleHexCodeToIntArray(hexString)
        self.Skills[20] = hexValues[3]  # ironflesh
        self.Skills[21] = hexValues[4]  # power_strike
        self.Skills[22] = hexValues[5]  # power_throw
        self.Skills[23] = hexValues[6]  # power_draw

        return self.Skills

    # All known 48 skills (maybe more available)
    # example: 274 131072 0 1 0 0
    def StartUpAll(self, tmpArray):
        # read first set of values (if value is A then set it to 10)
        hexString = hexc.Dec2Hex(tmpArray[0])
        hexValues = hexc.ConvertSingleHexCodeToIntArray(hexString)
        self.Skills[0] = hexValues[0]   # persuasion | - - - X - - -
        self.Skills[1] = hexValues[1]   # reserved_IV | - - - X - - -
        self.Skills[2] = hexValues[2]   # reserved_III | - - - X - - -
        self.Skills[3] = hexValues[3]   # reserved_II | - - - X - - -
        self.Skills[4] = hexValues[4]   # reserved_I | - - - X - - -
        self.Skills[5] = hexValues[5]   # prisoner_management | - - - X - - -
        self.Skills[6] = hexValues[6]   # leadership | - - - X - - -
        self.Skills[7] = hexValues[7]   # trade | - - - X - - -

        # read second set of values
        hexString = hexc.Dec2Hex(tmpArray[1])
        hexValues = hexc.ConvertSingleHexCodeToIntArray(hexString)
        self.Skills[8] = hexValues[0]   # tactics | - - - X - - -
        self.Skills[9] = hexValues[1]   # pathfinding | - - - X - - -
        self.Skills[10] = hexValues[2]  # spotting | - - - X - - -
        self.Skills[11] = hexValues[3]  # inventory_management | - - - X - - -
        self.Skills[12] = hexValues[4]  # wound_treatment | - - - X - - -
        self.Skills[13] = hexValues[5]  # surgery | - - - X - - -
        self.Skills[14] = hexValues[6]  # first_aid | - - - X - - -
        self.Skills[15] = hexValues[7]  # engineer | - - - X - - -

        # read third set of values
        hexString = hexc.Dec2Hex(tmpArray[2])
        hexValues = hexc.ConvertSingleHexCodeToIntArray(hexString)
        self.Skills[16] = hexValues[0]  # horse_archery | - - - X - - -
        self.Skills[17] = hexValues[1]  # looting | - - - X - - -
        self.Skills[18] = hexValues[2]  # reserved_VIII | - - - X - - -
        self.Skills[19] = hexValues[3]  # reserved_VII | - - - X - - -
        self.Skills[20] = hexValues[4]  # reserved_VI | - - - X - - -
        self.Skills[21] = hexValues[5]  # reserved_V | - - - X - - -
        self.Skills[22] = hexValues[6]  # trainer | - - - X - - -
        self.Skills[23] = hexValues[7]  # tracking | - - - X - - -

        # read fourth set of values
        hexString = hexc.Dec2Hex(tmpArray[3])
        hexValues = hexc.ConvertSingleHexCodeToIntArray(hexString)
        self.Skills[24] = hexValues[0]  # reserved_XII
        self.Skills[25] = hexValues[1]  # reserved_XI
        self.Skills[26] = hexValues[2]  # reserved_X
        self.Skills[27] = hexValues[3]  # reserved_IV | - - - X - - -
        self.Skills[28] = hexValues[4]  # weapon_master | - - - X - - -
        self.Skills[29] = hexValues[5]  # shield | - - - X - - -
        self.Skills[30] = hexValues[6]  # athletics | - - - X - - -
        self.Skills[31] = hexValues[7]  # riding | - - - X - - -

        # read fifth set of values
        hexString = hexc.Dec2Hex(tmpArray[4])
        hexValues = hexc.ConvertSingleHexCodeToIntArray(hexString)
        self.Skills[32] = hexValues[0]  # reserved_XVI ?
        self.Skills[33] = hexValues[1]  # reserved_XV | - - - X - - -
        self.Skills[34] = hexValues[2]  # reserved_XIV | - - - X - - -
        self.Skills[35] = hexValues[3]  # ironflesh | - - - X - - -
        self.Skills[36] = hexValues[4]  # power_strike | - - - X - - -
        self.Skills[37] = hexValues[5]  # power_throw | - - - X - - -
        self.Skills[38] = hexValues[6]  # power_draw | - - - X - - -
        self.Skills[39] = hexValues[7]  # reserved_XIII

        # read sixth set of values
        hexString = hexc.Dec2Hex(tmpArray[5])
        hexValues = hexc.ConvertSingleHexCodeToIntArray(hexString)
        self.Skills[40] = hexValues[0]  # reserved_XVII
        self.Skills[41] = hexValues[1]  # reserved_XVIII

        if len(hexString.lstrip('0')) <= 2:
            return self.Skills

        # check are there more?
        self.Skills[42] = hexValues[2]  # reserved_XIX ???
        self.Skills[43] = hexValues[3]  # reserved_XX ???
        self.Skills[44] = hexValues[4]  # reserved_XXI ???
        self.Skills[45] = hexValues[5]  # reserved_XXII ???
        self.Skills[46] = hexValues[6]  # reserved_XXIII ???
        self.Skills[47] = hexValues[7]  # reserved_XXIV ???

        return self.Skills
