import pytest
import subprocess

def test_exercise_1():
    result = subprocess.run(["./exercise-1.py", "numbers.txt", "5"], capture_output=True)

    assert(result.returncode == 0)
    output = result.stdout.decode() # translate from bytes to utf-8
    assert(float(output) == 498)
