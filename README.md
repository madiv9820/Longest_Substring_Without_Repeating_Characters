# Longest Substring Without Repeating Characters 🔡

Given a string `s`, find the **length of the longest substring** that contains **no duplicate characters**.

### Problem Statement 📘

A **substring** is a **continuous** part of a string.

Your goal is to scan the string and find the longest stretch where every character appears **only once**.

Important:
- We need a **substring**, not a subsequence
- Characters must stay **contiguous**
- Repeated characters break the current valid window

### Examples 💡

#### Example 1
**Input:** `s = "abcabcbb"`  
**Output:** `3`

**Explanation:**  
The longest substring without repeating characters is `"abc"` with length **3**.  
`"bca"` and `"cab"` also work, but the maximum length is still **3** ✅

#### Example 2
**Input:** `s = "bbbbb"`  
**Output:** `1`

**Explanation:**  
The longest valid substring is just `"b"` because every next character repeats immediately 🔁

#### Example 3
**Input:** `s = "pwwkew"`  
**Output:** `3`

**Explanation:**  
One valid answer is `"wke"` with length **3**.  
`"pwke"` is a **subsequence**, not a substring, so it does **not** count 🚫

### Constraints 📏

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces


### In Short 📝

Find the longest **continuous** part of the string where **no character repeats**.

### Approach Comparison 📊

| Approach | Time Complexity | Space Complexity | Key Idea | Verdict |
| --- | --- | --- | --- | --- |
| Brute Force 🐢 | `O(n^3)` | `O(n)` | Check every possible substring | Good for learning, not for large inputs |
| Sliding Window with Set 🪟 | `O(n)` | `O(n)` | Expand and shrink a unique-character window | Clean and interview-friendly |
| Sliding Window with Index Map 🚀 | `O(n)` | `O(n)` | Track character positions for smarter duplicate handling | More precise than a plain set |
| Sliding Window with ASCII Table ⚡ | `O(n)` | `O(1)` | Use fixed-size last-seen indices for direct jumps | Fastest and best final choice 🏆 |

### Approach Guides 🗂️

- [Brute Force Approach 🐢](docs/brute_force/README.md)
- [Sliding Window with Set 🪟](docs/sliding_window_set/README.md)
- [Sliding Window with Index Map 🚀](docs/sliding_window_index_map/README.md)
- [Sliding Window with ASCII Table ⚡](docs/sliding_window_ascii_table/README.md)

---
