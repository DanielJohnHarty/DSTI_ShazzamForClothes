# Shazzam For Clothes

## Task
Create a service which on, reception of a photo or an image from a user, can provide relevant recommendations for wheere the user can buy clothes similar to those in the image.

>A user sees a person with an appealing outfit or piece of clothing. Being as little weird as possible, user takes a picture using the service interface/application. After processing the image, the service returns a series of recommendations for the user to buy related items of clothing from online stores.

![Image Processing Daemon Service](https://github.com/DanielJohnHarty/DSTI_ShazzamForClothes/blob/master/Documents/imgs/img_proc_daemon.png)

![User Shazzam Process](https://github.com/DanielJohnHarty/DSTI_ShazzamForClothes/blob/master/Documents/imgs/user_shazzam_process.png)


# ***QUICK START Part 1 - Setup***

# ***Step 1*** - *Install Anaconda based Python3 distribution on your machine*

You only need this if you don't have Anaconda already. Entering:
```conda --version```
...on your command line prompt will return a variant of "Not Found" if you don't have it.


[Anaconda Download](https://www.anaconda.com/distribution/#download-section)


# ***Step 2*** - *Download package*

```git clone https://github.com/DanielJohnHarty/DSTI_ShazzamForClothes.git```

# ***Step 3*** - *Create virtual environment*

cd into your ShazzamForClothes directory and recreate it's virtual environment using the following command:

- ```conda env create -f environment.yml```


# ***Step 4*** - *Create your config.ini*

In the folder ***ShazzamFoorClothes/config***, there is a file called ***config_default.ini*** which details all the keys, ids and passwords etc. that the package needs. 

Rename ***config_default.ini*** to ***config.ini*** and add the necessary details. **Don't "quote" strings in the ini file**.

# ***QUICK START Part 2 - Basic database_api Usage***

The database_api subpackage has a single 'Database' class which uses the credentials in your config.ini file to connect to the database.

Step 1: Import the module

```import ShazzamForClothes.database_api as db_api```

Step 2: Instantiate the Database class as an object

```db = db_api.Database()```

Step 3: Open a conection to the database

```db.open_connection()``` 

Step 4: Use the ***Database.run_query*** method to query the database.
```
sql="SELECT * FROM RAW_IMAGES;"
results = db.run_query(sql)
```

Step 5: Iterate through the results
```
for result in results:
    print(result)
```

***Database Structure Proposition***
![Database Structure](https://github.com/DanielJohnHarty/DSTI_ShazzamForClothes/blob/master/Documents/imgs/database_structure.png)

![Database_api instance run_query method](https://github.com/DanielJohnHarty/DSTI_ShazzamForClothes/blob/master/Documents/imgs/run_query.png)

### **You are encouraged to subclass the Database class for your team's activities.**


# ***QUICK START Part 3 - Image Preprocessing***

The img_preprocessor subpackage includes a multitude of functions to preprocess images. They are short, concise and understandable so rather than describe each of them, I recommend you [check out the code here.](https://github.com/DanielJohnHarty/DSTI_ShazzamForClothes/blob/master/ShazzamForClothes/img_preprocessor/img_api.py)

The following constants are defined in the ***img_preprocessor.img_api*** module:

- **STANDARD_IMAGE_SIZE = (224, 224)**

- **STANDARD_IMAGE_MODE = "RGB"**

The ***standardise_img*** function encompasses image loading, conversion and resizing in a single function call but the implementation will have to be adjusted if project requirements change.

### **You are encouraged to contribute to the ***img_preprocessor.img_api*** module**