from setuptools import setup

setup(
    name="wolfheaders",
    version="1.0.0",
    author="Lee",
    description="HTTP Security Header Analyzer",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    py_modules=[
        "wolfheaders",
        "banner",
        "analyzer",
        "scorer",
    ],
    install_requires=[
        "requests",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "wolfheaders=wolfheaders:main",
        ]
    },
    python_requires=">=3.9",
)