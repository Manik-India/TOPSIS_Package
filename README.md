## Project Description

# TOPSIS-Python

***
pypi: <https://pypi.org/project/Topsis-Manik-101903077/>
<br>

***

### What is TOPSIS?
Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) originated in the 1980s as a multi-criteria decision making method. TOPSIS chooses the alternative of shortest Euclidean distance from the ideal solution, and greatest distance from the negative-ideal solution.

### How to use this package?
First you have to install the package name 'Topsis_Manik_101903077' using the following command:
```bash
pip install Topsis_Manik_101903077
```
{If it doesn't work use version after above command}

### Arguments Required:
(Assumne we have 3 attributes in dataset.)
1. You have to required one .csv file. (101903077-data.csv)
2. Pass weights to each attribute. (e.g.: "1,1,1")
3. Pass impacts to each attribute. (e.g.: "+,-,+")
4. Pass the name of the file with you want to put on .csv file. (101903077-result.csv)

Example:
```bash
from topsis_Manik_101903077.TOPSIS import *
TOPSIS_Manik('101903077-data.csv','1,1,1','+,-,+','101903077-result')
```


### Keep Smiling and Do Coding!!!
##### Manik
##### 101903077
