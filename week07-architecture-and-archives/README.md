# CICF Week 7

The goals for this week are to

1. Call a web service from the command line
1. Be able to specify HTTP headers with `curl` requests
1. Be able to manipulate JSON files


## Tutorial

This week we will look at web services.

Start by looking at the human version of a web page.
Open your VM, and then open the web browser and visit

    https://orcid.org/0000-0002-1825-0097

This is (should be?) the only fictional person with an ORCID record.
Notice how we see his name, and some information about him.

Lets look at this under the hood.
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
There are some other headers, some are important to the client, and some are more just for debugging.

Below the response headers is the response body, and we have some HTML encoded text which is the displayed webpage.
So this shows the distinction between HTTP—the transport protocol—and HTML—the text that forms the "web page".

We can add other headers to our request.
Of course, if the server doesn't understand a header it can ignore it or return an error, its choice.

Lets add the header `Accepts: application/json`.
Type that into the box labeled "HTTP Request Headers"
This is asking the server that we don't want an HTML page, instead we want a JSON encoded response.

Now we get an interesting response.
The first line has a 302 response code.
This is the server telling us that we need to retry at a different URL.
The `Location:` header is telling us the new URL to use.

So then we retry and we get another redirect.
Do you see what is going on?

Finally on the third try we get what we are looking for.
And the response body is full of JSON.

Thinking of this architecture, why do you think the servers used a redirect rather than just returning the JSON in the first place?

### Looking at the JSON

We have mentioned JSON but I don't think we have really looked at it in much depth.
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
Albeit, it is easier for machines to find information in the JSON record.

Try entering `.person.name` in the Filter box.
You should see the following JSON:

```json
{
  "created-date": {
    "value": 1460757617078
  },
  "last-modified-date": {
    "value": 1504850007188
  },
  "given-names": {
    "value": "Josiah"
  },
  "family-name": {
    "value": "Carberry"
  },
  "credit-name": null,
  "source": null,
  "visibility": "public",
  "path": "0000-0002-1825-0097"
}
```

The filter box takes a pattern and returns the pieces of the input that match.
In this case it is starting at the top, looking for the key `person`, and then looking for the key `name`, and returning whatever it found.
The model of the name is probably more complicated than you expected.
We have metadata on when it was created and updated, the name itself is split into given and family names.
There is a credit and source fields, and a visibility level.

The dates probably don't look like any date you've seen before.
Any ideas what is going on?

Sometimes web services use a string like "20240319T20:14:36.245Z" to represent times.
Sometimes they use something called UNIX epoch time, which is the number of seconds since
January 1, 1970.
It is up to the service to decide how to handle time.
In this case we can decode the time.
There are a few ways of doing it.
Easiest is to use a website reference:

    https://www.unixtimestamp.com/

Another way is to use the command line:

    (in linux): date --date='@1460757617078'
    (on macos): date -r 1460757617078

This actually gives a wildly wrong number, since the server is actually using _milliseconds_ since the UNIX epoch.
Lets adjust by removing the last three digits (i.e. dividing by 1000):

    (in linux): date --date='@1460757617'
    (on macos): date -r 1460757617

(The difference in commands comes from MacOS actually descending via a BSD Unix. Architecture choices made 30 and 40 years ago are still showing up.)


Lets now look at this briefly on the command line:

    curl -s -v "https://orcid.org/0000-0002-1825-0097" 2>&1 | less

This displays the original webpage.
Note that the request is on lines starting with a ">"
and the response headers are on lines starting with "<".

    curl -s -v -L -H "Accept: application/json" "https://orcid.org/0000-0002-1825-0097" 2>&1 | less

We can change the accept header:

    curl -s -v -L -H "Accept: application/xml" "https://orcid.org/0000-0002-1825-0097" 2>&1 | less

We can change the method:

    curl -s -v -L -X "POST" -H "Accept: application/xml" "https://orcid.org/0000-0002-1825-0097" 2>&1 | less

In this case we get a response with status code 405, indicating an error.



## Resources

* [Glue work and systems design](https://apenwarr.ca/log/?m=202012)
* [Building and operating a pretty big storage system](https://www.allthingsdistributed.com/2023/07/building-and-operating-a-pretty-big-storage-system.html)

Software Architecture
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

