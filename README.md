# Monthly Challenge Project

## Overview
This is a Django project designed to present a unique challenge for each month of the year. The project consists of 12 links, each corresponding to a month. When a link is clicked, it redirects to a page displaying the challenge for that particular month.

## Features
- **12 Monthly Challenges**: Each month has its own dedicated challenge.
- **Django Framework**: Built using Django for robust backend support.
- **Dynamic Routing**: Each month's link dynamically routes to the respective challenge page.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Mohamed-Salem-Ali/Month-Challenges.git
    cd Month-Challenges
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

- Visit `http://127.0.0.1:8000/` in your web browser.
- Click on any month's link to view the challenge for that month.

## Project Structure

- **challenges/**: Contains the Django app for the challenges.
  - **templates/challenges/**: HTML templates for the challenge pages.
  - **urls.py**: URL routing for the challenges.
  - **views.py**: View functions to handle the logic for each month's challenge.

- **monthly_challenge/**: Main project directory.
  - **settings.py**: Project settings.
  - **urls.py**: URL routing for the project.

## Example

Here's a simple example of how the project routes and views might look:

### urls.py (in challenges app)
```python
from django.urls import path
from . import views

urlpatterns = [
    path('<int:month>/', views.monthly_challenge, name='month-challenge'),
]
