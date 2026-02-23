from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():

    return """
    <html>

    <head>

        <title>Flask API Playground</title>

        <style>

            body {
                font-family: Arial, sans-serif;
                margin: 40px;
            }

            h1 {
                margin-bottom: 10px;
            }

            a {
                display: inline-block;
                margin-right: 20px;
                margin-top: 10px;
                font-size: 18px;
            }

        </style>

    </head>


    <body>

        <h1>Welcome to Your First Flask App</h1>

        <p>
            This app demonstrates how Flask can fetch data from an API
            and display it as a table and charts.
        </p>

        <p>
            Try the following pages:
        </p>

        <a href="/users">View User Table</a>

        <a href="/charts">View Charts Dashboard</a>


    </body>

    </html>
    """

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

            <!-- 
              STUDENT EXERCISE:
              Add two more columns here to display: age and year
            -->

        </tr>
        """


    html = f"""
    <html>

    <head>

        <title>User List</title>

        <style>

            body {{
                font-family: Arial, sans-serif;
                margin: 20px 40px;
            }}


            table {{
                border-collapse: collapse;
                width: 80%;
                margin-bottom: 4px;
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


                <!-- 
                  STUDENT EXERCISE: 
                  Add two more headers here: Age and Year
                -->


            </tr>


            {rows}


        </table>


        <a href="/charts">View Charts</a>


    </body>

    </html>
    """


    return html

@app.route("/charts")
def charts_page():

    url = "https://api-swagger-playground.onrender.com/users"
    response = requests.get(url)
    users = response.json()

    # prepare year distribution
    year_counts = {}
    age_counts = {}

    for u in users:

        year = u["year"]
        year_counts[year] = year_counts.get(year, 0) + 1

        # STUDENT EXERCISE:
        # Add code to count how many students are in each age.
        # Hint: Look at how year_counts is calculated and apply the same pattern.

    html = f"""
    <html>

    <head>

        <title>User Charts</title>

        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

        <style>

            body {{
                font-family: Arial, sans-serif;
                margin: 20px 40px;
            }}

            .container {{
                display: flex;
                gap: 40px;
            }}

            .chart-box {{
                flex: 1;
                margin-bottom: 4px;
            }}

            canvas {{
                background: #fafafa;
                border: 1px solid #ddd;
                padding: 20px;
            }}

        </style>

    </head>


    <body>

        <div class="container">

            <div class="chart-box">

                <h2>Distribution by School Year</h2>

                <canvas id="yearChart"></canvas>

            </div>


            <div class="chart-box">

                <h2>Distribution by Age</h2>

                <canvas id="ageChart"></canvas>

            </div>

        </div>

        <a href="/users">View Table</a>

<script>

const yearDataRaw = {year_counts};
const ageDataRaw = {age_counts};


const yearLabelsMap = {{

    1: "Freshman",
    2: "Sophomore",
    3: "Junior",
    4: "Senior"

}};


const yearLabels = [];
const yearValues = [];

let otherCount = 0;


for (const [year, count] of Object.entries(yearDataRaw)) {{

    if (yearLabelsMap[year]) {{

        yearLabels.push(yearLabelsMap[year]);
        yearValues.push(count);

    }} else {{

        otherCount += count;

    }}

}}


if (otherCount > 0) {{

    yearLabels.push("Other");
    yearValues.push(otherCount);

}}



const ageLabels = Object.keys(ageDataRaw);

const ageValues = Object.values(ageDataRaw);



new Chart(document.getElementById('yearChart'), {{

    type: 'pie',

    data: {{

        labels: yearLabels,

        datasets: [{{
            data: yearValues
        }}]

    }}

}});


new Chart(document.getElementById('ageChart'), {{

    type: 'bar',

    data: {{

        labels: ageLabels,

        datasets: [{{
            label: 'Students',
            data: ageValues
        }}]

    }},

    options: {{

        responsive: true,

        scales: {{

            x: {{

                title: {{
                    display: true,
                    text: "Age"
                }}

            }},

            y: {{

                beginAtZero: true,

                ticks: {{

                    stepSize: 1

                }},

                title: {{
                    display: true,
                    text: "Number of Students"
                }}

            }}

        }}

    }}

}});

</script>


    </body>

    </html>
    """

    return html


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

