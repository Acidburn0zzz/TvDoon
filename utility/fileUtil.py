import os
from os.path import expanduser

# Global Section Variables
PATH = expanduser("~") + "/.config/tvdoon/"

def checkConfExist():
    # create conf directory
    if not os.path.exists(PATH):
        os.makedirs(PATH)

    # create favourite.conf file
    try:
        favFile = open(PATH + "favourites.conf", "r")
    except (OSError, IOError) as e:
        open(PATH + "favourites.conf", "a").close()

    return