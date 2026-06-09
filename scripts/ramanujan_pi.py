"""Compute pi to 30 decimal places using Ramanujan's 1/pi series.

Ramanujan series:
  1/pi = (2*sqrt(2)/9801) * sum_{k>=0} (4k)! * (1103 + 26390k) / ((k!)^4 * 396^(4k))

Precision strategy:
- Each term contributes ~8 correct decimal digits (ratio ~1/396^4 per step).
- TERM_COUNT = 8 yields ~64 digits of series accuracy.
- GUARD_DIGITS = 20 so working precision = 50, well past the 30-digit target.
- sqrt(2) is computed in Decimal at working precision via Decimal(2).sqrt().
- Factorials and integer powers are computed as exact Python ints, then
  converted to Decimal inside the active localcontext.
"""

import math
from decimal import ROUND_DOWN, Decimal, localcontext

DECIMAL_PLACES: int = 30
GUARD_DIGITS: int = 20
WORKING_PRECISION: int = DECIMAL_PLACES + GUARD_DIGITS
TERM_COUNT: int = 8
SQRT_RADICAND: int = 2
SERIES_PREFACTOR_NUM: int = 2
SERIES_DENOM: int = 9801
LINEAR_BASE: int = 1103
LINEAR_STEP: int = 26390
POWER_BASE: int = 396
POWER_EXP_MULT: int = 4
FACTORIAL_MULT: int = 4
KFACT_POWER: int = 4
REFERENCE_PI: str = "3.141592653589793238462643383279"
ROUNDING_MODE: str = ROUND_DOWN


def ramanujan_term(k: int) -> Decimal:
    """Return the k-th term of the Ramanujan series as a Decimal.

    Assumes a localcontext with sufficient precision is active.
    Term: (4k)! * (1103 + 26390*k) / ((k!)^4 * 396^(4k))
    """
    numerator_fact: int = math.factorial(FACTORIAL_MULT * k)
    k_fact: int = math.factorial(k)
    linear_coeff: int = LINEAR_BASE + LINEAR_STEP * k
    power_val: int = POWER_BASE ** (POWER_EXP_MULT * k)
    denominator: int = (k_fact ** KFACT_POWER) * power_val
    return Decimal(numerator_fact) * Decimal(linear_coeff) / Decimal(denominator)


def ramanujan_series(term_count: int) -> Decimal:
    """Sum terms 0..term_count-1 of the Ramanujan series."""
    total = Decimal(0)
    for k in range(term_count):
        total += ramanujan_term(k)
    return total


def compute_pi(places: int, guard_digits: int, term_count: int) -> Decimal:
    """Compute pi truncated to `places` decimal places.

    Sets up a localcontext at precision = places + guard_digits,
    computes sqrt(2) in Decimal, builds the Ramanujan prefactor,
    sums the series, and returns 1 / (prefactor * series) truncated
    to exactly `places` decimal places (ROUND_DOWN matches the
    standard digit-expansion convention for pi).
    """
    precision = places + guard_digits
    with localcontext() as ctx:
        ctx.prec = precision
        sqrt2 = Decimal(SQRT_RADICAND).sqrt()
        prefactor = (Decimal(SERIES_PREFACTOR_NUM) * sqrt2) / Decimal(SERIES_DENOM)
        series = ramanujan_series(term_count)
        pi_value = Decimal(1) / (prefactor * series)
        quantizer = Decimal(1).scaleb(-places)
        return pi_value.quantize(quantizer, rounding=ROUNDING_MODE)


def format_pi(value: Decimal, places: int) -> str:
    """Return fixed-point string with exactly `places` digits after the decimal."""
    return f"{value:.{places}f}"


def main() -> None:
    """Compute and print pi to DECIMAL_PLACES decimal places.

    Raises SystemExit with non-zero code if the result does not match
    REFERENCE_PI — a wrong result must surface as an error, not be silently
    printed.
    """
    pi = compute_pi(DECIMAL_PLACES, GUARD_DIGITS, TERM_COUNT)
    formatted = format_pi(pi, DECIMAL_PLACES)
    print(formatted)
    if formatted != REFERENCE_PI:
        raise SystemExit(
            f"Result mismatch:\n  got:      {formatted}\n  expected: {REFERENCE_PI}"
        )


if __name__ == "__main__":
    main()
