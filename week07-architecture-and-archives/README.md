# CICF Week 7

The goals for this week are to

1. Use Swagger UI to explore API endpoints (GET, POST, PATCH, DELETE)
2. Build a simple Flask web application to interact with a live web API using HTTP
3. Understand the basics of software architecture and design patterns in the context of web services


## Tutorial

This week we will look at web services.

<!-- keep orcid in week 7? -->

Start by looking at the human version of a web page.
Open your VM, and then open the web browser and visit

    https://orcid.org/0000-0002-1825-0097

This is (should be?) the only fictional person with an ORCID record.
The page displays his name and some information about him.

Let's look at this under the hood.
Make a new browser tab and go to this website:

    https://base64.guru/tools/http-request-online

We will first look at HTTP requests with this and then from the command line.
Enter the previous ORCID URL into the URL box.
Choose HTTP request version 1.1.

We see the request sent.
It has the HTTP method, `GET`, and a few headers.
These headers are standard boilerplate.

Then below we see the response headers.
The first line has the response code, in this case "200 OK".
We have some more headers describing the data:
it is `text/html`.
There are some other headers, some are important to the client, and some are for debugging.

Below the response headers is the response body, and we have some HTML encoded text which is the displayed webpage.
So this shows the distinction between HTTP—the transport protocol—and HTML—the text that forms the "web page".

We can add other headers to our request.
Of course, if the server doesn't understand a header it can ignore it or return an error, its choice.

I would then look at this using the JSON response ORCID can provide, but
the website now requires a sign-in before providing this.
So, let's look at OpenAlex.

## Open Alex

<!-- move to week 6-->

Surprisingly, there is no complete database of all academic scholarship.
There are a few aggregators that try to index as much as they can.
One is [Google Scholar](https://scholar.google.com/), others are [DataCite Commons](https://commons.datacite.org),
and [OpenAlex](https://openalex.org).
There are also more specialized databases, such as [PubMed](https://pubmed.ncbi.nlm.nih.gov/) for medical research.

OpenAlex is a catalog of open science papers, people, datasets, institutions, and so on.
In the browser visit the page:

    https://openalex.org/works/w2764299839

This, again, is a human readable page provided by the catalog.
Let's try asking for a JSON representation.
Add the header `Accepts: application/json` by typing that into the box labeled "HTTP Request Headers".
This is asking the server that we don't want an HTML page, instead we want a JSON encoded response.
In this case, we get a page that wants us to use javascript.
This seems to be a newer technique to prevent bots from scraping data off a page.
But the information is all available at the API endpoint:

    https://api.openalex.org/works/W2764299839

Now we get an interesting response.
The first line has a 302 response code.
This is the server telling us that we need to retry at a different URL.
The `Location:` header is telling us the new URL to use.
Why? It seems to want us to use a capital "W".
The second request returns a JSON response body.
It is all on one line.
Sometimes servers do this, since the line breaks are not needed to decode the JSON.

Thinking of this architecture, why do you think the servers used a redirect rather than just returning the JSON in the first place?


### Looking at the JSON

<!-- move to week 5? -->

Copy the JSON response and paste it into this web page:

    https://jqplay.org/

Paste it into the box labeled "JSON".
In the box labeled "filter" enter `.`, a single period.

You will see a formatted version of the JSON appear in the box on the right.
JSON is a simple way of structuring data to send between computers.
Since it is text-based, it is easy for people to inspect it.
However there is no support for comments, so it is not ideal for ongoing things that a human might be editing, such as configuration files.

There are 6 kinds of values in JSON:
* numbers
* strings
* true/false
* null
* objects
* arrays

Most JSON responses are an object, which is indicated by a matching pair of curly braces, `{}`.
Inside the curly braces of an object there are a list of
key-value pairs separated by commas.

All of the information in HTML record should also appear in the JSON record.

Try entering `.title` in the Filter box.
You should see the following JSON:

```json
"Citizen science provides a reliable and scalable tool to track disease-carrying mosquitoes"
```

Now try `.mesh`.
You should see a big list.
Now do `.mesh[3]`:

```json
{
  "descriptor_ui": "D009032",
  "descriptor_name": "Mosquito Control",
  "qualifier_ui": "Q000379",
  "qualifier_name": "methods",
  "is_major_topic": true
}
```

The filter box takes a pattern and returns the pieces of the input that match.

MeSH are subject headings curated by the National Library of Medicine.
Let's look up this term:

    https://www.ncbi.nlm.nih.gov/mesh/

Search for `D009032`.
This let's us share topic headings with others and we can all agree on what they mean.
We can also agree on the codes used to represent each topic.

Vocabularies like MeSH are very useful, but each takes effort to develop and there all have a defined scope.
Another useful place to define shared terms is WikiData.

    https://www.wikidata.org

And we can also find the Wikidata term for MeSH:

    https://www.wikidata.org/wiki/Q2003646


## Again on the command line

Now let's do all this on the command line.

    curl -H 'Accepts: application/json' 'https://api.openalex.org/works/w2764299839'

This just returns the redirect.
We need to ask "curl" to follow the redirects:

    curl -L -H 'Accepts: application/json' 'https://api.openalex.org/works/w2764299839'

We can see more information being passed with the `-v` "verbose" option.

    curl -v -H 'Accepts: application/json' 'https://api.openalex.org/works/w2764299839' 2>&1 | less

Note that the request is on lines starting with a ">"
and the response headers are on lines starting with "<".

Let's save the json response:

    curl -L -H 'Accepts: application/json' 'https://api.openalex.org/works/w2764299839' > mosq.json

The `jq` tool can work on the command line as well.

    jq .mesh[3] mosq.json


## Data, Archives, and APIs

In this module, we treat the API as a simple gateway to an archive:

- Data is stored in structured form (JSON)
- The API defines how data can be accessed
- Clients do not access data files directly

This separation is common in real systems where archives must be
stable, reusable, and accessible by many tools.

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

In the `POST /users endpoint`, click "Try it out", input your basic informtion per the JSON requires 
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

Then in the `GET /users` endpoint, click "Try it out" and then click "Execute". You will see the request and response details again. Code `200` means the request was successful. The response body contains the information of all users, including the user you just created.

### Essential Concepts 

#### Common HTTP Methods

| Method | What it does | Example use in this week |
|------|-------------|--------------------------|
| GET  | Retrieve data from a server | Get a list of users |
| POST | Send new data to a server | Add a new user |
| PUT  | Update existing data | Update user info |
| DELETE | Remove data | Delete a user |

#### Common HTTP Status Codes

| Code range | Meaning | Example |
|-----------|--------|---------|
| 2xx | Success | 200 OK, 201 Created |
| 3xx | Redirection | 301 Moved Permanently |
| 4xx | Client error | 400 Bad Request, 404 Not Found |
| 5xx | Server error | 500 Internal Server Error |

## Build a simple Flask app

Flask is a very simple python framework for making web applications.
Here is a Flask app showing how a web server works.
Let's set up the virtual envrionment and run Flask.

    $ source ~/venv/bin/activate
    $ pip install flask requests
    $ flask --app app run

You will see some text, including that the server is running on localhost "http://127.0.0.1:5000".
127.0.0.1 refers to the current computer. The 5000 says the server is listening on port 5000 on the current computer.
Open a web browser and type in the URL `localhost:5000`. You will see a page showing "Hello World." 
This is because in the file `app.py` we match that route `/` and say to return that text.
Enter `localhost:5000/users` in the browser, you will see a page with the table of all users we just created in the Swagger UI.

- **Your Computer**
  - **Web Server** (running)
    - **Port 5000** (`http://localhost:5000`)
      - **Route `/`**
        - Code runs in `app.py`
        - Browser shows: **Hello World**
      - **Route `/users`**
        - Code runs in `app.py`
        - Browser shows: **Users table**


### Data Visualization 

Next, we will add data visualization to our Flask app.
We will create:

- a pie chart showing the distribution of students by school year

- a bar chart showing the distribution of students by age

These visualizations will help us better understand the user data.

<!-- Yaxue TODO: Confirm tutorial scope and timing with Don -->

## Resources

<!-- Yaxue TODO: Update Resources list based on tutorial scope -->

* [Glue work and systems design](https://apenwarr.ca/log/?m=202012)
* [Building and operating a pretty big storage system](https://www.allthingsdistributed.com/2023/07/building-and-operating-a-pretty-big-storage-system.html)

Software Architecture
* [Software Architects: Do We Need 'em](https://www.bredemeyer.com/who.htm) by Ruth Malan(by the way, this site has many other excellent articles on software architecture).
* [Explaining Software Design](https://explaining.software/)
* [5 essential patterns of software architecture](https://www.redhat.com/architect/5-essential-patterns-software-architecture)
* [List of software architecture styles and patterns](https://en.wikipedia.org/wiki/List_of_software_architecture_styles_and_patterns)
* [Design Patterns, Architectural Patterns](https://cs.nyu.edu/~jcf/classes/g22.2440-001_sp06/slides/session8/g22_2440_001_c82.pdf)
* [14 software architecture design patterns to know](https://www.redhat.com/architect/14-software-architecture-patterns)
* [Roy Fielding's Misappropriated REST Dissertation](https://twobithistory.org/2020/06/28/rest.html) is a great read showing how the term REST was appropriated for what we call REST today.

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

* [List of HTTP Status Codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
* [List of HTTP Methods](https://en.wikipedia.org/wiki/HTTP#Request_methods)
* JSON [RFC 4627: The application/json Media Type for JavaScript Object Notation (JSON)](https://www.ietf.org/rfc/rfc4627.txt)
* ORCID [API v3.0 Guide](https://github.com/ORCID/orcid-model/blob/master/src/main/resources/record_3.0/README.md)
* Python Flask [minimal application](https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application)

