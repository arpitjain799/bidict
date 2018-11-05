#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 Joshua Bronson. All Rights Reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# First run all tests that pytest discovers.


from pytest import main as pytest_main
exit_code = pytest_main()


# pytest's doctest support doesn't support Sphinx extensions
# (see https://www.sphinx-doc.org/en/latest/usage/extensions/doctest.html)
# so †est the code in the Sphinx docs using Sphinx's own doctest support.
from sphinx.cmd.build import main as sphinx_main
exit_code = sphinx_main('-b doctest -d docs/_build/doctrees docs docs/_build/doctest'.split()) or exit_code


exit(exit_code)
