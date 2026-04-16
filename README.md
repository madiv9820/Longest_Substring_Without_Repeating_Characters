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

---