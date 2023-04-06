# SOFTWARE DEVELOPMENT

**Software development** is a process of **conceiving, specifying, designing, programming, documentating, testing,** and **bug** fixing involved in creating and maintaining applications, frameworks, or other software components.

# BASIC CHALLENGE

## 1. Generate Random Number
 Here is a simple Python function that will generate a random number between 0 and 100.
 ```python
    import random
    
    def generate_random_number():
        return random.randint(0, 100)
    random_number = generate_random_number()
    
    print(random_number)
```
This will generate a random number between 0 and 100 (inclusive), store it in the **'random_number'** variable, and then print it to the console.

Make sure to import the **'random'** module at the beginning of your Python file so that you can use the **'randint'** function.

## 2. Generate Random String
 Here is a Python function that will generate a random string that can contain lowercase letters, uppercase letters, numbers, and special characters.
 ```python
    import random
    import string

    def generate_random_string(length):
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        return ''.join(random.choice(letters) for i in range(length))

    random_string = generate_random_string(10)
    print(random_string)
```
In this function, we first import the **'random'** and **'string'** modules. The **'string'** module provides us with constants containing all lowercase letters (**'string.ascii_lowercase'**), uppercase letters (**'string.ascii_uppercase'**), digits (**'string.digits'**), and punctuation characters (**'string.punctuation'**).

The **'generate_random_string'** function takes a single argument **'length'**, which specifies the length of the random string to generate. We then concatenate all of these constant strings together to form a string of all possible characters. Finally, we use a **'for'** loop to generate a random character from this combined string **'length'** number of times, and **'join'** these characters together into a final string using the join method.

## 3. String and Array
 Here is a Python function that will take a string containing a name and split it into an array.
 ```python
    def split_name_into_array(name):
    return name.split()
    
    full_name = "Udin, Ujang, Asep"
    name_array = split_name_into_array(full_name)
    print(name_array)
```
In this function, we take a single argument **'name'**, which is a string containing a full name. We then use the **'split()'** method of strings to split the name into an array of separate words. By default, **'split()'** splits the string on whitespace, so this will work for names that consist of a first and last name separated by a space.

Note that this function assumes that the input name is in the correct format (i.e., contains only a first and last name separated by a space). If the input name contains more than two words or is in a different format, this function may not work as expected.

## 4. Detect Leap Year
Here is a Python function that will determine whether a given year is a leap year.
 ```python
   def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = 2023
if is_leap_year(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
```
In this function, we take a single argument year, which is the **'year'** we want to check for leapness. We then use a series of **'if'** statements to check whether the year is a leap year. The rules for determining leap years are:

- Every year that is evenly divisible by 4 is a leap year.
- However, years that are divisible by 100 are not leap years, unless they are also divisible by 400.

So the function first checks whether the year is divisible by 4 using the modulo operator **'%'**. If it is, it then checks whether it is divisible by 100 and 400 using nested **'if'** statements. If the year meets any of the conditions for being a leap year, the function returns **'True'**. Otherwise, it returns **'False'**.

## 5. Print Object
 Here is a Python function that will take an array of objects, where each object has a **'name'** and **'age'** property, and print out the data.
 ```python
   def print_object_data(data):
    for i, obj in enumerate(data):
        print(f"{i+1}. Nama: {obj['name']}, usia: {obj['age']}")

data = [
    {
        "name": "Udin",
        "age": 10
    },
    {
        "name": "Ujang",
        "age": 11
    },
    {
        "name": "Asep",
        "age": 12
    }
]

print_object_data(data)
```
In this function, we take a single argument **'data'**, which is an array of objects. We then use a **'for'** loop to iterate over each object in the array, and use the **'print()'** function to print out the **'name'** and **'age'** properties of each object. We add an extra **'print()'**' call at the end of each iteration to print a blank line and make the output more readable.

## 6. Classification
Here is a modified version of the function that will print the data in the requested format.
 ```python
    def group_people(data):
    groups = {
        "sex": {"male": [], "female": []},
        "age": {"under20": [], "older": []},
        "marriage": {"single": [], "double": []},
        "status": {"student": [], "employee": []}
    }
    
    for person in data:
        # Group by sex
        if person["sex"] == "male":
            groups["sex"]["male"].append(person["name"])
        elif person["sex"] == "female":
            groups["sex"]["female"].append(person["name"])
        
        # Group by age
        if person["age"] < 20:
            groups["age"]["under20"].append(person["name"])
        else:
            groups["age"]["older"].append(person["name"])
        
        # Group by marital status
        if person["marital"] == "single":
            groups["marriage"]["single"].append(person["name"])
        else:
            groups["marriage"]["double"].append(person["name"])
        
        # Group by job status
        if person["social"] == "student":
            groups["status"]["student"].append(person["name"])
        else:
            groups["status"]["employee"].append(person["name"])
    
    return groups

data = [
    {
        "name":"udin",
        "sex":"male",
        "age":10,
        "marital":"single",
        "social":"student"
    },
    {
        "name":"ujang",
        "sex":"male",
        "age":25,
        "marital":"married",
        "social":"employee"
    },
    {
        "name":"icih",
        "sex":"female",
        "age":10,
        "marital":"single",
        "social":"student"
    },
    {
        "name":"eneng",
        "sex":"female",
        "age":100,
        "marital":"married",
        "social":"employee"
    },
    {
        "name":"asep",
        "sex":"male",
        "age":20,
        "marital":"single",
        "social":"employee"
    }
]

result = group_people(data)
print(result)
```
In this version, we use a f-string to format the output string. The **'enumerate()'** function is used to iterate over the array of objects and keep track of the index **'i'** of each object, which is used to number the output strings starting from 1.

## 7. Find A
Here's a Python function that takes a word and number of loops, and returns the count of 'a' in the looped word.
 ```python
    def count_a(word, num_loops):
    looped_word = word * num_loops
    count = looped_word.count('a')
    return count

word = 'aha'
num_loops = 3
count = count_a(word, num_loops)
print(count)  # Output: 6
```
- First, the function multiplies the given word with the number of loops to create a looped word.
- Then, it counts the number of occurrences of **'a'** in the looped word using the **'count()'** method.
- Finally, it returns the count of **'a'**.
