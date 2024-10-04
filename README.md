# ATM-Project

## Project Overview

The ATM-Project is a Django-based web application that simulates the functionalities of an Automated Teller Machine (ATM). It allows users to interact with the system as both administrators and users, performing essential banking operations such as checking balances, withdrawing money, and managing accounts. The project follows Agile development practices to ensure continuous improvements and collaboration throughout its lifecycle.

## Features

- **User Account Management**: 
  - Create, view, and update user accounts.
  - User authentication and authorization for secure access.
  
- **ATM Operations**:
  - Check account balance.
  - Withdraw funds from the account.
  - Deposit money into an account.

- **Administrator Panel**:
  - Manage users and their accounts.
  - Monitor transactions and system activities.
  
- **SQLite Database**:
  - Database for storing user and transaction data.
  
## Setup Instructions

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- Django
- Git (optional, if you want to clone the project)

### Installation Steps

1. **Clone the repository** (if using Git):
    ```bash
    git clone <repository-url>
    ```
   
2. **Navigate to the project directory**:
    ```bash
    cd ATM-Project-main(1)
    ```

3. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install project dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:8000/`.

## Technologies Used

- **Django**: Python-based web framework for building robust web applications.
- **SQLite**: Database used for storing user and transaction data.
- **HTML/CSS**: Front-end technologies for the user interface.
- **Agile Development**: Development methodology followed to ensure continuous delivery and feedback.