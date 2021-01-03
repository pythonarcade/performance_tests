Moving Sprites Speed Comparison
===============================

This is a benchmark for testing how fast moving sprites can be drawn to the
screen using both the Arcade library and PyGame.

Here are screenshots from both the libraries:

.. figure:: ../../../result_data/arcade/draw_moving_sprites.png
    :width: 25%

    Screenshot from Arcade moving sprites

.. figure:: ../../../result_data/pygame20/draw_moving_sprites.png
    :width: 25%

    Screenshot from Pygame moving sprites

Important Notes:
----------------

* Arcade scales sprites using the graphics card, Pygame scales sprites by
  an algorithm run on the CPU side. The resulting look is different, please
  click on and expand the screenshots to see the difference.
* Loading an image takes time. Arcade automatically caches images, so loading
  the same image over and over does not take additional time. For Pygame this
  needs to be done by the programmer. This benchmark includes this caching,
  which adds some complexity to the code. If this isn't done, there is a
  noticeable pause every time new coins are added, and the Pygame performance
  is very bad.

The figure below graphs FPS vs. number of moving sprites.
Once the FPS starts
dropping much below 60 FPS, the users will notice the game slow down.
Practically, the number of moving sprites should be kept above this
drop-off number.

The results, of course, will vary depending on the computer that you run it on.
You can run the benchmarks yourself to see how they perform on your computer.

.. figure:: ../../../result_charts/draw_moving_sprites/fps_comparison.svg

    Frames-Per-Second vs. number of moving sprites

How does this break down? Sprites in Pygame are drawn by the CPU. As the number
of sprites goes up, so does the time to draw. In Arcade, sprites are drawn by the
GPU. With the sprites already on the graphics card, and the graphics card having
many parallel processors, this is where Arcade gets its time advantage:

.. image:: ../../../result_charts/draw_moving_sprites/time_to_draw_comparison.svg

It does take longer for Arcade to move sprites than Pygame. In addition to
changing the position of the sprite in local computer memory, the new position
of the sprite must be changed on the GPU. If the sprites don't move at all, Arcade
can draw hundreds of thousands of sprites and still keep 60 FPS.

.. image:: ../../../result_charts/draw_moving_sprites/time_to_move_comparison.svg

.. toctree::
   :maxdepth: 1
   :caption: Source Code:

   pygame_source
   arcade_source
