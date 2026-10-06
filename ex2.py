import typing as t

import algb


def main():
    mod6 = algb.RingCandidate(
        add=_mod6_add,
        negate=_mod6_negate,
        multiply=_mod6_mul,
        zero="0",
        one="1",
        other_elements=("2", "3", "4", "5"),
    )

    assert algb.is_ring(mod6)
    assert algb.is_commutative_ring(mod6)

    _ = t.assert_type(mod6, "algb.CommutativeRing")

    mod6 = algb.FieldCandidate(
        add=_mod6_add,
        negate=_mod6_negate,
        multiply=_mod6_mul,
        multiplicative_inverse=_mod6_reciprocal,  # !!
        zero="0",
        one="1",
        other_elements=("2", "3", "4", "5"),
    )

    match algb.check_field_axioms(mod6):
        case (
            "ADD CLOSED",
            "ADD ASSOCIATIVE",
            "ADD COMMUTATIVE",
            "ADD IDENTITY VALID",
            "ADD INVERSES VALID",
            "DISTRIBUTIVE",
            "MUL CLOSED",
            "MUL ASSOCIATIVE",
            "MUL IDENTITY VALID",
            "MUL INVERSES INVALID",  # !!
            "NONTRIVIAL",
        ):
            pass

        case _:
            raise AssertionError

    assert not algb.is_field(mod6)


def _is_mod6(x: str) -> t.TypeIs[t.Literal["0", "1", "2", "3", "4", "5"]]:
    return x in {"0", "1", "2", "3", "4", "5"}


def _mod6_add(a: str, b: str):
    if not _is_mod6(a) or not _is_mod6(b):
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
            return "0"
        case ("2", "5"):
            return "1"
        case ("3", "0"):
            return "3"
        case ("3", "1"):
            return "4"
        case ("3", "2"):
            return "5"
        case ("3", "3"):
            return "0"
        case ("3", "4"):
            return "1"
        case ("3", "5"):
            return "2"
        case ("4", "0"):
            return "4"
        case ("4", "1"):
            return "5"
        case ("4", "2"):
            return "0"
        case ("4", "3"):
            return "1"
        case ("4", "4"):
            return "2"
        case ("4", "5"):
            return "3"
        case ("5", "0"):
            return "5"
        case ("5", "1"):
            return "0"
        case ("5", "2"):
            return "1"
        case ("5", "3"):
            return "2"
        case ("5", "4"):
            return "3"
        case ("5", "5"):
            return "4"


def _mod6_negate(a: str):
    if not _is_mod6(a):
        return "UNDEFINED"

    match a:
        case "0":
            return "0"
        case "1":
            return "5"
        case "2":
            return "4"
        case "3":
            return "3"
        case "4":
            return "2"
        case "5":
            return "1"


def _mod6_mul(a: str, b: str):
    if not _is_mod6(a) or not _is_mod6(b):
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
        case ("2", "0"):
            return "0"
        case ("2", "1"):
            return "2"
        case ("2", "2"):
            return "4"
        case ("2", "3"):
            return "0"
        case ("2", "4"):
            return "2"
        case ("2", "5"):
            return "4"
        case ("3", "0"):
            return "0"
        case ("3", "1"):
            return "3"
        case ("3", "2"):
            return "0"
        case ("3", "3"):
            return "3"
        case ("3", "4"):
            return "0"
        case ("3", "5"):
            return "3"
        case ("4", "0"):
            return "0"
        case ("4", "1"):
            return "4"
        case ("4", "2"):
            return "2"
        case ("4", "3"):
            return "0"
        case ("4", "4"):
            return "4"
        case ("4", "5"):
            return "2"
        case ("5", "0"):
            return "0"
        case ("5", "1"):
            return "5"
        case ("5", "2"):
            return "4"
        case ("5", "3"):
            return "3"
        case ("5", "4"):
            return "2"
        case ("5", "5"):
            return "1"


def _mod6_reciprocal(a: str):
    if not _is_mod6(a):
        return "UNDEFINED"

    match a:
        case "0":
            return "UNDEFINED"
        case "1":
            return "1"
        case "2":
            return "UNDEFINED"
        case "3":
            return "UNDEFINED"
        case "4":
            return "UNDEFINED"
        case "5":
            return "5"


if __name__ == "__main__":
    main()
