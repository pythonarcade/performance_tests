.. _how-to-recreate:

How To Recreate The Results
===========================

**Step 1:**
Clone the repository on your computer:

https://github.com/pythonarcade/performance_tests

**Step 2:**
Make sure ``requirements.txt`` is loaded for your environment using your
IDE, or:

``python -m pip install -r requirements.txt``

**Step 3:**
Run ``src/__main__.py`` which should:

* Run all tests
* Generate all graphs using Matplotlib
* Generate all documents using Sphinx

**Step 4:**
Look at the resulting documents in ``doc/build``

```
cd performance_tests
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cd src
python __main__.py

```