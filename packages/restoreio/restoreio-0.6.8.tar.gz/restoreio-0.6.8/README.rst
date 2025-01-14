******
|logo|
******

``restoreio`` is a Python package to **Restore** **I**\ ncomplete **O**\ ceanographic dataset, with specific focus on ocean surface velocity data. This package can also generate data ensembles and perform statistical analysis, which allows uncertainty qualification of such datasets.

Links
=====

* `Online Gateway <https://restoreio.org>`_
* `Documentation <https://ameli.github.io/restoreio>`_
* `PyPI <https://pypi.org/project/restoreio/>`_
* `Anaconda Cloud <https://anaconda.org/s-ameli/restoreio>`_

Install
=======

Install with ``pip``
--------------------

|pypi|

::

    pip install restoreio

Install with ``conda``
----------------------

|conda-version|

::

    conda install -c s-ameli restoreio

Supported Platforms
===================

Successful installation and tests performed on the following operating systems and Python versions:

.. |y| unicode:: U+2714
.. |n| unicode:: U+2716

+----------+--------+-------+-------+-------+-------+-------+-----------------+
| Platform | Arch   | Python Version                        | Continuous      |
+          |        +-------+-------+-------+-------+-------+ Integration     +
|          |        |  3.7  |  3.8  |  3.9  |  3.10 |  3.11 |                 |
+==========+========+=======+=======+=======+=======+=======+=================+
| Linux    | X86-64 |  |y|  |  |y|  |  |y|  |  |y|  |  |y|  | |build-linux|   |
+----------+--------+-------+-------+-------+-------+-------+-----------------+
| macOS    | X86-64 |  |y|  |  |y|  |  |y|  |  |y|  |  |y|  | |build-macos|   |
+----------+--------+-------+-------+-------+-------+-------+-----------------+
| Windows  | X86-64 |  |n|  |  |y|  |  |y|  |  |y|  |  |y|  | |build-windows| |
+----------+--------+-------+-------+-------+-------+-------+-----------------+

.. |build-linux| image:: https://img.shields.io/github/actions/workflow/status/ameli/restoreio/build-linux.yml
   :target: https://github.com/ameli/restoreio/actions?query=workflow%3Abuild-linux 
.. |build-macos| image:: https://img.shields.io/github/actions/workflow/status/ameli/restoreio/build-macos.yml
   :target: https://github.com/ameli/restoreio/actions?query=workflow%3Abuild-macos
.. |build-windows| image:: https://img.shields.io/github/actions/workflow/status/ameli/restoreio/build-windows.yml
   :target: https://github.com/ameli/restoreio/actions?query=workflow%3Abuild-windows

Documentation
=============

|deploy-docs|

See `documentation <https://ameli.github.io/restoreio/index.html>`__, including:

* `Installation Guide <https://ameli.github.io/restoreio/install.html>`__
* `User Guide <https://ameli.github.io/restoreio/user_guide/user_guide.html>`__
* `API Reference <https://ameli.github.io/restoreio/api.html>`__
* `Examples <https://ameli.github.io/restoreio/examples.html>`__
* `Publications <https://ameli.github.io/restoreio/cite.html>`__

Usage
=====

An installation of ``restoreio`` can be used in two ways: (1) as an importable python package or (2) as a standalone executable in the command line environment.

As a Python Package
-------------------

You may import ``restoreio`` in python. The main functions of this package are:

* `restoreio.restore <https://ameli.github.io/restoreio/generated/restoreio.restore.html#restoreio.restore>`__: restores incomplete data, generates ensembles, and performs statistical analysis. You may import this function as

  ::

    from restoreio import restore

* `restoreio.scan <https://ameli.github.io/restoreio/generated/restoreio.scan.html#restoreio.scan>`__: performs a pre-scan of your NetCDF dataset. You may import this function as

  ::

    from restoreio import scan

As a Standalone Executable
--------------------------

Alternatively, you may use ``restoreio`` as a standalone executable (outside of python environment) which can be executed in command line. When ``restoreio`` is installed, the following executables are available:

* `restore <https://ameli.github.io/restoreio/cli_restore.html>`__: This executable is identical to ``restoreio.restore`` function in the Python interface.
* `restore-scan <https://ameli.github.io/restoreio/cli_scan.html>`__: This executable is identical to ``restoreio.scan`` function in the Python interface.

To use these executables, make sure the ``/bin`` directory of your python installation is set on your ``PATH`` environment variable. For instance, if your python is installed on ``/opt/minicinda3/``, add this path ``/opt/miniconda3/bin`` directory to ``PATH`` by

::

    export PATH=/opt/minicinda/bin:$PATH

You may place the above line in ``~/.bashrc`` to make the above change permanently.

Online Web-Based Interface
==========================

Alongside ``restoreio`` python package, we have additionally developed a web server to serve as a web-based interface for this software. This platform is available at: `https://restoreio.org <https://restoreio.org>`__.

This online gateway allows users to efficiently process both local and remote datasets. The computational tasks are executed on the server side, leveraging the parallel processing capabilities of a high-performance computing cluster. Moreover, the web-based interface seamlessly integrates an interactive globe map, empowering sophisticated visualization of the results within the online platform.

How to Contribute
=================

We welcome contributions via `GitHub's pull request <https://github.com/ameli/restoreio/pulls>`_. If you do not feel comfortable modifying the code, we also welcome feature requests and bug reports as `GitHub issues <https://github.com/ameli/restoreio/issues>`_.

How to Cite
===========

If you publish work that uses ``restoreio``, please consider citing the manuscripts available `here <https://ameli.github.io/restoreio/cite.html>`_.

License
=======

|license|

This project uses a `BSD 3-clause license <https://github.com/ameli/restoreio/blob/main/LICENSE.txt>`_, in hopes that it will be accessible to most projects. If you require a different license, please raise an `issue <https://github.com/ameli/restoreio/issues>`_ and we will consider a dual license.

.. |logo| image:: https://raw.githubusercontent.com/ameli/restoreio/main/docs/source/_static/images/icons/logo-restoreio-light.svg
   :width: 200
.. |license| image:: https://img.shields.io/github/license/ameli/restoreio
   :target: https://opensource.org/licenses/BSD-3-Clause
.. |deploy-docs| image:: https://img.shields.io/github/actions/workflow/status/ameli/restoreio/deploy-docs.yml?label=docs
   :target: https://github.com/ameli/restoreio/actions?query=workflow%3Adeploy-docs
.. |binder| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/ameli/restoreio/HEAD?filepath=notebooks%2Fquick_start.ipynb
.. |codecov-devel| image:: https://img.shields.io/codecov/c/github/ameli/restoreio
   :target: https://codecov.io/gh/ameli/restoreio
.. |pypi| image:: https://img.shields.io/pypi/v/restoreio
   :target: https://pypi.org/project/restoreio/
.. |conda-version| image:: https://img.shields.io/conda/v/s-ameli/restoreio
   :target: https://anaconda.org/s-ameli/restoreio
