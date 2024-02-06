# clipboard.py is a program that allows the user
# to have multiple items on the clipboard at once

import sys
import pyperclip

text = {'agree' : "Yes I agree", 
        'busy' : "I am busy", 
        'upsell' : "Buy again"}

if len(sys.argv) < 2:
    print("Usage: python clipboard.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]      # This takes the first command line argument
if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard")
else:
    print(f"There is no text for {keyphrase}")