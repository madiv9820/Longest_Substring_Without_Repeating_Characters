# Sliding Window with Set 🪟

### Intuition 💡

Instead of checking every substring from scratch, we can keep a **moving window** that always contains **unique characters**.

If the next character is safe to include, we expand the window.
If it creates a duplicate, we shrink the window from the left until it becomes valid again.

This saves a lot of repeated work compared to brute force. 🚀

### Approach 🛠️

1. Use two pointers:
   `left_Pointer` for the start of the window  
   `right_Pointer` for the end of the window
2. Keep a `set` of characters currently inside the window.
3. If `s[right_Pointer]` is not in the set:
   add it, expand the window, and update the answer.
4. If it is already in the set:
   remove `s[left_Pointer]` and move `left_Pointer` forward.
5. Continue until `right_Pointer` reaches the end of the string.

The key idea is that the current window is always kept valid before measuring it. 🎯

### Pseudocode 🧾

```text
set answer = 0
set left = 0
set right = 0
set seen = empty set

while right < length of s:
    if s[right] is not in seen:
        add s[right] to seen
        right = right + 1
        answer = max(answer, right - left)
    else:
        remove s[left] from seen
        left = left + 1

return answer
```

### Complexity 📊

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Why It’s Better ✨

Each character enters the set at most once and leaves at most once, so we avoid rechecking the same work again and again.

This is the classic sliding-window version and a strong interview-friendly solution. 💪

---