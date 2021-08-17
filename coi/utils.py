import subprocess
from pathlib import Path
from string import Template
from argparse import Namespace


def get_template_path(path=None) -> Path:
    """

    """
    coi_path = Path(__file__).parents[0]
    return coi_path / 'templates'


def get_template(name=None) -> Template:
    """

    """
    if name:
        return
    fname = get_template_path() / 'ic-loop.tmpl'
    with open(fname, "r") as f:
        templ = Template(f.read())
    return templ

# val = subprocess.check_call("./script.sh '%s'" % arg, shell=True)
# subprocess.run()

def get_cmd(args: Namespace) -> str:
    """

    """
    # load template string

    templ = get_template()
    return templ.substitute(vars(args))


def run_cmd(cmd: str):
    """

    """
    subprocess.run(cmd, shell=True,)


def get_char():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
