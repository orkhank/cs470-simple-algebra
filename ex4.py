import typing as t

import algb


def main():
    mod7 = algb.FieldCandidate(
        add=_mod7_add,
        negate=_mod7_negate,
        multiply=_mod7_mul,
        multiplicative_inverse=_mod7_reciprocal,
        zero="0",
        one="1",
        other_elements=("2", "3", "4", "5", "6"),
    )

    assert algb.is_field(mod7)

    mul_mod7 = algb.extract_multiplicative_group(mod7)

    mul2_mod7 = (mul_mod7, "2")
    mul3_mod7 = (mul_mod7, "3")

    assert algb.is_transformation(mul2_mod7)
    assert algb.is_transformation(mul3_mod7)

    div2_mod7 = algb.inverse(mul2_mod7)  # 2 ^ -1 mod 7
    assert div2_mod7 == (mul_mod7, "4")

    _3div2_mod7 = (div2_mod7, mul3_mod7)
    assert algb.are_composable(_3div2_mod7)
    assert algb.compose(_3div2_mod7) == (mul_mod7, "5")

    # divide by zero?
    # the type system will get angry
    mul0_mod7 = (mul_mod7, "0")
    assert not algb.is_transformation(mul0_mod7)

    div0_mod7 = algb.inverse(mul0_mod7)
    assert div0_mod7 == (mul_mod7, "UNDEFINED")
    assert not algb.is_transformation(div0_mod7)


def _is_mod7(x: str) -> t.TypeIs[t.Literal["0", "1", "2", "3", "4", "5", "6"]]:
    return x in {"0", "1", "2", "3", "4", "5", "6"}


def _mod7_add(a: str, b: str):
    if not _is_mod7(a) or not _is_mod7(b):
        return "UNDEFINED"

    match (a, b):
        case ("0", "0"):
            return "0"
        case ("0", "1"):
            return "1"
        case ("0", "2"):
            return "2"
        case ("0", "3"):
            return "3"
        case ("0", "4"):
            return "4"
        case ("0", "5"):
            return "5"
        case ("0", "6"):
            return "6"
        case ("1", "0"):
            return "1"
        case ("1", "1"):
            return "2"
        case ("1", "2"):
            return "3"
        case ("1", "3"):
            return "4"
        case ("1", "4"):
            return "5"
        case ("1", "5"):
            return "6"
        case ("1", "6"):
            return "0"
        case ("2", "0"):
            return "2"
        case ("2", "1"):
            return "3"
        case ("2", "2"):
            return "4"
        case ("2", "3"):
            return "5"
        case ("2", "4"):
            return "6"
        case ("2", "5"):
            return "0"
        case ("2", "6"):
            return "1"
        case ("3", "0"):
            return "3"
        case ("3", "1"):
            return "4"
        case ("3", "2"):
            return "5"
        case ("3", "3"):
            return "6"
        case ("3", "4"):
            return "0"
        case ("3", "5"):
            return "1"
        case ("3", "6"):
            return "2"
        case ("4", "0"):
            return "4"
        case ("4", "1"):
            return "5"
        case ("4", "2"):
            return "6"
        case ("4", "3"):
            return "0"
        case ("4", "4"):
            return "1"
        case ("4", "5"):
            return "2"
        case ("4", "6"):
            return "3"
        case ("5", "0"):
            return "5"
        case ("5", "1"):
            return "6"
        case ("5", "2"):
            return "0"
        case ("5", "3"):
            return "1"
        case ("5", "4"):
            return "2"
        case ("5", "5"):
            return "3"
        case ("5", "6"):
            return "4"
        case ("6", "0"):
            return "6"
        case ("6", "1"):
            return "0"
        case ("6", "2"):
            return "1"
        case ("6", "3"):
            return "2"
        case ("6", "4"):
            return "3"
        case ("6", "5"):
            return "4"
        case ("6", "6"):
            return "5"


def _mod7_negate(a: str):
    if not _is_mod7(a):
        return "UNDEFINED"

    match a:
        case "0":
            return "0"
        case "1":
            return "6"
        case "2":
            return "5"
        case "3":
            return "4"
        case "4":
            return "3"
        case "5":
            return "2"
        case "6":
            return "1"


def _mod7_mul(a: str, b: str):
    if not _is_mod7(a) or not _is_mod7(b):
        return "UNDEFINED"

    match (a, b):
        case ("0", "0"):
            return "0"
        case ("0", "1"):
            return "0"
        case ("0", "2"):
            return "0"
        case ("0", "3"):
            return "0"
        case ("0", "4"):
            return "0"
        case ("0", "5"):
            return "0"
        case ("0", "6"):
            return "0"
        case ("1", "0"):
            return "0"
        case ("1", "1"):
            return "1"
        case ("1", "2"):
            return "2"
        case ("1", "3"):
            return "3"
        case ("1", "4"):
            return "4"
        case ("1", "5"):
            return "5"
        case ("1", "6"):
            return "6"
        case ("2", "0"):
            return "0"
        case ("2", "1"):
            return "2"
        case ("2", "2"):
            return "4"
        case ("2", "3"):
            return "6"
        case ("2", "4"):
            return "1"
        case ("2", "5"):
            return "3"
        case ("2", "6"):
            return "5"
        case ("3", "0"):
            return "0"
        case ("3", "1"):
            return "3"
        case ("3", "2"):
            return "6"
        case ("3", "3"):
            return "2"
        case ("3", "4"):
            return "5"
        case ("3", "5"):
            return "1"
        case ("3", "6"):
            return "4"
        case ("4", "0"):
            return "0"
        case ("4", "1"):
            return "4"
        case ("4", "2"):
            return "1"
        case ("4", "3"):
            return "5"
        case ("4", "4"):
            return "2"
        case ("4", "5"):
            return "6"
        case ("4", "6"):
            return "3"
        case ("5", "0"):
            return "0"
        case ("5", "1"):
            return "5"
        case ("5", "2"):
            return "3"
        case ("5", "3"):
            return "1"
        case ("5", "4"):
            return "6"
        case ("5", "5"):
            return "4"
        case ("5", "6"):
            return "2"
        case ("6", "0"):
            return "0"
        case ("6", "1"):
            return "6"
        case ("6", "2"):
            return "5"
        case ("6", "3"):
            return "4"
        case ("6", "4"):
            return "3"
        case ("6", "5"):
            return "2"
        case ("6", "6"):
            return "1"


def _mod7_reciprocal(a: str):
    if not _is_mod7(a):
        return "UNDEFINED"

    match a:
        case "0":
            return "UNDEFINED"
        case "1":
            return "1"
        case "2":
            return "4"
        case "3":
            return "5"
        case "4":
            return "2"
        case "5":
            return "3"
        case "6":
            return "6"


if __name__ == "__main__":
    main()
