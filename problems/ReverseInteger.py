class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x *= -1
        reversed_x = int(''.join(reversed(list(str(x)))))
        reversed_x *= (-1 if is_negative else 1)
        return reversed_x if reversed_x in range(-2 ** 31, 2 ** 31) else 0
