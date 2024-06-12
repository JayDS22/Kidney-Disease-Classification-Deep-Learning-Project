import setuptools

# While Uploading any code stack as a PYPI package, it displays the README.md on that website
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

#User Defined version
__version__ = "0.0.0"

REPO_NAME = " Kidney-Disease-Classification-Deep-Learning-Project"
AUTHOR_USER_NAME = "JayDS22"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "guwalanijj@gmail.om"

# Code to look for constructor file (__init__.py) in every package and download the packages in my local
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for CNN app',
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages= setuptools.find_packages(where="src")
)

# Create Virtual Environment
#- conda create -n cnn python=3.8 -y
#- conda activate cnn
