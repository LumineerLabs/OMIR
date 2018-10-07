from setuptools import setup, find_packages

setup(
    name='omir',
    version='0.1',
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        'librosa',
        'keras',
        'matplotlib',
        'numpy',
        'sklearn',
        'pandas',
        'ast',
        'IPython',
        ],
    author="Lane Haury",
    author_email="lane@lumineerlabs.com",
    description="Package of DSP and ML tools for doing streaming music analysis.",
    url="https://github.com/LumineerLabs/OMIR",
)