import subprocess
import sys
import re

def grade_assignments():
    try:
        result = subprocess.run(["pytest", "-q", "test/test_exercise_sheet0.py"], capture_output=True, text=True, check=True)
        passed_tests = len(re.findall(r"\.+", result.stdout))
        return passed_tests
    except subprocess.CalledProcessError as e:
        passed_tests = len(re.findall(r"\.+", e.output))
        return passed_tests

if __name__ == "__main__":
    grade = grade_assignments()
    print(f"Grade: {grade}")
    sys.exit(0)
