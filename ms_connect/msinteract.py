# This Python file uses the following encoding: utf-8

import os
# import sys
import importlib

import important as imp


class ModuleSystemInteract:
    def __init__(self):
        pass


def importHeader(name, startw=""):
    header_name = "header_" + name
    module = importlib.import_module(header_name)
    vs = imp.moduleVars(module, startw)
    return {"module": module, "vars": vs}


def importModuleIds(path):
    dir = os.listdir(path)
    files = [file for file in dir if file.startswith("ID_")]

    all_ids = []

    for file in files:
        modx = file.rstrip(".py")
        module = importlib.import_module(modx)
        vs = imp.moduleVars(module)
        all_ids.append(vs)

    # importlib.invalidate_caches()

    return all_ids


def importModuleFiles(path):
    dir = os.listdir(path)
    files = [file for file in dir if file.startswith("module_")]

    allx = []
    ally = []

    for file in files:
        modx = file.rstrip(".py")
        module = importlib.import_module(modx)
        vs = imp.moduleVars(module)
        allx.append(vs)
        ally.append(module)

    # importlib.invalidate_caches()

    return [allx, ally]
