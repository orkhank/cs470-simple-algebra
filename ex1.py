import typing as t

import algb


def main():
    add_mod6 = algb.GroupCandidate(
        operation=_mod6_add,
        inverse=_mod6_negate,
        identity="0",
        other_elements=("1", "2", "3", "4", "5"),
    )

    match algb.check_group_axioms(add_mod6):
        case (
            "CLOSED",
            "ASSOCIATIVE",
            "IDENTITY VALID",
            "INVERSES VALID",
        ):
            pass

        case _:
            raise AssertionError

    assert algb.is_group(add_mod6)
    assert algb.is_commutative_group(add_mod6)

    _ = t.assert_type(add_mod6, "algb.CommutativeGroup")

    add2_mod6 = (add_mod6, "2")
    assert algb.is_transformation(add2_mod6)

    _ = t.assert_type(add2_mod6, "algb.Transformation")

    sub2_mod6 = algb.inverse(add2_mod6)
    assert sub2_mod6 == (add_mod6, "4")
    assert algb.inverse(sub2_mod6) == add2_mod6

    _2sub2_mod6 = sub2_mod6, add2_mod6
    assert algb.are_composable(_2sub2_mod6)
    assert algb.compose(_2sub2_mod6) == (add_mod6, "0")

    _ = t.assert_type(_2sub2_mod6, "algb.ComposablePair")
    _ = t.assert_type(algb.compose(_2sub2_mod6), "algb.Transformation")


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


if __name__ == "__main__":
    main()
