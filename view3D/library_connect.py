# This Python file uses the following encoding: utf-8

import sys
# import platform
import ctypes
import ctypes.util

# from PyQt5.QtCore import QPluginLoader


class LibraryConnect:
    def __init__(self):
        pass

    # not working for testing
    # def read_dll_PyQt():
    #     path_lib = "./libopenBrf.so"
    #
    #    pluginLoader = QPluginLoader()
    #    pluginLoader.setFileName(path_lib)
    #    pluginLoader.instance()
    #    # plugin_obj = pluginLoader.instance()

    # not working for testing
    def activateOpenBrf():
        """ Python wrapper for the C shared library mylib"""
        print("testing openBrf usage")

        # Find the library and load it
        # mylib_path = ctypes.util.find_library("libopenBrf")
        mylib_path = ctypes.util.find_library("./libopenBrf")
        # mylib_path = ctypes.util.find_library("./openBrf")
        if not mylib_path:
            print("Unable to find the specified library.")
            sys.exit()

        try:
            mylib = ctypes.CDLL(mylib_path)
        except OSError:
            print("Unable to load the system C library")
            mylib = 0
            sys.exit()

        return mylib
