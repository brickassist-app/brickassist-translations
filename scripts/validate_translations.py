#!/usr/bin/env python3
import json
import os
import sys

FAILURES = []


def validate_arb(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            json.load(f)
    except json.JSONDecodeError as e:
        FAILURES.append(f"Invalid JSON in {path}: {e}")


def validate_text_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            f.read()
    except UnicodeDecodeError as e:
        FAILURES.append(f"Invalid text encoding in {path}: {e}")


for root, _, files in os.walk('.'):
    if root.startswith('./.git'):
        continue
    for name in files:
        if name.endswith('.arb'):
            validate_arb(os.path.join(root, name))
        elif root.startswith('./email_content') or root.startswith('./store_descriptions'):
            validate_text_file(os.path.join(root, name))

if FAILURES:
    print('Validation failed:')
    for f in FAILURES:
        print(' -', f)
    sys.exit(1)
else:
    print('All files validated successfully.')
