# DSA Practice

Personal 4-week data structures & algorithms practice log — solved problems with my own notes on reasoning, plus hand-rolled implementations of core data structures (no built-in `dict`/`sort`/etc. where the point is to learn the internals).

Goal: build solid logic fundamentals as a base for lower-level systems work (CUDA, kernel/driver dev, graphics).

## Structure

```
dsa-practice/
├── week1-arrays-strings/     # arrays, strings, two pointers, basic recursion
├── week2-hashtable-linkedlist/  # hash tables, linked lists, stacks, queues
├── week3-trees-graphs/       # binary trees, BST, BFS/DFS
├── week4-dp/                 # dynamic programming intro
└── data-structures/          # hand-rolled implementations from scratch
```

Each problem gets its own file: `NN_problem_name.py`. Every file has:
1. The problem statement (short, in my own words)
2. My first approach / where I got stuck
3. The final solution with comments explaining *why*, not just what

## Progress Tracker

### Week 1 — Arrays, Strings, Two Pointers, Recursion
- [✓] Two Sum
- [✓] Valid Anagram
- [✓] Contains Duplicate
- [✓] Valid Palindrome
- [ ] Best Time to Buy and Sell Stock
- [ ] Longest Substring Without Repeating Characters
- [ ] Hand-roll: Bubble Sort
- [ ] Hand-roll: Merge Sort

### Week 2 — Hash Tables, Linked Lists, Stack/Queue
- [ ] Group Anagrams
- [ ] Top K Frequent Elements
- [ ] Valid Parentheses
- [ ] Reverse Linked List
- [ ] Merge Two Sorted Lists
- [ ] Linked List Cycle
- [ ] Hand-roll: Hash Table (with collision handling)
- [ ] Hand-roll: Singly Linked List (insert/delete/reverse)

### Week 3 — Trees, Graphs
- [ ] Invert Binary Tree
- [ ] Maximum Depth of Binary Tree
- [ ] Same Tree
- [ ] Validate Binary Search Tree
- [ ] Binary Tree Level Order Traversal
- [ ] Number of Islands (BFS/DFS on a grid)
- [ ] Hand-roll: Binary Search Tree (insert/search/in-order traversal)
- [ ] Hand-roll: BFS + DFS on a simple graph

### Week 4 — Dynamic Programming
- [ ] Climbing Stairs
- [ ] House Robber
- [ ] Coin Change
- [ ] Longest Common Subsequence
- [ ] Write-up: what I learned this month (link it from this README)

## Notes

- Solving on [LeetCode](https://leetcode.com), following the [NeetCode 150](https://neetcode.io/practice) list roughly in this order.
- Language: Python for now (fastest to focus on logic, not syntax). May redo select problems in C/C++ later since that's closer to what systems/driver roles actually use.
