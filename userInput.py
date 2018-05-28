# chordFrequencyMapper/userInput.py

# this script handles user input and output

import getNoteInfo

CRED = '\033[91m'
CEND = '\033[0m'

def chord():
    try:
        type = input('Select chord type [major], [minor]: ')

        if type == 'major':
            try:
                root = input('Select root note e.g [A4], or [Db3], use flats only: ')

                print('Generating major chord...')
                print(CRED)
                getNoteInfo.chordMajor(root)
                print(CEND)

            except:
                print(CEND + 'Bad input, try typing a note like A4 or Ab4')

        elif type == 'minor':
            try:
                root = input('Select root note e.g [A4], or [Db3], use flats only: ')

                print('Generating minor chord...')
                print(CRED)
                getNoteInfo.chordMinor(root)
                print(CEND)

            except:
                print(CEND + 'Bad input, try typing a note like [A4] or [Ab4]')

    except:
        print(CEND + 'Error, bad input. Try: [major], [minor] or [exit]')

def note():
    try:
        root = input('Select root note e.g [A4] or [Db3]: ')
        print(CRED)
        getNoteInfo.displayNote(root)
        print(CEND)
    except:
        print(CEND + 'Bad input, try typing a note like [A4] or [Ab4]')

def inputLoop():
    print('Chord Frequency Mapper by Aidan Taylor\n')
    print('Type [exit] or press ctrl-c at any time to quit\n')

    while True:
        uIn = input('Do you want to know about a [note] or [chord]?: ')

        try:
            if uIn == 'chord':
                chord()
            elif uIn == 'note':
                note()
            elif uIn == 'exit' or uIn == 'quit':
                print('Goodbye!')
                break
        except:
            print('Bad input. Try: [note], [chord] or [exit]')
