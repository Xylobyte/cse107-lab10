"""
A program that opens a file and generates a markov chain from it. It then generates a sentence from the chain.

file: markov.py

author: Donovan Griego

Date: 11-01-2021

assignment: Lab 10
"""
import os
import random

def generate_markov_chain(file):
    """
    Generates and returns a markov chain from a file.

    file: the file to generate the chain from
    """
    chain = {}
    starts = []
    with open(file, 'r') as f:
        for line in f:
            words = line.split()
            if len(words) > 1:
                starts.append(words[0])
            for i in range(len(words) - 1):
                if words[i] not in chain:
                    chain[words[i]] = [words[i + 1]]
                else:
                    chain[words[i]].append(words[i + 1])
    return (chain, starts)

def generate_markov_sentence(chain, starts):
    """
    Generates and returns a markov chain sentence.

    chain: the markov chain to generate the sentence from
    starts: the list of words that can start a sentence
    """
    sentence = []
    sentence.append(random.choice(starts))
    while sentence[-1][-1] != '.' and sentence[-1][-1] != '?' and sentence[-1][-1] != '!' and len(sentence) <= 100:
        try :
            sentence.append(random.choice(chain[sentence[-1]]))
        except KeyError:
            break
    return ' '.join(sentence)

def main():
    # Get the filename from the user and make sure it exists
    file = input('Enter a filename: ')
    if not os.path.isfile(file):
        print('File does not exist')
        exit(1)
    chain = generate_markov_chain(file)
    print("Generated sentence:\n" + generate_markov_sentence(chain[0], chain[1]))



if __name__ == '__main__':
    main()