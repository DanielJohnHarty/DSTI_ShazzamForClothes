# Shazzam For Clothes

## Task
Create a service which on, reception of a photo or an image from a user, can provide relevant recommendations for wheere the user can buy clothes similar to those in the image.

>A user sees a person with an appealing outfit or piece of clothing. Being as little weird as possible, user takes a picture using the service interface/application. After processing the image, the service returns a series of recommendations for the user to buy related items of clothing from online stores.



![Database Structure](https://github.com/DanielJohnHarty/DSTI_ShazzamForClothes/blob/master/Documents/imgs/database_structure.png)

![Image Processing Daemon Service](https://github.com/DanielJohnHarty/DSTI_ShazzamForClothes/blob/master/Documents/imgs/img_proc_daemon.png)

![User Shazzam Process](https://github.com/DanielJohnHarty/DSTI_ShazzamForClothes/blob/master/Documents/imgs/user_shazzam_process.png)


## Description of this repository

This GitHub repo contains:

1. A python package *ShazzamForClothes* which can be imported into your where you can use its *subpackages* to perform different tasks. HEre is a short description of each subpackage and see the relevant section forther down in this document for more details and examples of usage. The code is also documented.

    - The *ShazzamForClothes.database_api* subpackage includes functions and classes to interact with the project relational database. 
    - The *ShazzamForClothes.img_preprocessor* subpackage includes functions and classes to perform preprocessing operations on images, such as changing their size, shape and image type.
    - The *ShazzamForClothes.s3_api* subpackage includes functions and classes to interact with the *s3* storage for the *ShazzamForClothes* project. This will likely be removed as *s3* storage may not be necessary to deliver the prototype. 
    - The *ShazzamForClothes.tests* subpackage is the space where tests are stored for all the *ShazzamForClothes* subpackages
    - The *ShazzamForClothes.config* subpackage contains the *config.ini file*, where all credentials and other confidential should be stored. The *config.ini* is in the .gitignore file meaning it will not be uploaded to github but a template version of the file *config_default.ini* which contains all the keys but none of the values. For the code to wrok reliably in *ShazzamForCLothes*, the first step is to create valid and omplete *config.ini*.

2. A travis continuous integration file which is used by travis each time a commit, performing the operations defined in the *.travis.yml* file.
3. A *.gitignore* file which explicitly denies the uplaoding of any cacheed files, confidential files or 2scrappy notes" from being pushed to github.
4. an *environment.yml* file, which is a manifest of the python environment used during development.
    - To recreate this environment on your machine, make sure you have an Conda/Anaconda or MiniConda python distribution on your system and enter: 
        - ***conda env create -f environment.yml***
    - If you install additional packages and want to update the environment.yml file, use the command:
        - ***conda env export --from-history > environment.yml***
5. The documents folder holds various documents, images and specifications.

