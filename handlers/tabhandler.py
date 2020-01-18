import os

def opentab(url: str):
    os.system("osascript switchtab.scpt %s" % (url))

if __name__ == '__main__':
    opentab("https://drive.google.com")