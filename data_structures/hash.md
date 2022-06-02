# Hash map / Hash Table
A data structure that can map keys to values. A hash map uses a hash function
to compute an index into an array of buckets or slots, from which the desired
value can be found. Used to map data of an arbitrary size to data of a fixed
size. The values returned by a hash function are called hash values, hash
codes, or simply hashes. If two keys map to the same value, a collision occurs.

Collision Resolution:
-  **Separate Chaining**: each bucket is independent, and contains a list of
	entries for each index. The time for hash map operations is the time to
	find the bucket (constant time), plus the time to iterate through the list.
-  **Open Addressing**: when a new entry is inserted, the buckets are examined,
	starting with the hashed-to-slot and proceeding in some sequence, until an
	unoccupied slot is found. The name open addressing refers to the fact that
	the location of an item is not always determined by its hash value.

Time Complexity:
-  Access: `O(1)`
-  Search: `O(1) or O(n)`
-  Insert: `O(1) or O(n)`
-  Remove: `O(1) or O(n)`

[![Click to watch explanation on YouTube](../images/hash.png?raw=true)](https://www.youtube.com/watch?v=A-ahUVi8pYQ)

## Problems

### Two Sum

[Problem #1](https://leetcode.com/problems/two-sum)

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

Example 1:
```python3
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

Example 2:

```python3
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

Example 3:

```python3
Input: nums = [3,3], target = 6
Output: [0,1]
```

Constraints:
-  `2 <= nums.length <= 104`
-  `-109 <= nums[i] <= 109`
-  `-109 <= target <= 109`
-  Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time
complexity?

</p></details>

<details><summary> Solution
</summary><p>

**Golang**:
 
```go
// TODO(exesse): paste solution here
```

**Python3**:

```python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {}
        for index in range(len(nums)):
            check = target - int(nums[index])
            if check in history:
                return [history[check], index]
            history[int(nums[index])] = index
```

</p></details>
