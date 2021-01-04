Draw Moving Shapes
==================

This is a benchmark for testing how fast moving shapes can be drawn to the screen.

.. figure:: ../../../result_data/arcade/moving_shapes_buffered.png
    :width: 25%

    Screenshot from Arcade moving shapes

.. figure:: ../../../result_data/pygame20/moving_shapes.png
    :width: 25%

    Screenshot from Pygame moving shapes

Important Notes:

* Pygame does not have support for rotating shapes
* Pygame code does not support transparency. (This should be possible, need a
  fix to this.)

Both libraries can speed drawing by batching things together. For example,
a house can be created by multiple drawing commands. These commands can be
batched so the house can be redrawn much faster.

* For Pygame, drawing with lots of shapes can be done on a surface, and then
  the surface can be drawn on the screen.
* For Arcade, drawing commands can be grouped together in a ShapeElementList.

.. toctree::
   :maxdepth: 2
   :caption: Source Code:

   pygame_source
   arcade_source

.. figure:: ../../../result_charts/shapes/fps_comparison.svg

    This shows Frames-Per-Second vs. number of shapes. Once the FPS starts
    dropping much below 60 FPS, the users will notice the game slow down.
    Practically, the number of moving shapes should be kept above this
    drop-off number.


