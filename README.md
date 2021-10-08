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
...\schedule-optimization> py manage.py runserver
```

With the Django development server running:
- Access the Django admin GUI by navigating to http://127.0.0.1:8000/admin
- Access the Django REST Framework GUI by navigating to http://127.0.0.1:8000/api

**In Vue.js:**
```bash
...\schedule-optimization\web_app_vue> npm run serve
```

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
...\schedule-optimization> py manage.py test
```

## Push small commits frequently.
No large, dirty commits plzkthx.

Keep your local repository up to date with the `main` repository.


