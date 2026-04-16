"""🧠 Approaches for Longest Substring Without Repeating Characters.

This file groups multiple ways to solve the same problem, beginning with
the most direct brute-force idea and gradually improving it into efficient
sliding-window solutions.

Why this file exists:
- to compare different strategies in one place
- to show how the same problem can be optimized step by step
- to keep the final `solution.py` small while preserving learning notes
"""

from typing import Set, Dict, List

class Approaches:
    """📚 Helper class containing all supported solving strategies."""

    def _solve_with_brute_force(self) -> int:
        """🐢 Brute-force approach.

        Idea:
        Check every possible substring and keep the longest one whose
        characters are all unique.

        How it works:
        For every start index `i`, try every end index `j`. For each
        substring `self._s[i : j + 1]`, compare its length with the size
        of its set. If both match, the substring has no duplicates.

        Complexity:
        Time  : O(n^3) in the worst case because slicing and set creation
                are repeated for every `(i, j)` pair.
        Space : O(n) for the temporary set built from a substring.
        """
        # 🏆 Stores the best duplicate-free substring length found so far.
        max_Substring_Length: int = 0

        # 📏 Total number of characters in the input string.
        n: int = len(self._s)
        
        for i in range(n):
            # 🚩 Starting index of the current candidate substring.
            for j in range(i, n):
                # 🏁 Ending index of the current candidate substring.
                # 🔍 A substring is valid only when all of its characters
                # remain unique after converting it into a set.
                if len(set(self._s[i : j + 1])) == (j - i + 1):
                    # 📈 Compare this valid substring with the best answer seen so far.
                    max_Substring_Length = max(max_Substring_Length, j - i + 1)

        return max_Substring_Length
    
    def _solve_with_sliding_window(self) -> int:
        """🪟 Sliding-window approach with a set.

        Idea:
        Maintain a window that always contains unique characters.

        How it works:
        `right_Pointer` tries to grow the window by adding the next
        character. If that character is not already present, the window
        stays valid and we update the answer. If it is a duplicate,
        `left_Pointer` moves forward and removes characters from the set
        until the duplicate disappears.

        Complexity:
        Time  : O(2n), which is effectively O(n), because each character is
                added to and removed from the set at most once.
        Space : O(n) for the set of characters in the current window.
        """
        # 🏆 Tracks the longest valid window seen during the scan.
        max_Substring_Length: int = 0
        
        # 👈 Left boundary of the current window.
        left_Pointer: int = 0
        
        # 👉 Right boundary of the current window. This is the next index
        # we want to try to include.
        right_Pointer: int = 0
        
        # 📏 Length of the input string.
        n: int = len(self._s)
        
        # 🧺 Holds all unique characters currently inside the window.
        unique_Characters: Set[str] = set()

        while right_Pointer < n:
            if self._s[right_Pointer] not in unique_Characters:
                # ✅ Safe to grow the window because the new character
                # does not break uniqueness.
                unique_Characters.add(self._s[right_Pointer])
                right_Pointer += 1
                # 📐 Window length is `right_Pointer - left_Pointer`
                # because `right_Pointer` is treated as exclusive.
                max_Substring_Length = max(max_Substring_Length, right_Pointer - left_Pointer)
            else:
                # ✂️ Shrink from the left until the duplicate character is
                # removed from the current window.
                unique_Characters.remove(self._s[left_Pointer])
                left_Pointer += 1

        return max_Substring_Length
    
    def _solve_with_index_map_sliding_window(self) -> int:
        """🚀 Sliding window with a character-to-index map.

        Idea:
        Track the characters inside the current window together with the
        indices where they appear.

        How it works:
        If the next character is not active in the map, extend the window.
        If it is already present, find its earlier index and remove every
        character from the left side up to that index. This restores the
        invariant that the current window contains no duplicates.

        Complexity:
        Time  : O(n), because each character enters and leaves the map at
                most once.
        Space : O(n) for the active characters stored in the map.
        """
        # 🏆 Best duplicate-free window length found so far.
        max_Substring_Length: int = 0

        # 👈 Left edge of the active sliding window.
        left_Pointer: int = 0
        
        # 👉 Right edge of the active sliding window.
        right_Pointer: int = 0
        
        # 📏 Number of characters in the input string.
        n: int = len(self._s)
        
        # 🗺️ Maps each character in the current window to its latest index.
        substring_Characters_With_Indices: Dict[str, int] = {}

        while right_Pointer < n:
            if substring_Characters_With_Indices.get(self._s[right_Pointer], -1) == -1:
                # 📌 Record the latest index of the current character and
                # continue expanding the valid window.
                substring_Characters_With_Indices[self._s[right_Pointer]] = right_Pointer
                right_Pointer += 1
                # 📐 The active window stays duplicate-free, so its size is valid.
                max_Substring_Length = max(max_Substring_Length, right_Pointer - left_Pointer)
            else:
                # ⏭️ The duplicate blocks the current expansion, so remove
                # everything from the left up to its previous occurrence.
                # 📍 This is the index of the earlier conflicting character.
                skip_Till_Index: int = substring_Characters_With_Indices[self._s[right_Pointer]]
                while left_Pointer <= skip_Till_Index:
                    # 🧹 Remove characters that are no longer inside
                    # the rebuilt window.
                    substring_Characters_With_Indices.pop(self._s[left_Pointer])
                    left_Pointer += 1
        
        return max_Substring_Length
    
    def _solve_with_ascii_index_window(self) -> int:
        """⚡ Optimized sliding window with an ASCII index table.

        Idea:
        Replace the dynamic set/map with a fixed-size array where each slot
        stores the latest index of an ASCII character.

        How it works:
        When we visit a character, we check the last index where it appeared.
        If that earlier index is still inside the current window, we jump
        `left_Pointer` directly to one position after it. Then we update the
        character's latest index and measure the current valid window.

        Complexity:
        Time  : O(n), because every character is processed once.
        Space : O(1), because the ASCII table has fixed size.
        """
        # 🏆 Stores the maximum valid window length seen so far.
        max_Substring_Length: int = 0

        # 👈 Start index of the current duplicate-free window.
        left_Pointer: int = 0
        
        # 👉 Current scanning position in the string.
        right_Pointer: int = 0
        
        # 📏 Total length of the string.
        n: int = len(self._s)
        
        # 🔢 Fixed-size table where each ASCII character stores its latest
        # seen index, or `-1` if it has not appeared yet.
        substring_Characters_With_Indices: List[int] = [-1] * 128

        while right_Pointer < n:
            # 🔤 Character currently being processed.
            current_Character: str = self._s[right_Pointer]
            if (
                    substring_Characters_With_Indices[ord(current_Character)] != -1
                and substring_Characters_With_Indices[ord(current_Character)] >= left_Pointer
            ):
                # 🎯 Jump over the earlier duplicate instead of shrinking
                # one step at a time.
                left_Pointer = substring_Characters_With_Indices[ord(current_Character)] + 1
            
            # 📝 Store the current index so future duplicates can be resolved
            # in constant time.
            substring_Characters_With_Indices[ord(current_Character)] = right_Pointer
            right_Pointer += 1
            # 📐 Measure the current duplicate-free window after any needed jump.
            max_Substring_Length = max(max_Substring_Length, right_Pointer - left_Pointer)
        
        return max_Substring_Length
