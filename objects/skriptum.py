# This Python file uses the following encoding: utf-8

from enum import Enum


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


class ObjectType(Enum):
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


class Skriptum:
    ID = ""
    Type = 0  # SCRIPT
    # ObjectType = ObjectType.DEFAULT

    def __init__(self, idName, objectType):
        self.ID = self.removePrefix(self.removeCodePrefix(idName.strip()))
        self.type = objectType
        pass

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
