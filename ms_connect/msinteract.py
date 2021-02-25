# This Python file uses the following encoding: utf-8

import os
import sys
import importlib

import important as imp
# import files.module_system as module_system


class ModuleSystemInteract:
    def __init__(self):
        # module_system.register_all()
        pass

    def importHeader(self, name, startw=""):
        header_name = "header_" + name
        module = importlib.import_module(header_name)
        vs = imp.moduleVars(module, startw)
        return {"module": module, "vars": vs}

    def importModuleIds(self, path):
        dir = os.listdir(path)
        files = [file for file in dir if file.startswith("ID_")]

        all_ids = []

        for file in files:
            modx = file.rstrip(".py")
            module = importlib.import_module(modx)
            # module = importlib.import_module("files.module_system." + modx, modx)
            # module = __import__('files.module_system.' + modx, globals(), locals(), [modx], 0)
            vs = imp.moduleVars(module)
            all_ids.append(vs)

        # importlib.invalidate_caches()

        return all_ids

    def importModuleFiles(self, path):
        dir = os.listdir(path)
        files = [file for file in dir if file.startswith("module_") and not file.endswith(".bak")]

        # sys.path.append(path)

        # path = os.path.realpath(path)
        # scriptpath = sys.path[0]
        # os.chdir(path)

        # print(path)
        # print(scriptpath)

        allx = []
        ally = []

        for file in files:
            modx = file.rstrip(".py")
            # module = importlib.import_module("files.module_system." + modx, modx)
            module = importlib.import_module(modx)
            # module = __import__('files.module_system.' + modx, globals(), locals(), [modx], 0)
            vs = imp.moduleVars(module)
            allx.append(vs)
            ally.append(module)

        # importlib.invalidate_caches()

        # os.chdir(scriptpath)

        return [allx, ally]
