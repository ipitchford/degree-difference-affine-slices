<!-- SPDX-License-Identifier: CC0-1.0 -->

# Assurance record

This document separates artefact integrity, executable replay, semantic
coverage, and external validation.

## Supplied archive

- **Input:** `degree_difference_affine_slices_final_source.zip`
- **Input SHA-256:**
  `d2827a5793330d57cf7800b41925e0999a69f5bf498842512fed90dcda869620`
- **Archive result:** CRC check passed; seven ordinary entries; no symlinks or
  path traversal detected.
- **Supplied artefact hashes:** all five hashes named in the supplied
  `verification_receipt.txt` matched.
- **Supplied PDF:** 14 pages; `qpdf --check` reported no structural errors;
  embedded fonts were present.

These checks establish integrity of the received bundle, not truth of its
claims.

## Local replay for this candidate

The repository checker was run in an isolated environment using:

- Python 3.13.5;
- SymPy 1.14.0; and
- mpmath 1.3.0.

The normal run and `python -O` run produced `verifier_output.txt`. The
fail-closed control changed the expected value of \(\det DF\) from \(-2\) to
\(0\); it was rejected under both modes.

The checker also constructs the manuscript's Sylvester matrix and verifies
the complete determinant identity symbolically for every positive bidegree
with \(r+s\le4\). Its separate base-point convention check covers every
\(1\le r,s\le8\). These remain finite checks; the all-degree theorem rests on
the manuscript proof.

The supplied TeX was also rebuilt separately with Tectonic 0.16.9 during
intake. The publication PDF was subsequently built from the revised
`paper.tex` and checked with `qpdf`. TeX engines and timestamps can differ, so
no byte-for-byte cross-environment PDF reproducibility claim is made.

## Assurance layers

| Layer | Current evidence | Not established |
|---|---|---|
| File integrity | SHA-256 manifest and release hashes | Mathematical correctness |
| Source/build | TeX compiles; PDF structurally checks | Bit-reproducible PDF across TeX systems |
| Formula execution | Exact SymPy replay, optimized replay, negative control | Coverage of general geometry |
| Semantic bridge | Human-readable claim map and manuscript explanations | Formal proof that code encodes every intended object |
| Provenance | Public-source comparison and repository-reported roles | Externally audited authorship or priority |
| External validation | Public issue/release surface for scrutiny | Independent reproduction, peer review, or formalisation |

See `verification_receipt.json` for commands and hashes, and `AI_INDEX.md`
for claim-level coverage.
