from setuptools import setup, find_packages

with open(file="requirements.txt", mode="r") as file:
    requirements = file.read().splitlines()

setup(
    name="medical-rag-chatbot",
    version="0.1.0",
    author="Saad Tariq",
    packages=find_packages(),
    install_requires=requirements
)