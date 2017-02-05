#!/usr/local/bin/python3
# mcb.py | saves clipboard text under keywords, or loads a saved clipboard
# state into the current clipboard.

# Usage:
# mv mcb.py /usr/local/bin/mcb
# mcb save <keyword> - Saves clipboard contents to keyword.
# mcb <keyword> - Loads keyword to clipboard.
# mcb list - Prints all saved keywords.

import sys, shelve, pyperclip

shelfFile = shelve.open('mcbData')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    shelfFile[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        print(str(list(shelfFile.keys())))
    elif sys.argv[1] in shelfFile:
        pyperclip.copy(shelfFile[sys.argv[1]])
    else:
        print('Can\'t find requested keyword..')

shelfFile.close()
