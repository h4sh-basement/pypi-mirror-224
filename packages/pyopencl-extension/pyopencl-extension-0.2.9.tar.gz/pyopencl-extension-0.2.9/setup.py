# from: https://github.com/navdeep-G/setup.py/blob/master/setup.py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'pyopencl-extension'
DESCRIPTION = 'This package extends PyOpenCl by providing an object-oriented kernel programming framework and ' \
              'debugging capabilities.'
URL = 'https://github.com/philipp-mohr/pyopencl-extension'
EMAIL = 'philipp.mohr@tuhh.de'
AUTHOR = 'P.Mohr'
REQUIRES_PYTHON = '>=3.10.0'
VERSION = '0.2.9'

# What packages are required for this module to be executed?
REQUIRED = [
    'numpy', 'pyopencl', 'mako', 'pycparser', 'pycparserext', 'pyastyle'  # 'requests', 'maya', 'records',
]

# What packages are optional?
EXTRAS = {
    'dev': [
        'pytest',
        'check-manifest',
        'twine',
        # 'reikna',
        'wheel'
    ]  # 'fancy feature': ['django'],
}

# Use .whl from other sources than pip?
DEPENDENCY_LINKS = []

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class LocalCommand(Command):
    """Support setup.py local installation and testing."""

    description = 'Build and test package locally'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from pathlib import Path
        self.status('Installing dependencies required for development')
        os.system(f'{Path(sys.executable).parent.joinpath("pip")}  install -e.[dev]')
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass
        try:
            self.status('Removing builds/lib to get rid os obsolete files...')
            rmtree(os.path.join(here, 'build/lib'))
        except OSError:
            pass
        self.status('Building Source and Wheel distribution…')
        os.system(f'{sys.executable} setup.py sdist bdist_wheel')
        # self.status('Building Source and Wheel (universal) distribution…')
        # os.system(f'{sys.executable} setup.py sdist bdist_wheel --universal')
        from pathlib import Path
        test_status = os.system(str(Path(sys.executable).parent.joinpath('pytest')))
        return test_status


class UploadCommand(LocalCommand):
    """Support setup.py upload."""

    description = 'Build, test, publish and tag (on Git) the package.'
    user_options = []

    def run(self):
        test_status = super().run()
        if test_status == 1:
            print('\n-----------------------------------\n'
                  'Tests failed. Upload to PyPI aborted...')
        else:
            self.status('Uploading the package to PyPI via Twine…')
            os.system('twine upload dist/* --repository pyopencl_extension ')

            self.status('Pushing git tags…')
            os.system('git tag v{0}'.format(about['__version__']))
            os.system('git push --tags')
        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["examples", "tests", "*.tests", "*.tests.*", "tests.*"]),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    dependency_links=DEPENDENCY_LINKS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
        'local': LocalCommand,
    },
)
