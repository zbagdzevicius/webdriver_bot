import setuptools
setuptools.setup(
     name='webdriver_bot',  
     version='0.22',
     author="Zygimantas Bagdzevicius",
     author_email="zbagdzevicius@gmail.com",
     description="wrapper for selenium",
     url="https://github.com/zbagdzevicius/webdriver_bot",
     packages=setuptools.find_packages(),
     include_package_data=True,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires=[
         'selenium',
     ],
 )