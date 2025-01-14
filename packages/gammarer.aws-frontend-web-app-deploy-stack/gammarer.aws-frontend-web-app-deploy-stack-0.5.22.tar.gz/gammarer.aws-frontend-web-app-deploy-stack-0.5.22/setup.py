import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "gammarer.aws-frontend-web-app-deploy-stack",
    "version": "0.5.22",
    "description": "This is an AWS CDK Construct to make deploying a Frontend Web App (SPA) deploy to S3 behind CloudFront.",
    "license": "Apache-2.0",
    "url": "https://github.com/yicr/aws-frontend-web-app-deploy-stack.git",
    "long_description_content_type": "text/markdown",
    "author": "yicr<yicr@users.noreply.github.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/yicr/aws-frontend-web-app-deploy-stack.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "gammarer.aws_frontend_web_app_deploy_stack",
        "gammarer.aws_frontend_web_app_deploy_stack._jsii"
    ],
    "package_data": {
        "gammarer.aws_frontend_web_app_deploy_stack._jsii": [
            "aws-frontend-web-app-deploy-stack@0.5.22.jsii.tgz"
        ],
        "gammarer.aws_frontend_web_app_deploy_stack": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.62.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "gammarer.aws-secure-bucket>=0.11.5, <0.12.0",
        "gammarer.aws-secure-cloudfront-origin-bucket>=0.7.1, <0.8.0",
        "gammarer.aws-secure-frontend-web-app-cloudfront-distribution>=0.7.8, <0.8.0",
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
