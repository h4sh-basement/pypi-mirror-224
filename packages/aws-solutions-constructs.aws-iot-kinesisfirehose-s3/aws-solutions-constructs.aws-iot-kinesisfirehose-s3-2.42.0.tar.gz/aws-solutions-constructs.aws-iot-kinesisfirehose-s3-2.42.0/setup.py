import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws-solutions-constructs.aws-iot-kinesisfirehose-s3",
    "version": "2.42.0",
    "description": "CDK Constructs for AWS IoT to AWS Kinesis Firehose to AWS S3 integration.",
    "license": "Apache-2.0",
    "url": "https://github.com/awslabs/aws-solutions-constructs.git",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/awslabs/aws-solutions-constructs.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_solutions_constructs.aws_iot_kinesisfirehose_s3",
        "aws_solutions_constructs.aws_iot_kinesisfirehose_s3._jsii"
    ],
    "package_data": {
        "aws_solutions_constructs.aws_iot_kinesisfirehose_s3._jsii": [
            "aws-iot-kinesisfirehose-s3@2.42.0.jsii.tgz"
        ],
        "aws_solutions_constructs.aws_iot_kinesisfirehose_s3": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.82.0, <3.0.0",
        "aws-solutions-constructs.aws-kinesis-firehose-s3==2.42.0",
        "aws-solutions-constructs.core==2.42.0",
        "constructs>=10.0.0, <11.0.0",
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
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
