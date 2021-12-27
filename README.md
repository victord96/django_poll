Polls
=====

Polls is a Django app to conduct Web-based polls. For each question,
visitors can choose between a fixed number of answers.

Quick start
-----------

1. Install poll_package included inside django-polls directory.

2. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

3. Include the polls URLconf in your project urls.py like this::

    path('polls/', include('polls.urls')),

4. Run ``python manage.py migrate`` to create the polls models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
