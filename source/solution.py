"""🎯 Final solution entry point for Longest Substring Without Repeating Characters.

This file keeps the LeetCode-facing `Solution` class small and clean.
The actual implementations live in `approaches.py`, while this file
chooses which approach should be used as the final answer.
"""

from source.approaches import Approaches

class Solution(Approaches):
    """🧩 Thin wrapper that selects the active solving strategy."""

    def lengthOfLongestSubstring(self, s: str) -> int:
        # 📝 Store the input on `self` so the helper methods in `Approaches`
        # can read the same string without passing it around repeatedly.
        self._s = s

        # 🧪 Alternative strategies are kept here for learning and comparison.
        # return self._solve_with_brute_force()
        # return self._solve_with_sliding_window()
        # return self._solve_with_index_map_sliding_window()

        # ⚡ Use the most optimized ASCII-index sliding window by default.
        return self._solve_with_ascii_index_window()
