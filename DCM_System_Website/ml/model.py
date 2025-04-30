{% extends 'base.html' %}
{% block content %}
<h2>Case Schedule (Prioritized)</h2>
<table>
    <thead>
        <tr>
            <th>Title</th>
            <th>Description</th>
            <th>Urgency</th>
            <th>Complexity</th>
            <th>Category</th>
        </tr>
    </thead>
    <tbody>
        {% for case in cases %}
        <tr>
            <td>{{ case.title }}</td>
            <td>{{ case.description }}</td>
            <td>{{ case.urgency }}</td>
            <td>{{ case.complexity }}</td>
            <td>{{ case.category }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
