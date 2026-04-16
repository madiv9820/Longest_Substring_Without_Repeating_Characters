# Brute Force Approach 🐢

### Intuition 💡

The most direct way to solve this problem is to try **every possible substring** and check whether it contains only **unique characters**.

It is not the fastest approach, but it is a great starting point because it helps us understand the problem clearly before moving to smarter sliding-window solutions.

### Approach 🛠️

1. Start from every index `i` in the string.
2. Extend the substring to every index `j >= i`.
3. For each substring `s[i:j+1]`, check if all characters are unique.
4. If it is valid, update the maximum length found so far.

The uniqueness check can be done by converting the substring into a `set`.

If:

`len(set(substring)) == len(substring)`

then the substring has no duplicate characters. ✅

### Pseudocode 🧾

```text
set answer = 0
set n = length of s

for i from 0 to n - 1:
    for j from i to n - 1:
        substring = s[i to j]

        if size of set(substring) == length of substring:
            answer = max(answer, length of substring)

return answer
```

### Complexity 📊

- **Time Complexity:** `O(n^3)`
- **Space Complexity:** `O(n)`

### Why It’s Slow 🐌

There are many substrings, and for each one we rebuild a set to check uniqueness. That repeated work becomes expensive very quickly as the string grows.

This approach is useful for learning, but not ideal for large inputs. 🚧

---