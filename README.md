### Installing project dependencies:
___
Update to Python 3.9 if you haven't already

Run the following in the project root directory:
```bash
schedule_optimization> pip install -r requirements.txt
```

Install the current version (16.x) of [Node.js](https://nodejs.org/en/download/current/)

On the command line, change the working directory to
```bash
path to \schedule_optimization\web_app_vue
```
then run
```bash
npm install web_app_vue
```

### Working with the project
___
**To run the app in Django:**
```bash
...\schedule-optimization> python manage.py runserver
```
With the Django server running:
- Access the Django admin GUI by navigating to http://127.0.0.1:8000/admin
- Access the Django REST Framework GUI by navigating to http://127.0.0.1:8000/api

**In Vue.js:**
```bash
...\web_app_vue> npm run serve
```


