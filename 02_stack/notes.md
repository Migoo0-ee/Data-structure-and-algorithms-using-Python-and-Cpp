Markdown

```
---
tags:
  - dsa
  - stack
  - cplusplus
  - programming
date: 2026-01-06
---

# 📚 Stack & C++ Fundamentals

> **Topic:** Data Structures & Algorithms (Stack) & C++ Concepts  
> **Date:** 2026/01/06

---

## 1. What is a Stack?
* **Concept:** Works on **LIFO** principle (**Last In, First Out**). The last element added is the first one to be removed.
* **Structure Example:**
  ```text
  [ 25 ] <- top (Size = 5)
  [ 20 ]
  [ 15 ]
  [ 10 ]
  [  5 ]
```

- **Initialization (`top` pointer):**
    
    - Initially, `top` starts at `-1` (meaning the stack is empty).
        
    - When adding the first element, we increment `top` (`top++`).
        

## 2. Key Stack Operations & Indexing

- **`top` Pointer:** It acts as an index tracking the topmost element.
    
    - _Example:_ `Print(Arr[top])` accesses the current top element.
        
- **Removal Behavior:** If `top` is at `25` (the top of the stack), it will be the **first number removed**.
    

## 3. Applications of Stack

- `Ctrl + Z` (Undo / Redo mechanisms in software)
    
- **Browser History / Navigation** (Back button functionality)
    

## 4. C++ Concepts: Call by Value vs Call by Reference

> **Question:** What's the difference between `Call by Value` and `Call by Reference` in C++?

- **Call by Value:**
    
    - Sends a **copy** of the variable.
        
    - Keeps the main variable safe in its **original state** (modifications inside the function don't affect the original).
        
- **Call by Reference:**
    
    - Accesses the memory **directly** (using `&`).
        
    - Modifications made inside the function directly alter the original variable.