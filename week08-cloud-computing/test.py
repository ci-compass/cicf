import pytest
import subprocess

def test_exercise_1():
    result = subprocess.run("./exercise-1.sh", capture_output=True)

    assert(result.returncode == 0)
    output = result.stdout.decode() # translate from bytes to utf-8
    assert(output == "https://doi.org/10.1016/s2666-5247(24)00016-8")
