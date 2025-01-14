#!/usr/bin/env python
# pylint: disable=W0142,W0403,W0404,W0613,W0622,W0622,W0704,R0904,C0103,E0611
#
# copyright 2003-2016 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This file is part of a CubicWeb cube.
#
# CubicWeb is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# CubicWeb is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with CubicWeb.  If not, see <http://www.gnu.org/licenses/>.
"""cubicweb_localperms setup module using data from
cubicweb_localperms/__pkginfo__.py file
"""

from os.path import join, dirname
from setuptools import find_packages, setup


here = dirname(__file__)

# load metadata from the __pkginfo__.py file so there is no risk of conflict
# see https://packaging.python.org/en/latest/single_source_version.html
pkginfo = join(here, 'cubicweb_localperms', '__pkginfo__.py')
__pkginfo__ = {}
with open(pkginfo) as f:
    exec(f.read(), __pkginfo__)

# get required metadatas
distname = __pkginfo__['distname']
version = __pkginfo__['version']
license = __pkginfo__['license']
description = __pkginfo__['description']
web = __pkginfo__['web']
author = __pkginfo__['author']
author_email = __pkginfo__['author_email']
classifiers = __pkginfo__['classifiers']

with open(join(here, 'README.rst')) as f:
    long_description = f.read()

# get optional metadatas
data_files = __pkginfo__.get('data_files', None)
dependency_links = __pkginfo__.get('dependency_links', ())

requires = {}
for entry in ("__depends__",):  # "__recommends__"):
    requires.update(__pkginfo__.get(entry, {}))

install_requires = ["{0} {1}".format(d, v and v or "").strip()
                    for d, v in requires.items()]


setup(
    name=distname,
    version=version,
    license=license,
    description=description,
    long_description=long_description,
    author=author,
    author_email=author_email,
    url=web,
    classifiers=classifiers,
    packages=find_packages(exclude=['test']),
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'cubicweb.cubes': [
            'localperms=cubicweb_localperms',
        ],
    },

    zip_safe=False,
)
