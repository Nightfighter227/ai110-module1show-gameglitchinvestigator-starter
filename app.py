import random
import streamlit as st

# FIX: Refactored game logic out of app.py into logic_utils.py and imported it
# here, using Claude Code in agent mode (I asked for the move; it edited both files).
from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

# FIX: Reordered attempt limits so they decrease with difficulty (Normal used to
# get more attempts than Easy). Found and corrected with Claude Code in agent mode.
attempt_limit_map = {
    "Easy": 10,
    "Normal": 7,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    # FIX: I fixed this myself — attempts must start at 0 (was 1, which threw the
    # attempt count and "attempts left" off by one from the first guess).
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Make a guess")

# FIX: The history/attempts display lagged one guess behind because it rendered
# before the guess was processed. Claude (agent mode) reworked this into st.empty()
# placeholders reserved here and filled below, so the view always shows current state.
info_placeholder = st.empty()
debug_placeholder = st.empty()

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    # FIX: New Game now resets the FULL game state, with Claude Code in agent mode.
    # Previously it only reset attempts + secret, leaving status="won"/"lost" (and
    # stale score/history), so after a finished game the button did nothing — the
    # game-over branch below kept firing. The secret also now uses the difficulty's
    # range (was hardcoded 1-100).
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.status = "playing"
    st.session_state.score = 0
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
# FIX: Changed st.stop() to elif so execution still reaches the placeholder-fill
# below on the game-over screen. Done with Claude Code in agent mode.
elif submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)

        # FIX: Removed the every-other-turn `str(secret)` cast that broke
        # comparisons (a correct guess couldn't win on even attempts). Claude
        # (agent mode) now always compares against the real int secret.
        secret = st.session_state.secret

        outcome, message = check_guess(guess_int, secret)

        if show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

# FIX: Fill the reserved slots now that state is current. The range text also uses
# {low}/{high} (was hardcoded "1 and 100"). Reworked with Claude Code in agent mode.
info_placeholder.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)
with debug_placeholder.container():
    with st.expander("Developer Debug Info"):
        st.write("Secret:", st.session_state.secret)
        st.write("Attempts:", st.session_state.attempts)
        st.write("Score:", st.session_state.score)
        st.write("Difficulty:", difficulty)
        st.write("History:", st.session_state.history)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
