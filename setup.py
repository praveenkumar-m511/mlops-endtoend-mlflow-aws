import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "mlops-endtoend-mlflow-aws"
AUTHOR_USER_NAME = "praveenkumar-m511"
SRC_REP0 = "molpsProject"
AUTHOR_EMAIL = "praveenmcvls@gmail.com"

setuptools.setup(
    name=SRC_REP0,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app using mlops with mlflow",
    long_description=long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",

    },
    package_dir={"": "src"}
,    packages=setuptools.find_packages(where="src")
)
