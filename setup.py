from setuptools import setup, find_packages

setup(
    name="juegos_azar",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="David Escrivá",
    author_email="david97escriva@gmail.com",
    description="Una librería con juegos de azar escritos en Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/esscri97/juegos_azar",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
) 