import string
import sys
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def getDictionary(filename):
    dict = []
    with open(filename, encoding='latin-1') as file:
        for line in file:
            # The rstrip method gets rid of the "\n" at the end of each line
            dict.append(line.rstrip().lower())
    return dict

def decode(coded_string, dictionary):
    alphabet = string.ascii_lowercase * 2
    substitutions = {}

    for shift in range(1, 26):
        possibility = ''.join([alphabet[alphabet.index(x) + shift] if x in alphabet else x for x in coded_string])
        substitutions[possibility] = 0
    
    no_match = True # used later to check if any possibility is real

    for substitution in substitutions:
        for str in substitution.split(' '): # test if each word of substitution exists
            for word in dictionary:
                if str == word:
                    substitutions[substitution] += 1 # if word exists we upgrade probability
                    no_match = False
    
    if no_match:
        print('\nSorry, but none of the possibilities were real. Either you didn\'t pick the proper langauage, or your doesn\'t mean anything.')
    else:
        sorted_substitutions = sorted([(value, key) for (key, value) in substitutions.items()], reverse=True)
        print(f'\nThe highest probability stands for "{sorted_substitutions[0][1]}"')

# Input handling
if len(sys.argv) <= 1:
    print('\nYou must provide a string to uncipher.')
elif len(sys.argv) > 2 and sys.argv[1] == '--dict':
    try:
        dic_file_path = os.path.join(THIS_FOLDER, sys.argv[2])
        dictionary = getDictionary(dic_file_path)
        decode(sys.argv[3].lower(), dictionary)
    except:
        print('\nSorry, this file does not exist.')
elif len(sys.argv) == 2:
    dic_file_path = os.path.join(THIS_FOLDER, 'en.txt')
    dictionary = getDictionary(dic_file_path)
    decode(sys.argv[1].lower(), dictionary)


