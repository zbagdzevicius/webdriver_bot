import setuptools
setuptools.setup(
     name='webdriver_bot',  
     version='0.24',
     author="Zygimantas Bagdzevicius",
     author_email="zbagdzevicius@gmail.com",
     description="wrapper for selenium",
     url="https://github.com/zbagdzevicius/webdriver_bot",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires=[
         'selenium',
     ],
 )