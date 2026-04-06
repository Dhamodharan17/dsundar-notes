# Stack Problems

This file is reserved for stack-related problem notes, solutions, and references.

## Section Links

- Notion Stack Notes:


## Monotonic Stack Basics

- Monotonic Increasing Stack: Keep elements in increasing order; pop while top is greater than current.
- Monotonic Decreasing Stack: Keep elements in decreasing order; pop while top is smaller than current.

```python
# Example: next greater element
def next_greater():
    num = [10, 9, 8, 14, 20, 1, 11]
    nge = [-1] * len(num)
    stack = []  # stores indices

    n = len(num)
    # next greater is on the right, so traverse from right to left
    for i in range(n - 1, -1, -1):
        while stack and num[stack[-1]] <= num[i]:
            stack.pop()

        nge[i] = -1 if not stack else num[stack[-1]]
        stack.append(i)

    print(*nge)

```

```python
# Example: previous smaller element
def prev_smaller():
    num = [2, 3, 4, 1, 2, 3, 5]
    pse = [-1] * len(num)
    stack = []  # stores indices

    # previous smaller is on the left, so traverse left to right
    for i in range(len(num)):
        # remove all larger/equal values; they cannot be previous smaller
        while stack and num[stack[-1]] >= num[i]:
            stack.pop()

        pse[i] = -1 if not stack else num[stack[-1]]
        stack.append(i)

    print(*pse)

```

## V.V.V IMPORTANT

When an index is popped, that bar becomes the limiting minimum for one maximal width.
```python
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # increasing stack of indices
        maxi = 0
        n = len(heights)

        for i in range(n + 1):
            cur = 0 if i == n else heights[i]  # sentinel to flush stack

            # Current bar breaks the increasing condition.
            # Compute areas for bars that can no longer extend to the right.
            while stack and heights[stack[-1]] >= cur:

                ind = stack.pop()
                # Popped bar is the limiting (minimum) height for its valid span.
                h = heights[ind]

                # Rectangle spans from left_smaller + 1 to i - 1.
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1

                maxi = max(maxi, h * w)

            stack.append(i)

        return maxi
```

<details>
<summary>Why popped height is used (Histogram intuition)</summary>

Good thinking, but for histogram this is the key:

In an increasing stack, stack[-1] is larger than earlier bars, yes.
But when we pop one bar h, we are not taking a rectangle over whole stack start to top.

We compute rectangle where popped bar h is the minimum across its valid span.

So no, we do not take min(stack start, stack top).

What boundaries mean at pop time:

1. Current index i is first smaller on right of h.
2. New stack top after pop is first smaller on left of h.
3. Therefore every bar between those boundaries has height >= h.
4. So rectangle height is exactly h (popped height), not min of stack endpoints.

Why endpoint-min idea fails:

- Endpoints are just two bars; minimum rectangle height depends on all bars in the range.
- Stack method already encoded this by popping until smaller boundaries are found.

Short rule to remember:

When an index is popped, that bar becomes the limiting minimum for one maximal width.

</details>


## Stack Problem Solving

### Patterns

- Balanced Brackets: Push opening brackets, and match/validate on closing brackets.
- Next Greater/Smaller Element: Use monotonic stack to track candidates efficiently.
- Expression Evaluation: Use one or two stacks for operands/operators.
- Undo/Backtracking: Store previous states or actions in stack form.
- DFS (Iterative): Replace recursion with an explicit stack.

### Problem Tracker

| S.No | Problem Name | Hint | Solution Link | Reference |
|---|---|---|---|---|
| 1 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Push opening chars, pop and validate on closing chars |  |  |
| 2 | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | Build next-greater map using decreasing stack |  |  |
| 3 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Keep indices in decreasing temperature order |  |  |
| 4 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Use increasing stack with sentinel to compute width |  |  |
