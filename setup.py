from setuptools import setup,find_packages

setup(name="cesus-income",
      version="0.0.1",
      author="Cmnepali",
      author_email="cmnepali@gmail.com",
      packages=find_packages(),
      install_reqires=["pandas","numpy","flask"])