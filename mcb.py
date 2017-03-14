#!/usr/bin/env python3
# mcb.py | saves clipboard text under keywords, or loads a saved clipboard
# state into the current clipboard.

import sys, shelve, pyperclip

shelfFile = shelve.open('mcbData')

if len(sys.argv) == 2:
    # mcb list -- list keywords
    if sys.argv[1] == '--list' or sys.argv[1] == '-l':
        print(str(list(shelfFile.keys())))
    elif sys.argv[1] in shelfFile:
        print(shelfFile[sys.argv[1]])
        pyperclip.copy(shelfFile[sys.argv[1]])
    else:
        print('Keyword not found')

if len(sys.argv) == 3:
    if sys.argv[1] == '--save' or sys.argv[1] == '-s':
        shelfFile[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1] == '--delete' and sys.argv[2] == '--all' or '-a':
        shelfFile.clear()
    elif sys.argv[1] == '--delete' or sys.argv[1] == '-d' and sys.argv[2] in list(shelfFile.keys()):
        del shelfFile[sys.argv[2]]

shelfFile.close()
