import io
import os
import re
import sys
from shutil import rmtree

from setuptools import Command, setup

# Package meta-data.
name = "ternaus_cleantext"
description = "Clean text from extra spaces and special symbols as in the CLIP model."
url = "https://github.com/ternaus/ternaus-cleantext"
email = "iglovikov@gmail.com"
author = "Vladimir Iglovikov"
requires_python = ">=3.0.0"
current_dir = os.path.abspath(os.path.dirname(__file__))


def get_version() -> str:
    version_file = os.path.join(current_dir, name, "__init__.py")
    with io.open(version_file, encoding="utf-8") as f:
        return re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', f.read(), re.M).group(1)


# What packages are required for this module to be executed?
try:
    with open(os.path.join(current_dir, "requirements.txt"), encoding="utf-8") as f:
        required = f.read().split("\n")
except FileNotFoundError:
    required = []

version = get_version()

about = {"__version__": version}


def get_long_description() -> str:
    base_dir = os.path.abspath(os.path.dirname(__file__))
    with io.open(os.path.join(base_dir, "README.md"), encoding="utf-8") as f:
        return f.read()


class UploadCommand(Command):

    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Print things in bold."""

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds...")
            rmtree(os.path.join(current_dir, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution...")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine...")
        os.system("twine upload dist/*")

        self.status("Pushing git tags...")
        os.system("git tag v{0}".format(about["__version__"]))
        os.system("git push --tags")

        sys.exit()


setup(
    name=name,
    version=version,
    description=description,
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Vladimir Iglovikov",
    license="MIT",
    url=url,
    packages=["ternaus_cleantext"],
    install_requires=required,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    cmdclass={"upload": UploadCommand},
)
