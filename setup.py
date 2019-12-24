import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Endless-Sky-Mission-Builder',
    version='0.4.0',
    license='GPLv3',
    author='shitwolfymakes',
    author_email='shitwolfymakes@gmail.com',
    description='A RAD tool to help decrease the time it takes to create missions for Endless Sky',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/shitwolfymakes/Endless-Sky-Mission-Builder',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7'
)
