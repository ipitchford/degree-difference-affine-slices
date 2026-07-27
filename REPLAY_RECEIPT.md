<!-- SPDX-License-Identifier: CC0-1.0 -->

# Local replay receipt

Generated 27 July 2026 at 21:29 UTC.

**Assurance class:** local replay by the publication-preparation agent. This
is not independent external reproduction, external human review, peer review,
or formalisation.

## Environment

- macOS 26.5.2 (build 25F84), arm64
- Python 3.13.5
- SymPy 1.14.0
- mpmath 1.3.0
- Tectonic 0.16.9
- qpdf 12.3.2

The Python dependencies are pinned in `requirements.txt`. The PDF was built
with Tectonic because the host's unrelated minimal TinyTeX installation did
not contain every package required by `paper.tex`.

## Commands and results

### Exact symbolic replay

```sh
make PYTHON=<isolated-venv>/bin/python verify
```

Exit status: `0`.

The target:

1. ran the exact checker under ordinary Python;
2. compared its output byte-for-byte with `verifier_output.txt`;
3. repeated the run under `python -O`;
4. mutated the expected value of \(\det DF\) from \(-2\) to \(0\);
5. confirmed that the mutated checker failed in ordinary and optimized
   modes; and
6. compared the control transcript with `negative_control_output.txt`.

The checker derives the full Sylvester resultant and verifies the complete
determinant identity in every positive bidegree with \(r+s\le4\). It also
checks the manuscript's base-point sign convention for
\(1\le r,s\le8\), plus the explicit parametrisation, inverse, maps,
Jacobians, collision, discriminant-coordinate conversion, and triple-root
formulas.

### Candidate PDF

```sh
make TECTONIC=<tectonic-0.16.9> pdf-tectonic
cp build/paper.pdf paper.pdf
qpdf --check paper.pdf
```

Each command exited `0`. The final TeX pass had resolved references and
citations. The resulting PDF has 15 US-letter pages, is unencrypted, and
contains embedded fonts. The release PDF is not claimed to rebuild
byte-for-byte across TeX engines or timestamps.

### Citation metadata

```sh
cffconvert --validate --infile CITATION.cff
```

Exit status: `0`; valid under CFF schema 1.2.0.

## Core artefact hashes

```text
f642d2c0f499ee49e45c522f6c3259dd6aaa28e2e477df632d03a716c157f5d5  paper.pdf
3342a85b6b6d5378948b70aa97a675643255e53dbc13dfe68bc6495a8d6b1930  paper.tex
7b1890e9fc212272a180b1fefd5d2644ce10724f73691ab8978585fc37560ac5  verify_degree_difference_affine_slices.py
c0c1807f103a0f085c18b6786d66169f03748b3eeee3f0356cc174c18b34aa92  test_fail_closed.py
c81eab141ee6ad2ea0cbf32a35554fe69f48c83f06cc448550db57403d9e68e1  verifier_output.txt
8cce4ff76f5d3a4d0f9770aa0cd0ecf9dd170c63db72ca85b8e33e220ce5f405  negative_control_output.txt
5c538a2903754af889db079cdd91e9319ae4a9ab0701173e54ff351183ec76c6  requirements.txt
```

`MANIFEST.sha256` covers the full tracked publication set.
