# SPDX-License-Identifier: CC0-1.0

.PHONY: all pdf pdf-tectonic verify verify-normal verify-optimized verify-controls check-pdf clean

PYTHON ?= python3
LATEXMK ?= latexmk
QPDF ?= qpdf
TECTONIC ?= tectonic

TEX := paper.tex
RELEASE_PDF := paper.pdf
BUILD_DIR := build
BUILD_PDF := $(BUILD_DIR)/paper.pdf
VERIFY := verify_degree_difference_affine_slices.py
CONTROL := test_fail_closed.py
EXPECTED := verifier_output.txt
CONTROL_EXPECTED := negative_control_output.txt

all: verify pdf check-pdf

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

pdf: | $(BUILD_DIR)
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error -outdir=$(BUILD_DIR) $(TEX)

pdf-tectonic: | $(BUILD_DIR)
	$(TECTONIC) -X compile --outdir $(BUILD_DIR) --outfmt pdf --print --untrusted $(TEX)

verify: verify-normal verify-optimized verify-controls

verify-normal: | $(BUILD_DIR)
	$(PYTHON) $(VERIFY) > $(BUILD_DIR)/verifier_output.normal.txt
	diff -u $(EXPECTED) $(BUILD_DIR)/verifier_output.normal.txt
	cat $(BUILD_DIR)/verifier_output.normal.txt

verify-optimized: | $(BUILD_DIR)
	$(PYTHON) -O $(VERIFY) > $(BUILD_DIR)/verifier_output.optimized.txt
	diff -u $(EXPECTED) $(BUILD_DIR)/verifier_output.optimized.txt

verify-controls: | $(BUILD_DIR)
	( $(PYTHON) $(CONTROL); $(PYTHON) -O $(CONTROL) ) > $(BUILD_DIR)/negative_control_output.txt
	diff -u $(CONTROL_EXPECTED) $(BUILD_DIR)/negative_control_output.txt
	cat $(BUILD_DIR)/negative_control_output.txt

check-pdf: pdf
	$(QPDF) --check $(BUILD_PDF)

clean:
	$(LATEXMK) -C -outdir=$(BUILD_DIR) $(TEX)
	rm -f $(BUILD_DIR)/verifier_output.normal.txt
	rm -f $(BUILD_DIR)/verifier_output.optimized.txt
	rm -f $(BUILD_DIR)/negative_control_output.txt
