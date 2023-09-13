
# Project Title

E-Commerce Django Rest Framework Backend




## Installation

Install and configure the project

### Recommended but optionals steps.

* Create a virtual enviroment.
```bash
python3 -m venv .venv
```
* Activate the virtual enviroment.
```bash
cd .venv/Scripts
activate.ps1
```

### Install dependencies and configurations.

Step 1. Install the dependencies.
```bash
  pip install -r requirements.txt
```

Step 2. Navigate to the ecommerce folder and make the migrations.
```bash
  cd ecommerce
  python3 manage.py makemigrations
  python3 manage.py migrate
```
Step 3. Generate the static files.
```bash
  python3 manage.py collectstatic
```
Step 4. Create a super user!.
```bash
  python3 manage.py createsuperuser
```
Step 5. Voilà! Now you can execute the server
```bash
  python3 manage.py runserver
```

Now you can navigate to **/admin** route to access to the admin panel, or you can go to:

***/redocs***

or...

***/docs***

To read the auto-generated documentation!