# wemanity-gilded-rose
Kata for wemanity job interview  
Requirements : https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.txt

# how to use
This kata solution was coded using Python 3.6.9 on Ubuntu 18.04.5 LTS.

The legacy code can be found in the file legacy_gilded_rose.py
The solution can be found in the file gilded_rose.py

To test the solution, you will first need to install Python 3 then, in a command prompt:
1. Run the unit tests entering the following command line
```bash
python3 test_gilded_rose.py
```
2. Run the text fixture entering the following command line with optional parameter to set the number of days to simulate (default = 2)
```bash
python3 texttest_fixtyre.py [days_to_simulate]
```

# my environment
To develop this solution I created a virtual environment in which I added two packages to test for code coverage  
Here were the steps I followed to create this environment, after opening a command prompt and navigating to my code repository :
1. Install pip3
```bash
sudo apt install python3-pip
```
2. Install virtualenv
```bash
sudo pip3 install virtualenv
```
3. Create a new virtual environment named gildedrose
```bash
virtualenv gildedrose
```
4. Enter the virtual environment
```bash
source gildedrose/bin/activate
```
5. Install the packages coverage and pytest-coverage
```bash
pip install coverage
pip install pytest-cov
```
6. Create HTML report to see code coverage
```bash
pytest --cov-report html  --cov=gilded_rose .\test_gilded_rose.py
```
Now there should be a new repository called "htmlcov" in your code repository. In this folder is a file called gilded_rose_py.html. Open it using a browser to see code coverage. Mine looks like this :  
![htmlcov](https://user-images.githubusercontent.com/16143121/119800561-2f90ca00-bedd-11eb-844b-5911a88a2f2c.png)
