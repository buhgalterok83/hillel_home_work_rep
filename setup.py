from setuptools import setup, find_packages

setup(
    name="my_project",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "selenium"
    ],
    entry_points={
        "pytest11": [
            "my_project = my_project.pytest_plugin"
        ]
    },
)
