from typing import Callable
import numpy as np
from sys import argv

NO_PROMPTS = "-q" in argv

def input_matrix(prompt: str = "Matrix:", print_back = True) -> np.ndarray:
    """Wrapper function."""
    matrix = _input_matrix(prompt)
    if print_back:
        print_matrix(matrix, "Input matrix:")
    return matrix

def _input_matrix(prompt) -> np.ndarray:
    if not NO_PROMPTS:
        print(prompt)
    data = []
    while True:
        try:
            line_msg = f"L{len(data) + 1} >> " if not NO_PROMPTS else ""
            i = input(line_msg)
            if len(i) == 0:
                break
            # if i == "s":
            #     data = [[1.0, 3.0, 3.0, 5.0], [4.0, 5.0, 6.0, 6.0], [9.0, 8.0, 7.0, 7.0], [1.0, 2.0, 3.0, 4.0]]
            #     break
            # if i == "d":
            #     data = [[1.0, 2.0, 3.0, 4.0, 5.0], [6.0, 7.0, 8.0, 9.0, 6.0], [3.0, 7.0, 8.0, 7.0, 2.0]]
            #     break
            # if i == "e":
            #     data = [[1.0, 5.0, 3.0, -4.0, 20.0], 
            #             [3.0, 1.0, -2.0, 0.0, 9.0],
            #             [5.0, -7.0, 0.0, 10.0, -9.0],
            #             [0.0, 3.0, -5.0, 0.0, 1.0]]
            #     break
            data.append(list(map(float, i.split(" "))))
        except KeyboardInterrupt:
            print()
            exit(0)
        # End of file
        except EOFError:
            break
    return np.array(data)
    
def print_matrix(matrix: np.ndarray, msg: str = "Matrix:", round: int = 2) -> None:
    copy = np.round(matrix, round)
    print(msg)
    print(copy)

def print_exc_and_exit(e: Exception) -> None:
    print(e)
    exit(1)