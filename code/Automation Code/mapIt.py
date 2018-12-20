#! python3
# mapIt.py = Launches a map in the browser using an address from the
# command line or clipboard

import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address fom clipboard
    address = pyperclip.paste()
    
webbrowser.open('https://www.google.com/maps/place/' + address)
    
    