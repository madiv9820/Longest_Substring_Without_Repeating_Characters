# Sliding Window with ASCII Table ⚡

### Intuition 💡

This is the fastest and cleanest version in this project.

Instead of using a dynamic set or dictionary, we use a **fixed-size array** where each position stores the latest index of an ASCII character.

That means:
- lookup is fast
- updates are fast
- and when we see a duplicate, we can jump the left pointer directly

It is a sharp, optimized sliding-window solution. 🏎️

### Approach 🛠️

1. Create an array of size `128` filled with `-1`.
2. Each index represents one ASCII character.
3. Use `left_Pointer` and `right_Pointer` to track the current window.
4. For each character:
   find its previously seen index from the array.
5. If that old index is still inside the current window:
   move `left_Pointer` directly to `old_index + 1`.
6. Update the current character’s latest index.
7. Measure the current valid window length.

The big win is that we **jump** instead of shrinking one step at a time. 🎯

### Pseudocode 🧾

```text
set answer = 0
set left = 0
set last_seen = array of size 128 filled with -1

for right from 0 to length of s - 1:
    current = s[right]
    current_index = ASCII value of current

    if last_seen[current_index] >= left:
        left = last_seen[current_index] + 1

    last_seen[current_index] = right
    answer = max(answer, right - left + 1)

return answer
```

### Complexity 📊

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Why This One Wins 🏆

Every character is processed once, and duplicate handling becomes extremely efficient.

That is why this is the best fit for the final implementation in `solution.py`. ✅

---