<div align="center">
<h1 align="center">
<img src="https://github.com/TiagoIesbick/little-lemon-capstone/blob/main/src/assets/images/logo.png" width="200" />
<br>api-little-lemon
</h1>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Jinja-B41717.svg?style&logo=Jinja&logoColor=white" alt="Jinja" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Django-092E20.svg?style&logo=Django&logoColor=white" alt="Django" />
</p>
<img src="https://img.shields.io/github/languages/top/TiagoIesbick/api-little-lemon?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/TiagoIesbick/api-little-lemon?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/TiagoIesbick/api-little-lemon?style&color=5D6D7E" alt="GitHub commit activity" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#%EF%B8%8F-modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running api-little-lemon](#-running-api-little-lemon)
    - [🧪 Tests](#-tests)
- [🎯 Endpoints](#-endpoints)
- [🤝 Contributing](#-contributing)

---


## 📍 Overview

Fully functioning API project for the fictional Little Lemon restaurant so that the client application developers can use the APIs to develop web and mobile applications. People with different roles will be able to browse, add and edit menu items, place orders, browse orders, assign delivery crew to orders and finally deliver the orders.

Filtering, pagination, sorting and throttling capabilities as well as authentication and authorization.

Developed  with 💜 by Tiago Iesbick

---

## 📦 Features

- User management and token based authentication with [djoser](https://djoser.readthedocs.io/en/latest/index.html);
- Add and remove users from groups;
- List, create, retrieve, update and destroy categories;
- List, create, retrieve, update and destroy menu items;
- List, create and destroy shopping cart;
- List and create orders;
- Retrieve, update and destroy single order.

---


## 📂 Repository Structure

```sh
└── api-little-lemon/
    ├── LittleLemon/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── LittleLemonAPI/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations/
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── permissions.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── Pipfile
    ├── Pipfile.lock
    ├── db.sqlite3
    ├── manage.py
    └── notes.txt
```


---

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Pipfile](https://github.com/TiagoIesbick/api-little-lemon/blob/master/Pipfile)           | The code in the Pipfile file specifies the dependencies and required versions of the packages for a project. In this case, it lists Django, Django Rest Framework, Djoser, Django Rest Framework XML, Django Filter, and Bleach as the required packages. The code also specifies that these packages should be fetched from the PyPI package repository and that they should be compatible with Python version 3.11. |
| [notes.txt](https://github.com/TiagoIesbick/api-little-lemon/blob/master/notes.txt)       | The code contains user credentials for a superuser, manager, delivery crew, and customers. Each user has a username, email, and password associated with their account.                                                                                                                                                                                                                                               |
| [Pipfile.lock](https://github.com/TiagoIesbick/api-little-lemon/blob/master/Pipfile.lock) | Pipfile.lock replaces the requirements.txt file used in most Python projects and adds security benefits of tracking the packages hashes that were last locked. This file is managed automatically through locking actions.                                                                                                                                                                                                                                                                                                                                                                                             |
| [manage.py](https://github.com/TiagoIesbick/api-little-lemon/blob/master/manage.py)       | A command-line utility that lets you interact with this Django project in various ways.                                                                                                                                                                                                                                                                                                                                                                                             |
| [db.sqlite3](https://github.com/TiagoIesbick/api-little-lemon/blob/master/db.sqlite3)       | Database created with models from models.py and the users from notes.txt.                                                                               |

</details>

<details closed><summary>Littlelemon</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                                         |
| ---                                                                                              | ---                                                                                                                                                                                                                                                                                             |
| [settings.py](https://github.com/TiagoIesbick/api-little-lemon/blob/master/LittleLemon/settings.py) | The code defines the settings for a Django project called LittleLemon. It includes configuration for database, internationalization, static files, authentication, and pagination. Additionally, it installs and configures various Django applications and libraries for REST API development. |
| [urls.py](https://github.com/TiagoIesbick/api-little-lemon/blob/master/LittleLemon/urls.py)         | Main URL dipatcher.                                                                                                                                                                                                                                                                       |
| [wsgi.py](https://github.com/TiagoIesbick/api-little-lemon/blob/master/LittleLemon/wsgi.py)         | The Web Server Gateway Interface (WSGI, pronounced whiskey or WIZ-ghee) is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language.                                                                                                                                                                                                                                                                       |
| [asgi.py](https://github.com/TiagoIesbick/api-little-lemon/blob/master/LittleLemon/asgi.py)         | ASGI (Asynchronous Server Gateway Interface) provides an interface between async Python web servers and applications while it supports all the features provided by WSGI.                                                                                                                                                                                                                                                                       |

</details>

<details closed><summary>Littlelemonapi</summary>

| File                                                                                                      | Summary                   |
| ---                                                                                                       | ---                       |
| [tests.py](https://github.com/TiagoIesbick/api-little-lemon/blob/master/LittleLemonAPI/tests.py)             | Create your tests here    |
| [permissions.py](https://github.com/TiagoIesbick/api-little-lemon/blob/master/LittleLemonAPI/permissions.py) | Permissions functions and classes |
| [urls.py](https://github.com/TiagoIesbick/api-little-lemon/blob/master/LittleLemonAPI/urls.py)               | Secondary URL dispatcher |
| [views.py](https://github.com/TiagoIesbick/api-little-lemon/blob/master/LittleLemonAPI/views.py)             | Python functions and classes that takes http requests and returns http response. |
| [models.py](https://github.com/TiagoIesbick/api-little-lemon/blob/master/LittleLemonAPI/models.py)           | Tables and fields of our database. |
| [admin.py](https://github.com/TiagoIesbick/api-little-lemon/blob/master/LittleLemonAPI/admin.py)             | The admin.py file is used to display our models in the Django admin panel. |
| [apps.py](https://github.com/TiagoIesbick/api-little-lemon/blob/master/LittleLemonAPI/apps.py)               | The apps.py convention merely allows Django to load them automatically when INSTALLED_APPS contains the path to an application module rather than the path to a configuration class. |
| [serializers.py](https://github.com/TiagoIesbick/api-little-lemon/blob/master/LittleLemonAPI/serializers.py) | Serializers in Django REST Framework are responsible for converting objects into data types understandable by javascript and front-end frameworks. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data. |

</details>

<details closed><summary>Migrations</summary>

| File                                                                                                                   | Summary                   |
| ---                                                                                                                    | ---                       |
| [0001_initial.py](https://github.com/TiagoIesbick/api-little-lemon/blob/master/LittleLemonAPI/migrations/0001_initial.py) | Django creates a migration file inside the migration folder for each model to create the table schema, and each table is mapped to the model of which migration is created. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- i Python 3.11`

`- i Pipenv`

### 🔧 Installation

1. Clone the api-little-lemon repository:
```sh
git clone https://github.com/TiagoIesbick/api-little-lemon
```

2. Change to the project directory:
```sh
cd api-little-lemon
```

3. Create a virtualenv:
```sh
pipenv shell
```

4. Install the dependencies:
```sh
pipenv install
```

### 🤖 Running api-little-lemon

```sh
python manage.py runserver
```

### 🧪 Tests
```sh
pytest
```

---


## 🎯 Endpoints

| Available endpoints | Methods    | Description |
|---------------------|------------|-------------|
| `/admin/` | GET | Django administration. |
| `/api/users/` | GET, POST, HEAD, OPTIONS | List and create users. |
| `/api/users/me/` | GET, PUT, PATCH, DELETE, HEAD, OPTIONS | Retrieve, update and destroy your own user. |
| `/api/users/confirm/` | GET, PUT, PATCH, DELETE, HEAD, OPTIONS | Finish user process. |
| `/api/users/resend_activation/` | POST, OPTIONS | Re-send the activation e-mail. |
| `/api/users/set_password/` | POST, OPTIONS | Change user password. |
| `/api/users/reset_password/` | POST, OPTIONS | Send email to user with password reset link. |
| `/api/users/reset_password_confirm/` | POST, OPTIONS | Finish reset password process. |
| `/api/users/set_username/` | POST, OPTIONS | Change username field. |
| `/api/users/reset_username/` | POST, OPTIONS | Send email to user with username reset link. |
| `/api/users/reset_username_confirm/` | POST, OPTIONS | Finish reset username process. |
| `/token/login/` | POST, OPTIONS | Obtain user authentication token. |
| `/token/logout/` | POST, OPTIONS | Logout user (remove user authentication token). |
| `/api/groups/manager/users` | GET, OPTIONS, POST | List and add users to managers group. |
| `/api/groups/manager/users/<int>` | OPTIONS, DELETE | Remove user from managers group. |
| `/api/groups/delivery-crew/users` | GET, OPTIONS, POST | List and add users to delivery crew. |
| `/api/groups/delivery-crew/users/<int>` | OPTIONS, DELETE | Remove user from delivery crew. |
| `/api/categories` | GET, POST, HEAD, OPTIONS | List and create categories. |
| `/api/categories/<int>` | GET, PUT, PATCH, DELETE, HEAD, OPTIONS | Retrieve, update and destroy single category. |
| `/api/menu-items` | GET, POST, HEAD, OPTIONS | List and create menu items. |
| `/api/menu-items/<int>` | GET, PUT, PATCH, DELETE, HEAD, OPTIONS | Retrieve, update and destroy single menu item. |
| `/api/cart/menu-items` | GET, POST, DELETE, HEAD, OPTIONS | List, create and destroy shopping cart. |
| `/api/orders` | GET, POST, HEAD, OPTIONS | List and create orders. |
| `/api/orders/<int>` | GET, PUT, PATCH, DELETE, HEAD, OPTIONS | Retrieve, update and destroy single order. |

---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---
