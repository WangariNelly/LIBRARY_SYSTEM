## Library Management System

This is a web application for helping librarians keep track of books issued.

# Technologies

HTML,
Tailwindcss,
JavaScript,
Python3 (flask),
Database (Mysql)

# Author
Nelly Wangari (nellywangari30@gmail.com)

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
