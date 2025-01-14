#!/usr/bin/env python
"""

    Tokenizer for Icelandic text

    Copyright (C) 2022 Miðeind ehf.
    Original author: Vilhjálmur Þorsteinsson

    This software is licensed under the MIT License:

        Permission is hereby granted, free of charge, to any person
        obtaining a copy of this software and associated documentation
        files (the "Software"), to deal in the Software without restriction,
        including without limitation the rights to use, copy, modify, merge,
        publish, distribute, sublicense, and/or sell copies of the Software,
        and to permit persons to whom the Software is furnished to do so,
        subject to the following conditions:

        The above copyright notice and this permission notice shall be
        included in all copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
        EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
        MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
        IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
        CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
        TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
        SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

from typing import Any

import io
import re

from glob import glob
from os.path import basename, dirname, join, splitext
from setuptools import find_packages, setup  # type: ignore


def read(*names: str, **kwargs: Any) -> str:
    try:
        return io.open(
            join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")
        ).read()
    except (IOError, OSError):
        return ""


# Load version string from file
__version__ = "[missing]"
exec(open(join("src", "tokenizer", "version.py")).read())

setup(
    name="tokenizer",
    version=__version__,
    license="MIT",
    description="A tokenizer for Icelandic text",
    long_description="{0}\n{1}".format(
        re.compile("^.. start-badges.*^.. end-badges", re.M | re.S).sub(
            "", read("README.rst")
        ),
        re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", read("CHANGELOG.rst")),
    ),
    long_description_content_type="text/x-rst",
    author="Miðeind ehf.",
    author_email="mideind@mideind.is",
    url="https://github.com/mideind/Tokenizer",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    package_data={"tokenizer": ["py.typed", "tokenizer.pyi"]},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Natural Language :: Icelandic",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Text Processing :: Linguistic",
    ],
    keywords=["nlp", "tokenizer", "icelandic"],
    # Set up a tokenize command (tokenize.exe on Windows),
    # which calls main() in src/tokenizer/main.py
    entry_points={
        "console_scripts": [
            "tokenize=tokenizer.main:main",
        ],
    },
)
