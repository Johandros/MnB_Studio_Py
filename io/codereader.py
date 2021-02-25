# This Python file uses the following encoding: utf-8

from PySide2.QtCore import QObject

from script import Script
from troop import Troop

from msinteract import ModuleSystemInteract as MSInteract


# Constants
MINUS_ZERO = "-0,0000001337"
MINUS_ZERO_ALT = "-1.337E-07"
MINUS = "-"

FILES_PATH = "./files/"
MS_DATA_PATH = FILES_PATH + "module_data/"
MS_FILES_PATH = FILES_PATH + "module_system/"

FILES = (
    "scripts.txt",
    "mission_templates.txt",
    "presentations.txt",
    "menus.txt",
    "troops.txt",
    "item_kinds1.txt",
    "strings.txt",
    "simple_triggers.txt",
    "triggers.txt",
    "info_pages.txt",
    "meshes.txt",
    "music.txt",
    "quests.txt",
    "sounds.txt",
    "scene_props.txt",
    "tableau_materials.txt",
    "map_icons.txt",
    "conversation.txt",
    "factions.txt",
    "actions.txt",
    "party_templates.txt",
    "parties.txt",
    "skills.txt",
    "postfx.txt",
    "skins.txt",
    "particle_systems.txt",
    "scenes.txt",
    )

UNUSED_CODES = (
    "else_try_begin",
    "end_try",
    )

# had ulong previously

LOCAL_MIN = 1224979098644774912
LOCAL_MAX = 1224979098644775040  # max. 128 local variables

REG0 = 72057594037927936
REG127 = 72057594037928063  # max. 128 registers

QUICKSTRING_MIN = 1585267068834414592
QUICKSTRING_MAX = 1600000000000000000  # max?

GLOBAL_MIN = 144115188075855872
GLOBAL_MAX = 145000000000000000  # max?

# region TYPES
TRP_PLAYER = 360287970189639680
TROOP_MAX = 370000000000000000  # max?

SCRIPT_MIN = 936748722493063168
SCRIPT_MAX = 940000000000000000  # max?

STRING_MIN = 216172782113783808
STRING_MAX = 217000000000000000  # max?

SPR_MIN = 1080863910568919040
SPR_MAX = 1100000000000000000  # max?

PRSNT_MIN = 1513209474796486656
PRSNT_MAX = 1513210000000000000  # max?

FAC_MIN = 432345564227567616
FAC_MAX = 433000000000000000  # max?

P_MAIN_PARTY = 648518346341351424
P_MAX = 648600000000000000  # max?

ITM_MIN = 288230376151711744
ITM_MAX = 290000000000000000  # max?

SCENE_MIN = 720575940379279360
SCENE_MAX = 720575940380000000  # max?

MESH_MIN = 1441151880758558720
MESH_MAX = 1450000000000000000  # max?

PT_MIN = 576460752303423488
PT_MAX = 576500000000000000  # max?

MT_MIN = 792633534417207296
MT_MAX = 792700000000000000  # max?

SKL_MIN = 1369094286720630784
SKL_MAX = 1369094286720700000  # max?

SND_MIN = 1152921504606846976
SND_MAX = 1152921504607000000  # max?

PSYS_MIN = 1008806316530991104
PSYS_MAX = 1009000000000000000  # max?

MENU_MIN = 864691128455135232
MENU_MAX = 865000000000000000  # max?

QUEST_MIN = 504403158265495552
QUEST_MAX = 504500000000000000  # max?

TABLEAU_MAT_MIN = 1729382256910270464
TABLEAU_MAT_MAX = 1730000000000000000  # max?

TRACK_MIN = 1657324662872342528
TRACK_MAX = 1660000000000000000  # max?

MAP_ICON_MIN = 129703669268270
MAP_ICON_MAX = 130000000000000  # max?

# INFO_PAGE
# DIALOG
# POST_FX

ANIM_MIN = 1801439850948198400
ANIM_MAX = 1810000000000000000  # max?
# ANIM_MAX = ulong.MaxValue - int.MaxValue;


# for "static" use
ObjectsExpected = 0
ObjectsRead = 0
ModPath = ""
ProjectPath = ""




# TODO: RETHINK LATER!!!

#  @staticmethod¶  # for static methods :P def f(arg1, arg2, ...):

ms = MSInteract()

# ids = ms.importModuleIds(MS_FILES_PATH)
# print(ids)

module_elements = ms.importModuleFiles(MS_FILES_PATH)
for i, e in enumerate(module_elements[0]):
    for name in e:
        if name.startswith("factions"):
            factions = getattr(module_elements[1][i], "factions")
            # print(factions[0])


Elements = []  # list with lists with element names - use module system
for i in range(0, len(FILES)):
    Elements.append([])  # empty list





class CodeReader(QObject):
    filepath = ""

# Properties

    @property
    def Scripts(self):
        return Elements[0]

    @property
    def MissionTemplates(self):
        return Elements[1]

    @property
    def Presentations(self):
        return Elements[2]

    @property
    def GameMenus(self):
        return Elements[3]

    @property
    def Troops(self):
        return Elements[4]

    @property
    def Items(self):
        return Elements[5]

    # Simple Triggers - None
    # Triggers - None

    @property
    def Strings(self):
        return Elements[6]

    @property
    def InfoPages(self):
        return Elements[7]

    @property
    def Meshes(self):
        return Elements[8]

    @property
    def Tracks(self):
        return Elements[9]

    @property
    def Quests(self):
        return Elements[10]

    @property
    def Sounds(self):
        return Elements[11]

    @property
    def SceneProps(self):
        return Elements[12]

    @property
    def TableauMaterials(self):
        return Elements[13]

    @property
    def MapIcons(self):
        return Elements[14]

    # Dialogs - None

    @property
    def Factions(self):
        return Elements[15]

    @property
    def Animations(self):
        return Elements[16]

    @property
    def PartyTemplates(self):
        return Elements[17]

    @property
    def Parties(self):
        return Elements[18]

    @property
    def Skills(self):
        return Elements[19]

    @property
    def PostFXParams(self):
        return Elements[20]

    # Skins - None

    @property
    def ParticleSystems(self):
        return Elements[21]

    @property
    def Scenes(self):
        return Elements[22]

    # -- EXTRA - always last --

    @property
    def QuickStrings(self):
        return Elements[23]

    @property
    def GlobalVariables(self):
        return Elements[24]
    # --

# Functions
    def __init__(self, filepath):
        CodeReader.filepath = filepath
        pass

    def readScripts(self):
        scripts = []

        file = open(CodeReader.filepath, "r")
        file.readline()  # skip version line

        # add expected script amount (as number) to overall expected
        global ObjectsExpected
        ObjectsExpected += int(file.readline())

        # read all lines and create script objects
        script = []
        scriptLines = []
        for line in file:
            # skip empty lines
            if len(line) > 1:
                line = line.strip()

                # check code start
                if line[0:1].isnumeric():
                    # separate code parts and prepare for decompile
                    scriptlines = line.split()
                    line = script[0]
                    script = []  # len(scriptlines) + 1
                    script.append(line)

                    # TODO: create function
                    # script = decompileScriptCode(script, scriptLines)
                else:
                    # TODO: create script class
                    # if len(script) > 0:
                    #     scripts.append(new Script(script))

                    # prepare new script object
                    scriptname = line.split()[0]
                    script = [scriptname]

        file.close()

        if len(script) > 0:
            s = Script(script)
            scripts.append(s)

        global ObjectsRead
        ObjectsRead += len(scripts)

        print(ObjectsRead)
        print(ObjectsExpected)

        print("readScripts done")

        return scripts

    def readTroops(self):
        troops = []

        file = open(CodeReader.filepath, "r")
        file.readline()  # skip version line

        maxTroops = int(file.readline())

        global ObjectsExpected
        ObjectsExpected += maxTroops

        for i in range(0, maxTroops):
            raw_data = []

            for j in range(0, 7):
                raw_data.append(file.readline())

            troops.append(Troop(raw_data))

        global ObjectsRead
        ObjectsRead += len(troops)

        print(ObjectsRead)
        print(ObjectsExpected)

        print("readTroops done")

        return troops

    def w(self):
        print()

    def reset(self, clearAllLists=False, resetModpath=False):
        global ObjectsExpected
        ObjectsExpected = 0
        global ObjectsRead
        ObjectsRead = 0

        if resetModpath:
            self.ModPath = ""
        if clearAllLists:
            self.clearLists()

    def clearLists(self):
        self.codeDeclarations.clear()
        self.codeValue.clear()
        # all elements from all modules
        self.elements.clear()



