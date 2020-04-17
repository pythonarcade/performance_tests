Collision Tests
===============

The collision test checks how fast the library can determine if a sprite is
touching another sprite.

.. figure:: ../../../result_data/arcade/collision.png
    :width: 25%

    Screenshot from Arcade collision test

.. figure:: ../../../result_data/pygame/collision.png
    :width: 25%

    Screenshot from Pygame collision test

Important notes:

* Pygame detects collisions based on an unrotated rect that encompasses the entire
  sprite, including transparent pixels.
* Pygame does support creating `masks <https://www.pygame.org/docs/ref/mask.html>`_
  for pixel-perfect collision detection. This benchmoark code uses just the faster rect
  detection.
* Arcade will auto-trim the hit-box sides and corners based on transparent pixels.
  Arcade also supports rotating the hit box with the sprite.
* Pygame uses fast collision detection using C. While still O(N), it can detect
  collisions very quickly using native code.
* Arcade can use Spatial hashing. If the target list has sprites that don't move
  or change often, collision detection can come close to O(1). Spatial hashing slows
  sprite movement, so there is a trade-off. Without spatial hashing, collision
  detection is much slower because Arcade uses pure Python.
* Pygame's drop-off in FPS comes from the time it takes to draw the sprites,
  not from the time it takes to resolve collisions.

.. toctree::
   :maxdepth: 2
   :caption: Source Code:

   pygame_source
   arcade_source

.. image:: ../../../result_charts/collision/fps_comparison.svg

.. image:: ../../../result_charts/collision/time_to_move.svg