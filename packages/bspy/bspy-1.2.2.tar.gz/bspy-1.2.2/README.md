# bspy
Library for manipulating and rendering b-spline curves, surfaces, and multidimensional manifolds with non-uniform knots in each dimension.

The [Spline](https://ericbrec.github.io/bspy/bspy/spline.html) class has a method to fit multidimensional data for 
scalar and vector functions of single and multiple variables. Other methods add, subtract, multiply, and linearly transform splines. 
There are methods to evaluate spline values, derivatives, normals, and integrals, as well as methods that return spline representations 
of derivatives, normals, integrals, and convolutions. In addition, there are methods to manipulate the domain of splines, including trim, 
reparametrize, add and remove knots, elevate and extrapolate, and fold and unfold. Finally, there are methods to compute the zeros and contours of a spline and to intersect two splines.

The [SplineOpenGLFrame](https://ericbrec.github.io/bspy/bspy/splineOpenGLFrame.html) class is an 
[OpenGLFrame](https://pypi.org/project/pyopengltk/) with custom shaders to render spline curves and surfaces.

The [DrawableSpline](https://ericbrec.github.io/bspy/bspy/drawableSpline.html) class converts a 
[Spline](https://ericbrec.github.io/bspy/bspy/spline.html) to a curve or surface that can be drawn in a 
[SplineOpenGLFrame](https://ericbrec.github.io/bspy/bspy/splineOpenGLFrame.html). Only 1D and 2D splines can be converted.

The [bspyApp](https://ericbrec.github.io/bspy/bspy/bspyApp.html) class is a 
[tkinter.Tk](https://docs.python.org/3/library/tkinter.html) app that hosts a 
[SplineOpenGLFrame](https://ericbrec.github.io/bspy/bspy/splineOpenGLFrame.html), 
a listbox full of splines, and a set of controls to adjust and view the selected splines.

The [bspyGraphics](https://ericbrec.github.io/bspy/bspy/bspyApp.html#bspyGraphics) class is a graphics engine to display splines.
It launches a [bspyApp](https://ericbrec.github.io/bspy/bspy/bspyApp.html) and issues commands to the app for use 
in [jupyter](https://jupyter.org/) notebooks and other scripting environments.

![bspyApp rendering the Utah teapot](https://ericbrec.github.io/bspy/bspyApp.png "bspyApp rendering the Utah teapot")

The full documentation for bspy can be found [here](https://ericbrec.github.io/bspy), its GitHub project can be found 
[here](https://github.com/ericbrec/bspy), a test suite can be found [here](https://github.com/ericbrec/bspy/tree/main/tests), and
a set of examples, including a jupyter notebook, can be found [here](https://github.com/ericbrec/bspy/tree/main/examples).