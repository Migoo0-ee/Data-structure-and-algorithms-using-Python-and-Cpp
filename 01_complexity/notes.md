

````
---
tags:
  - dsa
  - computer-science
  - notes
date: 2026-09-04
---

# 1. Introduction to Data Structures & Algorithms

## What's the DS?
It is data organization, management, and storage format that enables efficient access and modifications.

## DS Classification
```mermaid
graph TD
    DS[Data Structures] --> Linear[Linear]
    DS --> NonLinear[Non-Linear]
````

### 1. Linear Data Structures

- **Definition:** Elements are sequentially ordered. Each element is connected to its previous and next element (except the first and last).
    
- **Examples:** `Array`, `Linked List`, `Stack`, `Queue`.
    

### 2. Non-Linear Data Structures

- **Definition:** Non-sequentially ordered. They are linked together in a hierarchical or network-like manner. So, one element can be linked to one or more elements at the same time.
    
- **Examples:** `Tree`, `Graph`.
    

# 2. Complexity Analysis

Code snippet

```
graph TD
    Complexity --> Time[Time Complexity]
    Complexity --> Space[Space Complexity]
```

- **Time Complexity:** How much the code will take to perform the required info/operations.
    
- **Space Complexity:** How much the code will consume (memory) to perform the requirements.
    

> [!NOTE] In our life right now, we focus on **Time Complexity** more than **Space Complexity**, because all of us almost have good devices (high RAM/storage).

## Asymptotic Notations (Complexity Measuring Units)

- **Best Case:** Ω (Omega Notation) - Minimum time/resources required.
    
- **Average Case:** Θ (Theta Notation) - Expected time/resources for typical input.
    
- **Worst Case:** O (Big O Notation) - Maximum time/resources required (upper bound).
    

## Complexity of Basic Operations & Control Flow

- Basic arithmetic operations (`+`, `-`, `*`, `/`, `+=`, `-=`, etc.), variable assignments, and conditional statements (`if`, `else`, `elif`) take **Constant Time** -> O(1).
    

### Loop Growth Rules

- If the loop variable increases/decreases by addition or subtraction (e.g., `i++`, `i += c`), the complexity is **Linear** -> O(n).
    
- If the loop variable increases/decreases by multiplication or division (e.g., `i *= 2`, `i /= 2`), the complexity is **Logarithmic** -> O(logn).
    

# 3. Code Examples & Complexity Analysis

## Example 1: Linear Search / While Loop

Python

```
index = 0
sum_val = int(input())
while index <= sum_val:
    index += 1
```

- **Time Complexity:** 1+n⟹O(n) (Worst Case).
    
- **Best Case / Formula Alternative:** If solved mathematically, e.g., `Result = n * (n + 1) / 2`, the complexity becomes O(1).
    

## Example 2: Common Complexities Scale

O(1),O(logn),O(n),O(nlogn),O(n2),O(n3)

## Example 3: Nested Loops (Logarithmic & Linear)

C++

```
for (int i = 1; i < n; i *= 2) {
    Print(i);
}
```

- **Time Complexity:** O(log2​n) (Base depends on the multiplier/divisor factor).
    

## Example 4: Combined Nested Loops

C++

```
int i, j = 0;
for (int i = 0; i < n; i++) {              // O(n)
    for (int j = 0; j < n3; j += 3) {      // O(n)
        Print(i + j);
    }
}
```

- **Total Complexity:** 1+n+(n×3n​)⟹O(n2).
    

## Example 5: Multi-Range Nested Loops (Python)

Python

```
for i in range(1, 100):                   # Constant range ~ O(1)
    for j in range(100, 1000):             # Constant range ~ O(1)
        for k in range(1000, 10000, 2):    # Constant range ~ O(1)
            k *= 2
```

- Note: If ranges are fixed constants, complexity is O(1). If ranges depend on n:
    
    - **Complexity:** O(n2log2​n).
        

## Example 6: Multiple Independent Loops

C++

```
for (int i = 2; i < n; i += 4) { // O(n)
    // ...
}
for (int k = 0; k < n; k = k * 2) { // O(log n)
    // ...
}
```

- **Combined Complexity:** O(nlog2n).
    

> **Golden Rule for Functions:** If there is a function call inside your code, look at what that function contains first, calculate its complexity, and then substitute it into the outer complexity calculation!