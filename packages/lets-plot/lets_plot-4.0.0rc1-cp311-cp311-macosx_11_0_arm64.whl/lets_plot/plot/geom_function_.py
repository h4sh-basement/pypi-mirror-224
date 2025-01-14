#  Copyright (c) 2023. JetBrains s.r.o.
#  Use of this source code is governed by the MIT license that can be found in the LICENSE file.
try:
    import pandas as pd
except ImportError:
    pd = None

try:
    import polars as pl
except ImportError:
    pl = None

from .core import aes
from .geom import _geom

__all__ = ['geom_function']

_fun_x_name, _fun_y_name = 'x', 'y'


def _linspace(start, stop, num):
    if num == 1:
        return [start]

    step = (stop - start) / (num - 1)

    return [start + step * i for i in range(num)]


def _get_default_xrange(xlim, n):
    default_xlim = [0.0, 1.0]
    default_size = 512

    start, stop = xlim if xlim is not None else default_xlim
    size = n if n is not None else default_size

    return _linspace(start, stop, size)


def _get_fun_data(mapping, data, fun, xlim, n):
    aes_x_value = None
    if mapping is not None and 'x' in mapping.as_dict():
        aes_x_value = mapping.as_dict()['x']

    if isinstance(aes_x_value, str) and data is not None:
        xs = data[aes_x_value]
    elif hasattr(aes_x_value, '__iter__'):
        xs = aes_x_value
    else:
        xs = _get_default_xrange(xlim, n)

    if fun is None:
        ys = [None] * len(xs)
    else:
        ys = [fun(x) for x in xs]

    if data is None:
        return {_fun_x_name: xs, _fun_y_name: ys}
    else:
        if isinstance(data, dict):
            return {**data, **{_fun_y_name: ys}}
        elif pd is not None and isinstance(data, pd.DataFrame):
            return data.assign(**{_fun_y_name: ys})
        elif pl is not None and isinstance(data, pl.DataFrame):
            return data.with_columns(**{_fun_y_name: pl.Series(values=ys)})
        else:
            raise Exception("Unsupported type of data: {0}".format(data))


def _get_mapping(mapping):
    mapping_dict = mapping.as_dict() if mapping is not None else {}
    x_mapping_dict = {'x': _fun_x_name}
    y_mapping_dict = {'y': _fun_y_name}

    return aes(**{**x_mapping_dict, **mapping_dict, **y_mapping_dict})


def geom_function(mapping=None, *, data=None, stat=None, geom=None, position=None, show_legend=None, tooltips=None,
                  fun=None, xlim=None, n=None,
                  color_by=None,
                  **other_args):
    """
    Compute and draw a function.

    Parameters
    ----------
    mapping : `FeatureSpec`
        Set of aesthetic mappings created by `aes()` function.
        Aesthetic mappings describe the way that variables in the data are
        mapped to plot "aesthetics".
    data : dict or Pandas or Polars `DataFrame`
        The data to be used in this layer. Specify to describe the definition area of a function.
        If None, the default, the data will not be used at all.
    stat : str, default='identity'
        The statistical transformation to use on the data generated by the function.
        Supported transformations: 'identity' (leaves the data unchanged),
        'smooth' (performs smoothing - linear default),
        'density2d' (computes and draws 2D kernel density estimate).
    geom : str, default='line'
        The geometry to display the function, as a string.
    position : str or `FeatureSpec`, default='identity'
        Position adjustment, either as a string ('identity', 'stack', 'dodge', ...),
        or the result of a call to a position adjustment function.
    show_legend : bool, default=True
        False - do not show legend for this layer.
    tooltips : `layer_tooltips`
        Result of the call to the `layer_tooltips()` function.
        Specify appearance, style and content.
    fun : function
        A function of one variable in Python syntax.
    xlim : list of float, default=[0.0, 1.0]
        Range of the function. Float array of length 2.
    n : int, default=512
        Number of points to interpolate along the x axis.
    color_by : {'fill', 'color', 'paint_a', 'paint_b', 'paint_c'}, default='color'
        Define the color aesthetic for the geometry.
    other_args
        Other arguments passed on to the layer.
        These are often aesthetics settings used to set an aesthetic to a fixed value,
        like color='red', fill='blue', size=3 or shape=21.
        They may also be parameters to the paired geom/stat.

    Returns
    -------
    `LayerSpec`
        Geom object specification.

    Notes
    -----
    `geom_function()` understands the following aesthetics mappings:

    - x : x-axis value.
    - alpha : transparency level of a layer. Accept values between 0 and 1.
    - color (colour) : color of the geometry. String in the following formats: RGB/RGBA (e.g. "rgb(0, 0, 255)"); HEX (e.g. "#0000FF"); color name (e.g. "red"); role name ("pen", "paper" or "brush").
    - linetype : type of the line. Codes and names: 0 = 'blank', 1 = 'solid', 2 = 'dashed', 3 = 'dotted', 4 = 'dotdash', 5 = 'longdash', 6 = 'twodash.
    - size : line width.

    Examples
    --------
    .. jupyter-execute::
        :linenos:
        :emphasize-lines: 9

        import numpy as np
        from scipy.stats import norm
        from lets_plot import *
        LetsPlot.setup_html()
        np.random.seed(42)
        x = np.random.normal(size=500)
        ggplot() + \\
            geom_density(aes(x='x'), data={'x': x}) + \\
            geom_function(fun=norm.pdf, xlim=[-4, 4], color="red")

    |

    .. jupyter-execute::
        :linenos:
        :emphasize-lines: 5-6

        from lets_plot import *
        LetsPlot.setup_html()
        data = {'x': list(range(-5, 6))}
        ggplot() + \\
            geom_function(aes(x='x', color='y', size='y'), \\
                          data=data, fun=lambda t: t**2, show_legend=False) + \\
            scale_color_gradient(low="red", high="green") + \\
            scale_size(range=[1, 4], trans='reverse')

    |

    .. jupyter-execute::
        :linenos:
        :emphasize-lines: 4-5

        from math import sqrt
        from lets_plot import *
        LetsPlot.setup_html()
        fun_layer = lambda fun: geom_function(fun=fun, xlim=[-2, 2], n=9, \\
                                              stat='density2d', geom='density2d')
        gggrid([
            ggplot() + fun_layer(lambda t: t),
            ggplot() + fun_layer(lambda t: t**2),
            ggplot() + fun_layer(lambda t: 2**t),
            ggplot() + fun_layer(lambda t: sqrt(4 - t**2)) + coord_fixed(ratio=2),
        ], ncol=2)

    """
    fun_stat = stat if stat is not None else 'identity'
    fun_geom = geom if geom is not None else 'line'

    return _geom(fun_geom,
                 mapping=_get_mapping(mapping),
                 data=_get_fun_data(mapping, data, fun, xlim, n),
                 stat=fun_stat,
                 position=position,
                 show_legend=show_legend,
                 sampling=None,
                 tooltips=tooltips,
                 color_by=color_by,
                 **other_args)
