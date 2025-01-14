#! /usr/bin/env python

import os
from setuptools import setup
import sys

PACKAGE_NAME = "bedboss"
REQDIR = "requirements"

# Additional keyword arguments for setup().
extra = {}

with open(f"{PACKAGE_NAME}/_version.py", "r") as versionfile:
    __version__ = versionfile.readline().split()[-1].strip("\"'\n")


def read_reqs(reqs_name):
    deps = []
    with open(os.path.join(REQDIR, f"requirements-{reqs_name}.txt"), "r") as f:
        for l in f:
            if not l.strip():
                continue
            deps.append(l)
    return deps


DEPENDENCIES = read_reqs("all")
extra["install_requires"] = DEPENDENCIES

scripts = None

with open("README.md") as f:
    long_description = f.read()

setup(
    name=PACKAGE_NAME,
    packages=[PACKAGE_NAME],
    version=__version__,
    description="Pipelines for genomic region file to produce bed files, "
    "and it's statistics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    keywords="project, bioinformatics, sequencing, ngs, workflow",
    url=f"https://github.com/databio/{PACKAGE_NAME}/",
    authors=[
        "Oleksandr Khoroshevskyi",
        "Michal Stolarczyk",
        "Ognen Duzlevski",
        "Jose Verdezoto",
        "Bingjie Xue",
    ],
    license="BSD2",
    entry_points={
        "console_scripts": [
            "bedboss = bedboss.__main__:main",
        ],
    },
    package_data={PACKAGE_NAME: ["templates/*"]},
    scripts=scripts,
    include_package_data=True,
    test_suite="tests",
    tests_require=read_reqs("dev"),
    setup_requires=(
        ["pytest-runner"] if {"test", "pytest", "ptr"} & set(sys.argv) else []
    ),
    **extra,
)
