# Jump Search

## :rocket: Introduction

This repository contains an implementation of the Jump Search algorithm in Python.

## Introduction

Jump Search is a searching algorithm used to find the position of a target value within a sorted array. It works by jumping ahead by a fixed number of steps and then linearly searching for the target value in that range. This process is repeated until the target value is found or the end of the array is reached.

## Implementation

The jump search algorithm is implemented in the `jump_search` function in the `jump_search.py` file. The function takes an array and a target value as input and returns the index of the target value if found, or -1 if not found.

## Usage

To use the jump search algorithm, follow these steps:

1. Clone this repository to your local machine.
2. Open the `jump_search.py` file.
3. Modify the `arr` variable to contain your desired array.
4. Modify the `target` variable to contain the value you want to search for.
5. Run the script.

## Example usage of the jump search algorithm

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11

result = jump_search(arr, target)
if result != -1:
    print(f"Target value {target} found at index {result}")
else:
    print("Target value not found in the array")
