## Problem

Implement a doubly circular linked list with non-negative integers. Each integer represents the height of a mountain. For example, (1->2->3->4->5), (2->3->4->5->1), (4->3->2->1->5) are all possible ways of traversing from node to node.

For 2 mountains to be mutually visible, they need to meet the requirements:

1. `A` and `B` must not be the same mountain

2. When `A` and `B` are adjacent, they definitely can see each other

3. When `A` and `B` are not adjacent, `A` and `B` are vible to each other if all mountains between them are shorter or equal to the `min(height_of_A, height_of_B)`.

Implement a class method `visible_mountain_pairs(self) -> int` which returns total number of unique visible mountain pairs in the current `CircularLinkedList`.

Assume that the CircularLinkedList will always have at least 2 nodes.

## Examples

(4->2->2->5->1) has 8 pairs: (4, 2), (4, 2), (4, 5), (2, 2), (2, 5), (2, 5), (5, 1), (1, 4)

(1->5->3->4->2) has 7 pairs: (1, 5), (5, 2), (5, 3), (5, 4), (3, 4), (4, 2), (2, 1)

(1->5->6->4->2) has 7 pairs: (1, 5), (5, 6), (6, 4), (4, 2), (4, 5), (2, 1), (2, 5)