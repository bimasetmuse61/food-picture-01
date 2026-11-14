"""food-picture-01 entry: write the hero food picture to the output directory.

The entry ships a single food photograph (food.jpg) and this program copies
it byte-for-byte to entry.png, so every run produces identical bytes.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "food.jpg"


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"food image missing: {SOURCE}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Binary copy: the output is exactly the shipped photograph, every run.
    shutil.copyfile(SOURCE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
