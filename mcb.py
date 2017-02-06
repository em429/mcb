#!/usr/local/bin/python3
# mcb.py | saves clipboard text under keywords, or loads a saved clipboard
# state into the current clipboard.

import sys, shelve, pyperclip

shelfFile = shelve.open('mcbData')

print(len(sys.argv))

if len(sys.argv) == 2:
    # mcb list -- list keywords
    if sys.argv[1].lower() == 'list':
        print(str(list(shelfFile.keys())))
    elif sys.argv[1] == '-l' and sys.argv[2] in shelfFile:
        print(shelfFile[sys.argv[2]])
        pyperclip.copy(shelfFile[sys.argv[1]])
    else:
        shelfFile[sys.argv[1]] = pyperclip.paste()

shelfFile.close()
