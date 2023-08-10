# pyLangevitour

[![PyPI - Version](https://img.shields.io/pypi/v/langevitour.svg)](https://pypi.org/project/langevitour)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/langevitour.svg)](https://pypi.org/project/langevitour)

Python interface for [langevitour](https://github.com/pfh/langevitour/). langevitour is an HTML widget that randomly tours projections of a high-dimensional dataset with an animated scatter-plot.

[![](docs/images/LangeviTour.gif)](https://colab.research.google.com/github/Wytamma/pyLangevitour/blob/main/examples/notebook.ipynb)

For more information see the langevitour [Github repo](https://github.com/pfh/langevitour) or [website](https://logarithmic.net/langevitour/).

## Installation

```console
pip install langevitour
```

## Python usage 

```python
import numpy as np

from langevitour import LangeviTour

# Generate a sample dataset
X = []
group = []
n = 20000

def r():
    return np.random.normal(0, 0.02)

for i in range(n):
    a = i/n * np.pi * 2
    X.append([
        10 + np.sin(a)/3 + r(),
        20 + np.sin(a*2)/3 + r(),
        30 + np.sin(a*3)/3,
        40 + np.sin(a*4)/3,
        50 + np.sin(a*5)/3
    ])
    group.append(int(i*4/n))

# Extra axes (specified as columns of a matrix)
extra_axes = [[1], [2], [0], [0], [0]]
extra_axes_names = ["V1+2*V2"]

tour = LangeviTour(
    X,
    group=group,
    levels=["a", "b", "c", "d"],
    extra_axes=extra_axes,
    extra_axes_names=extra_axes_names,
    scale=[2, 1, 1, 1, 1],
    center=[10, 20, 30, 40, 50],
    point_size=1,
)
tour.write_html("langevitour_plot.html")
```

pyLangevitour also works in [jupyter notebooks](https://colab.research.google.com/github/Wytamma/pyLangevitour/blob/main/examples/notebook.ipynb).



## License

`pyLangevitour` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
