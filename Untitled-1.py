def contains_char(secret_word: str, guess_character: str) -> bool:
    """seachers for a char through the entire string."""
    assert len(guess_character) == 1
    count: int = 0
