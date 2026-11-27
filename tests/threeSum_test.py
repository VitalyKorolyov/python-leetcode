from importlib import import_module

import pytest

Solution = import_module("solutions.3sum").Solution


def _assert_triplets_equal(actual, expected):
    actual_triplets = sorted(tuple(sorted(triplet)) for triplet in actual)
    normalized_expected = sorted(tuple(sorted(triplet)) for triplet in expected)
    assert actual_triplets == normalized_expected


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        pytest.param(
            [-1, 0, 1, 2, -1, -4],
            [(-1, -1, 2), (-1, 0, 1)],
            id="standard-example",
        ),
        pytest.param(
            [-2, 0, 1, 1, 2],
            [(-2, 0, 2), (-2, 1, 1)],
            id="two-triplets",
        ),
        pytest.param([0, 0, 0, 0], [(0, 0, 0)], id="duplicate-zeros"),
        pytest.param([1, 2, -2, -1], [], id="no-solution"),
        pytest.param([], [], id="empty-input"),
        pytest.param([0, 0], [], id="fewer-than-three-values"),
    ],
)
def test_three_sum_returns_expected_unique_triplets(nums, expected):
    result = Solution().threeSum(nums)

    _assert_triplets_equal(result, expected)
    assert all(len(triplet) == 3 and sum(triplet) == 0 for triplet in result)
    assert len({tuple(sorted(triplet)) for triplet in result}) == len(result)
