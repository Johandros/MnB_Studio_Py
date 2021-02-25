# This Python file uses the following encoding: utf-8

import os
# import sys

from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

from skriptum import ObjectType as OType
from codereader import TXT_FILES
from codereader import CodeReader


class Studio(QWidget):
    def __init__(self):
        super().__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    def mbstudio_start(self, warband_path):
        # FOR TESTING
        base_path = warband_path + "/Modules/Native/"

        allObjects = []

        codeReader = CodeReader(base_path + TXT_FILES[OType.Script])
        # scripts = codeReader.readScripts()
        # allObjects.append(scripts)

        codeReader = CodeReader(base_path + TXT_FILES[OType.Troop])
        troops = codeReader.readTroops()
        allObjects.append(troops)

        print([troops[52]])

        # print("Scripts: {}".format(len(scripts)))
        print("Troops: {}".format(len(troops)))

        # for x, troop in enumerate(troops):
        #    print("[" + str(x) + "] - " + troop.ID + ": " + troop.Name)

        print(len(allObjects))
        # FOR TESTING
