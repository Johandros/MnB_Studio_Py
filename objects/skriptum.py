# This Python file uses the following encoding: utf-8

from enum import IntEnum

import msinteract

from headervariable import HeaderVariable


# TODO: Optimize this, since it is redundant
#   (only dialog and tableau are changing)
Prefixes = ["script", "mt", "prsnt", "menu", "trp", "itm", "str",
            "simple_trigger", "trigger", "ip", "mesh", "track",
            "qst", "snd", "spr", "tableau", "icon", "dialog",
            "fac", "anim", "pt", "p", "skl", "pfx", "skin",
            "psys", "scn"]

CodePrefixes = ["script", "mt", "prsnt", "menu", "trp", "itm", "str",
                "simple_trigger", "trigger", "ip", "mesh", "track",
                "qst", "snd", "spr", "tab", "icon", "dlga", "fac",
                "anim", "pt", "p", "skl", "pfx", "skin",
                "psys", "scn"]


class ObjectType(IntEnum):
    Script = 0
    MissionTemplate = 1
    Presentation = 2
    GameMenu = 3
    Troop = 4
    Item = 5
    GameString = 6
    SimpleTrigger = 7
    Trigger = 8
    InfoPage = 9
    Mesh = 10
    Music = 11
    Quest = 12
    Sound = 13
    SceneProp = 14
    TableauMaterial = 15
    MapIcon = 16
    Dialog = 17
    Faction = 18
    Animation = 19
    PartyTemplate = 20
    Party = 21
    Skill = 22
    PostFX = 23
    Skin = 24
    ParticleSystem = 25
    Scene = 26
    # extra
    START = Script
    END = Scene
    DEFAULT = START


class Skriptum:
    ID = ""
    Type = 0  # SCRIPT
    # ObjectType = ObjectType.DEFAULT

    _headerVariables = []

    def __init__(self, idName, objectType):
        self.ID = self.removePrefix(self.removeCodePrefix(idName.strip()))
        self.Type = objectType
        pass

    def __str__(self):
        return "" \
            "ID: {0}\n" \
            "Type: {1}\n" \
            "".format(self.ID, self.Type)

    def prefix(self):
        return Prefixes[self.Type]

    def codePrefix(self):
        return CodePrefixes[self.Type]

    def removePrefix(self, idName):
        prex = self.prefix()
        if (idName.startswith(prex)):
            idName = idName[len(prex)]
        return idName

    def removeCodePrefix(self, idName):
        prex = self.codePrefix()
        if (idName.startswith(prex)):
            idName = idName[len(prex)]
        return idName

    # SetFlags(ulong gu, List<HeaderVariables> variables)
    def SetFlags(self, gz, startw=""):
        text = ""
        for variable in self._headerVariables:
            x = int(variable.VariableValue)
            if (x & gz) == x:
                text += variable.VariableName + '|'

        if len(text) != 0:
            text = text.rstrip('|')
        else:
            text = str(gz)

        return text

    # SetFlagsGZ(string text, List<HeaderVariable> variables)
    def SetFlagsGZ(self, text, startw=""):
        gz = 0
        sp = text.split('|')
        for variable in self._headerVariables:
            for flag in sp:
                if variable.VariableName == flag:
                    gz |= int(variable.VariableValue)
        return gz

    # TODO: rename and rethink later
    def GetHeaderVariableList(self, header="xyz", startw=""):
        # TODO: get header file from type or global var in file?
        headerVarBox = msinteract.importHeader(header, startw)  # tag_
        headerVarsModule = headerVarBox["module"]
        headerVarsNames = headerVarBox["vars"]

        headerVars = []
        for var_name in headerVarsNames:
            val = getattr(headerVarsModule, var_name)
            headerVar = HeaderVariable(val, var_name)
            headerVars.append(headerVar)
