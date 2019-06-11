from setuptools import setup

setup(
    name = "lifxcmd",
    packages = ["lifxcmd"],
    install_requires = ["lifxlan"],
    extras_require = {
        "COLOUR": ["colour>=0.1.5"]
        },
    entry_points = {
        "console_scripts": ['lifxcmd = lifxcmd.lifxcmd:main']
        },
    version = "4",
    description = "A Python program that allows easy control of all bulbs on a network, or a specific bulb if required",
    author = "Steven Smith",
    author_email = "stevensmith.ome@gmail.com",
    license = "MIT",
    url = "https://github.com/blha303/lifxcmd",
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators"
        ]
    )
