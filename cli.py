import argparse
import csv
import json
import os
import random

parser = argparse.ArgumentParser(description='Create or practice a Hypermnesia flashcard deck.')
parser.add_argument(
    '-c',
    '--create-deck',
    type=argparse.FileType('r'),
    help='Creates a Hypermnesia deck from a .csv file.',
)
parser.add_argument(
    '-r',
    '--run-deck',
    type=argparse.FileType('r'),
    help='Runs a practice session from a .hypermnesia.json file.',
)
parser.add_argument(
    '-s',
    '--scramble-deck',
    action='store_true',
    help='Scrambles the order of a deck before practicing.',
)

args = parser.parse_args()
if args.create_deck:
    reader = csv.reader(args.create_deck)
    new_deck = []

    for row in reader:
        new_deck.append({str(row[0]): row[1]})

    path = args.create_deck.name[:-4] + ".hypermnesia.json"
    with open(path, "w", encoding="UTF-8") as f:
        json.dump(new_deck, f)

    print(f'Deck "{path}" created!')
elif args.run_deck:
    with open(args.run_deck.name, "r", encoding="UTF-8") as f:
        deck = json.load(f)

    if args.scramble_deck: random.shuffle(deck)

    for idx, card in enumerate(deck):
        os.system('clear')
        front = list(card.keys())[0]
        user_input = ''
        try:
            user_input = input(front + ': ')
        except KeyboardInterrupt:
            print('\nSee you soon! 👋')
            exit()
        if user_input == deck[idx][front]:
            input('☑️  Correct!')
        else:
            input(f'❌ Incorrect. The correct answer is: "{deck[idx][front]}"')
            insert_point = random.randint(idx+1, len(deck)+1)
            deck.insert(insert_point, card)

    print(f'Practice session finished! You have mastered {args.run_deck.name[:-17]} 🎉')
