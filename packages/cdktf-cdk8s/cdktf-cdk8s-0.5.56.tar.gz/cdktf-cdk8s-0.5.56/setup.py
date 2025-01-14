import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdk8s",
    "version": "0.5.56",
    "description": "A compatibility layer for using cdk8s constructs within Terraform CDK.",
    "license": "MPL-2.0",
    "url": "https://github.com/cdktf/cdktf-cdk8s.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdktf/cdktf-cdk8s.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdk8s",
        "cdktf_cdk8s._jsii"
    ],
    "package_data": {
        "cdktf_cdk8s._jsii": [
            "cdktf-cdk8s@0.5.56.jsii.tgz"
        ],
        "cdktf_cdk8s": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "cdk8s>=2.1.6",
        "cdktf-cdktf-provider-kubernetes>=6.0.0",
        "cdktf>=0.16.0",
        "constructs>=10.0.25, <11.0.0",
        "jsii>=1.87.0, <2.0.0",
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
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
