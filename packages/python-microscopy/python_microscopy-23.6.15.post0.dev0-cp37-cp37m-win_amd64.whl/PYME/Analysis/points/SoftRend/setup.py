#!/usr/bin/python

##################
# setup.py
#
# Copyright David Baddeley, 2009
# d.baddeley@auckland.ac.nz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################

#!/usr/bin/env python
import sys
if sys.platform == 'darwin':#MacOS
    linkArgs = ['-headerpad_max_install_names']
else:
    linkArgs = ['-static-libgcc']
    
qhullSources = ['user.c', 'global.c', 'stat.c', 'io.c', 'geom2.c', 'poly2.c',
       'merge.c', 'geom.c', 'poly.c', 'qset.c', 'mem.c', 'usermem.c', 'userprintf.c', 'rboxlib.c','random.c','libqhull.c']

qhullSources = ['qhull/' + s for s in qhullSources]

def configuration(parent_package = '', top_path = None):
    from numpy.distutils.misc_util import Configuration, get_numpy_include_dirs
    config = Configuration('SoftRend', parent_package, top_path)

    srcs = ['triRend.c','drawTriang.c', 'triangRend.c']

    config.add_extension('triRend',
        sources=srcs + qhullSources,
        include_dirs = [get_numpy_include_dirs()] + ['qhull'],
	extra_compile_args = ['-O3', '-fno-exceptions', '-ffast-math'],
        extra_link_args=linkArgs)

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(description = 'c coded triangle and tetrahedra drawing functions',
    	author = 'David Baddeley',
       	author_email = 'd.baddeley@auckland.ac.nz',
       	url = '',
       	long_description = """
c coded triangle and tetrahedra drawing functions
""",
          license = "GPL",
          **configuration(top_path='').todict()
          )
