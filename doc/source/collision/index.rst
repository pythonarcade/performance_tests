Time to find colliding sprites
==============================

The collision test checks how fast the library can determine if a sprite is
touching another sprite.

.. figure:: ../../../result_data/arcade/collision.png
    :width: 25%

    Screenshot from Arcade collision test

.. figure:: ../../../result_data/pygame/collision.png
    :width: 25%

    Screenshot from Pygame collision test

Important Notes:
----------------

* Pygame detects collisions based on an unrotated rect that encompasses the entire
  sprite, including transparent pixels. Arcade will trim off the transparent
  pixels automatically, supports rotated sprites, and the "hit box" can be a polygon
  rather than a rectangle.
* Pygame does support creating `masks <https://www.pygame.org/docs/ref/mask.html>`_
  for pixel-perfect collision detection. This benchmark code uses just the faster rect
  detection.
* Arcade can use *spatial hashing*. If the target list has sprites that don't move
  or change often, collision detection can come close to O(1). Spatial hashing slows
  sprite movement, so there is a trade-off.

Results
-------

When looking at the graph below, it is important to note that Pygame's drop-off
in FPS comes from the time it takes to draw the sprites, not from the time it
takes to resolve collisions.


.. image:: ../../../result_charts/collision/fps_comparison.svg

By looking at the time measurements, we can see that with spatial hashing turned
on, collision detection takes about the same in Pygame and Arcade. With spatial
hashing turned off, Arcade takes longer.

(With spatial hashing turned on, it takes
longer to move a sprite, so spatial hashing should only be used with stationary
sprites. In most cases, walls in a game stay still, so this isn't normally an
issue.)

.. image:: ../../../result_charts/collision/collision.svg

.. toctree::
   :maxdepth: 2
   :caption: Source Code:

   pygame_source
   arcade_source

