# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycreate2wg', 'pycreate2wg.bin']

package_data = \
{'': ['*']}

install_requires = \
['colorama', 'pyserial>=3.4,<4.0', 'simplejson']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata']}

entry_points = \
{'console_scripts': ['create_monitor = pycreate2wg.bin.create_monitor:main',
                     'create_reset = pycreate2wg.bin.create_reset:main',
                     'create_shutdown = pycreate2wg.bin.create_shutdown:main']}

setup_kwargs = {
    'name': 'pycreate2wg',
    'version': '0.8.0',
    'description': 'A library to control iRobot Create 2 with python',
    'author': 'walchko',
    'author_email': 'walchko@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/pycreate2/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
