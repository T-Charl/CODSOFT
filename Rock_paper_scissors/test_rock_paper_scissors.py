import pytest

from rock_paper_scissors import determine_winner


def test_user_win_outcomes():
    assert determine_winner("rock", "scissors") == "user"
    assert determine_winner("paper", "rock") == "user"
    assert determine_winner("scissors", "paper") == "user"


def test_user_lose_outcomes():
    assert determine_winner("rock", "paper") == "comp"
    assert determine_winner("paper", "scissors") == "comp"
    assert determine_winner("scissors", "rock") == "comp"


def test_draw_outcome():
    assert determine_winner("rock", "rock") == "both"
    assert determine_winner("paper", "paper") == "both"
    assert determine_winner("scissors", "scissors") == "both"
