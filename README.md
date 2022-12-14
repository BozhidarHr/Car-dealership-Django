<h2>Car Dealership Django Project</h2>

In order to run the project:

1. Clone the repo
 ```bash
 git clone https://github.com/BozhidarHr/Car-dealership-Django.git
 ```
 
 2. Create virtualenv
 ```bash
 cd my-project
 virtualenv env
 ```
 
 3. Activate virtualenv
 Windows
 ```bash
 env\Scripts\activate
 ```
 MAC OS/ Linux
 ```bash
 source env/bin/activate
 ```
 
4. Add dependencies 
```bash
 pip install -r requirements.txt
 ```
 
 5.Run migrations to set up database. 
  ```bash
 python manage.py migrate
 ```
 The projects uses postgreSQL database.

 Note: You can run the default django database - sqlite by changing the database settings in settings.py:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
 ```
 6.Start the server
 ```bash
 python manage.py runserver
 ```
 Note: If you experience "Secret key" issue when starting, make sure your .env files are set up in the configurations.
 
