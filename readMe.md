# Python List (Array) Methods Cheat Sheet 📋

This is a quick-reference guide to all the standard methods for Python's `list` object, along with common built-in functions used with lists.

---

## List Methods

These methods are called directly on a list object (e.g., `my_list.append()`).

| Method Syntax                          | Description                                                                                             | Example                                                                                                  |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **`list.append(item)`** | Adds a single item to the **end** of the list. Modifies the list **in-place**.                          | `L = [1, 2]` <br> `L.append(3)` <br> `L` is now `[1, 2, 3]`                                                |
| **`list.extend(iterable)`** | Appends all items from an iterable (e.g., another list) to the end. Modifies the list **in-place**.     | `L = [1, 2]` <br> `L.extend([3, 4])` <br> `L` is now `[1, 2, 3, 4]`                                        |
| **`list.insert(index, item)`** | Inserts an item at a specific position. Modifies the list **in-place**.                                 | `L = [1, 3]` <br> `L.insert(1, 2)` <br> `L` is now `[1, 2, 3]`                                             |
| **`list.remove(item)`** | Removes the **first** matching item from the list. Raises `ValueError` if the item isn't found.           | `L = [1, 2, 2]` <br> `L.remove(2)` <br> `L` is now `[1, 2]`                                                |
| **`list.pop([index])`** | Removes and **returns** the item at the given index. If no index, removes and returns the **last** item.  | `L = [1, 2, 3]` <br> `x = L.pop(1)` <br> `x` is `2`, `L` is `[1, 3]`                                         |
| **`list.clear()`** | Removes all items from the list. Modifies the list **in-place**.                                        | `L = [1, 2, 3]` <br> `L.clear()` <br> `L` is now `[]`                                                      |
| **`list.index(item, [start], [end])`** | Returns the index of the **first** matching item. Raises `ValueError` if not found.                     | `L = [1, 2, 3]` <br> `L.index(2)` returns `1`                                                             |
| **`list.count(item)`** | Returns the number of times an item appears in the list.                                                | `L = [1, 2, 2]` <br> `L.count(2)` returns `2`                                                             |
| **`list.sort(key=None, reverse=False)`** | Sorts the list **in-place**. Use `key` for custom sorting and `reverse=True` for descending order.      | `L = [3, 1, 2]` <br> `L.sort()` <br> `L` is now `[1, 2, 3]`                                                |
| **`list.reverse()`** | Reverses the order of elements **in-place**.                                                            | `L = [1, 2, 3]` <br> `L.reverse()` <br> `L` is now `[3, 2, 1]`                                             |
| **`list.copy()`** | Returns a **shallow copy** of the list.                                                                 | `L1 = [1, 2]` <br> `L2 = L1.copy()` <br> `L2.append(3)` <br> `L1` is `[1, 2]`, `L2` is `[1, 2, 3]`           |

---

## Related Built-in Functions

These functions are not methods but are commonly used with lists.

| Function Syntax        | Description                                                                          | Example                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| **`len(list)`** | Returns the number of items in the list.                                             | `len([1, 2, 3])` returns `3`                                                     |
| **`sorted(iterable)`** | Returns a **new sorted list** from an iterable, leaving the original unchanged.        | `L = [3, 1, 2]` <br> `sorted(L)` returns `[1, 2, 3]`. `L` is still `[3, 1, 2]`     |
| **`min(list)`** | Returns the smallest item in the list.                                               | `min([3, 1, 2])` returns `1`                                                     |
| **`max(list)`** | Returns the largest item in the list.                                                | `max([3, 1, 2])` returns `3`                                                     |
| **`sum(list)`** | Returns the sum of all items in the list (items must be numbers).                    | `sum([1, 2, 3])` returns `6`                                                     |
| **`enumerate(list)`** | Returns an enumerate object containing pairs of (index, value) for each item.        | `list(enumerate(['a', 'b']))` returns `[(0, 'a'), (1, 'b')]`                     |