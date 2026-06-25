# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The game initially seemed to have its hints backwards, saying "Go Higher" when it should be saying "Go Lower" and vice versa. I also noticed that it was not possible to start a new game without fully reloading the page. The attempts counter in the debug info and the actual number of previous guesses recorded are off by 1 as it seems like the previous guess is only recorded once one guess after it is submitted not when that previous guess itself is submitted. In that same vein, the guess counter gives you one more guess than indicated.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 60 | "Go Lower" |"Go Higher"| None |
| 12 | "Go Higher"| "Go Lower" | None |
| New Game | New game started | New secret was generated but new guesses were not allowed | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Code for this project. Most of the AI suggestions were right like the AI fix for the str formatting on even numbered guesses that prevented a user from winning on those guesses. Since this app had an interactive interface it was easy to simply play the game to verify that fixes worked and in this case, verifying that I could win on any guess. AI was slightly misleading when I was trying to fix the lagging history and attempt numbers. It initally "fixed it" but the entire UI changed. After some prompting Claude was able to fix it but it took some trial and error.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided that a bug was fixed when I could visually verify that the expected behavior was occuring by playing the game. For example, in the "Go Higher" mismatch, I knew that the bug was fixed when I guessed a number that should say "Go Higher" and the hint output was correct. I understood the test structure on my own, AI only really helped write the tests.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit essentially "reruns" your entire code top to bottom, meaning that global variables in the traditional sense are reset which means that you must save them in Streamlit's session state, which acts like a typical global variable.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I think that verifying AI output is something that I want to continue forward. Making sure that I understand code output from AI is vital for me and I did it all throughout this project. I think next time I work with AI I will clearly set rules at the beginning of a session. I think my perception of AI generated code remained mostly the same, but it reinforced the idea that AI can be very useful as long as I remain in control
