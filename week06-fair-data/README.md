# CICF Week 6

The goals for the week 6 lab are to:

1. Look at data catalogues
1. Download data and plot it
1. Interact with an API to get data

## Tutorial

A data catalogue is a site that provides a way to search for papers and datasets, but dosen't store the actual data.
This means they are not repositories, but they do help us find data that is in repositories.
This helps with the findable part of FAIR and is a use case anticipated by the 2016 FAIR paper,
where machine agents that look for data both on their own, and at our behest was envisioned.

## ORCID

Lets start by looking at an ORCID record.
Visit the ORCID record [0000-0002-1825-0097](https://orcid.org/0000-0002-1825-0097).
This is (or should be) the only fictional person with an ORCID record.
The page displays his name and some information about him.
It is the page for humans.


<!-- TODO: needs revision for ORCID API

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

-->

## Open Alex

Surprisingly, there is no complete database of all academic scholarship.
There are a few aggregators that try to index as much as they can.
Some of these are [Google Scholar](https://scholar.google.com/),
[DataCite Commons](https://commons.datacite.org),
and [OpenAlex](https://openalex.org).
There are also more specialized databases, such as [PubMed](https://pubmed.ncbi.nlm.nih.gov/) for biomedical research.

OpenAlex is a catalog of open science papers, people, datasets, institutions, and so on.
In the browser visit [the following page](https://openalex.org/works/w2764299839):

    https://openalex.org/works/w2764299839

This is the human readable page provided by the catalog.
Let's try asking for a JSON representation by using the HTTP header `Accepts: application/json`.
In this case, we get a page that wants us to use javascript.
This seems to be a newer technique to prevent bots from scraping data off a page.
But the information is all available at the API endpoint by using `api.openalex.org`:

    curl -H 'Accepts: application/json' https://api.openalex.org/works/W2764299839 > alex.json

The JSON returned is considered "human readable" since it is not encoded as a binary stream.
However, it is quite hard to actually understand it.
We can reformat it to make it nicer:

    $ jq . alex.json | less


### Looking at JSON (aside)

JSON is a simple way of structuring data to send between computers.
Since it is text-based, it is easy for people to inspect it.
However there is no support for comments, so it is not ideal for ongoing things that a human might be editing, such as configuration files.
There are also online tools to work with JSON data.
Copy the JSON response and paste it into the box labeled "JSON" on the [JQ playground](https://jqplay.org) web page.
In the box labeled "Query" enter a single period, `.`.
A formatted version of the JSON will appear in the right-hand box.

There are 6 kinds of values in JSON:
* numbers
* strings
* true/false
* null
* objects
* arrays

Most JSON is packaged up as an object, which is indicated by a matching pair of curly braces, `{}`.
Inside the curly braces of an object there are a list of
key-value pairs separated by commas.

The Query box takes a pattern and returns the pieces of the input that match.
Try entering `.title` in the Query box.
You should see the following JSON:

```json
"Citizen science provides a reliable and scalable tool to track disease-carrying mosquitoes"
```

Now try `.mesh`.
You should see a big list.
Now do `.mesh[3]`:

```json
{
  "descriptor_ui": "D000071244",
  "descriptor_name": "Zika Virus",
  "qualifier_ui": "Q000502",
  "qualifier_name": "physiology",
  "is_major_topic": false
}

```

The `jq` tool can work on the command line as well.

    jq .mesh[3] alex.json

MeSH are subject headings maintained by the National Library of Medicine.
We can look up this term. Go to the [MeSH home page](https://www.ncbi.nlm.nih.gov/mesh/).
Search for `D000071244`.
You will see the entry for "Zika Virus".

Vocabularies like MeSH are very useful, but they take effort to develop and maintain.
Another useful place to define shared terms is [WikiData](https://www.wikidata.org).
The same term for Zika virus is in WikiData with identifier [Q202864](https://www.wikidata.org/wiki/Q202864),
and in the NCBI taxon database as [54320](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=64320)

Why does the same thing show up in so many databases?
Because each database is for a different purporse, so each shows a different aspect of the thing.
MeSH is used for organizing papers at the NLM.
Wikidata is a general purporse database that mostly cross-references all these other entries.
The NCBI Taxon database is trying to be a complete catalog of species of living things (plus virus, etc).


### NEON

NEON (National Ecological Observatory Network) is an NSF Major Facility that
collects and provides long-term logtududional ecological data.
They are an interesting Major Facility since in addition to recorded measurements,
they also have physical samples available for loan.

We will start at their [data portal](https://data.neonscience.org/data-products/explore)

Search for "mosquito". Then select the item "[Mosquitoes sampled from CO2 Traps](https://data.neonscience.org/data-products/DP1.10043.001/RELEASE-2026)".
Near the bottom of the item page there is a grid showing which months data is available from each site.
Choose the buttom "Download Data".

For the two sites WI-D16-ABBY and MI-D05-UNDE choose the data for the years 2024 and 2025.
And then download the data.

The data is organized as many files.
For the mosquito counts, there is one CSV file per site location per month.
Each file includes a line for every mosquito collected.
We want to count mosquitoes by month and by site.



## Resources

* [RDF Standard](https://www.w3.org/RDF/)
* [Cool things to do with RDF](https://medium.com/@dallemang/jug-o-cool-things-i-do-with-rdf-3cdb5b059192)
* [JSON](https://www.json.org/json-en.html) and the formal [ECMA-404](https://ecma-international.org/publications-and-standards/standards/ecma-404/), [ISO 21778:2017](https://www.iso.org/standard/71616.html), [RFC 8259](https://datatracker.ietf.org/doc/html/rfc8259)
* [JSON-LD](https://json-ld.org/)
* [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page)
* [OpenAlex](https://openalex.org/)
* [ORCID](https://orcid.org/)
* [ROR](https://ror.org/)
* [Datacite Commons](http://commons.datacite.org)
* [Science on schema.org](https://github.com/ESIPFed/science-on-schema.org)
* [Schema.org](https://schema.org/)

**Pandas Tutorials and Stuff**

- [https://www.w3schools.com/python/pandas/default.asp][]
- the [Official Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [Pandas cookbook](https://github.com/jvns/pandas-cookbook) (created by the great Julia Evans, and community maintained since)


