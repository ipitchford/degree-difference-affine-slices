<!-- SPDX-License-Identifier: CC0-1.0 -->

# Machine-readable ClaimPack

The current repository tree includes a machine-readable ClaimPack at
[`claimpacks/degree-difference-affine-slices/claimpack.json`](claimpacks/degree-difference-affine-slices/claimpack.json).
Its records provide claim-level discovery metadata, evidence links, separate
assessment dimensions, and content-derived identifiers for automated readers.

Validate the package with the candidate ClaimPack implementation pinned to
tag `v0.1.0-candidate.1`:

```sh
tmp_dir=$(mktemp -d)
git clone --depth 1 --branch v0.1.0-candidate.1 \
  https://github.com/ipitchford/claimpack.git "$tmp_dir/claimpack"
python3 -m venv "$tmp_dir/venv"
"$tmp_dir/venv/bin/python" -m pip install "$tmp_dir/claimpack"
"$tmp_dir/venv/bin/claimpack" validate \
  claimpacks/degree-difference-affine-slices
```

## Assurance and release boundary

This ClaimPack is post-release discovery metadata. It was added after the
`v0.1-candidate` GitHub tag and the archive identified by version DOI
`10.5281/zenodo.21647593`; it is not part of either immutable release
artefact. It does not change the manuscript, its claims, citations, evidence,
or status.

A valid ClaimPack establishes structural integrity and faithful transport of
the records it contains. It does **not** establish mathematical correctness,
proof completeness, formal verification, independent reproduction, peer
review, novelty, or acceptance. The candidate and non-verification boundaries
in [`README.md`](README.md), [`AI_INDEX.md`](AI_INDEX.md), and
[`STATUS.md`](STATUS.md) remain controlling.

The current-tree [`MANIFEST.sha256`](MANIFEST.sha256) has been advanced to
cover this post-release metadata layer. The manifest and contents preserved in
the historical tag and DOI archive remain unchanged.
