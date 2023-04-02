Draw Moving Shapes
==================

This is a benchmark for testing how fast moving shapes can be drawn to the screen.

In summary:

1. Arcade is crazy-slow in drawing shapes.
2. Pygame is the fastest for unrotated rects with no alpha.
3. For anything else, Pyglet shapes are the fastest, easiest to use,
   and have the most features.

One should note that Pyglet and Arcade drawing is interchangable.
You can use Arcade sprites and Pyglet shapes together if you like.

Both Arcade and Pyglet make it easy to draw shapes with transparency and rotation.
Pygame supports these features, but it is not straight-forward.

Unrotated Rectangles
--------------------

.. figure:: ../../../result_charts/shapes/fps_comparison.svg

    This shows Frames-Per-Second vs. number of shapes. Once the FPS starts
    dropping much below 60 FPS, the users will notice the game slow down.
    Practically, the number of moving shapes should be kept above this
    drop-off number.

Output
^^^^^^
.. figure:: ../../../result_data/arcade/moving_shapes_buffered.png
    :width: 25%

    Screenshot from Arcade moving shapes

.. figure:: ../../../result_data/pygame/moving_shapes.png
    :width: 25%

    Screenshot from Pygame moving shapes

.. figure:: ../../../result_data/pyglet/moving_shapes.png
    :width: 25%

    Screenshot from Pyglet moving shapes

More info
^^^^^^^^^

Both libraries can speed drawing by batching things together. For example,
a house can be created by multiple drawing commands. These commands can be
batched so the house can be redrawn much faster.

* For Pygame, drawing with lots of shapes can be done on a surface, and then
  the surface can be drawn on the screen.
* For Arcade, drawing commands can be grouped together in a ShapeElementList.
* For Pyglet, drawing commands are put together in a Batch.

.. toctree::
   :maxdepth: 2
   :caption: Source Code:

   pygame_source
   arcade_source
   pyglet_source

Rotated Rectangles
------------------

.. figure:: ../../../result_charts/shapes/fps_comparison_rotated.svg

    This shows Frames-Per-Second vs. number of shapes. Once the FPS starts
    dropping much below 60 FPS, the users will notice the game slow down.
    Practically, the number of moving shapes should be kept above this
    drop-off number.

Output
^^^^^^

.. figure:: ../../../result_data/pygame/moving_rotating_shapes.png
    :width: 25%

    Screenshot from Pygame moving shapes

.. figure:: ../../../result_data/pyglet/moving_rotating_shapes.png
    :width: 25%

    Screenshot from Pyglet moving shapes


More info
^^^^^^^^^

This section is to test rotating rectangles. Pyglet gets built-in
acceleration via the graphics card, where Pygame does everything on
the CPU. Pyglet pulls ahead in performance.

