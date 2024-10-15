[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16561795)
# File handling challenge

## Task 1 - Reading a file
There is a basic text file called task_1.txt

You need to write a function which will read in this file

Each line has one item, an integer value

Your function should add up all the values and return the result

Ensure the function is named ```task_1()```

## Task 2 - Italian Menu

You have been asked to create a simple ordering system for an Italian Takeaway

The menu is stored as a CSV, where each item is specified with a letter-number code (e.g. S1) - menu.csv

Customers order food by entering the food codes, for example a user could order: ```S4,P3,P7,X2,D4,C1,W2```

You should write a function which asks users to input menu options to order food, they should be able to enter as many as they wish

For each option they pick, the function should find the price of that menu item and keep a running total

Once the user has picked everything they want the funciton should **return** the total cost

Ensure the funciton is called ```task_2()```

## Task 3 - Contact Book

You have a file called contact.json, this is a simple "contact book"

Each entry in the file has a key which is someones name, and a value which is a JSON string containing their number and email

Your task is to write a function which will read in the content of the JSON file, then ask the user to enter a name

If the name is in the JSON data then you should **return** a string following this format

```Number: {number}, Email: {email}```

Otherwise you should **return** the following message:
```User not found.```