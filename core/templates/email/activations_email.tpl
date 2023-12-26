{% extends "mail_templated/base.tpl" %}

{% block subject %}
account activations
{% endblock %}

{% block html %}

<a href="http://127.0.0.1:8000/accounts/api/v1/activations/confirm/{{token}}">http://127.0.0.1:8000/accounts/api/v1/activations/confirm/{{token}}</a>
{% endblock %}