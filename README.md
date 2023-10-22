# HashMap Implementations in Python

## Description

This project involves the development of two distinct HashMap implementations:

1. **Chaining-based HashMap**: Utilizes a dynamic array and singly linked list to handle collisions using the chaining method.
2. **Open Addressing-based HashMap**: Utilizes a dynamic array and resolves collisions using open addressing with quadratic probing.

Both implementations are required to support specific methods for adding, removing, fetching, and checking elements in the HashMap. Additionally, some utility methods such as resizing the table and calculating table load are mandated.

## Features

- **Dynamic Array and Singly Linked List**: Incorporation of pre-written classes for DynamicArray and LinkedList to create the HashMap structures.
- **Versatile Method Implementations**: Methods include `put()`, `get()`, `remove()`, `contains_key()`, `clear()`, `empty_buckets()`, `resize_table()`, `table_load()`, and `get_keys()`.
- **Collision Handling**:
  - Chaining method using LinkedLists.
  - Open Addressing with Quadratic Probing.
  
- **Robust Testing**: While Gradescope provides initial tests, additional custom tests are encouraged to ensure complete coverage.

## General Instructions

1. Submit Python v3 code to Gradescope before the deadline.
2. Optimal code should pass all tests on Gradescope.
3. Custom test cases are recommended for comprehensive validation.
4. Include appropriate comments throughout the code, especially method docstrings.
5. Use the provided skeleton code as a foundation and adhere to method names and I/O parameters.
6. Ensure iterative implementations for all methods.
7. Test your code with different types of objects beyond integers. These objects are guaranteed to have correct implementations of methods like `__eq__`, `__lt__`, `__gt__`, `__ge__`, `__le__`, and `__str__`.

## Restrictions

- Do not use built-in Python data structures or their methods.
- All operations on DynamicArray or LinkedList should be performed using their methods, without directly accessing their variables.
- Direct access to variables in `HashMap`, `SLNode`, and `HashEntry` classes is allowed.

## Usage

### Prerequisites

- Python 3.x

### Installation

```bash
git clone https://github.com/haleyekrueger/hashmap-implementation.git
cd hashmap-implementation
```

### Using the HashMap

```python
from hash_map_sc import HashMap as ChainingHashMap
from hash_map_oa import HashMap as OpenAddressingHashMap

# For Chaining-based HashMap
ch_map = ChainingHashMap()
ch_map.put("key1", "value1")
print(ch_map.get("key1"))

# For Open Addressing-based HashMap
oa_map = OpenAddressingHashMap()
oa_map.put("key1", "value1")
print(oa_map.get("key1"))
```

## Contact

Haley Krueger - h.elaine.krueger@gmail.com

Project Link: https://github.com/haleyekrueger/hashmap-implementation
