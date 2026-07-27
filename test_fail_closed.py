#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Negative control for the exact symbolic checker.

The control changes one expected value in a temporary copy of the checker.
A successful control means the deliberately false expectation is rejected.
No Python ``assert`` statement is used, so the control remains active under
``python -O``.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> None:
    checker = Path(__file__).with_name(
        "verify_degree_difference_affine_slices.py"
    )
    source = checker.read_text(encoding="utf-8")
    correct = 'assert_equal(det_f, -2, "det DF")'
    deliberately_wrong = 'assert_equal(det_f, 0, "det DF")'

    occurrences = source.count(correct)
    if occurrences != 1:
        raise RuntimeError(
            "control could not identify exactly one det DF expectation; "
            f"found {occurrences}"
        )

    mutated = source.replace(correct, deliberately_wrong)
    with tempfile.TemporaryDirectory(prefix="affine-slices-control-") as tmp:
        mutated_checker = Path(tmp) / checker.name
        mutated_checker.write_text(mutated, encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(mutated_checker)],
            check=False,
            capture_output=True,
            text=True,
        )

    if result.returncode == 0:
        raise RuntimeError(
            "fail-closed control failed: the false determinant expectation "
            "was accepted"
        )
    if "AssertionError: det DF failed" not in result.stderr:
        raise RuntimeError(
            "checker failed for an unexpected reason:\n" + result.stderr
        )

    mode = "optimized" if sys.flags.optimize else "normal"
    print(
        "Fail-closed control passed "
        f"({mode} mode): false det DF expectation was rejected."
    )


if __name__ == "__main__":
    main()
