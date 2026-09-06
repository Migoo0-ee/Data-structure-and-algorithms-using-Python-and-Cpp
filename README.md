# Data Structures and Algorithms using Python and C++

A collection of classic data structures and algorithm implementations, written in both **Python** and **C++** for comparison and deeper understanding of syntax, performance, and low-level behavior.

Structured to follow **Adel Nasim's "Data Structures Full Course In Arabic"** (37 lessons), implementing each topic in both languages as I go through the course.

## 📌 Goal

This repo is a personal learning journey to master Data Structures and Algorithms by implementing the same concepts in two different languages — one high-level (Python) and one low-level (C++) — to better understand:

- How each language handles memory and performance
- Time and space complexity trade-offs
- Language-specific syntax and idioms for the same logical problem

## 📂 Repository Structure

```
.
├── python/
│   ├── 01_complexity/
│   ├── 02_stack/
│   ├── 03_queue/
│   ├── 04_array_based_list/
│   ├── 05_linked_list/
│   ├── 06_doubly_linked_list/
│   ├── 07_trees/
│   ├── 08_huffman_coding/
│   ├── 09_sorting/
│   ├── 10_searching/
│   ├── 11_hashing/
│   └── 12_graphs/
│
├── cpp/
│   ├── 01_complexity/
│   ├── 02_stack/
│   ├── 03_queue/
│   ├── 04_array_based_list/
│   ├── 05_linked_list/
│   ├── 06_doubly_linked_list/
│   ├── 07_trees/
│   ├── 08_huffman_coding/
│   ├── 09_sorting/
│   ├── 10_searching/
│   ├── 11_hashing/
│   └── 12_graphs/
│
└── README.md
```

Each topic folder contains the same set of problems solved in both languages, so you can compare implementations side by side.

## 📚 Topics Covered (following the course order)

- **Complexity** — Big O analysis
- **Stack** — array-based, linked-list-based, balanced parentheses, infix→postfix, expression evaluation
- **Queue** — simple queue, circular queue (array-based), linked-list-based queue
- **Array-Based List** — implementation from scratch
- **Linked List** — insert/remove (first, last, at position), reverse, search
- **Doubly Linked List** — insert/remove (first, last, at position)
- **Trees** — binary trees, tree traversal (pre/in/post/level order), BST (insert/delete/search, successor/predecessor/max/min), AVL trees (rotations)
- **Huffman Coding Algorithm**
- **Sorting Algorithms** — selection, bubble, insertion, merge, quick, heap sort
- **Searching Algorithms** — linear search, binary search
- **Hashing** — hash tables
- **Graphs** — introduction & representation, BFS, DFS, Dijkstra's shortest path

## 🧠 Complexity Analysis

Each solution includes a note on:
- Time Complexity (Big O)
- Space Complexity (Big O)
- Notes on trade-offs between the Python and C++ implementation where relevant

## 🚀 How to Run

### Python
```bash
cd python/<topic>
python3 <filename>.py
```

### C++
```bash
cd cpp/<topic>
g++ <filename>.cpp -o output
./output
```

## 📈 Progress Tracker

| # | Topic | Python | C++ |
|---|-------|:------:|:---:|
| 1 | Complexity | ⬜ | ⬜ |
| 2 | Stack (array + linked, parentheses, infix→postfix) | ⬜ | ⬜ |
| 3 | Queue (simple, circular, linked) | ⬜ | ⬜ |
| 4 | Array-Based List | ⬜ | ⬜ |
| 5 | Linked List (insert/remove/reverse/search) | ⬜ | ⬜ |
| 6 | Doubly Linked List | ⬜ | ⬜ |
| 7 | Trees (Binary, Traversal, BST, AVL) | ⬜ | ⬜ |
| 8 | Huffman Coding | ⬜ | ⬜ |
| 9 | Sorting (Selection/Bubble/Insertion/Merge/Quick/Heap) | ⬜ | ⬜ |
| 10 | Searching (Linear/Binary) | ⬜ | ⬜ |
| 11 | Hashing (Hash Table) | ⬜ | ⬜ |
| 12 | Graphs (Intro, BFS, DFS, Dijkstra) | ⬜ | ⬜ |

## 🤝 Contributing

This is primarily a personal learning repo, but suggestions, corrections, or alternative approaches are welcome via issues or pull requests.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
