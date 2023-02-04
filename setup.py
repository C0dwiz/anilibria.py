from codecs import open
from pathlib import Path

import tomli
from setuptools import find_packages, setup

with open("pyproject.toml", "rb") as f:
    pyproject = tomli.load(f)


def get_long_description() -> str:
    return (Path(__file__).parent / "README.md").read_text()


def get_requirements(filename: str) -> list[str]:
    return (Path(__file__).parent / filename).read_text().splitlines()


setup(
    name=pyproject["tool"]["poetry"]["name"],
    version=pyproject["tool"]["poetry"]["version"],
    author="Damego",
    author_email="danyabatueff@gmail.com",
    description=pyproject["tool"]["poetry"]["description"],
    extras_require={"readthedocs": get_requirements("requirements-docs.txt")},
    include_package_data=True,
    install_requires=get_requirements("requirements.txt"),
    license="GPL-3.0 License",
    long_description_content_type="text/markdown",
    long_description=get_long_description(),
    url="https://github.com/Damego/anilibria.py",
    packages=find_packages(),
    python_requires=">=3.10",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
