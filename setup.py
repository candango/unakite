#!/usr/bin/env python
#
# Copyright 2019 Flavio Garcia
# Copyright 2016-2017 Veeti Paananen under MIT License
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unakite
from setuptools import setup
from codecs import open
try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

with open("README.md", "r") as fh:
    long_description = fh.read()


# Solution from http://bit.ly/29Yl8VN
def resolve_requires(requirements_file):
    requirements = parse_requirements("./%s" % requirements_file,
            session=False)
    return [str(ir.req) for ir in requirements]


setup(
    name="unakite",
    version=unakite.get_version(),
    license=unakite.__licence__,
    description="S3 proxy for binary fies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/candango/unakite",
    author=unakite.get_author(),
    author_email=unakite.get_author_email(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=["unakite"],
    install_requires=resolve_requires("requirements/basic.txt"),
)
