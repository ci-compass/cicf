from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/users")
def user_list_page():
    url = f"https://api-swagger-playground.onrender.com/users"
    response = requests.get(url)
    users = response.json()
    rows = ""
    for u in users:
        rows += f"""
        <tr>
            <td>{u['id']}</td>
            <td>{u['name']}</td>
            <td>{u['email']}</td>
            <td>{u['age']}</td>
            <td>{u['year']}</td>
        </tr>
        """

    html = f"""
    <html>
    <head>
        <title>User List</title>
        <style>
            table {{
                border-collapse: collapse;
                width: 80%;
            }}
            th, td {{
                border: 1px solid #ccc;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f4f4f4;
            }}
        </style>
    </head>
    <body>
        <h2>All Users</h2>
        <table>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Age</th>
                <th>Year</th>
            </tr>
            {rows}
        </table>
    </body>
    </html>
    """

    return html
