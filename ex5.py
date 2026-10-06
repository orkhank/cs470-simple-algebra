import typing as t

import algb


def main():
    mod2 = algb.FieldCandidate(
        add=_mod2_add,
        negate=_mod2_negate,
        multiply=_mod2_mul,
        multiplicative_inverse=_mod2_reciprocal,
        zero="0",
        one="1",
        other_elements=(),
    )

    assert algb.is_field(mod2)


def _is_mod2(x: str) -> t.TypeIs[t.Literal["0", "1"]]:
    return x in {"0", "1"}


def _mod2_add(a: str, b: str):
    if not _is_mod2(a) or not _is_mod2(b):
        return "UNDEFINED"

    # addition is XOR
    match (a, b):
        case ("0", "0"):
            return "0"

        case ("0", "1"):
            return "1"

        case ("1", "0"):
            return "1"

        case ("1", "1"):
            return "0"


def _mod2_negate(a: str):
    if not _is_mod2(a):
        return "UNDEFINED"

    return a


def _mod2_mul(a: str, b: str):
    if not _is_mod2(a) or not _is_mod2(b):
        return "UNDEFINED"

    # multiplication is AND
    match (a, b):
        case ("0", "0"):
            return "0"

        case ("0", "1"):
            return "0"

        case ("1", "0"):
            return "0"

        case ("1", "1"):
            return "1"


def _mod2_reciprocal(a: str):
    if not _is_mod2(a):
        return "UNDEFINED"

    match a:
        case "0":
            return "UNDEFINED"
        case "1":
            return "1"


if __name__ == "__main__":
    main()
