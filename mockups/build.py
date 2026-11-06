"""Build every sample interface into public/demo/. Run: python3 mockups/build.py"""
import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
for name in ("pms", "pos", "dms", "web", "shop"):
    try:
        importlib.import_module(name).build()
    except ModuleNotFoundError as e:
        if e.name != name:
            raise
        print("skip", name, "(not written yet)")
