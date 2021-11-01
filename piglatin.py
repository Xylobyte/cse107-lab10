"""
A program that opens a file and translates it to piglatin. It then writes the translation to a new file.

file: piglatin.py

author: Donovan Griego

Date: 11-01-2021

assignment: Lab 10
"""

import os

def translate(infile, outfile):
    """
    translates infile to piglatin, with respect to punctuation, then writes
    the translation to outfile

    infile: string
    outfile: string
    """
    # Check if files exist
    if not os.path.exists(infile):
        print("Error: File", infile, "does not exist")
        exit(1)
    with open(infile, 'r') as infile, open(outfile, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if line == '':
                outfile.write('\n')
            else:
                words = line.split()
                for word in words:
                    if not word[-1].isalpha():
                        punct = word[-1]
                        word = word[:-1]
                    else:
                        punct = ''
                    if word[0] in 'aeiou':
                        word += 'way'
                    else:
                        vowel_index = 0
                        for i in range(len(word)):
                            if word[i] in 'aeiou':
                                vowel_index = i
                                break
                        word = word[vowel_index:] + word[:vowel_index] + 'ay'
                    word += punct
                    outfile.write(word + ' ')


def main():
    infile = input("Enter English filename >>> ")
    outfile = input("Enter filename to write to >>> ")
    translate(infile, outfile)

if __name__ == '__main__':
    main()