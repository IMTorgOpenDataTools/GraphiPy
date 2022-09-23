from pathlib import Path

from setuptools import setup, find_packages


readme = Path("README.md").read_text(encoding="utf-8")
version = '0.1.0'   #Path("_version.py").read_text(encoding="utf-8")
with open('requirements.txt') as f:
    required = f.read().splitlines()
about = {}
#exec(version, about)


setup(
    name='graphipy',
    version='0.1.0',
    author="",
    description="GraphiPy simplifies the extraction of data from different social media websites. Instead of having to study the different APIs of each website, just provide the API keys and use GraphiPy!",
    long_description=readme,
    url="https://github.com/IMTorgOpenDataTools/GraphiPy",
    packages=find_packages(include=['graphipy']),
    python_requires=">=3.10",
    install_reqs = required
)