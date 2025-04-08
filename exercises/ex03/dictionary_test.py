"""Dictionary_test"""

__author__ = "730677063"

from dictionary import invert, count, favorite_color, bin_len


# edge n 2 use tests for invert
def test_invert_take_only() -> None:
    """testing invert edge take only"""
    assert invert({}) == {}


def test_invert_take_1() -> None:
    """testing invert use take 1"""
    assert invert({"a": "im", "b": "here"}) == {"im": "a", "here": "b"}


def test_invert_take_2() -> None:
    """testing invert use take 2"""
    assert invert({"1": "2", "3": "4", "5": "6"}) == {"2": "1", "4": "3", "6": "5"}

    # edge n 2 use tests for invert


def test_count_take_only() -> None:
    """testing count edge take only"""
    assert count([]) == {}


def test_count_take_1() -> None:
    """testing count use take 1"""
    assert count(["potato", "white", "corn", "yellow", "cabbage", "green"]) == {
        "potato": 1,
        "white": 1,
        "corn": 1,
        "yellow": 1,
        "cabbage": 1,
        "green": 1,
    }


def test_count_take_2() -> None:
    """testing count use take 2"""
    assert count(["mama", "mama", "mama"]) == {"mama": 3}

    # edge n 2 use case for favorite_color


def test_favorite_color_take_only() -> None:
    """testing favorite_color edge take only"""
    assert favorite_color({}) == ""


def test_favorite_color_take_1() -> None:
    """testing favorite_color use take 1"""
    assert favorite_color({"maya": "red", "jason": "blue"}) == "red"


def test_favorite_color_take_2() -> None:
    """testing favorite_color use take 2"""
    assert (
        favorite_color(
            {
                "jake": "red",
                "jace": "blue",
                "kevin": "purple",
                "bill": "blue",
                "billy": "red",
                "bob": "blue",
            }
        )
        == "blue"
    )

    # edge n 2 use case for bin_len


def test_bin_len_take_only() -> None:
    """testing bin_len edge take only"""
    assert bin_len([]) == {}


def test_bin_len_take_1() -> None:
    """testing bin_len use take 1"""
    assert bin_len(["hot", "foods", "yes"]) == {
        3: {"hot", "yes"},
        5: {"foods"},
    }


def test_bin_len_take_2() -> None:
    """testing bin_len use take 2"""
    assert bin_len(["why", "why", "fix"]) == {3: {"why", "fix"}}
