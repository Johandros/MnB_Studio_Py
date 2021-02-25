# This Python file uses the following encoding: utf-8


class HeaderVariable:
    @property
    def VariableName(self):
        return self._VariableName

    @property
    def VariableValue(self):
        return self._VariableValue

    def __init__(self, val, name):
        self._VariableValue = val
        self._VariableName = name
        pass
