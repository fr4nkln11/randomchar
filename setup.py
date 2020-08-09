import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="randomChar",
    version="0.1.0",
    author="Franklin Ikeh",
    author_email="ikehfranklind3c0d3r@gmail.com",
    description="A package that makes random character or sequence generation much easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fr4nkl1n-1k3h/randomChar",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
