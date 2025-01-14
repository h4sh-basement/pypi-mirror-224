from os import path

from setuptools import find_namespace_packages, setup

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="kisters.network_store.model_library",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    author="Jesse VanderWees",
    author_email="jesse.vanderwees@kisters-bv.nl",
    description="Model library for the Kisters Network Store ecosystem",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/kisters/network-store/model-library",
    packages=find_namespace_packages(include=["kisters.*"]),
    zip_safe=False,
    install_requires=["pydantic"],
    extras_require={"test": ["pytest"]},
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Operating System :: OS Independent",
    ],
)
