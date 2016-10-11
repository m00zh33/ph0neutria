#!/usr/bin/python
from ConfigParser import SafeConfigParser
import os

class baseObj:
    def __init__(self, multiProcess, userAgent, outputFolderName, outputFolder, deleteOutput, dateFormat, malShareApi, malShareApiKey, disableMalShare, malShareRemoteOnly, malShareRemoteFirst, malc0deUrl, vxVaultUrl, viperUrlAdd, viperUrlFind):
        self.multiProcess = multiProcess
        self.userAgent = userAgent
        self.outputFolderName = outputFolderName
        self.outputFolder = outputFolder
        self.deleteOutput = deleteOutput
        self.dateFormat = dateFormat
        self.malShareApi = malShareApi
        self.malShareApiKey = malShareApiKey
        self.disableMalShare = disableMalShare
        self.malShareRemoteOnly = malShareRemoteOnly
        self.malShareRemoteFirst = malShareRemoteFirst
        self.malc0deUrl = malc0deUrl
        self.vxVaultUrl = vxVaultUrl
        self.viperUrlAdd = viperUrlAdd
        self.viperUrlFind = viperUrlFind

def getBaseConfig(rootDir):
    parser = SafeConfigParser()
    parser.read(os.path.join(rootDir, 'config', 'settings.conf'))

    multiProcess = parser.get("Core", "multiprocess")
    userAgent = parser.get("Core", "useragent")
    outputFolderName = parser.get("Core", "outputfolder")
    outputFolder = os.path.join(rootDir, outputFolderName)
    deleteOutput = parser.get("Core", "deleteoutput")
    dateFormat = parser.get("Core", "dateformat")
    malShareApi = parser.get("MalShare", "apiurl")
    malShareApiKey = parser.get("MalShare", "apikey")
    disableMalShare = parser.get("MalShare", "disable")
    malShareRemoteOnly = parser.get("MalShare", "remoteonly")
    malShareRemoteFirst = parser.get("MalShare", "remotefirst")
    malc0deUrl = parser.get("Malc0de", "url")
    vxVaultUrl = parser.get("VXVault", "url")
    viperUrlAdd = parser.get("Viper", "addurl")
    viperUrlFind = parser.get("Viper", "findurl")
    return baseObj(multiProcess, userAgent, outputFolderName, outputFolder, deleteOutput, dateFormat, malShareApi, malShareApiKey, disableMalShare, malShareRemoteOnly, malShareRemoteFirst, malc0deUrl, vxVaultUrl, viperUrlAdd, viperUrlFind)

