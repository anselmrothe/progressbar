import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="progressbar",
    version="1.0.4",
    author="Anselm Rothe",
    author_email="anselm@nyu.edu",
    description="Progressbar for Python",
    long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/anselmrothe/progressbar",
    # packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 ",
        "Operating System :: OS Independent",
    ]
)
