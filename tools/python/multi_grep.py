import sys
import multi_ssh

def run(sshmod, grep_args):
    com = "grep "+grep_args
    multi_ssh.run(sshmod, com)

if __name__ == "__main__":
    ags = sys.argv
    if len(ags) == 2:
        sshmod = multi_ssh.ImpureProd()
        run(sshmod, ags[1])
    else:
        print "needs one args"
