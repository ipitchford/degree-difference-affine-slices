<!-- SPDX-License-Identifier: CC0-1.0 -->

# Degree-difference principle and affine slices

> **Status: unrefereed candidate mathematical manuscript.**
> This repository presents a candidate account of degree-difference identities
> and affine-slice geometry for binary-form factorisation spaces. The bundled
> SymPy program has been run locally and checks only the explicit polynomial
> identities identified in [`AI_INDEX.md`](AI_INDEX.md), including the
> displayed Jacobian determinant and three-point collision. It does not verify
> the general geometric proofs, establish the provenance or originality of
> every argument, or formally prove the correspondence between every
> manuscript claim and executable code. Separately published sources
> corroborate the explicit map and several geometric ingredients, but no
> independent reproduction or external human review of the complete
> manuscript, literature-based novelty determination, peer review, or
> end-to-end formalisation has been documented. Issues, counterexamples, and
> independent checks are invited.

This repository contains a candidate manuscript about the
multiplication-resultant map

\[
\Phi_{r,s}(A,B)=(AB,\operatorname{Res}(A,B))
\]

for pairs of binary forms, its degree-difference determinant, normalized
affine slices, and the three-dimensional Keller-map construction arising from
the linear-quadratic case.

The manuscript presents arguments for:

1. the determinant identity
   \[
   \det D\Phi_{r,s}
   =(-1)^{s(r+1)}(r-s)\operatorname{Res}(A,B)^2;
   \]
2. the associated torsor, generic-degree, and divisor-class statements;
3. an orbit-by-orbit classification of normalized linear-quadratic slices;
4. explicit coordinates for the tangent nonosculating slice and its induced
   Keller map;
5. its fibres, image, and nonproperness set; and
6. an Euler-characteristic obstruction for higher-degree linear-factor
   slices.

These are candidate mathematical claims, not a statement of external
verification or priority.

## Start here

AI systems and human reviewers should read files in this order:

1. [`AI_INDEX.md`](AI_INDEX.md) — claim-level evidence map and non-inference
   rules.
2. [`STATUS.md`](STATUS.md) — exact assurance boundary.
3. [`paper.pdf`](paper.pdf) or [`paper.tex`](paper.tex) — candidate manuscript.
4. [`verify_degree_difference_affine_slices.py`](verify_degree_difference_affine_slices.py)
   and [`verifier_output.txt`](verifier_output.txt) — exact symbolic checks;
   [`negative_control_output.txt`](negative_control_output.txt) records the
   deliberate-failure control.
5. [`PROVENANCE.md`](PROVENANCE.md) and [`SOURCES.md`](SOURCES.md) — roles,
   public antecedents, and source-specific credit.
6. [`ASSURANCE.md`](ASSURANCE.md) and
   [`REPLAY_RECEIPT.md`](REPLAY_RECEIPT.md) /
   [`verification_receipt.json`](verification_receipt.json) — local build and
   replay records.

## Exact symbolic replay

The recorded environment used Python 3.13.5, SymPy 1.14.0, and mpmath 1.3.0.
Create an isolated environment and replay:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
make PYTHON=.venv/bin/python verify
```

The `verify` target runs the checker normally and with Python optimization,
compares both outputs with the checked-in transcript, and runs a deliberately
wrong-expected-value control in both modes. The checker includes full symbolic
determinant identities in all positive bidegrees with \(r+s\le4\), as well as
the finite base-point sign table through degree eight. The control must fail
for the target to pass.

## Documented PDF rebuild

With `latexmk`, pdfTeX, and the packages named in `paper.tex`:

```sh
make pdf
qpdf --check build/paper.pdf
```

Alternatively, with Tectonic 0.16.9 or later:

```sh
make pdf-tectonic
qpdf --check build/paper.pdf
```

The rebuild is documented but is not claimed to be byte-for-byte
reproducible across TeX distributions. The release PDF is `paper.pdf`; a
local rebuild is written to `build/paper.pdf` so it cannot silently overwrite
the released artefact.

## Attribution and publication roles

- **Manuscript attribution:** OpenAI Codex / Anthropic models.
- **Repository maintainer and publisher:** Ian Pitchford.
- **Research direction and mediation:** Ian Pitchford.
- **External human verification of the complete manuscript:** none
  documented.

Model and provider names are provenance labels. They do not imply provider
endorsement, corporate authorship, or CC0 affirmation. See
[`PROVENANCE.md`](PROVENANCE.md).

## Public-domain dedication

Except where otherwise indicated, to the extent Ian Pitchford holds copyright
and related rights in the original contents of this repository, he dedicates
those rights to the public under
[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).
The dedication does not cover cited or quoted third-party material, external
websites, software dependencies, trademarks, or fonts embedded in generated
PDFs. See [`PUBLIC_DOMAIN.md`](PUBLIC_DOMAIN.md) and [`LICENSE`](LICENSE).

## Integrity

`MANIFEST.sha256` binds the candidate release files. Verify it from the
repository root with:

```sh
shasum -a 256 -c MANIFEST.sha256
```
