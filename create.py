import os
import subprocess

cmd = 'git diff --name-only ' + os.environ['TRAVIS_COMMIT_RANGE']

out = subprocess.check_output(cmd.split()).decode('utf-8')
print(out)
