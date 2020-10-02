# Django restful framework training

## A few comments on the training

  1. I've started by installing these main dependencies below
    `pip install django djangorestfulframework pygments`

  2. Then I started a project called tutorial
    `django-admin startproject tutorial`

  3. changed to the correct directory
    `cd tutorial`

  4. I then created and started an app called snippets
    `python manage.py startapp snippets`

  5. I then added custom setting inside settings.py > installed apps
    `'rest_framework',
    'snippets.apps.SnippetsConfig'`
    That allows me to use rest framework and have communication with the app snippets

  6. python manage.py makemigrations snippets & python manage.py migrate

  7. Creates a serializer file

  8. Creates first CRUD operations inside serializer

  9. Changes class serializer to `ModelSerializer`

  10. Creates views at `snippets > views.py`

  11. Creates urls file in `snippets > urls.py`

  12. Import snippet urls to main url file `tutorial > urls.py`

**BONUS**

  13. We then installed httpie `pip install httpie` and run in your shell `http http://127.0.0.1:8000/snippets/`

  14. Imports response util from `rest_framework_response`

  15. Adds `format=None` to views' functions as a param