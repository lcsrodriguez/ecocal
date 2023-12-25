import setuptools
from ecocal import (__version__,
                    __author__,
                    __package_name__)

with open("README.md", "r") as f:
    long_description = f.read()

PYTHON_MODULE_NAME: str = __package_name__
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setuptools.setup(
)
