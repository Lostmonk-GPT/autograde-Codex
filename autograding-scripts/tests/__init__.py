import sys
from pathlib import Path

src = Path(__file__).resolve().parents[1] / 'src'
if str(src) not in sys.path:
    sys.path.insert(0, str(src))
