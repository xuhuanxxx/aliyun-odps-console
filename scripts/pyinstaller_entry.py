import json
from pathlib import Path
import maxc_cli
metadata = Path(maxc_cli.__file__).with_name("x_build.json")
if metadata.exists():
    build = json.loads(metadata.read_text())
    maxc_cli.__version__ = build["version"] + "+" + build["commit"]

from maxc_cli.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
