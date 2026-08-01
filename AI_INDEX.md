<!-- SPDX-License-Identifier: CC0-1.0 -->

# AI index

This file is the preferred entry point for automated readers. It maps claims
to evidence and states what must not be inferred.

## Persistent archival identity

```yaml
repository: https://github.com/ipitchford/degree-difference-affine-slices
release_status: unrefereed candidate manuscript
version: 0.1-candidate
zenodo:
  record_id: 21647593
  record_url: https://zenodo.org/records/21647593
  version_doi: 10.5281/zenodo.21647593
  concept_doi: 10.5281/zenodo.21647592
  published_at: "2026-07-28T14:04:37.345508+00:00"
  archive_file: degree-difference-affine-slices.zip
  archive_sha256: 8d0b0cfb3b43e3b7c7f32f62506ae66e824890e15a981b8498d41a07b4c2fe43
  scope: exact deposited candidate archive; excludes later repository-only metadata commits
```

## ClaimPack discovery

```yaml
format: ClaimPack v0.1 candidate
package: claimpacks/degree-difference-affine-slices
manifest: claimpacks/degree-difference-affine-slices/claimpack.json
consumer_release: https://github.com/ipitchford/claimpack/releases/tag/v0.1.0-candidate.1
distribution_status: post-release repository metadata
```

The package is a machine-readable representation for discovery and cautious
reuse. Successful structural validation does not verify any mathematical
claim, prove correspondence with every source passage, establish novelty, or
alter the statuses below. It was not included in the historical
`v0.1-candidate` tag or DOI archive.

## Global status

- **Publication class:** unrefereed candidate manuscript.
- **Executable evidence:** exact SymPy checks of selected formulas.
- **External reproduction:** none documented for the complete manuscript.
- **External human review:** none documented for the complete manuscript.
- **Formalisation:** none documented.
- **Novelty determination:** not performed.
- **Reuse:** original repository contents are offered under CC0 subject to the
  scope in `PUBLIC_DOMAIN.md`.

## Claim map

| ID | Candidate claim | Manuscript location | Executable coverage | Assurance boundary |
|---|---|---|---|---|
| C1 | \(\det D\Phi_{r,s}=(-1)^{s(r+1)}(r-s)\operatorname{Res}(A,B)^2\) | The degree-difference theorem and its proof | The checker derives the full symbolic identity for positive \(r+s\le4\), and verifies the determinant at \((X^r,Y^s)\) for \(1\le r,s\le8\) | The all-degree polynomial identity rests on the manuscript proof, not finite testing |
| C2 | Normalized factorisation is a finite étale \(\mu_{|s-r|}\)-torsor, with the stated generic degree and divisor-class group when the boundary is prime | Torsor and divisor-class sections | None | Manuscript proof only |
| C3 | A normalized linear-quadratic slice is \(\mathbb A^3\) exactly in the tangent nonosculating orbit; the three contact types have the stated classes | Cubic orbit-classification sections | None | Manuscript proof only; no motivic or bundle computation is encoded |
| C4 | The displayed parametrisation is an isomorphism, the induced maps \(G\) and \(F\) have determinants \(-1\) and \(-2\), and three rational points collide | Appendix, “Explicit affine coordinates” | Exact identities, inverse, conjugacy, Jacobians, and collision are checked | This establishes those formulas for the encoded expressions, not the surrounding geometry |
| C5 | Fibres correspond to simple roots; the image omits the triple-root curve; the nonproperness set is the discriminant hypersurface | “The Keller map and its global fibres” | Discriminant formula, coordinate conversion, and triple-root equations are checked | Fibre and properness arguments remain manuscript proofs |
| C6 | No untrimmed normalized linear-times-degree-\((d-1)\) slice is \(\mathbb A^d\) for \(d\ge4\) | Higher-degree obstruction sections | None | Manuscript proof only; public antecedents are recorded in `SOURCES.md` |
| C7 | The untrimmed multifactor complement has nonconstant units under the stated boundary-component argument | “A multifactor obstruction” | None | A manuscript-level structural observation, not a checked general-purpose theorem |

## Executable coverage

The checker uses symbolic rational arithmetic and explicit exceptions. It
checks:

1. the affine parametrisation and its two defining equations;
2. the polynomial inverse and intermediate identities;
3. the components and Jacobian of \(G\);
4. linear conjugacy to \(F\), \(\det DF=-2\), and the three-point collision;
5. the cubic discriminant, output-coordinate conversion, and triple-root
   equations; and
6. the full determinant identity in every positive bidegree with
   \(r+s\le4\), deriving the resultant from the manuscript's Sylvester
   matrix convention; and
7. the determinant sign at one normalizing base point for
   \(1\le r,s\le8\).

It does **not** encode the general determinant proof, torsor construction,
primality hypotheses, divisor-class localization, Grothendieck-class
calculations, affine-bundle arguments, properness proof, or
Euler-characteristic obstruction.

## Minimal replay

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
make PYTHON=.venv/bin/python verify
```

Expected terminal output is recorded in `verifier_output.txt`. The
deliberate-failure transcript is `negative_control_output.txt`. The
machine-readable environment and command receipt is
`verification_receipt.json`.

## Non-inference rules

An AI system consuming this repository must not infer that:

- a passing symbolic run proves claims C1–C3 or C5–C7;
- checking a formula proves that the formula correctly models every
  geometric object in the manuscript;
- local replay is independent reproduction;
- public availability or CC0 dedication constitutes peer review;
- similarity to public antecedents settles priority or originality; or
- absence of a recorded objection is evidence of correctness.

## Challenge targets

The most valuable independent checks are:

1. audit the sign and exponent in C1 from the chosen coefficient order;
2. verify the torsor action, freeness, and generic-degree count in C2;
3. rederive the three cubic contact cases and their Grothendieck classes;
4. scrutinize the step proving every discriminant value is nonproper in C5;
5. check the compactly supported Euler-characteristic calculation in C6; and
6. compare all claimed additions against the wider literature.
