geompreds - A Python wrapper for 2D predicates of Jonathan Richard Shewchuk

Many computational geometry applications use numerical tests known as the orientation and incircle tests. The orientation test determines whether a point lies to the left of, to the right of, or on a line or plane defined by other points. The incircle test determines whether a point lies inside, outside, or on a circle defined by other points. See [Adaptive Precision Floating-Point Arithmetic and Fast Robust Predicates for Computational Geometry](https://www.cs.cmu.edu/~quake/robust.html).

## Installation

- Download the source  
- Run `python -m pip install .` (or `python -m pip install -e .`)  
- Run the tests:
```bash
python -m unittest discover -s src/geompreds/tests -p "test_*.py"
```

## Usage

```python
from geompreds import orient2d, incircle

orient2d((0, 0), (10, 0), (10, 10))   # left turn (positive), looking from above
# => 100.0

orient2d((0, 0), (10, 0), (20, 0))   # straight (zero)
# => 0.0

orient2d((0, 0), (10, 0), (10, -10))  # right turn (negative), looking from above
# => -100.0

incircle((0,0), (10,0), (0,10), (0,10))     # on boundary
# => 0.0

incircle((0,0), (10,0), (0,10), (1,1))      # inside, value positive
# => 1800.0

incircle((0,0), (10,0), (0,10), (-100,-100)) # outside, value negative
# => -2200000.0
```

## Changelog

See `CHANGES.txt`.

## Bug reports

If you discover any bugs, feel free to create an issue on GitHub.

Please add as much information as possible to help us fix the possible bug. We also encourage you to help even more by forking and sending us a pull request.

The issue tracker is available at: https://github.com/bmmeijers/predicates/issues

## Maintainers

- [Martijn Meijers](https://github.com/bmmeijers)

## License

[MIT License](https://www.tldrlegal.com/l/mit)
