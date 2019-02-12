# Python setup.py template
# ====================================================================
#
# Usage:
#     - Replace PACKAGE_NAME with your desired package name
#     - Replace PACKAGE_URL with your package URL (usually github repo
#       page, or pypi package page)
#     - Replace PACKAGE_VERSION with your package version (usually 0.1
#       for the initial release)
#     - Pick a license. The default one in this example setup.py is
#       BSD; a few other options are provided commented-out.
#     - Un-comment the desired classifiers, delete the rest
#     - Fill in author information (name, email), and description
#
# ====================================================================

import os
from setuptools import setup, find_packages

version = 'PACKAGE_VERSION'

here = os.path.dirname(__file__)

with open(os.path.join(here, 'README.rst')) as fp:
    longdesc = fp.read()

with open(os.path.join(here, 'CHANGELOG.rst')) as fp:
    longdesc += "\n\n" + fp.read()


setup(
    name='PACKAGE_NAME',
    version=version,
    packages=find_packages(),
    url='PACKAGE_URL',

    license='BSD License',
    # license='MIT License',
    # license='Apache 2.0 License',

    author='',
    author_email='',
    description='',
    long_description=longdesc,

    install_requires=[],
    # tests_require=tests_require,
    # test_suite='tests',

    classifiers=[
        # 'License :: OSI Approved :: BSD License',
        # 'License :: OSI Approved :: MIT License',
        # 'License :: OSI Approved :: Apache Software License',
        # 'License :: Public Domain',

        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',

        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.6',
        # 'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 2 :: Only',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
        # 'Programming Language :: Python :: 3.2',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
        # 'Programming Language :: Python :: 3.7',
        # 'Programming Language :: Python :: 3 :: Only',

        # 'Programming Language :: Python :: Implementation :: CPython',
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: PyPy',
        # 'Programming Language :: Python :: Implementation :: Stackless',
    ],
    # entry_points={
    #     'console_scripts': ['PACKAGE_NAME=PACKAGE_NAME.cli:main'],
    # },
    package_data={'': ['README.rst', 'CHANGELOG.rst']},
    include_package_data=True,
    zip_safe=False)
