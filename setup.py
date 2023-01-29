import re

import setuptools

# Get the version
version_regex = r'__version__ = ["\']([^"\']*)["\']'
with open("getnet/__init__.py", "r") as f:
    text = f.read()
    match = re.search(version_regex, text)

    if match:
        VERSION = match.group(1)
    else:
        raise RuntimeError("No version number found!")

print("Version: {}".format(VERSION))

APP_NAME = "getnet-python"

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=APP_NAME,
    version=VERSION,
    description="A Getnet SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Fabio Vitor",
    author_email="fabvitor2010@gmail.com",
    url="https://github.com/FVitor7/getnet-python",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=["requests>=2.0.0", "requests-oauthlib>=1.2.0", "python-dateutil==2.8.1"],
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    zip_safe=False,
)
