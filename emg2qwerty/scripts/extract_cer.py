#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("Usage: extract_cer.py <train_log_file>")

log_path = Path(sys.argv[1])
text = log_path.read_text(encoding="utf-8", errors="ignore")

def _extract(metric: str):
    # Matches both float and tensor(float) forms from printed results
    pattern = rf"'{re.escape(metric)}':\s*(?:tensor\()?([0-9]*\.?[0-9]+)"
    matches = re.findall(pattern, text)
    return float(matches[-1]) if matches else None

result = {
    "log_file": str(log_path),
    "val_CER": _extract("val/CER"),
    "test_CER": _extract("test/CER"),
}

print(json.dumps(result, indent=2, sort_keys=True))
