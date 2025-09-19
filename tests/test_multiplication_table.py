from multiplication_table import multiplication_table
from io import StringIO
import sys

def test_multiplication_table_1_to_5():
    expected_output = """1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
"""
    captured_output = StringIO()
    sys.stdout = captured_output
    multiplication_table(5)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == expected_output

def test_multiplication_table_1_to_3():
    expected_output = """1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
"""
    captured_output = StringIO()
    sys.stdout = captured_output
    multiplication_table(3)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == expected_output

def test_multiplication_table_1_to_10():
    captured_output = StringIO()
    sys.stdout = captured_output
    multiplication_table(10)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    
    assert "1 x 1 = 1" in output
    assert "5 x 5 = 25" in output
    assert "10 x 10 = 100" in output
    assert "2 x 3 = 6" in output
    assert "7 x 8 = 56" in output

def test_multiplication_table_uses_nested_loops():
    captured_output = StringIO()
    sys.stdout = captured_output
    multiplication_table(2)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    
    lines = output.strip().split('\n')
    assert len(lines) == 4

def test_multiplication_table_single_number():
    expected_output = "1 x 1 = 1\n"
    captured_output = StringIO()
    sys.stdout = captured_output
    multiplication_table(1)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == expected_output

def test_multiplication_table_format():
    captured_output = StringIO()
    sys.stdout = captured_output
    multiplication_table(2)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    
    lines = output.strip().split('\n')
    for line in lines:
        assert " x " in line
        assert " = " in line
        parts = line.split(" = ")
        assert len(parts) == 2
        assert parts[1].isdigit()  
