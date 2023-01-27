from skbuild import setup  # This line replaces 'from setuptools import setup'


setup(
    name="example",
    version="0.0.1",
    description="a minimal example package",
    author='Joris Van den Bossche',
    license="MIT",
    packages=['example'],
    python_requires=">=3.7",
)
