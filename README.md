# Minimum Steps to Group All Black Balls to the Right

## 🧩 Problem Description

There are `n` balls on a table, each colored either **black** or **white**.

You are given a **0-indexed binary string** `s` of length `n`, where:

- `'1'` represents a **black** ball  
- `'0'` represents a **white** ball  

In one step, you may choose **two adjacent balls** and swap them.

https://thita.ai/problems/separate-black-and-white-balls

Your task is to return the **minimum number of steps** required to group:

- All **white balls (`0`) to the left**
- All **black balls (`1`) to the right**

---

## 📌 Examples

### Example 1

**Input:**
s = "101"


**Output:**
1


**Explanation:**

Swap `s[0]` and `s[1]`:

"101" → "011"


All black balls are now grouped to the right.

---

### Example 2

**Input:**

s = "100"


**Output:**

2


**Explanation:**

"100" → swap(0,1) → "010"
"010" → swap(1,2) → "001"

---

## 📋 Constraints

- `1 <= n == s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`

---

## 💡 Approach

### Counting Inversions (Greedy Observation)

To group all black balls (`1`) to the right, every time a black ball appears **before** a white ball (`"10"` pattern), it must eventually be swapped.

Each such pair represents **one required swap**.

### Efficient Strategy

1. Traverse the string from left to right.
2. Keep track of how many `'1'`s (black balls) have been seen so far.
3. When you encounter a `'0'`:
   - It must pass all previously seen `'1'`s.
   - Add the number of seen `'1'`s to the total steps.

This works because each white ball must cross all black balls that appear before it.

---

## 🧠 Why This Works

Each swap reduces one inversion (`"10"` pair).

The total number of swaps needed equals the total number of such inversions in the string.

Instead of physically simulating swaps (which would be too slow), we simply **count the inversions directly** in one pass.

---

## ⏱️ Time & Space Complexity

- **Time Complexity:** `O(n)`  
  Single pass through the string.

- **Space Complexity:** `O(1)`  
  Only counters are used.

---

## ✅ Summary

- Each `"10"` pair requires one swap.
- Count how many black balls appear before each white ball.
- Add them up to get the minimum number of steps.
- Efficient `O(n)` solution for large inputs up to `10^5`.

---
