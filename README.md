## Library Management System

LibMS( Library Management System) is a software for monitoring and controlling library transactions.It mainly focuses on basic operations in a library which includes adding new members, new books,updating new information,searching books and borrowing and returning of books.It automates the most tedious activities.It comprises of a relational database,software to interact with the database and two graphical user interfaces one for the users and the other for the librarian

# Technologies Software and Hardware

**HTML,
Tailwindcss,
JavaScript,
Python3 (flask),
Database (Mysql**)


# Author
Nelly Wangari(nellywangari30@gmail.com)

# Folders and directories
|   **File**   |   **Description**   |
| -------------- | --------------------- |
|[app](/build/app/) | Has [css](/build/app/static/), [html](/build/app/templates/), and [image](/build/app/static/img/) directories containing templates and resources for the website.|
|[Main App](/build/app/lbs.py)| Main script of the application|
|[Base](/build/app/common/base.py)| Initialize SQLAlchemy|
|[Blueprint](/build/app/blueprint/)| Blueprint defining routes fro interacting with the the pages of our website.|
|[Models](/build/app/models/)| Has python files defining table schemas and database operations.|
|[Utils](./build/app/utils/)| Util classes for generating books and users.|
|[Add Books and Users](./build/app/auto_insert_book_users.py)| Automatically adds books and users with help of functions in util directory.|
|[Project Tree](./lbs_tree.txt)| .txt file showing project tree|

# HOW TO USE

```python
Clone this repository and build the project using Visual Studio or any text editor of your choice.
If you are using the terminal cd into "lIBRARY_SYSTEM" directory.
Run the following code on your terminal "pip install -r requirements.txt" to install all the project dependancies
Type the following on the terminal "export FLASK_APP=lbs.py" and press Enter
Then, "flask run" and press Enter
This will open the development server and you will be able to access the project on your browser using the following address **"http://127.0.0.1:5000/"**
```

[def]: ../../../Pictures/Screenshots/Screenshot%20from%202023-03-29%2013-00-05.png