# This Python file uses the following encoding: utf-8

from skriptum import Skriptum
from skriptum import ObjectType


class MissionTemplate(Skriptum):
    @property
    def Flags(self):
        return self._Flags

    @property
    def FlagsGZ(self):
        return self._FlagsGZ

    @property
    def MissionType(self):
        return self._MissionType

    @property
    def MissionTypeGZ(self):
        return self._MissionTypeGZ

    @property
    def Description(self):
        return self._Description

    @property
    def EntryPoints(self):
        return self._EntryPoints

    @property
    def Triggers(self):
        return self._Triggers

    @property
    def HeaderInfo(self):
        return (self.ID, self.Flags, self.MissionType, self.Description)

    def __init__(self, headerInfo):
        super().__init__(headerInfo[0], ObjectType.MissionTemplate)

        # if headerVariables == null:
        #     headerVariables = GetHeaderVariableList()

        # if missionTypes == null:
        #     missionTypes = GetMissionTypes()

        if headerInfo[1].isnumeric():
            self._FlagsGZ = int(headerInfo[1])  # ulong
            # self._Flags = SetFlags(FlagsGZ, headerVariables)
        else:
            self._Flags = headerInfo[1]
            # self._FlagsGZ = SetFlagsGZ(Flags, headerVariables)

        if headerInfo[2].isnumeric():
            self._MissionTypeGZ = int(headerInfo[2])  # int
            # self._MissionType = SetFlags(FlagsGZ, headerVariables)
        else:
            self._MissionType = headerInfo[2]
            # self._MissionTypeGZ = SetFlagsGZ(Flags, headerVariables)

        self._MissionType = headerInfo[2]  # redundant when if ???
        self._Description = headerInfo[3]

    def AddEntryPoint(self, entryPoint):
        self._EntryPoints.append(entryPoint)

    def AddTrigger(self, trigger):
        self._Triggers.append(trigger)
