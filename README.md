# calendar

# Upcoming events notificator


# The following is step by step instruction on how to get on with this application.

# First of all this repository includes absolutely all the files required to work, except for redis service, which is run in separate environment.


# After successfully cloning this repo to your environment, navigate to directory with a file named manage.py

# To start application firstly initiate work of celery services via 'celery -A notifications worker -l info'
# Then start django server via 'py manage.py runserver'

# You will also have to switch on redis service for celery to connect to it.

# To work with the pages you are required to send data via POST, sometimes GET will work

# Now you can navigate to 'localhost:8000/passless/auth/email/' providing 'email' key with the value of your email via json.
# At the moment the email sending is dummy model for testing you can obtain your token in Django console.

# Later after you obtained your 6 digit token navigate to 'localhost:8000/passless/auth/token' adding 'token' field with your 6 digit token as a value.
# That page will provide you with a token for authorization in the application. In order to keep authenticated you will have to provide 'Authorization: Token your_toke_here' in the headers of your request.

# Now new user account is created for your email and you can use functionality of the application.

# In order to create your first event navigate to 'localhost:8000/events/' and provide json file with the fields 'name', 'date_start', 'notify_me_in'.

# Or you can navigate via REST fw browsable API and do it in a browsable manner.

# That will create your first event and a task to send a notification to your email at time you specified in 'notify_me_in' field at earliest.

# The page you have just worked with fully supports CRUD requests, thus you can manipulate your events in any manner you wish.

# The problem with Updating date of notification is known of, it might be fixed, but that celery would not be used. You can make it with Django functionality only.

# Later you can also add events of specified country via 'localhost:8000/api/add_country_events/' providing 'caountry' field and a valid country as a value for it.

# That will create all the events of that country to your events list.

# Note that if you do not provide the page with country name it will add events of Kazakhstan as a default value.

