# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

## Demo Walkthrough


- [X] Describe the game's purpose. :\
It's a number-guessing game built with Streamlit. The app picks a secret number within a range that depends on the chosen difficulty (Easy 1–20, Normal 1–100, Hard 1–200), and the player tries to guess it within a limited number of attempts. After each guess the game tells you whether to go higher or lower, tracks your score and guess history, and ends when you either guess correctly or run out of attempts. A "Developer Debug Info" panel reveals the secret and internal state for testing.

- [X] Detail which bugs you found. :\
There were many bugs in the code the most obvious being that the hint system was backwards (saying "Go Lower" when the opposite was true). The attempt counter was also not working properly and the history in the debug menu was suffering for the same reason. The "New Game" button was also not working properly making it impossible to start a new game without fully reloading the page.
- [X] Explain what fixes you applied. :\
I worked through the bugs one at a time, mostly using Claude Code in agent mode:
- **Backwards hints:** corrected the "Go LOWER / Go HIGHER" messages in `check_guess` so the direction matches whether the guess was too high or too low.
- **The "commitment issues" secret:** removed the code that cast the secret to a string on every other attempt, which had broken comparisons so a correct guess couldn't even register as a win. The secret now stays a stable int.
- **Attempt counter:** changed the starting attempt count from `1` to `0` so the count and the "attempts left" display are accurate from the very first guess.
- **Lagging debug info:** the history/attempts panel rendered *before* a guess was processed, so it always showed last turn's state. I reworked it to use `st.empty()` placeholders that are filled *after* the guess is handled, so it's always current (and kept it in its original spot on the page).
- **Difficulty mismatches:** Hard now has the widest range (1–200, was narrower than Normal), attempt limits decrease with difficulty (Easy 10 → Normal 7 → Hard 5), the range text and the new-game secret both respect the selected difficulty, and the prompt no longer hardcodes "1 and 100".
- **Scoring glitches:** a "Too High" guess used to *add* points on even attempts — it now always deducts 5, and the win-bonus off-by-one was fixed so fast wins are rewarded correctly.
- **New Game button:** it only reset attempts + secret, leaving `status` as won/lost, so after a finished game it did nothing. It now resets the full state (status, score, and history too).
- **Refactor & tests:** moved all game logic into `logic_utils.py`, fixed the existing tests (they compared against the wrong return shape), added a `conftest.py` so `pytest` finds the module, and added a regression test for the "Too High" scoring bug.


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 12
2. Game returns "Too Low"
3. User enters a guess of 38 → "Too High"
4. Score updates correctly after each guess
5. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ pytest tests/
============================= test session starts =============================
platform win32 -- Python 3.13.14, pytest-9.1.0, pluggy-1.6.0
rootdir: ...\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 4 items

tests\test_game_logic.py ....                                            [100%]

============================== 4 passed in 0.02s =============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
