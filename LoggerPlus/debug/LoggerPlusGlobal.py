import shutil
import LoggerPlus

from panda3d.core import loadPrcFile, ConfigPageManager
from otp.ai.MagicWordGlobal import *

logger = LoggerPlus.LoggerPlus()

CONFIG_MGR = ConfigPageManager.getGlobalPtr()
# Set primary config file (default is first explicitly loaded):
CONFIG_FILE = None

@magicWord(category=CATEGORY_ADMINISTRATOR, types=[str, str])
def config(var, val):
    """
    Make config variables configurable in-game.

    Args:
        var (str): the config variable's name.
        val (str): the config variable's value.

    Examples:
        ~config want-game-tables t (enables tables)
        ~config want-game-tables f (disables tables)
    """
    if CONFIG_FILE:
        fileSrc = CONFIG_FILE
    else:
        pageIndex = CONFIG_MGR.getNumExplicitPages() - 1
        fileSrc = CONFIG_MGR.getExplicitPage(pageIndex).getName()
    found = False
    hash = "#" if len(val) == 1 and not val.isdigit() else ""
    val = " {0}{1}\r\n".format(hash, val)

    newConfig = var + val
    shutil.move(fileSrc, fileSrc + "~")
    destination = open(fileSrc, "w")
    source = open(fileSrc + "~", "r")

    for line in source:
        lenLine = 0
        lineParts = line.split()
        if len(lineParts) > 1:
            lenLine = len(lineParts[0])
        if lenLine and var in line and len(var) == lenLine:
            destination.write(newConfig)
            found = True
        else:
            destination.write(line)

    source.close()
    destination.close()

    if not found:
        with open(fileSrc, "a") as f:
            f.write("\n" + newConfig)

    loadPrcFile(fileSrc)
    messenger.send(var + " updated")
    return
