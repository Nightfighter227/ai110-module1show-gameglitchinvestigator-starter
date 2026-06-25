from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win.
    # check_guess returns (outcome, message), so compare the outcome.
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_too_high_always_deducts_points():
    # Regression test for the "Too High" scoring glitch: the buggy version did
    # `if attempt_number % 2 == 0: return current_score + 5`, so a too-high guess
    # ADDED points on even-numbered attempts instead of deducting. A wrong (too
    # high) guess must always cost 5 points, regardless of attempt parity.
    assert update_score(100, "Too High", 2) == 95   # even attempt (where the bug lived)
    assert update_score(100, "Too High", 4) == 95   # another even attempt
    assert update_score(100, "Too High", 1) == 95   # odd attempt, for symmetry
