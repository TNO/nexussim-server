================
Contributing
================

Welcome to ``nexussim-server`` contributor's guide.

This document focuses on getting developers or any potential contributor familiarized
with the development processes, but `other kinds of contributions`_ are also
appreciated.

Please notice, all users and contributors are expected to be **open,
considerate, reasonable, and respectful**. When in doubt, `Python Software
Foundation's Code of Conduct`_ is a good reference in terms of behavior
guidelines.


Issue Reports
=============

If you experience bugs or general issues with ``nexussim-server``, please have a look
on the `issue tracker`_. If you don't see anything useful there, please feel
free to fire an issue report.

.. tip::
   Please don't forget to include the closed issues in your search.
   Sometimes a solution was already reported, and the problem is considered
   **solved**.

New issue reports should include information about your programming environment
(e.g., operating system, Python version) and steps to reproduce the problem.
Please try also to simplify the reproduction steps to a very minimal example
that still illustrates the problem you are facing. By removing other factors,
you help us to identify the root cause of the issue.

Code Contributions
==================

Submit an issue
---------------

Before you work on any non-trivial code contribution it's best to first create
a report in the `issue tracker`_ to start a discussion on the subject.
This often provides additional considerations and avoids unnecessary work.

Create an environment
---------------------

Before you start coding, we recommend creating an isolated `virtual
environment`_ to avoid any problems with your installed Python packages.
This can easily be done via either |virtualenv|_::

    virtualenv <PATH TO VENV>
    source <PATH TO VENV>/bin/activate

or Miniconda_::

    conda create -n nexussim-server python=3 six virtualenv pytest pytest-cov
    conda activate nexussim-server

Clone the repository
--------------------

#. Create an user account on |the repository service| if you do not already have one.
#. Fork the project repository_: click on the *Fork* button near the top of the
   page. This creates a copy of the code under your account on |the repository service|.
#. Clone this copy to your local disk::

   git clone https://github.com/TNO/nexussim-server.git
    cd nexussim-server

#. You should run::

    pip install -U pip setuptools -e .

   to be able to import the package under development in the Python REPL.

#. Initialize the submodules::

    git submodule update --init --recursive

Working on changes
------------------

#. Create a branch to hold your changes::

    git checkout -b my-feature

   and start making changes. Never work on the main branch!

#. Start your work on this branch. Don't forget to add docstrings_ to new
   functions, modules and classes, especially if they are part of public APIs.

#. Add yourself to the list of contributors in ``AUTHORS.rst``.

#. When you’re done editing, do::

    git add <MODIFIED FILES>
    git commit

   to record your changes in git_.

   .. important:: Don't forget to add unit tests and documentation in case your
      contribution adds an additional feature and is not just a bugfix.

      Moreover, writing a `descriptive commit message`_ is highly recommended.
      In case of doubt, you can check the commit history with::

         git log --graph --decorate --pretty=oneline --abbrev-commit --all

      to look for recurring communication patterns.

#. Please check that your changes don't break any unit tests with::

    tox

   (after having installed |tox|_ with ``pip install tox`` or ``pipx``).

   You can also use |tox|_ to run several other pre-configured tasks in the
   repository. Try ``tox -av`` to see a list of the available checks.


Submit your contribution
------------------------

#. If everything works fine, push your local branch to |the repository service| with::

    git push -u origin my-feature

#. Go to the web page of your fork and click |contribute button|
   to send your changes for review.

   Find more detailed information in `creating a PR`_. You might also want to open
   the PR as a draft first and mark it as ready for review after the feedbacks
   from the continuous integration (CI) system or any required fixes.


Troubleshooting
---------------

The following tips can be used when facing problems to build or test the
package:

#. Make sure to fetch all the tags from the upstream repository_.
   The command ``git describe --abbrev=0 --tags`` should return the version you
   are expecting. If you are trying to run CI scripts in a fork repository,
   make sure to push all the tags.
   You can also try to remove all the egg files or the complete egg folder, i.e.,
   ``.eggs``, as well as the ``*.egg-info`` folders in the ``src`` folder or
   potentially in the root of your project.

#. Make sure to have a reliable |tox|_ installation that uses the correct
   Python version (e.g., 3.7+). When in doubt you can run::

    tox --version
    # OR
    which tox

   If you have trouble and are seeing weird errors upon running |tox|_, you can
   also try to create a dedicated `virtual environment`_ with a |tox|_ binary
   freshly installed. For example::

    virtualenv .venv
    source .venv/bin/activate
    .venv/bin/pip install tox
    .venv/bin/tox -e all

#. `Pytest can drop you`_ in an interactive session in the case an error occurs.
   In order to do that you need to pass a ``--pdb`` option (for example by
   running ``tox -- -k <NAME OF THE FALLING TEST> --pdb``).
   You can also setup breakpoints manually instead of using the ``--pdb`` option.


Maintainer tasks
================

.. _other kinds of contributions: https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source
.. _Python Software Foundation's Code of Conduct: https://policies.python.org/python.org/code-of-conduct/
.. _issue tracker: https://github.com/TNO/nexussim-server/issues
.. _tox: https://tox.wiki/
.. _virtualenv: https://virtualenv.pypa.io/
.. _Miniconda: https://docs.conda.io/en/latest/miniconda.html
.. _project repository: https://github.com/TNO/nexussim-server
.. _repository service: https://github.com
.. _docstrings: https://peps.python.org/pep-0257/
.. _git: https://git-scm.com/
.. _descriptive commit message: https://cbea.ms/git-commit/
.. _creating a PR: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
.. _upstream repository: https://github.com/TNO/nexussim-server
.. _Pytest can drop you: https://docs.pytest.org/en/stable/how-to/failures.html#dropping-to-pdb

.. |tox| replace:: tox
.. |virtualenv| replace:: virtualenv
.. |the repository service| replace:: GitHub
.. |contribute button| replace:: pull request button
