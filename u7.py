# All code copied from the answers to these two StackExchange questions:
# https://askubuntu.com/questions/555055/how-to-make-autokey-type-unicode-characters
# https://stackoverflow.com/questions/43860227/python-getting-and-setting-clipboard-data-with-subprocesses

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from subprocess import Popen, PIPE

# TODO: Make it save the keyboard contents and put it back after it sends the character

def getClipboardData():
    p = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

def setClipboardData(data):
    p = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()

def paste_character(symbol):
    c = Popen(['xclip', '-selection', 'clipboard'], stdin=PIPE) # (Copied code)
    data = getClipboardData() # Get initial clipboard data

    c.communicate(symbol.encode('utf-8')) # (Copied code)
    keyboard.send_keys('<ctrl>+v') # (Copied code)
    time.sleep(10)

    setClipboardData(data) # Replace clipboard data

# The generator script should add one or more calls to paste_character() here:
paste_character('ũ')