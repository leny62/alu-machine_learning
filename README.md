
## Requirements

- Python 3.x
- NumPy
- Matplotlib
- SciPy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/leny62/alu-machine_learning.git
cd alu-machine_learning
```

2. Install required packages:
```bash
pip install --user numpy matplotlib scipy
```

## Projects

### Plotting
- `0-line.py`: Basic line plotting example
- `101-pca.py`: Principal Component Analysis visualization

### Linear Algebra
- `0-slice_me_up.py`: Array slicing operations with examples:
  ```python
  arr = [9, 8, 2, 3, 9, 4, 1, 0, 3]
  arr1 = arr[:2]    # First two numbers: [9, 8]
  arr2 = arr[-5:]   # Last five numbers: [4, 1, 0, 3]
  arr3 = arr[1:6]   # 2nd through 6th numbers: [8, 2, 3, 9, 4]
  ```
- `1-trim_me_down.py`: Matrix column extraction example:
  ```python
  matrix = [[1, 3, 9, 4, 5, 8], 
            [2, 4, 7, 3, 4, 0], 
            [0, 3, 4, 6, 1, 5]]
  the_middle = [row[2:4] for row in matrix]  # Extract columns 3 and 4
  # Result: [[9, 4], [7, 3], [4, 6]]
  ```

## Usage

To run any of the Python scripts:

```bash
python3 math/plotting/0-line.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact

- Website: [https://www.lenycodes.tech/](https://www.lenycodes.tech/)
- Email: lihirwe6@gmail.com