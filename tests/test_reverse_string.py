from reverse_string import reverse_string

def test_reverse_string_simple():
    """Test reversing a simple string"""
    assert reverse_string("hello") == "olleh"

def test_reverse_string_single_character():
    """Test reversing a single character"""
    assert reverse_string("a") == "a"

def test_reverse_string_empty():
    """Test reversing an empty string"""
    assert reverse_string("") == ""

def test_reverse_string_palindrome():
    """Test reversing a palindrome"""
    assert reverse_string("racecar") == "racecar"

def test_reverse_string_numbers():
    """Test reversing a string with numbers"""
    assert reverse_string("12345") == "54321"

def test_reverse_string_mixed():
    """Test reversing a mixed string"""
    assert reverse_string("a1b2c3") == "3c2b1a"

def test_reverse_string_spaces():
    """Test reversing a string with spaces"""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_special_characters():
    """Test reversing a string with special characters"""
    assert reverse_string("!@#$%") == "%$#@!"

def test_reverse_string_long():
    """Test reversing a longer string"""
    original = "abcdefghijklmnopqrstuvwxyz"
    expected = "zyxwvutsrqponmlkjihgfedcba"
    assert reverse_string(original) == expected

def test_reverse_string_uses_loop():
    """Test that function uses loop (indirect test by checking it works)"""
    test_cases = ["abc", "123", "hello", "test", "python"]
    for test_case in test_cases:
        result = reverse_string(test_case)
        assert len(result) == len(test_case)
        assert result == test_case[::-1]  
