import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PriceHero-mehtaarn000",
    version="0.4.4",
    author="mehtaarn000",
    description="A python module that will allow users to get product prices information from a multitude of different websites. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mehtaarn000/PriceHero",
    packages=['PriceHero'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)