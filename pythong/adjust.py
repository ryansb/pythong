#!/bin/env python
# -*- coding: utf8 -*-

import os
import sys


def site_packages_walk():
    for spdir in [f for f in sys.path if f.endswith('packages')]:
        for res in os.walk(spdir):
            yield res

packages_iter = site_packages_walk()
