from guessing_game import guessing_game
from io import StringIO
import sys

def test_guessing_game_correct_guess():
    sys.stdin = StringIO("15\n")
    result = guessing_game()
    assert result == "Congratulations! You guessed it!"

def test_guessing_game_multiple_guesses():
    sys.stdin = StringIO("5\n10\n20\n15\n")
    result = guessing_game()
    assert result == "Congratulations! You guessed it!"

def test_guessing_game_high_low_hints():
    sys.stdin = StringIO("20\n10\n15\n")
    result = guessing_game()
    assert result == "Congratulations! You guessed it!"

def test_guessing_game_negative_number():
    sys.stdin = StringIO("-5\n15\n")
    result = guessing_game()
    assert result == "Congratulations! You guessed it!"

def test_guessing_game_zero():
    sys.stdin = StringIO("0\n15\n")
    result = guessing_game()
    assert result == "Congratulations! You guessed it!"

def test_guessing_game_large_number():
    sys.stdin = StringIO("100\n15\n")
    result = guessing_game()
    assert result == "Congratulations! You guessed it!"

def test_guessing_game_uses_while_loop():
    sys.stdin = StringIO("1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n")
    result = guessing_game()
    assert result == "Congratulations! You guessed it!"

def test_guessing_game_target_is_15():
    sys.stdin = StringIO("15\n")
    result = guessing_game()
    assert result == "Congratulations! You guessed it!"
