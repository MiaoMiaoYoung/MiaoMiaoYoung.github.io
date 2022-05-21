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