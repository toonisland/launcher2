import subprocess
import os
import unicodedata
from string import *

from launcher_globals import *



class GameStarter():

    def __init__(self):
        pass
    
    def launchGame(self):
        # This still needs work but I guess this is slightly better
        cookie = str((self.uiCallback.uName + self.uiCallback.pWord))
        GAME_SERVER = "73.126.179.188"
        ### Game starting commands ###
        TIA_PLAYCOOKIE = self.uiCallback.uName + self.uiCallback.pWord
        if platform.system() == 'Windows':               
            cmd_00 = 'SET TIA_PLAYCOOKIE=' + TIA_PLAYCOOKIE + ' && set TIA_GAMESERVER=' + GAME_SERVER + ' && TIAEngine.exe'
        if platform.system() == 'Linux' or platform.system() == 'Darwin':
            cmd_00 = 'export TIA_PLAYCOOKIE=' + TIA_PLAYCOOKIE + ' && export TIA_GAMESERVER=' + GAME_SERVER + ' && chmod +x TIAEngine && ./TIAEngine'
        # Before we run the command lets set the username variables to null
        self.uiCallback.uName = False
        self.uiCallback.pWord = False
        cookie = False

        subprocess.call(cmd_00, shell=True)

        return



