from setuptools import setup, find_packages

setup(
    name="dev-dien-airdrop",
    version="0.1.2",
    description="A package for automatically claiming airdrops.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Smart Airdrop",
    author_email="smileuptn@gmail.com",
    url="https://github.com/Ngocgiau2000/dev-dien-airdrop",
    packages=find_packages(),
    install_requires=[
        "colorama",
        "requests",
        "brotli",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
