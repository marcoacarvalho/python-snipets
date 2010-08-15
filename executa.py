from subprocess import Popen, PIPE
import shlex

class Exec:
    """
from executa import Exec
e = Exec('cat /etc/passwd')
stdout,stderr = e.execute()
print stdout
print stderr
"""
    def __init__(self,cmd):
        self.cmd = shlex.split(cmd)

    def execute(self):
        p = Popen(self.cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        return (stdout, stderr)
