# CICF Week 8

The goals for this week's tutorial are:

1.  Learn to interact with cloud storage using the S3 API
2.  Perform a simplified distributed computation using the map-reduce paradigm

## Tutorial

Modern cloud computing often favors __managed services__ like GitHub Codespaces.
Managed services provide pre-configured, on-demand environments that allow us to focus on the application logic and data processing rather than the underlying infrastructure.
Most cloud providers also offer __object storage__, which is different from a traditional file system.
It is designed to store massive amounts of unstructured data (images, logs, data files) and is accessed via an API (usually the S3 API, named after the Amazon Web Services object storage service).
In this exercise, we will use **DigitalOcean Spaces**, which is S3-compatible.

We first need to install a few python libraries:

    $ pip install boto3 dotenv

### Setting up your Credentials

To interact with the cloud storage, you need credentials.
These should **NEVER** be committed to GitHub.

1.  Copy `week08-cloud-computing/.env-template` to `week08-cloud-computing/.env`.
2.  Add the DigitalOcean Spaces keys to this file. The key will be distributed in class.

We can see if it works by running the list items script in this directory.

    $ ./list-bucket.py

There are a lot of keys in this bucket.
While object stores do not have a notion of "directory" or "heirarchy", people simulate it by giving keys
prefixes that include slash characters, e.g. `/.
To make working with these kind of situations easier, APIs and libraries allow us to provide a prefix
to filter keys by.

    $ ./list-bucket.py group1/


### The Map-Reduce Paradigm

**Map-Reduce** is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster.
Its name comes from the two step involved:

 - Map Step: Filter and sort data.
 - Reduce Step: Consolidate the results from the map step.

The key constraint is that no communication is needed between nodes during the map step.
This makes is simple to parallelize the code: to process more items we just need to add more nodes to do the map step.

### Aggregating Metadata from OpenAlex

Take a look at [`openalex_map_reduce.py`](./openalex_map_reduce.py). This script:
2.  **Map Step**: From each raw JSON record, it extracts the publication year, citation count, and primary topic.
3.  **Reduce Step**: It aggregates these individual records to calculate:
    *   The total number of records.
    *   The average citation count.
    *   The most cited work in the dataset.
    *   The count of works published each year.
    *   The top 5 most frequent topics.

Run the script from your terminal:

	$ cd week08-cloud-computing
	$ ./openalex_map_reduce.py group1

The aggregated metadata is writen to the file `openalex_summary.json`.

In a "real" world scenario:
-   The **Map** step would happen on hundreds of different machines simultaneously.
-   The data would stay in the cloud (not downloaded to your local machine).
-   You would use tools like **Apache Spark** or **AWS Lambda** to orchestrate the work.

### Group Task

1. First, update the script to also extract the ORCID identifiers for any authors on each work.
2. Then alter the script to upload the resulting summary file back to the bucket. Ensure your group name is in the name of the file.
3. If you have time, can you visualize the results of your summary? Can you include the other group's summary files too?


### Monitoring & Costs

Even though we aren't managing VMs, when using cloud services we still need to monitor:
-   API Calls: Every time you list or download a file, it costs a tiny amount of money.
-   Storage: Storing large datasets incurs monthly costs.
-   Egress: Moving data *out* of a cloud provider is often the most expensive part! For example, moving the data from the DigitalOcean storage to the GitHub code space costs a little bit for each gigabyte transferred.

### Next steps: try things on your own

We have just scratched the surface of a large topic.
You should definitely explore things on your own.
Find learning material that works for you, in a format that works for you.

Here are some cloud provider's materials to start with:

- [Getting Started with Amazon Web Services](https://aws.amazon.com/getting-started/)
- [Google Cloud Learning Hub](https://cloud.google.com/learn)
- [Microsoft Azure documentation](https://learn.microsoft.com/en-us/azure/)
- [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/en-us/iaas/Content/home.htm)
- [DigitalOcean Documentation](https://docs.digitalocean.com/)

If you want to try out things on your own later, using free credits
offered by some cloud vendors would be a good place to start.

- Amazon Web Services offers a subset of their products under a [free tier][aws-free-tier].
- Google Cloud Platform also has [free tier][gcp-free-tier].
- Microsoft Azure too lets you try some of their cloud products [for free][azure-free-tier].
- Oracle Cloud has some [free offerings][oracle-free-tier].
- One of the perks of GitHub Student Developer Pack is $200 USD worth of [DigitalOcean credit][do-student-pack].

[aws-free-tier]: https://aws.amazon.com/free/
[gcp-free-tier]: https://cloud.google.com/free?hl=en
[azure-free-tier]: https://azure.microsoft.com/en-us/pricing/free-services
[oracle-free-tier]: https://www.oracle.com/cloud/free/
[do-student-pack]: https://www.digitalocean.com/github-students

## References

- [A General Introduction to Cloud Computing](https://www.digitalocean.com/community/tutorials/a-general-introduction-to-cloud-computing)
- [What is cloud computing?](https://aws.amazon.com/what-is-cloud-computing/)
- [MapReduce: Simplified Data Processing on Large Clusters](https://www.usenix.org/legacy/event/osdi04/tech/full_papers/dean/dean_html/),
the 2004 article by Jeffrey Dean and Sanjay Ghemawat introducing the map-reduce algorithm. (also [reprinted](https://dl.acm.org/doi/epdf/10.1145/1327452.1327492) in Communications of the ACM)
- [S3 Files and the changing face of S3](https://www.allthingsdistributed.com/2026/04/s3-files-and-the-changing-face-of-s3.html) is an interesting read on how filesystems and object stores are different and how AWS thought about it when they made a product that lets one view a pile of data either way. There are lots of technical tradeoffs.
