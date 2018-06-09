# chordFrequencyMapper/userInput.py

'''
this module handles user input and output
'''

import displayfromcsv

def chord():
    try:
        type = input('Select chord type [major], [minor]: ')

        if type == 'major':
            try:
                root = input('Select root note e.g [A4], or [Db3], use flats only: ')

                print('Generating major chord...\n')
                displayfromcsv.chord_major(root)
                print()

            except:
                print('Bad input, try typing a note like A4 or Ab4')

        elif type == 'minor':
            try:
                root = input('Select root note e.g [A4], or [Db3], use flats only: ')

                print('Generating minor chord...\n')
                displayfromcsv.chord_minor(root)
                print()

            except:
                print('Bad input, try typing a note like [A4] or [Ab4]')

    except:
        print('Error, bad input. Try: [major], [minor] or [exit]')

def note():
    try:
        root = input('Select root note e.g [A4] or [Db3]: ')
        print()
        displayfromcsv.display_note(root)

    except:
        print('Bad input, try typing a note like [A4] or [Ab4]')

def input_loop():
    print('Chord Frequency Mapper by Aidan Taylor\n')
    print('Type [exit] or press ctrl-c at any time to quit\n')

    while True:
        uin = input('Do you want to know about a [note] or [chord]?: ')

        try:
            if uin == 'chord':
                chord()
            elif uin == 'note':
                note()
            elif uin == 'exit' or uin == 'quit':
                print('Goodbye!')
                break
        except:
            print('Bad input. Try: [note], [chord] or [exit]')
