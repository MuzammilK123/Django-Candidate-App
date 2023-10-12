# Django Candidate Application

## Project Description
The Django Candidate Application is a web application that allows users to create accounts, log in, write and view blog posts, and contact the site administrators. This README provides essential information on how to set up and use the application.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Django Development](#django-development)
  - [Creating a Virtual Environment](#creating-a-virtual-environment)
  - [Running the Development Server](#running-the-development-server)
  - [Database Migrations](#database-migrations)
- [Dockerization](#dockerization)
  - [Docker Installation](#docker-installation)
  - [Building the Docker Image](#building-the-docker-image)
  - [Running the Docker Container](#running-the-docker-container)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Features
- User registration and authentication.
- Blog post creation and viewing.
- Contact form for users to reach site administrators.

## Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:
- Python (3.6+)
- Django
- Pip (Python Package Manager)

### Installation
1. **Clone the repository:**
   ```shell
   git clone https://github.com/yourusername/your-django-candidate-app.git

2. **Navigate to the project directory:**
   ```shell
   cd portfolio

3. **Install project dependencies:**
   ```shell
   pip install -r requirements.txt

4. **Perform database migrations:**
   ```shell
   python manage.py migrate

5. **Create a superuser for admin access:**
   ```shell
   python manage.py createsuperuser

### Dockerization

**Docker Installation:**

If you don't have Docker installed, please install it.

**Building the Docker Image**

docker build -t portfolio ./


**Running the Docker Container**

docker run portfolio .


### Usage

To run the application locally, execute the following command:
   ```shell
   python manage.py runserver