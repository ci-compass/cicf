import pytest
import subprocess
import glob
import re

def test_exercise_1():
    goal = glob.glob('e*')
    result = subprocess.run("./exercise-1.sh", capture_output=True)

    assert(result.returncode == 0)
    output = result.stdout.decode() # translate from bytes to utf-8
    assert(output.splitlines() == goal)

def test_exercise_2():
    result = subprocess.run("./exercise-2.sh")

    assert(result.returncode == 0)

    with open("source.txt","r") as f:
        source_list = [int(x) for x in f.readlines()]
    with open("sorted.txt", "r") as f:
        sorted_list = [int(x) for x in f.readlines()]

    actual_sorted = sorted(source_list)

	# make sure the starting file is not sorted
    assert(source_list != sorted_list)

    # is the sorted list correct?
    assert(sorted_list == actual_sorted)

def test_exercise_3():
    goal = 1
    try:
        with open("iris.csv", "r") as f:
            goal = len(re.findall("virginica", f.read()))
    except:
        pass

    result = subprocess.run("./exercise-3.sh", capture_output=True)

    assert(result.returncode == 0)
    output = result.stdout.decode() # translate from bytes to utf-8
    assert(int(output.splitlines()[0]) == goal)

