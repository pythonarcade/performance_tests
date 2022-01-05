Time to draw stationary sprites
===============================

This is a benchmark for testing how fast we can draw stationary sprites.

Here are screenshots from both the libraries:

.. figure:: ../../../result_data/arcade/draw_stationary_sprites.png
    :width: 40%

    Screenshot from Arcade

.. figure:: ../../../result_data/pygame/draw_stationary_sprites.png
    :width: 40%

    Screenshot from Pygame

Important Notes:
----------------

The figure below graphs FPS vs. number of sprites.
Once the FPS starts
dropping much below 60 FPS, the users will notice the game slow down.
Practically, the number of moving sprites should be kept above this
drop-off number.

The results, of course, will vary depending on the computer that you run it on.
You can run the benchmarks yourself to see how they perform on your computer.
See :ref:`how-to-recreate`.

.. figure:: ../../../result_charts/draw_stationary_sprites/fps_comparison.svg

    Frames-Per-Second vs. number of stationary sprites

Instead of looking at a FPS, the time to draw the sprites:

.. image:: ../../../result_charts/draw_stationary_sprites/time_to_draw_comparison.svg

.. toctree::
   :maxdepth: 1
   :caption: Source Code:

   pygame_source
   arcade_source
