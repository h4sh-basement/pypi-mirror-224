import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws_prototyping_sdk.cdk_graph_plugin_diagram",
    "version": "0.19.64",
    "description": "@aws-prototyping-sdk/cdk-graph-plugin-diagram",
    "license": "Apache-2.0",
    "url": "https://github.com/aws/aws-prototyping-sdk",
    "long_description_content_type": "text/markdown",
    "author": "AWS APJ COPE<apj-cope@amazon.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/aws/aws-prototyping-sdk"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_prototyping_sdk.cdk_graph_plugin_diagram",
        "aws_prototyping_sdk.cdk_graph_plugin_diagram._jsii"
    ],
    "package_data": {
        "aws_prototyping_sdk.cdk_graph_plugin_diagram._jsii": [
            "cdk-graph-plugin-diagram@0.19.64.jsii.tgz"
        ],
        "aws_prototyping_sdk.cdk_graph_plugin_diagram": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.81.0, <3.0.0",
        "aws_prototyping_sdk.aws_arch<1.0.0",
        "aws_prototyping_sdk.cdk_graph<1.0.0",
        "constructs>=10.2.39, <11.0.0",
        "jsii>=1.82.0, <2.0.0",
        "projen>=0.71.92, <0.72.0",
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
        "Development Status :: 4 - Beta",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
