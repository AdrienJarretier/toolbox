import urllib.request
import shutil
from pathlib import Path
import time


# returns the time singe last modification of "file_name" in seconds
def getLocalFileAge_s(file_name):
    p = Path(file_name)
    mtime = p.stat().st_mtime
    # time.ctime(mtime)
    return time.time() - mtime


def downloadAndSaveToFile(file_name):
    with urllib.request.urlopen('https://donnees.roulez-eco.fr/opendata/instantane') as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


# return bool, True if new file downloaded, False otherwise
def downloadIfLocalTooOld(file_name):

    AGE_THRESHOLD_S = 3600
    fileAge = getLocalFileAge_s(file_name)

    if fileAge > AGE_THRESHOLD_S:
        print("File is older than " + str(AGE_THRESHOLD_S) +
              " s ("+str(int(fileAge))+"), downloading fresh one")
        downloadAndSaveToFile(file_name)
        return True
    else:
        print("File is only " + str(int(fileAge)) + " s old, keeping it")
        return False
