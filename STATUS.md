<!-- SPDX-License-Identifier: CC0-1.0 -->

# Status and assurance boundary

**Status: unrefereed candidate mathematical manuscript.**

This repository presents a candidate account of degree-difference identities
and affine-slice geometry for binary-form factorisation spaces.

## What has been done

- The supplied source archive passed ZIP integrity and path-safety checks.
- Every hash recorded in the supplied receipt matched its named source
  artefact.
- The supplied PDF passed `qpdf --check`, and its pages were visually sampled.
- The LaTeX source was rebuilt locally as a separate build.
- The SymPy checker was replayed locally with exact rational arithmetic under
  ordinary and optimized Python execution.
- A negative control deliberately changes the expected Jacobian determinant;
  the checker rejects it under both execution modes.
- Public sources were inspected to improve credit for antecedent formulas and
  geometric arguments.

## What has not been established

- No independent external reproduction of the complete result is documented.
- No external human has reviewed the complete manuscript.
- No peer review or proof-assistant formalisation is documented.
- The symbolic checker covers selected explicit identities, not the general
  geometric arguments.
- No exhaustive literature search or novelty/priority determination has been
  performed.
- Repository structure, hashes, and successful execution do not themselves
  establish mathematical truth.

Publication under CC0 changes reuse permissions; it does not upgrade any
mathematical assurance level.
