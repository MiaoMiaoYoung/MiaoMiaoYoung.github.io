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

> **Backtracking**

带有重复元素，使用Python中的Counter进行统计计数，这样就可以避免重复选择（相当于进行剪枝）

```python
# nums = [1,1,2]
from collections import Counter
counter = Counter(nums)
# counter = {1:2, 2:1}
```

表示nums数组中，元素1有两个，元素2有一个

```python
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counters = Counter(nums)
        results = []
        
        def search(comb, counter):
            if len(comb) == len(nums):
                results.append(comb.copy())
                return
            
            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -=1
                    search(comb, counter)
                    comb.pop(-1)
                    counter[num] +=1
        
        search([],counters)
        return results
```


## 322. Coin Change

> You are given an integer array coins representing coins of different denominations and an integer amount > representing a total amount of money.
> 
> Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be > made up by any combination of the coins, return -1.
> 
> You may assume that you have an infinite number of each kind of coin.
> 
>> Example:
>> 
>> Input: coins = [1,2,5], amount = 11
>> 
>> Output: 3
>> 
>> Explanation: 11 = 5 + 5 + 1

> **Dynamic Programing**

1. 定义一个状态
    
    一般就是这个问题本身，比如这里求最小的硬币数，那么就把对应币值的最小硬币数作为状态

    (这里的状态数组可能会很大，不要怕，勇敢牛牛，不怕困难)

2. 进行状态递推，得到递推公式

    以硬币为例，先来看最简单的状态，只有1元硬币的情况：

    初始值dp[0] = 0 表示零块钱就需要0枚硬币，那么一块钱的时候就是在0块钱的基础上加1元 dp[1] = dp[0] + 1；两块钱就是在1元的基础上加1元 dp[2] = dp[1] + 1

    那么当有1元和5元两种面额的硬币时：

    如果需要组合5块钱的情况时，就有两种方案，一种是在四块钱的基础上加一张一元 dp[5] = dp[4] + 1，一种是直接拿五块钱 dp[5] = dp[0] + 1

    分析到这里就能得到状态转移方程

    $$dp[i] = min(dp[i], dp[i-coin] + 1)$$

3. 初始化

    dp[0] = 0表示零块钱就需要0枚硬币，而其他应该设置成特别大的值，可以math.inf，或者是设置一个特别大的值

4. 开始递归，返回结果

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [1e5] * (amount+1)
        dp[0] = 0
        
        for coin in coins:
            for i in range (coin, amount + 1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return dp[-1] if dp[-1] != 1e5 else -1
    
```

## 474. Ones and Zeros

> You are given an array of binary strings strs and two integers m and n.
> 
> Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
> 
> A set x is a subset of a set y if all elements of x are also elements of y.
> 
>> Example:
>>
>> Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
>> 
>> Output: 4
>> 
>> Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4. Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}. {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

> **Dynamic Programing**

题目就有点难看懂，最后终于理解了：需要在strs中挑出一个子集，这个子集中所有的0,1分别不能超过m,n，然后要求这个子集包含字符串的数目是最大的，也就是len()

定义状态：dp[ ]记录当前子集包含的字符串数目，重要的是状态是什么？dp[ ]应该是一个m*n的数组，状态是当前子集已经包含了的0,1

然后的话就是遍历所有的字符串元素，然后遍历状态的表进行选择

遍历的话其实还有一个要点，就是这个题里面这些字符串是只有一个，不能无限取，如果正向遍历的话就会导致前面硬币的问题，我已经拿1枚硬币了，但是我还能重复拿一枚硬币组成2元，所以这里可以采用倒序的遍历方式

```python
import math
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counters = [[s.count('0'),s.count('1')] for s in strs]
        dp = [[0 for _ in range(n+1)] for _ in range(m +1)]
        
        for zero, one in counters:
            for i in range(m, zero-1, -1):
                for j in range(n, one-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zero][j-one]+1)
        
        
        return dp[-1][-1] 
```
