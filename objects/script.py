# This Python file uses the following encoding: utf-8

from skriptum import Skriptum
from skriptum import ObjectType


class Script(Skriptum):
    Code = []

    def __init__(self, raw_data):
        super().__init__(raw_data[0], ObjectType.Script)

        for i in range(1, len(raw_data) - 1):
            self.Code.append(raw_data[i])
        pass
