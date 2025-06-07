from setuptools import setup, find_packages

setup(
    name="juegos_azar",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Tu Nombre",
    author_email="tu.email@ejemplo.com",
    description="Una librería de calculadoras matemáticas",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/calculadora-matematica",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 