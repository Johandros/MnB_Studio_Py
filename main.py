# This Python file uses the following encoding: utf-8

import sys

from PySide2.QtWidgets import QApplication


# import sub directories
sys.path.append("./gui")
sys.path.append("./io")
sys.path.append("./objects")
sys.path.append("./support")

sys.path.append("./ms_connect")
sys.path.append("./view3D")

sys.path.append("./files/module_system")
sys.path.append("./files/module_data")

# FIXME: PYTHONPATH var seems not to be working?
from studio import Studio

#  @staticmethod¶  # for static methods :P def f(arg1, arg2, ...):

# VARIABLES FOR TESTING
warband_path = "/home/john/.local/share/Steam/steamapps/common/MountBlade Warband"


if __name__ == "__main__":
    app = QApplication([])

    # widget = Studio()
    # widget.show()

    # testobj = read_dll_PyQt()
    # print(testobj)

    # activateOpenBrf()

    studio = Studio()
    # studio.show()

    studio.mbstudio_start(warband_path)

    # sys.exit(app.exec_())
