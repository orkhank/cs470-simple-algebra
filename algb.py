import typing as t


class GroupCandidate(t.NamedTuple):
    operation: t.Callable[[str, str], str]
    inverse: t.Callable[[str], str]
    identity: str
    other_elements: tuple[str, ...]


Group = t.NewType("Group", GroupCandidate)
CommutativeGroup = t.NewType("CommutativeGroup", Group)


def check_group_axioms(
    g: GroupCandidate,
) -> tuple[
    t.Literal["CLOSED", "NOT CLOSED"],
    t.Literal["ASSOCIATIVE", "NOT ASSOCIATIVE"],
    t.Literal["IDENTITY VALID", "IDENTITY INVALID"],
    t.Literal["INVERSES VALID", "INVERSES INVALID"],
]:
    # shorthands
    op = g.operation
    e = g.identity
    inv = g.inverse
    elements = frozenset((g.identity, *g.other_elements))

    closed = all((op(a, b) in elements) for a in elements for b in elements)
    associative = all(
        op(op(a, b), c) == op(a, op(b, c))
        for a in elements
        for b in elements
        for c in elements
    )
    identity_valid = all(op(a, e) == op(e, a) == a for a in elements)
    inverses_valid = all(
        inv(a) in elements and op(a, inv(a)) == op(inv(a), a) == e
        for a in elements
    )

    return (
        "CLOSED" if closed else "NOT CLOSED",
        "ASSOCIATIVE" if associative else "NOT ASSOCIATIVE",
        "IDENTITY VALID" if identity_valid else "IDENTITY INVALID",
        "INVERSES VALID" if inverses_valid else "INVERSES INVALID",
    )


def is_group(g: GroupCandidate) -> t.TypeIs[Group]:
    match check_group_axioms(g):
        case ("CLOSED", "ASSOCIATIVE", "IDENTITY VALID", "INVERSES VALID"):
            return True

        case _:
            return False


def is_commutative_group(g: Group) -> t.TypeGuard[CommutativeGroup]:
    op = g.operation
    elements = frozenset((g.identity, *g.other_elements))

    return all(op(a, b) == op(b, a) for a in elements for b in elements)


class RingCandidate(t.NamedTuple):
    add: t.Callable[[str, str], str]
    negate: t.Callable[[str], str]
    multiply: t.Callable[[str, str], str]
    zero: str
    one: str
    other_elements: tuple[str, ...]


Ring = t.NewType("Ring", RingCandidate)
CommutativeRing = t.NewType("CommutativeRing", Ring)


def check_ring_axioms(
    r: RingCandidate,
) -> tuple[
    t.Literal["ADD CLOSED", "ADD NOT CLOSED"],
    t.Literal["ADD ASSOCIATIVE", "ADD NOT ASSOCIATIVE"],
    t.Literal["ADD COMMUTATIVE", "ADD NOT COMMUTATIVE"],
    t.Literal["ADD IDENTITY VALID", "ADD IDENTITY INVALID"],
    t.Literal["ADD INVERSES VALID", "ADD INVERSES INVALID"],
    t.Literal["DISTRIBUTIVE", "NOT DISTRIBUTIVE"],
    t.Literal["MUL CLOSED", "MUL NOT CLOSED"],
    t.Literal["MUL ASSOCIATIVE", "MUL NOT ASSOCIATIVE"],
    t.Literal["MUL IDENTITY VALID", "MUL IDENTITY INVALID"],
]:
    # shorthands
    mul = r.multiply
    add = r.add
    neg = r.negate
    zero = r.zero
    one = r.one
    elements = frozenset((r.one, r.zero, *r.other_elements))

    add_closed = all(
        (add(a, b) in elements) for a in elements for b in elements
    )
    add_associative = all(
        add(add(a, b), c) == add(a, add(b, c))
        for a in elements
        for b in elements
        for c in elements
    )
    add_identity_valid = all(
        add(a, zero) == add(zero, a) == a for a in elements
    )
    add_inverses_valid = all(
        neg(a) in elements and add(a, neg(a)) == add(neg(a), a) == zero
        for a in elements
    )
    add_commutative = all(
        add(a, b) == add(b, a) for a in elements for b in elements
    )

    distributive = all(
        mul(a, add(b, c)) == add(mul(a, b), mul(a, c))
        and mul(add(a, b), c) == add(mul(a, c), mul(b, c))
        for a in elements
        for b in elements
        for c in elements
    )
    mul_closed = all(mul(a, b) in elements for a in elements for b in elements)
    mul_associative = all(
        mul(mul(a, b), c) == mul(a, mul(b, c))
        for a in elements
        for b in elements
        for c in elements
    )
    mul_identity_valid = all(mul(a, one) == mul(one, a) == a for a in elements)

    return (
        "ADD CLOSED" if add_closed else "ADD NOT CLOSED",
        "ADD ASSOCIATIVE" if add_associative else "ADD NOT ASSOCIATIVE",
        "ADD COMMUTATIVE" if add_commutative else "ADD NOT COMMUTATIVE",
        "ADD IDENTITY VALID" if add_identity_valid else "ADD IDENTITY INVALID",
        "ADD INVERSES VALID" if add_inverses_valid else "ADD INVERSES INVALID",
        "DISTRIBUTIVE" if distributive else "NOT DISTRIBUTIVE",
        "MUL CLOSED" if mul_closed else "MUL NOT CLOSED",
        "MUL ASSOCIATIVE" if mul_associative else "MUL NOT ASSOCIATIVE",
        "MUL IDENTITY VALID" if mul_identity_valid else "MUL IDENTITY INVALID",
    )


def is_ring(r: RingCandidate) -> t.TypeIs[Ring]:
    match check_ring_axioms(r):
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
        ):
            return True

        case _:
            return False


def is_commutative_ring(r: Ring) -> t.TypeGuard[CommutativeRing]:
    mul = r.multiply
    elements = frozenset((r.zero, r.one, *r.other_elements))

    return all(mul(a, b) == mul(b, a) for a in elements for b in elements)


class FieldCandidate(t.NamedTuple):
    add: t.Callable[[str, str], str]
    negate: t.Callable[[str], str]
    multiply: t.Callable[[str, str], str]
    multiplicative_inverse: t.Callable[[str], str]
    zero: str
    one: str
    other_elements: tuple[str, ...]


Field = t.NewType("Field", FieldCandidate)


def check_field_axioms(
    f: FieldCandidate,
) -> tuple[
    t.Literal["ADD CLOSED", "ADD NOT CLOSED"],
    t.Literal["ADD ASSOCIATIVE", "ADD NOT ASSOCIATIVE"],
    t.Literal["ADD COMMUTATIVE", "ADD NOT COMMUTATIVE"],
    t.Literal["ADD IDENTITY VALID", "ADD IDENTITY INVALID"],
    t.Literal["ADD INVERSES VALID", "ADD INVERSES INVALID"],
    t.Literal["DISTRIBUTIVE", "NOT DISTRIBUTIVE"],
    t.Literal["MUL CLOSED", "MUL NOT CLOSED"],
    t.Literal["MUL ASSOCIATIVE", "MUL NOT ASSOCIATIVE"],
    t.Literal["MUL IDENTITY VALID", "MUL IDENTITY INVALID"],
    t.Literal["MUL INVERSES VALID", "MUL INVERSES INVALID"],
    t.Literal["NONTRIVIAL", "TRIVIAL"],
]:
    # shorthands
    mul = f.multiply
    reciprocal = f.multiplicative_inverse
    add = f.add
    neg = f.negate
    zero = f.zero
    one = f.one
    elements = frozenset((f.one, f.zero, *f.other_elements))

    add_closed = all(
        (add(a, b) in elements) for a in elements for b in elements
    )
    add_associative = all(
        add(add(a, b), c) == add(a, add(b, c))
        for a in elements
        for b in elements
        for c in elements
    )
    add_identity_valid = all(
        add(a, zero) == add(zero, a) == a for a in elements
    )
    add_inverses_valid = all(
        neg(a) in elements and add(a, neg(a)) == add(neg(a), a) == zero
        for a in elements
    )
    add_commutative = all(
        add(a, b) == add(b, a) for a in elements for b in elements
    )

    distributive = all(
        mul(a, add(b, c)) == add(mul(a, b), mul(a, c))
        and mul(add(a, b), c) == add(mul(a, c), mul(b, c))
        for a in elements
        for b in elements
        for c in elements
    )
    mul_closed = all(mul(a, b) in elements for a in elements for b in elements)
    mul_associative = all(
        mul(mul(a, b), c) == mul(a, mul(b, c))
        for a in elements
        for b in elements
        for c in elements
    )
    mul_identity_valid = all(mul(a, one) == mul(one, a) == a for a in elements)

    # !!
    mul_inverses_valid = all(
        reciprocal(a) in elements
        and mul(a, reciprocal(a)) == mul(reciprocal(a), a) == one
        for a in (one, *f.other_elements)  # exclude zero
    )
    nontrivial = zero != one

    return (
        "ADD CLOSED" if add_closed else "ADD NOT CLOSED",
        "ADD ASSOCIATIVE" if add_associative else "ADD NOT ASSOCIATIVE",
        "ADD COMMUTATIVE" if add_commutative else "ADD NOT COMMUTATIVE",
        "ADD IDENTITY VALID" if add_identity_valid else "ADD IDENTITY INVALID",
        "ADD INVERSES VALID" if add_inverses_valid else "ADD INVERSES INVALID",
        "DISTRIBUTIVE" if distributive else "NOT DISTRIBUTIVE",
        "MUL CLOSED" if mul_closed else "MUL NOT CLOSED",
        "MUL ASSOCIATIVE" if mul_associative else "MUL NOT ASSOCIATIVE",
        "MUL IDENTITY VALID" if mul_identity_valid else "MUL IDENTITY INVALID",
        "MUL INVERSES VALID" if mul_inverses_valid else "MUL INVERSES INVALID",
        "NONTRIVIAL" if nontrivial else "TRIVIAL",
    )


def is_field(f: FieldCandidate) -> t.TypeIs[Field]:
    match check_field_axioms(f):
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
            "MUL INVERSES VALID",
            "NONTRIVIAL",
        ):
            return True

        case _:
            return False


def extract_additive_group(
    s: Field | CommutativeRing | Ring,
) -> CommutativeGroup:
    g = GroupCandidate(
        operation=s.add,
        inverse=s.negate,
        identity=s.zero,
        other_elements=(s.one, *s.other_elements),
    )
    g = Group(g)
    g = CommutativeGroup(g)
    return g


def extract_multiplicative_group(x: Field) -> CommutativeGroup:
    g = GroupCandidate(
        operation=x.multiply,
        inverse=x.multiplicative_inverse,
        identity=x.one,
        other_elements=x.other_elements,  # excludes zero
    )
    g = Group(g)
    g = CommutativeGroup(g)
    return g


Transformation = t.NewType("Transformation", tuple[Group, str])
"""An element in a group."""

ComposablePair = t.NewType(
    "ComposablePair", tuple[Transformation, Transformation]
)
"""Two transformations belonging to the same group."""


def is_transformation(x: tuple[Group, str]) -> t.TypeGuard[Transformation]:
    group, element = x

    return element == group.identity or element in group.other_elements


def are_composable(
    x: tuple[Transformation, Transformation],
) -> t.TypeIs[ComposablePair]:
    (left_group, _), (right_group, _) = x

    return left_group == right_group


def compose(pair: ComposablePair) -> Transformation:
    (g, left), (_, right) = pair
    composition = (g, g.operation(left, right))
    composition = Transformation(composition)
    return composition


def inverse(transformation: Transformation) -> Transformation:
    g, value = transformation
    inverse = (g, g.inverse(value))
    inverse = Transformation(inverse)
    return inverse
