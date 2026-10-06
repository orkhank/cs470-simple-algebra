import typing as t

import algb


def main():
    gf4 = algb.FieldCandidate(
        add=_gf4_add,
        negate=_gf4_negate,
        multiply=_gf4_mul,
        multiplicative_inverse=_gf4_reciprocal,
        zero="0",
        one="1",
        other_elements=("x", "x + 1"),
    )

    assert algb.is_field(gf4)


# F_2[x] / (x^2 + x + 1)
def _is_gf4(
    x: str,
) -> t.TypeIs[
    t.Literal[
        "0",
        "1",
        "x",
        "x + 1",
    ]
]:
    return x in {
        "0",
        "1",
        "x",
        "x + 1",
    }


def _gf4_add(a: str, b: str):
    if not _is_gf4(a) or not _is_gf4(b):
        return "UNDEFINED"

    # Addition is coefficient-wise XOR.
    match (a, b):
        case ("0", "0"):
            return "0"

        case ("0", "1"):
            return "1"

        case ("0", "x"):
            return "x"

        case ("0", "x + 1"):
            return "x + 1"

        case ("1", "0"):
            return "1"

        case ("1", "1"):
            return "0"

        case ("1", "x"):
            return "x + 1"

        case ("1", "x + 1"):
            return "x"

        case ("x", "0"):
            return "x"

        case ("x", "1"):
            return "x + 1"

        case ("x", "x"):
            return "0"

        case ("x", "x + 1"):
            return "1"

        case ("x + 1", "0"):
            return "x + 1"

        case ("x + 1", "1"):
            return "x"

        case ("x + 1", "x"):
            return "1"

        case ("x + 1", "x + 1"):
            return "0"


def _gf4_negate(a: str):
    if not _is_gf4(a):
        return "UNDEFINED"

    return a


def _gf4_mul(a: str, b: str):
    if not _is_gf4(a) or not _is_gf4(b):
        return "UNDEFINED"

    # a * b modulo (x^2 + x + 1)
    match (a, b):
        case ("0", "0"):
            return "0"

        case ("0", "1"):
            return "0"

        case ("0", "x"):
            return "0"

        case ("0", "x + 1"):
            return "0"

        case ("1", "0"):
            return "0"

        case ("1", "1"):
            return "1"

        case ("1", "x"):
            return "x"

        case ("1", "x + 1"):
            return "x + 1"

        case ("x", "0"):
            return "0"

        case ("x", "1"):
            return "x"

        case ("x", "x"):
            return "x + 1"

        case ("x", "x + 1"):
            return "1"

        case ("x + 1", "0"):
            return "0"

        case ("x + 1", "1"):
            return "x + 1"

        case ("x + 1", "x"):
            return "1"

        case ("x + 1", "x + 1"):
            return "x"


def _gf4_reciprocal(a: str):
    if not _is_gf4(a):
        return "UNDEFINED"

    match a:
        case "0":
            return "UNDEFINED"

        case "1":
            return "1"

        case "x":
            return "x + 1"

        case "x + 1":
            return "x"


if __name__ == "__main__":
    main()
