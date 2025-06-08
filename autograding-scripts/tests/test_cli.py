from subprocess import run, PIPE
import sys
from pathlib import Path


def test_cli_help():
    env = dict(PYTHONPATH=str(Path(__file__).resolve().parents[1] / 'src'))
    proc = run([sys.executable, '-m', 'autograding_scripts.main', '-h'], stdout=PIPE, stderr=PIPE, text=True, env={**env, **dict()})
    assert proc.returncode == 0
    assert 'usage' in proc.stdout.lower()
