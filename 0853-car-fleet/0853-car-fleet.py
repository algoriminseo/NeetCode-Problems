class Solution:
    # Constraints:
    # n == position.length == speed.length
    # 1 <= n <= 10 ^5
    # 0 <= target <= 10^6
    # 0 <= position[i] < target
    # All values in position are unique
    # 0 < speed[i] <= 10^5
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            stack.append((target - p ) /s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        