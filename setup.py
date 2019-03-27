import setuptools

long_description = open("README.md").read()

setuptools.setup(
    name="progressbarABC",
    version="1.0.5",
    author="Anselm Rothe",
    author_email="anselm@nyu.edu",
    description="Progressbar for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anselmrothe/progressbar",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 ",
        "Operating System :: OS Independent",
    ]
)
