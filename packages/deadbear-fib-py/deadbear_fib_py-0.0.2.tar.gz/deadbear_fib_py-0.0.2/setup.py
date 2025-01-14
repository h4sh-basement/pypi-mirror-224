from setuptools import find_packages, setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="deadbear_fib_py",
    version="0.0.2",
    author="Sean Baier",
    author_email="sean.baier@deadbear.io",
    description="Calculates a Fibonacci number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deadbearcode/pip-module-demo",
    install_requires=["PyYAML>=4.1.2", "dill>=0.2.8"],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "fib-number = deadbear_fib_py.cmd.fib_numb:fib_numb",
        ],
    },
    extras_require={"server": ["Flask>=1.0.0"]},
)
