# Sliding Window with Index Map 🚀

### Intuition 💡

The set-based sliding window works well, but when a duplicate appears, it removes characters **one by one** from the left.

We can do better by storing the **index** of each character in the current window. That way, when a duplicate appears, we know exactly how far the left side needs to move.

More information means smarter jumps. 🎯

### Approach 🛠️

1. Use two pointers:
   `left_Pointer` and `right_Pointer`
2. Keep a dictionary that maps each character to its latest index in the active window.
3. If the current character is not already active in the map:
   store its index, expand the window, and update the answer.
4. If it is already present:
   find the old index of that duplicate.
5. Remove every character from the map from `left_Pointer` up to that duplicate index.
6. Move `left_Pointer` past the duplicate and continue.

This keeps the window valid while giving us more control than a plain set. 🧠

### Pseudocode 🧾

```text
set answer = 0
set left = 0
set right = 0
set active_indices = empty map

while right < length of s:
    current = s[right]

    if current is not in active_indices:
        active_indices[current] = right
        right = right + 1
        answer = max(answer, right - left)
    else:
        duplicate_index = active_indices[current]

        while left <= duplicate_index:
            remove s[left] from active_indices
            left = left + 1

return answer
```

### Complexity 📊

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Why It’s Interesting 🔍

This version is a nice bridge between the basic sliding window and the most optimized one. It still maintains a clean window, but now it remembers where characters came from.

That added memory helps us reason about duplicates more precisely. 📌

---