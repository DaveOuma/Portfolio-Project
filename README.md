# Portfolio Project

## Overview
This portfolio project demonstrates the integration of multiple programming languages and frameworks to create a robust web application. The project leverages C, HTML, CSS, JavaScript, and Python, specifically using the Django framework. The aim is to showcase proficiency in various technologies and their seamless integration into a cohesive project.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Getting Started](#getting-started)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Running the Application](#running-the-application)
7. [Project Details](#project-details)
    - [C Application](#c-application)
    - [Django Application](#django-application)
        - [Models](#models)
        - [Views](#views)
        - [Templates](#templates)
        - [Static Files](#static-files)
8. [Contribution](#contribution)
9. [License](#license)
10. [Contact](#contact)

## Project Structure
The project consists of the following components:

### C Programming
- **Objective**: Build a command-line application leveraging C's systems programming capabilities.
- **Integration**: The C application is interfaced with the Django project via system calls or inter-process communication.

### Django (HTML and CSS)
- **Objective**: Create visually appealing and responsive web pages using Django's templating engine.
- **Integration**: Design a dynamic landing page with HTML and CSS managed by Django.

### JavaScript
- **Objective**: Create interactive web elements or a simple game to enhance user interaction.
- **Integration**: Integrate JavaScript with the Django-powered frontend.

### Python (Django)
- **Objective**: Build a Django application that automates a repetitive task or solves a real-world problem.
- **Integration**: Leverage Django's ORM and framework features for backend development.

## Getting Started

### Prerequisites
- Python 3.x
- Django 3.x
- GCC (GNU Compiler Collection) for compiling the C program

### Installation
Clone the repository:

```bash
git clone https://github.com/yourusername/portfolio-project.git
cd portfolio-project

Set up a virtual environment:

```bash
`python -m venv env`
`source env/bin/activate`      # On Windows use `env\Scripts\activate`
Install the required Python packages:

```bash
`pip install -r requirements.txt`
Compile the C application:

```bash
`gcc -o your_c_application path/to/your_c_application.c`
### Configuration

Update the Django settings as needed, such as database configurations, static file paths, etc.

Running the Application
Apply Django migrations:

```bash
`python manage.py migrate`
Start the Django development server:

```bash
`python manage.py runserver`
Access the application:

Open your web browser and navigate to http://127.0.0.1:8000.

<h2>  Project Details </h2>
[C Application]
- The C application is a command-line tool that demonstrates data structures, algorithms, and memory management. It runs as a separate process and interacts with the Django application via system calls.

[Django Application]
- The Django application consists of models, views, and templates to manage the frontend and backend logic.

<h2>Models</h2>
- YourModel: Represents data entities with fields such as name and created_at.
Views
home: The main view that calls the C application and renders the output on the homepage.
Templates
home.html: The main template that displays the output of the C application and integrates HTML, CSS, and JavaScript.
<h2>Static Files</h2>
CSS: Located in portfolio/static/css/.
JavaScript: Located in portfolio/static/js/.
Contribution
Contributions are welcome! Please fork the repository and create a pull request with your changes.

### License
This project is licensed under the MIT License.

### Contact
For any inquiries or feedback, please contact davidomuga@gmail.com.
