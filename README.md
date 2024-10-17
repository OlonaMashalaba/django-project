# Django Project

## How to Install
1. Clone the repository:
   ```
   git clone <repo_url>
   ```
2. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python manage.py runserver
   ```

## Docker Instructions
1. Build the Docker image:
   ```
   docker build -t django_app .
   ```
2. Run the container:
   ```
   docker run -p 8000:8000 django_app
   ```
