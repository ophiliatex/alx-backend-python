# Python - Variable Annotations

This project covers advanced Python concepts, specifically focusing on variable annotations. The goal is to understand type annotations in Python 3, how to use them for specifying function signatures and variable types, duck typing, and validating code with `mypy`.

## Learning Objectives

By the end of this project, you should be able to:
- Explain type annotations in Python 3.
- Use type annotations to specify function signatures and variable types.
- Understand duck typing.
- Validate code with `mypy`.

## Resources

- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.)
- All files must be executable
- The length of files will be tested using `wc`
- All modules should have a documentation
- All classes should have a documentation
- All functions (inside and outside a class) should have a documentation

## Tasks

### 0. Basic annotations - add
Write a type-annotated function `add` that takes two floats `a` and `b` and returns their sum as a float.
```python
def add(a: float, b: float) -> float:
    return a + b
```

### 1. Basic annotations - concat
Write a type-annotated function `concat` that takes two strings `str1` and `str2` and returns a concatenated string.
```python
def concat(str1: str, str2: str) -> str:
    return str1 + str2
```

### 2. Basic annotations - floor
Write a type-annotated function `floor` which takes a float `n` and returns the floor of the float.
```python
def floor(n: float) -> int:
    return math.floor(n)
```

### 3. Basic annotations - to string
Write a type-annotated function `to_str` that takes a float `n` and returns the string representation of the float.
```python
def to_str(n: float) -> str:
    return str(n)
```

### 4. Define variables
Define and annotate the following variables with the specified values:
- `a`, an integer with a value of 1
- `pi`, a float with a value of 3.14
- `i_understand_annotations`, a boolean with a value of True
- `school`, a string with a value of "Holberton"
```python
a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"
```

### 5. Complex types - list of floats
Write a type-annotated function `sum_list` which takes a list `input_list` of floats and returns their sum as a float.
```python
def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
```

### 6. Complex types - mixed list
Write a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float.
```python
def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
```

### 7. Complex types - string and int/float to tuple
Write a type-annotated function `to_kv` that takes a string `k` and an int or float `v` and returns a tuple. The first element is the string `k`. The second element is the square of the int/float `v` and should be annotated as a float.
```python
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v**2))
```

### 8. Complex types - functions
Write a type-annotated function `make_multiplier` that takes a float `multiplier` as argument and returns a function that multiplies a float by `multiplier`.
```python
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
```

### 9. Let's duck type an iterable object
Annotate the function `element_length` parameters and return values with appropriate types.
```python
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
```

### 10. Duck typing - first element of a sequence
Augment the following code with the correct duck-typed annotations:
```python
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
```

### 11. More involved type annotations
Given the parameters and return values, add type annotations to the function `safely_get_value`.
```python
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
```

### 12. Type Checking
Use `mypy` to validate the following piece of code and apply necessary changes.
```python
from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
```

## How to Run

To test the code, run the corresponding `main.py` files in the terminal. For example, to test task 0:
```bash
./0-main.py
```

To check type annotations using `mypy`:
```bash
mypy <file>.py
```

## Author
This project was created by Johnny.
