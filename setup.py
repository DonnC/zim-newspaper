import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRED = [
    'newspaper3k',
    'nltk'
]

setuptools.setup(
    name="newspaper-zw",
    version="1.0.0",
    author="Donald Chinhuru",
    author_email="donychinhuru@gmail.com",
    description="get newspaper from online leading Zimbabwe content providers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DonnC/zim-newspaper",
    license="MIT",
    install_requires=REQUIRED,
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
)
