# This Python file uses the following encoding: utf-8

import numpy as np

from skriptum import Skriptum
from skriptum import ObjectType

from skillhunter import SkillHunter
from facefinder import FaceFinder

from PySide2.QtWidgets import QMessageBox


# Constants
GUARANTEE_ALL = 0x07F00000  # 133169152‬

ERROR_MSG_1 = "You probably have too many lines found in troop init!"
ERROR_MSG_1 += "Check your files!"

ERROR_MSG_2 = "Too few lines found in troop init! Check your files!"

# Static/Global Properties
ShortProficies = False
sk = SkillHunter()


class Troop(Skriptum):
# Properties
  # General
    Name = ""
    PluralName = ""
    Flags = ""
    FlagsGZ = 0
    DialogImage = "0"
    # DialogImageGZ = 0
    SceneCode = ""
    SceneCodeGZ = 0
    Reserved = ""
    ReservedGZ = 0
    FactionID = 0
    Items = []  # List<int>
    ItemFlags = []  # List<ulong>

  # Upgrade Troop
    UpgradeTroop1 = 0
    UpgradeTroop2 = 0
    UpgradeTroop1ErrorCode = ""
    UpgradeTroop2ErrorCode = ""

  # Faces
    Face1 = ""
    Face2 = ""

  # Skills
    Skills = []

    # --Persuasion
    @property
    def Persuasion(self):
        return self.Skills[0]

    @Persuasion.setter
    def Persuasion(self, value):
        self.Skills[0] = value

    # --PrisonerManagement
    @property
    def PrisonerManagement(self):
        return self.Skills[1]

    @PrisonerManagement.setter
    def PrisonerManagement(self, value):
        self.Skills[1] = value

    # --Leadership
    @property
    def Leadership(self):
        return self.Skills[2]

    @Leadership.setter
    def Leadership(self, value):
        self.Skills[2] = value

    # --Trade
    @property
    def Trade(self):
        return self.Skills[3]

    @Trade.setter
    def Trade(self, value):
        self.Skills[3] = value

    # --Tactics
    @property
    def Tactics(self):
        return self.Skills[4]

    @Tactics.setter
    def Tactics(self, value):
        self.Skills[4] = value

    # --Pathfinding
    @property
    def Pathfinding(self):
        return self.Skills[5]

    @Pathfinding.setter
    def Pathfinding(self, value):
        self.Skills[5] = value

    # --Spotting
    @property
    def Spotting(self):
        return self.Skills[6]

    @Spotting.setter
    def Spotting(self, value):
        self.Skills[6] = value

    # --InventoryManagement
    @property
    def InventoryManagement(self):
        return self.Skills[7]

    @InventoryManagement.setter
    def InventoryManagement(self, value):
        self.Skills[7] = value

    # --WoundTreatment
    @property
    def WoundTreatment(self):
        return self.Skills[8]

    @WoundTreatment.setter
    def WoundTreatment(self, value):
        self.Skills[8] = value

    # --Surgery
    @property
    def Surgery(self):
        return self.Skills[9]

    @Surgery.setter
    def Surgery(self, value):
        self.Skills[9] = value

    # --FirstAid
    @property
    def FirstAid(self):
        return self.Skills[10]

    @FirstAid.setter
    def FirstAid(self, value):
        self.Skills[10] = value

    # --Engineer
    @property
    def Engineer(self):
        return self.Skills[11]

    @Engineer.setter
    def Engineer(self, value):
        self.Skills[11] = value

    # --HorseArchery
    @property
    def HorseArchery(self):
        return self.Skills[12]

    @HorseArchery.setter
    def HorseArchery(self, value):
        self.Skills[12] = value

    # --Looting
    @property
    def Looting(self):
        return self.Skills[13]

    @Looting.setter
    def Looting(self, value):
        self.Skills[13] = value

    # --Training
    @property
    def Training(self):
        return self.Skills[14]

    @Training.setter
    def Training(self, value):
        self.Skills[14] = value

    # --Tracking
    @property
    def Tracking(self):
        return self.Skills[15]

    @Tracking.setter
    def Tracking(self, value):
        self.Skills[15] = value

    # --WeaponMaster
    @property
    def WeaponMaster(self):
        return self.Skills[16]

    @WeaponMaster.setter
    def WeaponMaster(self, value):
        self.Skills[16] = value

    # --Shield
    @property
    def Shield(self):
        return self.Skills[17]

    @Shield.setter
    def Shield(self, value):
        self.Skills[17] = value

    # --Athletics
    @property
    def Athletics(self):
        return self.Skills[18]

    @Athletics.setter
    def Athletics(self, value):
        self.Skills18 = value

    # --Riding
    @property
    def Riding(self):
        return self.Skills[19]

    @Riding.setter
    def Riding(self, value):
        self.Skills[19] = value

    # --Ironflesh
    @property
    def Ironflesh(self):
        return self.Skills[20]

    @Ironflesh.setter
    def Ironflesh(self, value):
        self.Skills[20] = value

    # --PowerStrike
    @property
    def PowerStrike(self):
        return self.Skills[21]

    @PowerStrike.setter
    def PowerStrike(self, value):
        self.Skills[21] = value

    # --PowerThrow
    @property
    def PowerThrow(self):
        return self.Skills[22]

    @PowerThrow.setter
    def PowerThrow(self, value):
        self.Skills[22] = value

    # --PowerDraw
    @property
    def PowerDraw(self):
        return self.Skills[23]

    @PowerDraw.setter
    def PowerDraw(self, value):
        self.Skills[23] = value


  # Attributes
    Attributes = []

    # --Strength
    @property
    def Strength(self):
        return self.Attributes[0]

    @Strength.setter
    def Strength(self, value):
        self.Attributes[0] = value

    # --Agility
    @property
    def Agility(self):
        return self.Attributes[1]

    @Agility.setter
    def Agility(self, value):
        self.Attributes[1] = value

    # --Intelligence
    @property
    def Intelligence(self):
        return self.Attributes[2]

    @Intelligence.setter
    def Intelligence(self, value):
        self.Attributes[2] = value

    # --Charisma
    @property
    def Charisma(self):
        return self.Attributes[3]

    @Charisma.setter
    def Charisma(self, value):
        self.Attributes[3] = value

    # --Level
    @property
    def Level(self):
        return self.Attributes[4]

    @Level.setter
    def Level(self, value):
        self.Attributes[4] = value


  # Proficiencies
    ProficienciesSC = ""
    Proficiencies = []

    # --OneHanded
    @property
    def OneHanded(self):
        return self.Proficiencies[0]

    @OneHanded.setter
    def OneHanded(self, value):
        self.Proficiencies[0] = value

    # --TwoHanded
    @property
    def TwoHanded(self):
        return self.Proficiencies[1]

    @TwoHanded.setter
    def TwoHanded(self, value):
        self.Proficiencies[1] = value

    # --Polearm
    @property
    def Polearm(self):
        return self.Proficiencies[2]

    @Polearm.setter
    def Polearm(self, value):
        self.Proficiencies[2] = value

    # --Archery
    @property
    def Archery(self):
        return self.Proficiencies[3]

    @Archery.setter
    def Archery(self, value):
        self.Proficiencies[3] = value

    # --Crossbow
    @property
    def Crossbow(self):
        return self.Proficiencies[4]

    @Crossbow.setter
    def Crossbow(self, value):
        self.Proficiencies[4] = value

    # --Throwing
    @property
    def Throwing(self):
        return self.Proficiencies[5]

    @Throwing.setter
    def Throwing(self, value):
        self.Proficiencies[5] = value

    # --Firearm
    @property
    def Firearm(self):
        return self.Proficiencies[6]

    @Firearm.setter
    def Firearm(self, value):
        self.Proficiencies[6] = value

# Initilization
    def __init__(self, values):
        super().__init__(values[0].lstrip().split()[0], ObjectType.Troop)

        self.Skills = np.zeros(42, dtype=np.int)
        self.Attributes = np.zeros(5, dtype=np.int)
        self.Proficiencies = np.zeros(7, dtype=np.int)

        self.init(values)
        pass

    def init(self, values):
        self.reset()

        count = len(values)
        if count > 5 and count < 8:
            self.setFirstLine(values[0])
            self.setItems(values[1])
            self.setAttributes(values[2])
            self.setProficiencies(values[3])
            self.setSkills(values[4])
            self.setFaceCodes(values[5])
            return

        # show error when values are corrupted or otherwise wrong
        self.sendErrorMessage(ERROR_MSG_2)
        pass

# Set methods
    def setFirstLine(self, line):
        lineData = line.strip().split()

        if len(lineData) < 10:
            self.sendErrorMessage(ERROR_MSG_1)
            return

        # self.ID = lineData[0]  # in Skriptum
        self.Name = lineData[1].replace('_', ' ')
        self.PluralName = lineData[2].replace('_', ' ')

        self.DialogImage = lineData[3]

        # TODO rethink logic for direct python file usage
        flags = lineData[4].strip()
        if flags.isnumeric():
            self.FlagsGZ = int(flags)  # ulong
            # self.Flags = self.flagsFromVal(HexConv.dec2Hex(self.FlagsGZ))
        else:
            # self.FlagsGZ = self.flagsGZFromString(flags)
            self.Flags = flags

        self.setSceneCode(lineData[5])
        self.setReserved(lineData[6])

        self.FactionID = int(lineData[7])  # if not ID/numeric --> ERROR!!!

        try:
            self.UpgradeTroop1 = int(lineData[8])
        except:
            self.UpgradeTroop1ErrorCode = lineData[8]
            self.sendUpgradePathErrorMessage(1, self.UpgradeTroop1ErrorCode)

        try:
            self.UpgradeTroop2 = int(lineData[9])
        except:
            self.UpgradeTroop2ErrorCode = lineData[9]
            self.sendUpgradePathErrorMessage(2, self.UpgradeTroop2ErrorCode)

    def setItems(self, items):
        self.Items.clear()
        self.ItemFlags.clear()

        itemsNew = []
        itemsFlagsNew = []

        tmpList = items.strip().split()
        itemCount = int(len(tmpList) / 2)  # - 1

        for i in range(0, itemCount):
            itemX2 = tmpList[i * 2].strip()
            if itemX2 != "-1" and len(itemX2) != 0:
                itemFlag = tmpList[i * 2 + 1]
                itemsNew.append(int(itemX2))
                itemsFlagsNew.append(int(itemFlag) >> 24)  # ulong

        self.Items = itemsNew
        self.ItemsFlags = itemsFlagsNew

    def setSceneCode(self, sceneCode):
        self.SceneCodeGZ = int(sceneCode)  # ulong
        if self.SceneCodeGZ == 0:
            self.SceneCode = "no_scene"
        else:
            entryPoint = (self.SceneCodeGZ >> 16) & 0xFF
            code = self.SceneCodeGZ & 0xFFFF  # ushort.MaxValue
            self.SceneCode = str(code) + "|" + str(entryPoint)

    def setReserved(self, reserved):
        resV = "reserved"

        if reserved == resV:
            self.ReservedGZ = 0
        else:
            self.ReservedGZ = int(reserved)

        if self.ReservedGZ == 0:
            self.Reserved = resV
        else:
            self.Reserved = reserved

    def setAttributes(self, attributes):
        sp = attributes.strip().split()

        if len(sp) >= 5:
            self.Strength = int(sp[0])
            self.Agility = int(sp[1])
            self.Intelligence = int(sp[2])
            self.Charisma = int(sp[3])
            self.Level = int(sp[4])
            return
        elif len(sp) != 1:
            if sp[0].isnumeric():
                attribs = int(sp[0])  # ulong
                self.Strength = attribs & 0xFF  # int
                self.Agility = (attribs >> 8) & 0xFF  # int
                self.Intelligence = (attribs >> 16) & 0xFF  # int
                self.Charisma = (attribs >> 24) & 0xFF  # int
                self.Level = (attribs >> 32) & 0xFF  # int
                return

        self.sendErrorMessage(ERROR_MSG_2)

    def setProficiencies(self, proficies):
        profS = proficies[1:].split()
        if len(profS) >= 7:
            for i in range(0, len(profS)):
                self.Proficiencies[i] = int(profS[i])
            self.setProficiesSC()
            return
        elif len(profS) == 1:
            if profS[1].isnumeric():
                # TODO: make use of direct python access
                # self.Proficiencies = self.getProficiesFromSC(profS[0])
                return

        self.sendErrorMessage(ERROR_MSG_2)

    def setProficiesSC6(self, tmp):
        if self.OneHanded > 0:
            tmp += "wp_one_handed(" + str(self.Proficiencies[0])
        if self.TwoHanded > 0:
            tmp += ")|wp_two_handed(" + str(self.Proficiencies[1])
        if self.Polearm > 0:
            tmp += ")|wp_polearm(" + str(self.Proficiencies[2])
        if self.Archery > 0:
            tmp += ")|wp_archery(" + str(self.Proficiencies[3])
        if self.Crossbow > 0:
            tmp += ")|wp_crossbow(" + str(self.Proficiencies[4])
        if self.Throwing > 0:
            tmp += ")|wp_throwing(" + str(self.Proficiencies[5])
        return tmp

    def setProficiesSC(self):
        tmp = ""

        # if self.Proficiencies[:-1] == self.Proficiencies[:6]:
        if np.all(self.Proficiencies[:6] == self.Proficiencies[0]):
            tmp = "wp(" + str(self.Proficiencies[0])
        elif self.Proficiencies[:-1] == self.Proficiencies[:3]:
            tmp = "wpe(" + str(self.Proficiencies[2]) + ", "
            tmp += str(self.Proficiencies[3]) + ", "
            tmp += str(self.Proficiencies[4]) + ", "
            tmp += str(self.Proficiencies[5])
        elif self.Proficiencies[1] == (self.Proficiencies[0] + 20):
            if self.Proficiencies[1] == (self.Proficiencies[2] + 10):
                tmp = "wp_melee(" + str(self.Proficiencies[1])
        elif ShortProficies is False:
            tmp = self.setProficiesSC6(tmp)
        else:
            tmp = "wpex("
            profMinOne = len(self.Proficiencies) - 1
            for i in range(0, profMinOne):
                tmp += str(self.Proficiencies[i]) + ","
            tmp = tmp.rstrip(',')

        if self.Firearm > 0:
            tmp += ")|wp_firearm(" + str(self.Proficiencies[6])

        if len(tmp) != 0:
            self.ProficienciesSC = tmp.lstrip(')|') + ')'
        else:
            self.ProficienciesSC = "0"

    def setSkills(self, knowledge):
        skills = sk.ReadSkills(knowledge)
        for i in range(0, len(self.Skills)):
            self.Skills[i] = skills[i]

    def setFaceCodes(self, faceCode):
        ff = FaceFinder()
        ff.ReadFaceCode(faceCode)
        self.Face1 = ff.Face1
        self.Face2 = ff.Face2

# Rest and Error messages
    def resetIntArrays(self, array):
        for i in range(len(array)):
            array[i] = 0
        return array

    def reset(self):
        self.Name = ""
        self.PluralName = ""

        self.Attributes = self.resetIntArrays(self.Attributes)
        self.Proficiencies = self.resetIntArrays(self.Proficiencies)
        self.Skills = self.resetIntArrays(self.Skills)

        self.Items.clear()
        self.ItemFlags.clear()

        self.UpgradeTroop1 = 0
        self.UpgradeTroop2 = 0
        self.FactionID = 0

        self.DialogImage = "0"
        self.SceneCode = "0"
        self.Reserved = "0"
        pass

    def sendErrorMessage(self, errorMsg):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("ERROR")  # Application.ProductName
        msg.setStandardButtons(QMessageBox.Ok)
        # msg.buttonClicked.connect(msgbtn)
        msg.setText(errorMsg)

        retval = msg.exec_()
        return retval

    def sendUpgradePathErrorMessage(self, number, errorCode):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle("ERROR")  # Application.ProductName
        msg.setStandardButtons(QMessageBox.Ok)
        # msg.buttonClicked.connect(msgbtn)

        errorMsg = "ERROR (0x494%d) - %s" % (number, self.ID)
        errorMsg += " - UPGRADE_TROOP_%d: %s" % (number, errorCode)
        msg.setText(errorMsg)

        retval = msg.exec_()
        return retval

# debug and info
    def __str__(self):
        return "" \
            " - ID: {0}\n" \
            " - Type: {1}\n" \
            " - Name: {2}\n" \
            " - PluralName: {3}\n" \
            "".format(
                self.ID,  # General
                self.Type,
                self.Name,
                self.PluralName
            )

    def __repr__(self):
        basics = str(self)
        # UpgradeTroop1ErrorCode - probably redundant
        # UpgradeTroop2ErrorCode - probably redundant
        return "Troop:\n" \
            "{0}" \
            " - Flags: {1}\n" \
            " - FlagsGZ: {2}\n" \
            " - DialogImage: {3}\n" \
            " - SceneCode: {4}\n" \
            " - SceneCodeGZ: {5}\n" \
            " - Reserved: {6}\n" \
            " - ReservedGZ: {7}\n" \
            " - FactionID: {8}\n" \
            " - Items: {9}\n" \
            " - ItemFlags: {10}\n" \
            " - UpgradeTroop1: {11}\n" \
            " - UpgradeTroop2: {12}\n" \
            " - Face1: {13}\n" \
            " - Face2: {14}\n" \
            " - Skills: {15}\n" \
            " - Attributes: {16}\n" \
            " - ProficienciesSC: {17}\n" \
            " - Proficiencies: {18}\n" \
            "".format(
                basics,  # General
                self.Flags,
                self.FlagsGZ,
                self.DialogImage,
                self.SceneCode,
                self.SceneCodeGZ,
                self.Reserved,
                self.ReservedGZ,
                self.FactionID,  # later maybe faction name or code id
                self.Items,
                self.ItemFlags,
                self.UpgradeTroop1,  # Upgrade Troop
                self.UpgradeTroop2,
                self.Face1,  # Faces
                self.Face2,
                self.Skills,  # Skills
                self.Attributes,  # Attributes
                self.ProficienciesSC,  # Proficiencies
                self.Proficiencies
            )
