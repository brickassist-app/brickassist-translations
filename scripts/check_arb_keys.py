import json
import os
import sys
from glob import glob


def load_keys(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    keys = {k for k in data.keys() if not k.startswith('@')}
    return keys


def main(directory="in_app_content"):
    pattern = os.path.join(directory, '*.arb')
    files = sorted(glob(pattern))
    if not files:
        print(f"No ARB files found in {directory}")
        return 1
    base_keys = None
    success = True
    for fpath in files:
        keys = load_keys(fpath)
        if base_keys is None:
            base_keys = keys
        else:
            missing = base_keys - keys
            extra = keys - base_keys
            if missing or extra:
                success = False
                print(f"Key mismatch in {fpath}:")
                if missing:
                    print(f"  Missing keys: {sorted(missing)}")
                if extra:
                    print(f"  Extra keys: {sorted(extra)}")
    if success:
        print("All ARB files have consistent keys.")
    return 0 if success else 1


if __name__ == "__main__":
    dir_arg = sys.argv[1] if len(sys.argv) > 1 else "in_app_content"
    sys.exit(main(dir_arg))
