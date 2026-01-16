# CICF Week 6

The goals for the week 6 lab are to:

1. Look at data catalogues
1. Download data and plot it
1. Interact with an API to get data

## Tutorial

A data catalogue is a site that indexes papers and datasets, but dosen't store the actual data.
This means they are not repositories, but they do help us find data that is in repositories.
This is very FAIR, and is a use case anticipated by the 2016 FAIR paper, where they wrote about machine agents that look for data on their own, and at our behest.

### DataCite Commons

A data catalogue might seem simple, but it is non-trivial.
First, there are _many_ records, and there needs to be processes harvesting new and updated records from repositories and other data catalogues.

DataCite is one of the organizations that keep records for DOIs, so it is natural that they spend some effort to make a nice public search interface.

In the browser, go to the [DataCite Commons][] page.
You can see a search box.
Type in a search query, we will do "mosquito".
We get 37,570 works.
These are a combination of item types, years published, etc.
The facets on the left-hand side give an overview of the results.
Each record shows a title, list of authors, description, item type, item language, and a DOI.

Let's choose "2025" as a facet year.
We now see (at the time of this writing) 410 items.
The 6th item or so is "[Sampling Effort Data][]" by Mosquito Alert.
Clicking on the title takes us to the item page in Zenodo.

**Zenodo** is a general purpose repository.
And the interesting thing with this record is that it is an archived version of a GitHub repository.
[Mosquito Alert][] is a citizen science project to collect mosquito information from volunteers using a mobile app.
(They also have a [data portal][]).

Why would you want to archive a GitHub repository?
Git repositories are great collaboration tools.
But they have two drawbacks with respect to scholarship:
1) it is hard to cite a particular version of a Git repository, and 2) GitHub (or any other hosting site) is not archival storage.
For (1), while each version and commit in a git repository has a well-defined name—the commit hash—these names are not considered persistent identifiers since they do not fit into a global schema. In addition to the commit hash, you also need to know the repository name, and where to find the repository, and these things can change. Also, for a citation you need to provide information such as the release year, the creators, the license, and it is much easier to put everything into an archival repository and use that.
This is not to say Git is not useful; it is still extremely useful for the day-to-day running and collaboration on a project.

Download the data file (from the command line!).

    wget -i zenodo-links

It is a zip file, so let's look at it.

    $ unzip sampling_effort_data-v2025.02.25.zip
    $ cd Mosquito-Alert-sampling_effort_data-0b57d8f

There is a README file, A LICENSE file, and a CITATION file.
There is also a metadata file:

    $ nano sampling_effort_daily_cellres_05_metadata.json

This file is in JSON-LD (how do we know? There is a field named `@context`).
It describes the authors, and each variable in the file.

    $ gzip -d sampling_effort_daily_cellres_05.csv.gz

This is a huge file in CSV format, a very common format to receive data values in.
Each row is an individual data point, and each column names an attribute for that data point.

This file is quite big, and we need to use a tool to get some summary statistics.

    $ source ~/venv/bin/activate
    $ pip install pandas
    $ python3

OK, in the Python interactive environment let's load the CSV file.

```python
>>> import pandas as pd
>>> data = pd.read_csv("sampling_effort_daily_cellres_05.csv")

>>> data.head()
>>> data.tail()
>>> data.info()

>>> data['masked_lon'].max()
>>> data['masked_lon'].min()
```

Type Control-D to exit the interactive prompt.
We want to view a histogram, so start Jupyter and open the notebook `mosquito-alert.ipynb`.

    $ jupyter notebook


[DataCite Commons]: https://commons.datacite.org/
[Sampling Effort Data]: https://commons.datacite.org/doi.org/10.5281/zenodo.5802476
[Mosquito Alert]: https://www.mosquitoalert.com/
[data portal]: https://labs.mosquitoalert.com/metadata_public_portal/README.html



### NEON

Now, let's look at data provided by NEON (National Ecological Observatory Network).
They are an interesting Major Facility since in addition to recorded measurements,
they also have samples available for loan.

https://data.neonscience.org/data-products/explore

Search for "mosquito". Then select "Download data" from "Mosquitoes sampled from CO2 Traps".
There is a grid showing which months data is available from each site.
Choose two sites: ABBY and UNDE, and two years: 2023 and 2024.
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


