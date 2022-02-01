# Hypermnesia

Hypermnesia is a lightweight, smart flashcards app written in Python!


## Setup & Features
No dependencies required yet! Hypermnesia is current CLI-only and everything is done using the Python standard library.
```py
git clone https://github.com/ThatNerdSquared/hypermnesia.git
cd hypermnesia
python3 cli.py -h
```

- Hypermnesia creates decks (`.hypermnesia.json` files ) from `.csv` files. Pass one in using the `-c` flag.
- Run a practice session using the `-r` flag.
- Scramble the deck in a practice session using the `-s` flag.

## Future Plans
- [x] Allow partial/full reversal of cards (some/all answers become questions)
- [ ] Add information about success/failure rate per card into deck file
- [ ] Add smarter reshuffling based on success/failure rate
- [ ] PyInstaller packages and ability to install from `brew`, etc
- [ ] Add deck stats
- [ ] Add basic GUI
- [ ] Add deck stats graphs in GUI

If you enjoy using Hypermnesia and/or want to support further development, feel free to donate below!

<a href="https://www.buymeacoffee.com/nathanyeung" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
