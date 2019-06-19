import sys
import subprocess
from lib import unimpl

port = "22"

class ImpureDev:
    def  readTargets(self):
        print "== do readTargets"
        return ["dev1", "dev2"]
    def do_ssh(self, host, command):
        print "== do ssh"
        print host
        print command

class ImpureProd:
    def  readTargets(self):
        with open("./ssh_targets") as f:
          ret = f.readlines()
        return ret
    def do_ssh(self, host, command):
        sshcom = "ssh -p "+port+" "+host+" "+command
        subprocess.call([sshcom], shell=True)

def run(impl, command):
    ts = impl.readTargets()
    map(lambda a: impl.do_ssh(a, command), ts)

if __name__ == "__main__":
    ags = sys.argv
    if len(ags) == 2:
        impl = ImpureProd()
        run(impl, ags[1])
    else:
        print "needs one args"
