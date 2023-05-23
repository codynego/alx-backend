<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ _('home_title') }}</title>
</head>
<body>
    <h1>{{ _('home_header') }}</h1>
    {% if g.user %}
    <p>{{ _('logged_in_as', username=g.user.name) }}</p>
    {% else %}
    <p>{{ _('not_logged_in') }}</p>
    {% endif %}
    <p>{{ _('current_time_is', current_time=g.time) }}</p>
</body>
</html>
