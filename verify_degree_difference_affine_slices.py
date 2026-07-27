#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
"""Exact symbolic checks for selected formulas in the candidate manuscript.

All checks use SymPy over the rational numbers.  No floating-point
arithmetic and no random testing are used.

This program does not encode or prove the manuscript's general geometric
claims.  See AI_INDEX.md for the exact coverage boundary.
"""
from __future__ import annotations

import sympy as sp


def assert_zero(expr: sp.Expr, label: str) -> None:
    value = sp.cancel(sp.factor(sp.expand(expr)))
    if value != 0:
        raise AssertionError(f"{label} failed: {value}")


def assert_equal(lhs: sp.Expr, rhs: sp.Expr, label: str) -> None:
    assert_zero(lhs - rhs, label)


def check_general_base_sign(max_degree: int = 8) -> None:
    """Check the sign computation at (A,B)=(X^r,Y^s)."""
    for r in range(1, max_degree + 1):
        for s in range(1, max_degree + 1):
            size = r + s + 2
            jac = sp.zeros(size, size)

            # Source columns: a_0,...,a_r,b_0,...,b_s.
            # Target rows: product coefficients c_0,...,c_{r+s}, resultant.
            for i in range(r + 1):
                jac[s + i, i] = 1
            for j in range(s + 1):
                jac[j, r + 1 + j] = 1
            jac[-1, 0] = s
            jac[-1, r + 1 + s] = r

            expected = (-1) ** (s * (r + 1)) * (r - s)
            actual = int(jac.det())
            if actual != expected:
                raise AssertionError(
                    f"base sign failed for (r,s)=({r},{s}): "
                    f"actual {actual}, expected {expected}"
                )


def check_low_degree_full_identity(max_total_degree: int = 4) -> None:
    """Derive and check the full determinant identity in small bidegrees.

    The resultant is constructed as the determinant of the exact Sylvester
    matrix specified in the manuscript: ``s`` shifted rows of ``A`` followed
    by ``r`` shifted rows of ``B``.  This also audits the sign convention
    independently of the base-point derivative table.
    """
    t = sp.symbols("t_resultant")
    for r in range(1, max_total_degree):
        for s in range(1, max_total_degree - r + 1):
            a_coeffs = sp.symbols(f"a0:{r + 1}")
            b_coeffs = sp.symbols(f"b0:{s + 1}")
            source = a_coeffs + b_coeffs

            a_form = sum(
                a_coeffs[i] * t ** (r - i) for i in range(r + 1)
            )
            b_form = sum(
                b_coeffs[j] * t ** (s - j) for j in range(s + 1)
            )
            product_coeffs = sp.Poly(
                sp.expand(a_form * b_form), t
            ).all_coeffs()

            sylvester = sp.zeros(r + s, r + s)
            for row in range(s):
                for index, coefficient in enumerate(a_coeffs):
                    sylvester[row, row + index] = coefficient
            for shift in range(r):
                for index, coefficient in enumerate(b_coeffs):
                    sylvester[s + shift, shift + index] = coefficient
            manuscript_resultant = sp.expand(sylvester.det())
            outputs = product_coeffs + [manuscript_resultant]
            determinant = sp.Matrix(outputs).jacobian(source).det()
            expected = (
                (-1) ** (s * (r + 1))
                * (r - s)
                * manuscript_resultant**2
            )
            assert_equal(
                determinant,
                expected,
                f"full determinant identity for (r,s)=({r},{s})",
            )


def main() -> None:
    # ------------------------------------------------------------------
    # 1. Polynomial parametrisation and inverse.
    # ------------------------------------------------------------------
    a, y, z = sp.symbols("a y z")

    b = 1 + a * y
    c = 1 - sp.Rational(3, 2) * a * y + a**2 * z
    d = (
        sp.Rational(1, 2) * y
        - a * z
        + sp.Rational(3, 2) * a * y**2
        - a**2 * y * z
    )
    e = -2 * z + 4 * y**2 - 4 * a * y * z + 3 * a * y**3 - 2 * a**2 * y**2 * z

    resultant = a**2 * e - a * b * d + c * b**2
    hyperplane = a * d + b * c
    assert_equal(resultant, 1, "resultant normalisation")
    assert_equal(hyperplane, 1, "hyperplane normalisation")

    y_inverse = 2 * b * d - a * e
    z_inverse = 2 * d**2 + c * e + 6 * b * d**2 + 3 * b * c * e - sp.Rational(9, 2) * e
    assert_equal(y_inverse, y, "inverse formula for y")
    assert_equal(z_inverse, z, "inverse formula for z")

    # Intermediate identities used in the written inverse proof.
    assert_equal(a * (2 * b * d - a * e), b - 1, "intermediate identity 1")
    assert_equal(a**2 * (2 * d**2 + c * e), 2 + c - 3 * b * c, "intermediate identity 2")
    assert_equal(a**2 * e, 1 + b - 2 * b**2 * c, "intermediate identity 3")
    assert_equal(a**2 * z_inverse, c + sp.Rational(3, 2) * b - sp.Rational(5, 2), "intermediate identity 4")

    # ------------------------------------------------------------------
    # 2. Induced map G and its Jacobian.
    # ------------------------------------------------------------------
    G = (sp.expand(a * c), sp.expand(a * e + b * d), sp.expand(b * e))
    G_expected = (
        a - sp.Rational(3, 2) * a**2 * y + a**3 * z,
        sp.Rational(1, 2) * y
        - 3 * a * z
        + 6 * a * y**2
        - 6 * a**2 * y * z
        + sp.Rational(9, 2) * a**2 * y**3
        - 3 * a**3 * y**2 * z,
        -2 * z
        + 4 * y**2
        - 6 * a * y * z
        + 7 * a * y**3
        - 6 * a**2 * y**2 * z
        + 3 * a**2 * y**4
        - 2 * a**3 * y**3 * z,
    )
    for index, (actual, expected) in enumerate(zip(G, G_expected), start=1):
        assert_equal(actual, expected, f"expanded G_{index}")

    det_g = sp.Matrix(G).jacobian((a, y, z)).det()
    assert_equal(det_g, -1, "det DG")

    # ------------------------------------------------------------------
    # 3. Linear conjugacy to the announced map F.
    # ------------------------------------------------------------------
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    subs_a0 = {a: x1, y: x2, z: -sp.Rational(1, 2) * x3}
    G_after_A0 = tuple(sp.expand(component.subs(subs_a0)) for component in G)
    F_from_conjugacy = (
        G_after_A0[2],
        2 * G_after_A0[1],
        2 * G_after_A0[0],
    )

    F_expected = (
        (1 + x1 * x2) ** 3 * x3
        + x2**2 * (1 + x1 * x2) * (4 + 3 * x1 * x2),
        x2
        + 3 * x1 * (1 + x1 * x2) ** 2 * x3
        + 3 * x1 * x2**2 * (4 + 3 * x1 * x2),
        2 * x1 - 3 * x1**2 * x2 - x1**3 * x3,
    )
    for index, (actual, expected) in enumerate(zip(F_from_conjugacy, F_expected), start=1):
        assert_equal(actual, expected, f"B0 o G o A0, component {index}")

    det_f = sp.Matrix(F_expected).jacobian((x1, x2, x3)).det()
    assert_equal(det_f, -2, "det DF")

    collision_points = (
        {x1: 0, x2: 0, x3: -sp.Rational(1, 4)},
        {x1: 1, x2: -sp.Rational(3, 2), x3: sp.Rational(13, 2)},
        {x1: -1, x2: sp.Rational(3, 2), x3: sp.Rational(13, 2)},
    )
    collision_target = (-sp.Rational(1, 4), 0, 0)
    for number, point in enumerate(collision_points, start=1):
        image = tuple(sp.simplify(component.subs(point)) for component in F_expected)
        if image != collision_target:
            raise AssertionError(f"collision point {number} failed: {image}")

    # ------------------------------------------------------------------
    # 4. Discriminant, original output coordinates, and omitted curve.
    # ------------------------------------------------------------------
    U, V, W, t = sp.symbols("U V W t")
    cubic = U * t**3 + t**2 + V * t + W
    discriminant = sp.discriminant(cubic, t)
    discriminant_expected = V**2 - 4 * U * V**3 - 4 * W - 27 * U**2 * W**2 + 18 * U * V * W
    assert_equal(discriminant, discriminant_expected, "binary-cubic discriminant")

    P, Q, R = sp.symbols("P Q R")
    D = 16 * P - Q**2 - 18 * P * Q * R + Q**3 * R + 27 * P**2 * R**2
    assert_equal(
        D,
        -4 * discriminant_expected.subs({U: R / 2, V: Q / 2, W: P}),
        "D=-4 Delta(R/2,Q/2,P)",
    )

    triple_v = 1 / (3 * U)
    triple_w = 1 / (27 * U**2)
    triple_cubic = U * (t + 1 / (3 * U)) ** 3
    assert_equal(cubic.subs({V: triple_v, W: triple_w}), triple_cubic, "triple-root normal form")
    assert_equal(3 * U * triple_v, 1, "triple-root equation 3UV=1")
    assert_equal(27 * U**2 * triple_w, 1, "triple-root equation 27U^2W=1")

    collision_cubic = t**2 - sp.Rational(1, 4)
    assert_equal(
        collision_cubic,
        (t - sp.Rational(1, 2)) * (t + sp.Rational(1, 2)),
        "collision cubic factorisation",
    )

    # ------------------------------------------------------------------
    # 5. General determinant sign at the normalising base point.
    # ------------------------------------------------------------------
    check_low_degree_full_identity(max_total_degree=4)
    check_general_base_sign(max_degree=8)

    checks = [
        "parametrisation and defining equations",
        "polynomial inverse and intermediate identities",
        "components and Jacobian of G",
        "linear conjugacy to F, det DF, and collision",
        "discriminant coordinate conversion and triple-root curve",
        "full determinant identity for positive r+s <= 4",
        "general determinant sign for 1 <= r,s <= 8",
    ]
    print("All exact checks passed:")
    for item in checks:
        print(f"  - {item}")


if __name__ == "__main__":
    main()
