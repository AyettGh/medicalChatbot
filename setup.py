#for installing local pacckage in virtual env
from setuptools import find_packages,setup
setup(
    name='mcqgenerator',
    version='0.0.1',
    author='AyettGh',
    author_email='ghribiayett@gmail.com',
    install_requires=['openai','langchain','streamlit','python-dotenv','PyPDF2'],
    packages=find_packages()#finding local packages from local directory
)