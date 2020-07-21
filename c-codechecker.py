import os
import subprocess
import sys

for c_file in sys.argv[1:]:
    subprocess.run(['cc', c_file], check=True)

os.remove('a.out')
