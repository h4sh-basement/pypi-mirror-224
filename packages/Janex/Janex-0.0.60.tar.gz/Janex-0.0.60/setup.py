import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # Here is the module name.
    name="Janex",

    # version of the module
    version="0.0.60",

    # Name of Author
    author="Cipher58",

    download_url = 'https://github.com/Cipher58/Janex-Python.git',

    # your Email address
    author_email="cipher58public@gmail.com",

    # #Small Description about module
    # description="adding number",

    # long_description=long_description,

    # Specifying that we are using markdown file for description
    long_description=long_description,
    long_description_content_type="text/markdown",

    # Any link to reach this module, ***if*** you have any webpage or github profile
    url="https://github.com/Cipher58/Janex-Python",

    packages=setuptools.find_packages(),


    #if module has dependencies i.e. if your package rely on other package at pypi.org
    # then you must add there, in order to download every requirement of package

    install_requires=[
        "CipherProgram",
        ],


    license="Lily 1.0",

    # classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
