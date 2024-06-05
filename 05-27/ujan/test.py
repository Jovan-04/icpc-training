import subprocess
import sys

TIME_LIMIT = 5 # seconds

match len(sys.argv):
    case 1:
        solution = 'solution.py'
    case 2:
        solution = sys.argv[1]
    case _:
        raise ValueError('usage: python test.py [file]')

python = sys.executable
with open('in.txt') as in_:
    try:
        result = subprocess.run(
            [python, solution],
            stdin=in_,
            capture_output=True,
            timeout=TIME_LIMIT
        )
    except subprocess.TimeoutExpired:
        sys.exit('Time Limit Exceeded')
    except Exception:
        sys.exit('Judge Error')

if result.returncode != 0:
    sys.exit('Runtime Error')

out = result.stdout.decode().strip()
with open('ans.txt') as f:
    ans = f.read().strip()

if out != ans:
    sys.exit('Wrong Answer')
