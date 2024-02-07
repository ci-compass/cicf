# CICF Week 2

## Tutorial

### Machine Learning and AI: new-ish challenges in Scientific Computing

Scientific computing has two main areas these days: simulation, and "pattern finding".
Simulation is the traditional role: forcasting future situations (e.g. weather, structural engeerning, agent based modeling), creating models that can make good predictions, and running what-if scenerios.
The new role is as pattern finding, which comes from machine learning and AI.
For this we want to take a very, very, very large amount of data and find patterns in it by using approximation and statistical algorithms.
The goal is to conduct non-traditional analysis of scientific data to make _unexpected discoveries_.

Why does cyberinfrastructure care about this?
The ML/AI techniques need:
* huge amounts of data
* Fairly simple computation with extremely fast access to the data. (huge RAM, huge parallelism, all tightly connected)
* Problems often either *are* or *closely resemble* linear algebra

This means that scientific computing is appropriating hardware that have been developed over the past 30 years for graphics.
Computer graphics involve translating objects in a 3D coordinate system and mapping to 2D to render to the screen.
Graphics Processing Units are hardware processors developed to do these kind calculations very quickly.
And they are now finding a second use training AI models.
The tactic is to make the AI problem look like linear algebra, then do computation on a GPU.

An area of research currently is that while GPUs help with speeding up linear algebra problems, they don't speed the IO or other non-linear processing of the data.


### High Performance Networking:

Moving a terabyte or more of data is **hard**.
Most networks run the Internet Protocol (IP), usually as (TCP/IP), to coordinate sharing data between computers.
This protocol was originally designed in early 1980s and data throughput was not a design goal.
It relies on low latency between nodes and requires, among other things, a round trip message confirmation every 8 to 100k bytes.
This puts speed limits on the transfer rate based on the speed of light.
For example, going from North Carloina to San Francisco, there is a 100-150 millisecond round trip time, which gives an approximately 1 MBit/sec transfer rate.

[TCP performance](https://www.potaroo.net/ispcolumn/2000-09-latency.html)

Some ways to speed up data transfers:
* Put data on a disk drive and ship! high latency, but high throuput. e.g. Amazon snowball and [snowmobile](https://aws.amazon.com/snowmobile/)
* Use non-TCP and non-IP protocols
    * [Internet2](https://internet2.edu/), [ESnet (DOE)](https://www.es.net/)
    * [NSF FABRIC Testbed](https://fabric-testbed.net/)
    * Industry (e.g. [Facebook](https://engineering.fb.com/category/networking-traffic/)/Apple/Amazon/Netflix/ Google) are using custom high speed networking protocols

### Survey CI landscape at a Major Facility

This is an in class activity. Break into small groups and have 5 minutes to research the network and computing infrastructure deployed at a major facility.

## Resources

- News article on design of new HPC system at TACC: [With Vista, TACC now has three paths to its future horizon superomputer](https://www.nextplatform.com/2024/01/29/with-vista-tacc-now-has-three-paths-to-its-future-horizon-supercomputer/)

