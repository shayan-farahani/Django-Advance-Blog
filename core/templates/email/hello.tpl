{% extends "mail_templated/base.tpl" %}

{% block subject %}
account activations
{% endblock %}

{% block html %}
{{token}}
{% endblock %}