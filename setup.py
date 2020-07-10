#! /usr/bin/env python3

#   Copyright 2016, 2019 Denis Salem

#    This file is part of VenC.
#
#    VenC is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    VenC is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with VenC.  If not, see <http://www.gnu.org/licenses/>.

from os.path import expanduser, isdir
from os import listdir
from setuptools import setup

homedir = expanduser('~')

dst_themes_path = homedir+"/.local/share/bram"

extra_files = [(
    homedir+"/.local/share/bram",
    ["logo.png"]
)]
            
setup(
    name='bram',
    version='0.0.0',
    description='Braim Random Access Memory',
    author='Denis Salem',
    author_email='denissalem@tuxfamily.org',
    url='https://github.com/DenisSalem/bram',
    packages=[],
    license="GNU/GPLv3",
    platforms="Linux",
    long_description="Your tiny and friendly learn training.",
    classifiers=[
        "Environment :: X11",
        "Development Status :: 5 - Production/Stable"
    ],
    install_requires=[
          "pygobject"
    ],
    scripts=['bram'],
    data_files = extra_files
)
