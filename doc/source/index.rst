
Python Graphics Library Benchmarks
==================================

.. image:: ../../result_charts/draw_moving_sprites/fps_comparison.svg
   :width: 220px
   :target: draw_moving_sprites/index.html

.. image:: ../../result_charts/collision/fps_comparison.svg
   :width: 220px
   :target: collision/index.html

.. image:: ../../result_charts/shapes/fps_comparison.svg
   :width: 220px
   :target: shapes/index.html

This is a project to benchmark and compare different Python 2D graphics libraries.
These docs were run with:

* Pyglet |pyglet_version|
* Arcade |arcade_version|
* Pygame |pygame_version|.

Suggestions for improving these tests are welcome. See :ref:`how-to-recreate`
and submit a PR or `issue <https://github.com/pythonarcade/performance_tests/issues>`_.

.. toctree::
   :maxdepth: 1
   :caption: Tests:

   draw_stationary_sprites/index
   draw_moving_sprites/index
   collision/index
   shapes/index
   how_to_recreate
