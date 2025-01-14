import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "gcix",
    "version": "v0.0.6",
    "description": "GitLab CI X Library (X stands for multilanguage)",
    "license": "Apache-2.0",
    "url": "https://gitlab.com/gcix/gcix.git",
    "long_description_content_type": "text/markdown",
    "author": "Daniel von Essen<daniel@vonessen.eu>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://gitlab.com/gcix/gcix.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "gcix",
        "gcix._jsii"
    ],
    "package_data": {
        "gcix._jsii": [
            "gcix@v0.0.6.jsii.tgz"
        ],
        "gcix": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "jsii>=1.84.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": [
        "src/gcix/_jsii/bin/cfnwaiter"
    ]
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
