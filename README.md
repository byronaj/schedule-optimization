### Project tools documentation:  
___

[Django 3.2 Web Framework](https://docs.djangoproject.com/en/3.2/contents/)  
[Django REST Framework](https://www.django-rest-framework.org/)  
[Vue.js (v3) JavaScript Framework](https://v3.vuejs.org/)  
[Bulma CSS framework](https://bulma.io/documentation/)  


### Installing project dependencies:  
___

1. Update to Python 3.9 if you haven't already


2. Run the following in the project root directory:  
   ```bash
    ...\schedule_optimization> pip install -r requirements.txt
    ```

3. Install the current version (16.x) of [Node.js](https://nodejs.org/en/download/current/)


4. Change the working directory to

   ```bash
    ...\schedule_optimization\web_app_vue
    ```
   then run
   ```bash
    ...\web_app_vue> npm install
    ```

### Working with the project:
___

**To run the app in Django:**

```bash
...\schedule-optimization\web_app_django> py manage.py runserver
```

With the Django development server running:
- Access the Django admin GUI by navigating to http://127.0.0.1:8000/admin
- Access the Django REST Framework GUI by navigating to http://127.0.0.1:8000/api/v1

**In Vue.js:**
```bash
...\schedule-optimization\web_app_vue> npm run serve
```

### Django database updates:
___
1. `...\schedule-optimization\web_app_django> py manage.py makemigrations`
2. `...\schedule-optimization\web_app_django> py manage.py migrate`

### Checking for gaps in testing:
___
**Using the python tool, coverage:**
```bash
# The location of your virtual environment directory may vary.
> coverage run --omit='*/.virtualenvs/*' manage.py test
> coverage html
```
You will see a directory called `htmlcov` in the project root.

Open index.html to see which files don't have 100% coverage.

### Running tests:
___
```bash
...\schedule-optimization/web_app_django> py manage.py test
```

## Push small commits frequently.
___
No large, dirty commits plzkthx.

Keep your local repository up to date with the `main` repository.

### PyCharm IDE
___
Set this up so PyCharm knows where to find everything and to use the manage.py utility.
![PyCharm Screenshot](https://github.com/CSCI-540-SDP/schedule-optimization-web-app-stack-force/blob/main/images/pycharm_django_support.png)

**Now, to run a task with code completion and hints:**
1. On the main menu, choose **Tools | Run manage.py task**, or press `Ctrl+Alt+R`.
The **manage.py** utility starts in its own console.

2. Type the name of the desired task.

