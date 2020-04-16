Draw Moving Sprites
===================

This is a benchmark for testing how fast moving sprites can be drawn to the screen.

.. figure:: ../../result_data/arcade/draw_moving_sprites.png
    :width: 25%

    Screenshot from Arcade moving sprites

.. figure:: ../../result_data/pygame/draw_moving_sprites.png
    :width: 25%

    Screenshot from Pygame moving sprites

Important Notes:

* Arcade scales sprites using the graphics card, Pygame scales sprites by
  an algorithm run on the CPU side. The resulting look is different, please
  click on and expand the screenshots to see the difference.
* Loading an image takes time. Arcade automatically caches images, so loading
  the same image over and over does not take additional time. For Pygame this
  needs to be done by the programmer. This benchmark includes this caching,
  which adds some complexity to the code. If this isn't done, there is a
  noticeable pause every time new coins are added.


.. image:: ../../result_charts/draw_moving_sprites/fps_comparison.svg

.. image:: ../../result_charts/draw_moving_sprites/time_to_draw_comparison.svg

.. image:: ../../result_charts/draw_moving_sprites/time_to_move_comparison.svg

.. image:: ../../result_charts/draw_moving_sprites/arcade.svg

.. image:: ../../result_charts/draw_moving_sprites/pygame.svg

