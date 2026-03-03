# CICF Week 7

The goals for this week are to

1. Use Swagger UI to explore API endpoints (GET, POST, PATCH, DELETE)
2. Build a simple Flask web application to interact with a live web API using HTTP
3. Understand the basics of software architecture and design patterns in the context of web services

## Data, Archives, and APIs

In this module, we treat the API as a simple gateway to an archive:

- Data is stored in structured form (JSON)
- The API defines how data can be accessed
- Clients do not access data files directly

This separation allows archives to remain stable and reusable, while different clients—web browsers, scripts, and applications—can access the same archive through the API.

This architectural pattern is common in real-world systems, especially digital archives, where records must remain consistent and accessible over long periods of time.

    [ Browser / curl / Swagger UI ]
            |
        HTTP
            |
    [ API ]
            |
    Data Storage (JSON files, databases, etc.)

### Try API with Swagger UI

Open this url in a browser:

    https://yaxue1123.github.io/api-swagger-playground/

In the `POST /users endpoint`, click "Try it out", input your basic information according to the required JSON format
in the "Request body" box:

```json
{
  "name": "string",
  "email": "string",
  "age": 0,
  "year": 0
}
```

Then click the "Execute" button. You will see the request and response details, including the request URL, the request body, and the response body. Code `201` means the request was successful and a new resource was created. The response body contains the information of the new user you just created.

```
curl -X 'POST' \
  'https://api-swagger-playground.onrender.com/users' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "User1",
  "email": "user1@email.com",
  "age": 21,
  "year": 3
}'
```

Then in the `GET /users` endpoint, click "Try it out" and then click "Execute". You will see the request and response details again. Code `200` means the request was successful. The response body contains the information of all users, including the user you just created. The header `Accept: application/json` is asking the server to return a JSON response body. 

You can also try the `PATCH /users/{user_id}` endpoint. This endpoint allows you to update part of an existing user's information. Click on `PATCH /users/{user_id}`, then click "Try it out". Enter a user ID, for example 1, in the user_id field. In the request body, enter a JSON object with the fields you want to change, such as:

```
{
  "age": 21
}
```

Then click "Execute". If the request is successful, you will see status code 200, which means the user was updated successfully. The response body will show the updated user object. Notice that only the specified field was changed, while the other fields remained the same. This is what makes PATCH different from POST: POST creates a new resource, while PATCH modifies an existing one.

You can also try the `DELETE /users/{user_id}` endpoint. This endpoint deletes an existing user. Click on `DELETE /users/{user_id}`, then click "Try it out". Enter a user ID, for example 1, and click "Execute". If the request is successful, you will see status code `200`. The response body will show the user that was deleted. Now, go back to the GET /users endpoint and click "Execute" again. You will see that the deleted user is no longer in the list. This shows how the DELETE request removes a resource from the server.

--- 

### Essential Concepts 

#### Common HTTP Methods

| Method | What it does | Example use in this week |
|------|-------------|--------------------------|
| GET  | Retrieve data from a server | Get a list of users |
| POST | Send new data to a server | Add a new user |
| PATCH | Update part of a resource | Update user age |
| DELETE | Remove data | Delete a user |

#### Common HTTP Status Codes

| Code range | Meaning | Example |
|-----------|--------|---------|
| 2xx | Success | 200 OK, 201 Created |
| 3xx | Redirection | 301 Moved Permanently |
| 4xx | Client error | 400 Bad Request, 404 Not Found |
| 5xx | Server error | 500 Internal Server Error |

## Digital archives in production: OpenAlex

So far, we worked with a simple teaching API where the structure and behavior were easy to observe.

Now let’s look at a real-world example: OpenAlex.

Last week, we used OpenAlex to examine the JSON responses. This week, we revisit OpenAlex from a broader perspective. OpenAlex is a large-scale digital archive, and its API is the interface that makes this archive accessible to the outside world.

A digital archive:

- Collects and organizes records

- Preserves them over time

- Provides structured access through an API

---

### Human-readable page vs API endpoint

First, visit in your browser:

https://openalex.org/works/w2764299839

This is a human-readable webpage (HTML), designed for people.

Now visit:

https://api.openalex.org/works/w2764299839

This is the API endpoint (JSON), designed for programs.

Same resource.
Different representation.

---

### Redirect and canonical URLs

Now try something interesting.

In your browser address bar, manually change the URL to:

`https://openalex.org/works/W2764299839` and click enter.

The url automatically changed to `https://openalex.org/works/w2764299839` with a lowercase `w`.

A redirect occurred from the uppercase URL to the lowercase URL.

OpenAlex enforces a canonical URL format.
Even though uppercase and lowercase may logically refer to the same work, the system standardizes the path.

This ensures that all requests resolve to a single canonical URL.

In large digital archives:

- Each record must have one stable identity

- URLs must be consistent

- External systems may cite and store these identifiers

Canonicalization protects long-term reference integrity.

### Comparison to our simple API

Our simple API playground returned JSON directly, without redirects or canonicalization.

Simple API:   Client --> Server --> JSON

Real-world APIs often include additional layers like this to improve reliability, performance, and maintainability.

OpenAlex: Client --> Redirect[Canonical URL] --> Server[API Server] --> JSON

## Build a simple Flask app

Flask is a very simple python framework for making web applications.
Here is a Flask app showing how a web server works.

First, create and activate a virtual environment, then install the required packages:

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install flask requests

Then start the Flask development server:

    $ python app.py

You should see output similar to:

  * Serving Flask app 'app'
  * Debug mode: on
  * Running on http://127.0.0.1:5000
  * Debugger is active!

The server is running on localhost "http://127.0.0.1:5000".
127.0.0.1 refers to the current computer. The 5000 says the server is listening on port 5000 on the current computer.
Open a web browser and type in the URL `localhost:5000`. You will see a page showing "Welcome to Your First Flask App." 
This is because in the file `app.py` we match that route `/` and say to return that text.
Enter `localhost:5000/users` in the browser or click on the link `View Table`, you will see a page with the table of all users we just created in the Swagger UI. 

When running in debug mode, Flask will automatically reload when you save changes to the code. You only need to refresh the browser to see updates.

### Exercise #1: Display additional user data

Currently, the table only shows the user ID, name, and email. However, the API also returns additional information for each user, including their **age** and **school year**.

Your task is to modify the file `app.py` to display this information in the table.

Specifically:

1. Open the file `app.py`.

2. Locate the `/users` route.

3. Then find the part of the code where each table row is generated inside the loop [Line 82], add two additional table cells to display the user's age and school year.

4. Then Find the HTML table header section and add two new column headers: `Age` and `Year` [Line 148].

5. Save the File.

6. Refresh the browser. You should now see two new columns showing each user's age and school year.

This exercise demonstrates how Flask can retrieve data from an API and dynamically display it in a web page. In web applications, the server retrieves structured data (JSON) and converts it into human-readable HTML.

---

### Production note: using `flask run`

In production or more advanced setups, Flask applications are typically started using the Flask command-line interface:

    $ flask --app app run

The `flask run` command uses Flask’s built-in CLI to locate and start the application. This approach integrates better with environment variables and deployment tools, and is the standard method used in many production environments.

In this course, we use:
    
    $ python app.py

because it makes the application structure and execution flow easier to understand while learning.

### Data Visualization 

Next, we will add data visualization to our Flask app.
We will create:

- a pie chart showing the distribution of students by school year

- a bar chart showing the distribution of students by age

These visualizations will help us better understand the user data. Go to: `http://localhost:5000/charts`.

You should see a pie chart showing the distribution of students data by school year.

You will also see an empty bar chart area for the age distribution. This is because part of the code that prepares the age data has been intentionally disabled.

---

### Exercise #2: Fix the bar chart

Your task is to complete the missing code so that the bar chart correctly displays the number of students for each age.

1. Open the file `app.py`.

2. Locate the `/charts` route.

3. Inside the for loop near [Line 192], you will see a commented instruction. Add the line of code needed to count how many students have each age.

4. Save the file. 

5. Refresh the browser and see if the bar chart shows the distribution of students.

### Your first Flask app overview

- **Your Computer**
  - **Web Server** (running)
    - **Port 5000** (`http://localhost:5000`)
      - **Route `/`**
        - Code runs in `app.py`
        - Browser shows: **Hello World**
      - **Route `/users`**
        - Code runs in `app.py`
        - Browser shows: **Users Table**
      - **Route `/charts`**
        - Code runs in `app.py`
        - Browser shows: **Users Distribution Charts**

## Resources

* [Glue work and systems design](https://apenwarr.ca/log/?m=202012)
* [Building and operating a pretty big storage system](https://www.allthingsdistributed.com/2023/07/building-and-operating-a-pretty-big-storage-system.html)
* [Software Architects: Do We Need 'em](https://www.bredemeyer.com/who.htm) by Ruth Malan(by the way, this site has many other excellent articles on software architecture).
* [Explaining Software Design](https://explaining.software/)
* [5 essential patterns of software architecture](https://www.redhat.com/architect/5-essential-patterns-software-architecture)
* [List of software architecture styles and patterns](https://en.wikipedia.org/wiki/List_of_software_architecture_styles_and_patterns)
* [Design Patterns, Architectural Patterns](https://cs.nyu.edu/~jcf/classes/g22.2440-001_sp06/slides/session8/g22_2440_001_c82.pdf)
* [14 software architecture design patterns to know](https://www.redhat.com/architect/14-software-architecture-patterns)
* [Roy Fielding's Misappropriated REST Dissertation](https://twobithistory.org/2020/06/28/rest.html) is a great read showing how the term REST was appropriated for what we call REST today.
* [MDN Web Docs: HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
* [List of HTTP Status Codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
* [List of HTTP Methods](https://en.wikipedia.org/wiki/HTTP#Request_methods)
* Python Flask [minimal application](https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application)
* REST APIs [Richardson Maturity Model](https://martinfowler.com/articles/richardsonMaturityModel.html)

Jeff Bezos on [two types of decisions](https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm):

> Some decisions are consequential and irreversible or nearly irreversible –
> one-way doors – and these decisions must be made methodically, carefully,
> slowly, with great deliberation and consultation. If you walk through and
> don’t like what you see on the other side, you can’t get back to where you
> were before. We can call these Type 1 decisions. But most decisions aren’t
> like that – they are changeable, reversible – they’re two-way doors. If
> you’ve made a suboptimal Type 2 decision, you don’t have to live with the
> consequences for that long. You can reopen the door and go back through. Type
> 2 decisions can and should be made quickly by high judgment individuals or
> small groups.

