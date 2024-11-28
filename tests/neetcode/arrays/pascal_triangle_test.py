import pytest

from src.neetcode.arrays.pascal_triangle import Solution


# fmt: off
@pytest.mark.parametrize(
    "row_index, expected",
    [
        (0,  [1]),                                                   # Row 0
        (1,  [1, 1]),                                                # Row 1
        (2,  [1, 2, 1]),                                             # Row 2
        (3,  [1, 3, 3, 1]),                                          # Row 3
        (4,  [1, 4, 6, 4, 1]),                                       # Row 4
        (5,  [1, 5, 10, 10, 5, 1]),                                  # Row 5
        (6,  [1, 6, 15, 20, 15, 6, 1]),                              # Row 6
        (10, [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]),       # Row 10
        (20, [
            1, 20, 190, 1140, 4845, 15504, 38760, 77520, 125970,     # Row 20
            167960, 184756, 167960, 125970, 77520, 38760, 15504,
            4845, 1140, 190, 20, 1,
        ]),
    ],
)
# fmt: on
def test_get_row(row_index, expected):
    assert Solution().getRow(row_index) == expected


@pytest.mark.parametrize(
    "num_rows, expected",
    [
        (1, [[1]]),
        (2, [[1], [1, 1]]),
        (3, [[1], [1, 1], [1, 2, 1]]),
        (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (
            6,
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
                [1, 5, 10, 10, 5, 1],
            ],
        ),
    ],
)
def test_generate_triangle(num_rows, expected):
    assert Solution().generate(num_rows) == expected
