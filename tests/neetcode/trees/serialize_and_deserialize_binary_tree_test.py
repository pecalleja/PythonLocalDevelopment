import pytest

from src.common import TreeNode
from src.neetcode.trees.serialize_and_deserialize_binary_tree import Codec


def trees_are_equal(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    return (
        tree1.val == tree2.val
        and trees_are_equal(tree1.left, tree2.left)
        and trees_are_equal(tree1.right, tree2.right)
    )


# fmt: off
@pytest.mark.parametrize(
    "tree, serialized",
    [
        (
            None,
            "null"
        ),
        (
            TreeNode(1),
            "1,null,null"),
        (
            TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5))),  # noqa
            "1,2,3,null,null,4,5,null,null,null,null",
        ),
        (
            TreeNode(1, None, TreeNode(2, TreeNode(3))),
            "1,null,2,3,null,null,null",
        ),
    ],
)
# fmt: on
def test_codec(tree, serialized):
    codec = Codec()

    # Test serialization
    assert codec.serialize(tree) == serialized

    # Test deserialization and re-serialization for round-trip accuracy
    deserialized_tree = codec.deserialize(serialized)
    assert trees_are_equal(tree, deserialized_tree)
    assert codec.serialize(deserialized_tree) == serialized
