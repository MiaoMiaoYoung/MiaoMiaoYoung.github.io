---
title: "LeetCode"
date: 2022-01-01T15:01:38+08:00
draft: false
categories:
    - 学习
    - code
    - work
tags:
    - matrix
    - Linear Algebra
    - 从头再来
libraries:
    - katex

enableTocContent: true
---

# A Code A Day Keeps the Regret Away

## 47. Permutations II

> Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
> 
>> Example:
>>
>> Input: nums = [1,1,2]
>>
>> Output: [[1,1,2], [1,2,1], [2,1,1]]

带有重复元素，使用Python中的Counter进行统计计数，这样就可以避免重复选择（相当于进行剪枝）

```python
# nums = [1,1,2]
from collections import Counter
counter = Counter(nums)
# counter = {1:2, 2:1}
```

表示nums数组中，元素1有两个，元素2有一个