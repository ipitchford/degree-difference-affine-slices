<!-- SPDX-License-Identifier: CC0-1.0 -->

# Provenance

## Repository roles

- **Manuscript attribution:** OpenAI Codex / Anthropic models.
- **Repository maintainer and publisher:** Ian Pitchford.
- **Research direction and mediation:** Ian Pitchford.
- **CC0 affirmer:** Ian Pitchford, only to the extent he holds copyright and
  related rights in the original repository contents.
- **External human verification of the complete manuscript:** none
  documented.

The model labels are those supplied with the manuscript. Exact model versions,
session identifiers, and a complete prompt/response history were not included
in the source archive. These are repository-reported provenance statements,
not an externally audited authorship determination. Model and provider names
do not imply endorsement or make providers legal affirmers.

## Intake record

- **Received archive:**
  `/Users/admin/affine_hyperplane_slices/degree_difference_affine_slices_final_source.zip`
- **Archive SHA-256:**
  `d2827a5793330d57cf7800b41925e0999a69f5bf498842512fed90dcda869620`
- **Received date:** 27 July 2026.

The archive supplied a TeX manuscript, PDF, SymPy checker, text receipt,
README, and Makefile. Publication edits added candidate-status language,
precise source credit, CC0 scope, pinned Python dependencies, fail-closed
controls, machine-readable receipts, stable filenames, and an AI claim index.
The mathematical statements were not silently promoted beyond their supplied
status.

## Public-history credit

The manuscript and `SOURCES.md` distinguish these recorded roles:

- Alpöge's announcement credited Fable for the explicit counterexample.
- In the public discussion hosted by David Speyer, Will Sawin posted a
  ChatGPT-produced symmetric-product formulation prompted by Andy Jiang.
- Sawin later developed an iterated affine-line-bundle explanation through
  further ChatGPT discussion; Daniel Litt also supplied a related bundle
  argument.
- Jake Levinson gave a projective-geometric conic account of the tangent
  construction.
- David Speyer supplied the exact vector-bundle sequence quoted in the
  manuscript.
- A commenter using the name Skooi recorded the \(d-2\) divisor-class
  obstruction and a marked-simple-root/fibre description.
- Shubhodip Mondal recorded the \(\mathbb Z/|r-s|\mathbb Z\) pattern.
- Terence Tao's account records the displayed parametrisation, inverse,
  induced map, and the three hyperplane orbits.
- The contemporaneous ulam.ai manuscript contains the explicit map and
  fibre, image, and nonproperness descriptions.

These links establish public antecedents and corroboration, not complete
independence, priority, or novelty.

## Symbolic checker provenance

The supplied archive presents
`verify_degree_difference_affine_slices.py` as its supplementary exact
checker and contains no statement that it was copied or adapted from the
NASQRET notebook. A direct comparison on 27 July 2026 found that both use the
same public formulas for the Keller map, determinant, collision, and
discriminant, while the repository checker is structurally distinct and also
checks the manuscript parametrisation, inverse, conjugacy, triple-root
equations, and finite base-point sign table.

That comparison is a code-level observation, not a legal or externally
audited provenance determination. The checker is included in the CC0 scope
only as repository-reported original material and only to the extent the
affirmer holds the relevant rights. The NASQRET notebook is linked, not
redistributed.

## No priority claim

No exhaustive literature search was performed. This repository makes no
claim that any statement, proof, formulation, code, or terminology is novel
or first.
