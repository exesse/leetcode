# Data Structures and Algorithms
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/d48797b58ac24b858c3c508c544b0cfa)](https://www.codacy.com/gh/exesse/leetcode/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=exesse/leetcode&amp;utm_campaign=Badge_Grade)
[![Python](https://github.com/exesse/leetcode/actions/workflows/py_actions.yml/badge.svg)](https://github.com/exesse/leetcode/actions/workflows/py_actions.yml)
[![Go](https://github.com/exesse/leetcode/actions/workflows/go_actions.yml/badge.svg)](https://github.com/exesse/leetcode/actions/workflows/go_actions.yml)

Fun way to learn **Algorithms** and **Data Structures** by solving
[LeetCode](https://leetcode.com) problems. 

## Table of Contents
- [Data Structures](#data-structures)
  -  [Array](#array)
  -  [Hash Map](#hash-map)

-  [Algorithms](#algorithms)
   -  [Breadth First Search](#breadth-first-search)
   -  [Depth First Search](#depth-first-search)

## Data Structures
### Array
A a data structure consisting of a collection of elements (values or variables),
each identified by at least one array index or key.

**Time Complexity**:
-  Access: `O(1)`
-  Search: `O(n)`
-  Insert: `O(n)`
-  Remove: `O(n)`

[![Click to watch explanation on YouTube](images/array.gif?raw=true)](https://www.youtube.com/watch?v=OnPP5xDmFv0)

**Problems**:
-  [1. Two Sum](https://leetcode.com/problems/two-sum) | Solution in [go](solutions/1/solution_1.go), [python3](solutions/1/solution_1.py)

### Linked List
A linear collection of data elements, called nodes, each pointing to the next
node by means of a pointer. It is a data structure consisting of a group of
nodes which together represent a sequence. Possible types are:

-  *Singly-linked list*: linked list in which each node points to the next
    node and the last node points to null.

-  *Doubly-linked list*: linked list in which each node has two pointers, p
    and n, such that p points to the previous node and n points to the next
    node; the last node's n pointer points to null.

-  *Circular-linked list*: linked list in which each node points to the next
    node and the last node points back to the first node.

**Time Complexity**:
-  Access: `O(n)`
-  Search: `O(n)`
-  Insert: `O(1)`
-  Remove: `O(1)`

[![Click to watch explanation on YouTube](images/llist.gif?raw=true)](https://www.youtube.com/watch?v=zxkpZrozDUk)

### Hash Map
A data structure that can map keys to values. A hash map uses a hash function
to compute an index into an array of buckets or slots, from which the desired
value can be found. Used to map data of an arbitrary size to data of a fixed
size. The values returned by a hash function are called hash values, hash
codes, or simply hashes. If two keys map to the same value, a collision occurs.

**Collision Resolution**:
-  *Separate Chaining*: each bucket is independent, and contains a list of
	entries for each index. The time for hash map operations is the time to
	find the bucket (constant time), plus the time to iterate through the list.

-  *Open Addressing*: when a new entry is inserted, the buckets are examined,
	starting with the hashed-to-slot and proceeding in some sequence, until an
	unoccupied slot is found. The name open addressing refers to the fact that
	the location of an item is not always determined by its hash value.

**Time Complexity**:
-  Access: `O(1)`
-  Search: `O(1) or O(n)`
-  Insert: `O(1) or O(n)`
-  Remove: `O(1) or O(n)`

[![Click to watch explanation on YouTube](images/hash.png?raw=true)](https://www.youtube.com/watch?v=A-ahUVi8pYQ)

**Problems**:
-  [1. Two Sum](https://leetcode.com/problems/two-sum) | Solution in [go](solutions/1/solution_1.go), [python3](solutions/1/solution_1.py)

## Algorithms
### Breadth First Search
A graph traversal algorithm which explores the neighbor nodes first, before
moving to the next level neighbors.

**Time Complexity**: `O(|V| + |E|)`

[![Click to watch explanation on YouTube](images/bfs.gif?raw=true)](https://www.youtube.com/watch?v=pol4kGNlvJA)

### Depth First Search
A graph traversal algorithm which explores as far as possible along each branch
before backtracking.

**Time Complexity**: `O(|V| + |E|)`

[![Click to watch explanation on YouTube](images/dfs.gif?raw=true)](https://www.youtube.com/watch?v=wp5ohHFTieM)

**Problems**:
-  [200. Number of Islands](https://leetcode.com/problems/number-of-islands) | Solution in [go](solutions/200/solution_200.go), [python3](solutions/200/solution_200.py)
