# This Python file uses the following encoding: utf-8

# import os


def isNumeric(x):
    # yes, eric is numb :/
    numberic = False

    if type(x) == int or type(x) == float:
        numberic = True  # even python agrees

    # good that I am not eric, otherwise I would be returned... :P
    return numberic


def allVarNamesByNS(namespace):
    # exclude private or system variable e.g. __loader__
    return [name for name in namespace if not name.startswith("__")]


def allVarNamesByNSSpec(namespace, startw):
    # exclude private or system variable e.g. __loader__
    return [name for name in namespace if name.startswith(startw)]


def moduleVars(module, startw=""):
    allVars = vars(module)
    if startw == "":
        return allVarNamesByNS(allVars)
    else:
        return allVarNamesByNSSpec(allVars, startw)
