---
title: "CICF Week 8: Cloud Computing"
format:
  pptx:
    reference-doc: cicf-template.pptx
    fig-width: 300
  revealjs:
    slide-number: true
    theme: default
---

# Welcome to week eight of CICF!

## The plan this week

We will look at:

- Cloud computing
  - service models
  - deployment models
  - components
  - infrastructure as code

# The Basics

::: {.notes}

Set the stage: "Let’s start with the basics—what *is* the cloud, and
why does it matter?"

:::

---

## What is Cloud Computing?

- **Definition**: On-demand delivery of compute, storage, and
  networking over the internet, managed by a provider.

- **Key Traits**:
  - On-demand access
  - Scalability
  - Pay-as-you-go pricing

::: {.notes}

People joke that the cloud is somebody else's computer.  That
observation simplifies things a little, but it is not too far off.

We can think of cloud computing like renting computers, and other
computing infrastructure like storage and networking, that you do not
own. You use it when you need it, scale it up or down, and only pay
for what you use.

You will create resources when you need it. These resources will be
usually available within seconds.  This is a big step from having to
build and maintain these things by yourself.

You will also pay for only what you use.

:::

---

## Why Cloud?

- **Benefits**:
  - Cost efficiency
  - Flexibility
  - Global reach
- **Examples**:
  - Netflix (AWS)
  - Google Drive (Google Cloud)

::: {.notes}

The benefits of cloud computing is that you get cost efficiency and
flexibility and global reach.  It costs money and time to build and
run computing resources. You will also have to hire experts to build
and run these resources.

The big cloud computing providers have economies of scale. They are
very good at what they do.

Depending on what you need to do, it might be more effective to pay
for cloud computing.

An example is Netflix.  They stream their huge catalog of shows to
millions of people without owning or operating servers of their own.
They use AWS.

:::

---

## Evolution

- Physical servers → Virtualization → Cloud

::: {.notes}

In the past people used to have bulky server rooms.  Or people used to
rent rack space in data centers.  Or own their own data centers.

Then we figured out how to use virtual machines.

Then things moved to the cloud.

Each of those steps made computing faster, and, in many cases,
cheaper.

The pioneer in cloud computing is Amazon Web Services.  They built
extra server capacity to handle holiday shopping load on their
servers, but the rest of the time their servers were sitting idle.  
They figured that they can rent idle servers to other people and make
money from it.

Today I believe AWS is a more profitable business that Amazon.com.

:::

---

# Service Models

::: {.notes}

Now, let’s look at how the cloud serves us.  There are three big
models to know.

:::

---

## IaaS (Infrastructure as a Service)

- **Description**: Raw infrastructure (VMs, storage, networks)
- **Example**: AWS EC2, Google Cloud Platform, Microsoft Azure
- **Use Case**: Build your own server setup

::: {.notes}

IaaS is like renting a bare apartment.  You furnish it yourself.  This
is great people who want more control over how they do things.

:::

---

## PaaS (Platform as a Service)

- **Description**: Managed platforms for app development
- **Example**: Google App Engine, Heroku
- **Use Case**: Deploy a web app without server management

::: {.notes}

PaaS is like a furnished apartment.  You move in and start coding. You
do not want to deal with the hassle of setting up servers.

You will simply use a software development kit to write your
application against the service providers platform.  They will set up
the servers and set up the software pieces to run your application and
scale things up when necessary.

:::

---

## SaaS (Software as a Service)

- **Description**: Fully managed software
- **Example**: Google Docs, Microsoft 365
- **Use Case**: End-user applications

::: {.notes}

SaaS is like a hotel.  Everything’s ready.

:::

---

# Deployment Models

::: {.notes}

Next, where does the cloud live? 

There are three ways to deploy "the cloud".

:::

---

## Public Cloud

- **Description**: Shared resources from a provider
- **Example**: AWS, Google Cloud Platform, Microsoft Azure
- **Pros**: Cost-effective, scalable

::: {.notes}

Public cloud is like a shared co-working space.  They are relatively
inexpensive and flexible, but you share the space with others.

:::

---

## Private Cloud

- **Description**: Dedicated resources for one organization
- **Example**: On-premise or hosted (e.g., VMware, OpenStack)
- **Pros**: Control, security

::: {.notes}

Private cloud is like owning your office.  You get more control.  You
also pay more up-front for setting up things, and you pay recurring
expenses like utility bills.  

If you use something like VMWare, you will pay recurring license fees.

:::

---

## Hybrid and Multi-Cloud

- **Hybrid**: Public + private mix
  - e.g., Sensitive data on-premise, rest on AWS
- **Multi-Cloud**: Multiple providers
  - e.g., AWS + Google Cloud

::: {.notes}

Hybrid clouds are like a mix of home and office.  You rent some
infrastructure from a cloud provider.  You run some infrastructure on
your own.

Multi-cloud is mixing AWS and Google for the best of both.  Some
things might be cheaper or faster at one place.  Or you want
redundancy so that when one thing goes down the other will continue to
work.

:::

---

## Major cloud vendors

- Amazon Web Services (AWS)
- Microsoft Azure
- Google Cloud Platform (GCP)
- IBM Cloud
- Oracle Cloud Infrastructure (OCI)
- Alibaba Cloud
- DigitalOcean
- Hetzner Cloud

---

# Core Components

::: {.notes}

Now let us break down the cloud’s building blocks. They are: compute,
storage, networking.

We should note that most cloud providers offer a huge array of
offerings.  Compute, storage, and networking are the essentials.

:::

---

## Compute

- **Virtual Machines**: Rentable servers (e.g., AWS EC2)
- **Containers**: Lightweight units (e.g., AWS ECS or Elastic
  Container Service, EKS or Elastic Kubernetes Service)
- **Serverless**: Run code without servers (e.g., AWS Lambda)

::: {.notes}

Compute is the brain.  

Virtual machines are full servers that you set up and manage.

Sometimes you don't want to run virtual machines. You just want to run
some application in a container.  Amazon's Elastic Container Service
is a fully managed container orchestration services that supports
Docker containers.

Other providers also offer similar services, such as Azure Container
Instance, Google Kubernetes Engine, etc.

"Serverless" is a cloud computing model where you run code or
applications without managing the underlying servers.  You write your
code (or a "function"), upload it to the cloud, and the provider
automatically handles everything else - servers, scaling, and
maintenance. 

You only pay for the compute time your code actually uses, typically
measured in milliseconds, instead of paying for always-on
servers.

It is like renting a car only for the exact moments you drive, rather
than owning and maintaining one full-time.

AWS Lambda, for example, triggers your code in response to events
(like an HTTP request or a file upload) and scales instantly to handle
demand.  It is ideal for small, event-driven tasks or microservices.

:::

---

## Storage

- **Object Storage**: Files as objects (e.g., AWS S3)
- **Block Storage**: Hard drives for VMs (e.g., AWS EBS)
- **File Storage**: Shared systems (e.g., AWS EFS)

::: {.notes}

Storage is obviously the place where you store your stuff.

Three main kinds of storage systems are available in cloud
environments:

- Object storage is a storage system that manages data as discrete
  units called "objects." Each object includes the data itself,
  metadata, and a unique identifier (like a URL or key).
  
  They provide a flat structure: there is no hierarchical folder
  structure.  They are accessed via APIs rather than via traditional
  file systems.
  
  The prime example is Amazon S3, or Simple Storge Service.  Others:
  Google Cloud Storage, Azure Blob Storage.

- Block storage is storage that operates at a low level. It provides
  raw storage volumes that can be mounted to servers or virtual
  machines. And then you treat it like a traditional file system.
  
  Examples are: AWS Elastic Block Store (EBS), Azure Disk Storage,
  Google Persistent Disk.

- File storage organizes data into a hierarchical structure of files
  and directories.  It is accessed protocols like NFS (Network File
  System), SMB (Server Message Block), or CIFS.  They are not local to
  a VM -- multiple VMs can access them over a network.
  
Each of these storage types have their strengths and weaknesses.  You
will choose one over the other depending on what you need to do.

Object storage is good for storing backups, archives, or large media
files (images, videos).

Block storage is good for databases requiring fast, consistent I/O.

File storage is good for shared file systems for teams that need to
share documents and media.

:::

---

## Networking

- **DNS**: Domain to IP resolution (e.g., Route 53)
- **Load Balancers**: Traffic distribution (e.g., AWS ELB)
- **Virtual Networks**: Isolated setups (e.g., AWS VPC)
- **Security and Access Control**: Tools and policies to secure
  network traffic and restrict access (e.g., firewalls, access control
  lists, VPN, TLS)
- **Network Monitoring and Analytics**

::: {.notes}

Networking ties it together.  

DNS finds your site.

Load balancers share the load between various services or servers.

You probably do not want to route all communication between your
servers over the public internet.  You want an exclusive private route
between them.  So you would use something like AWS VPC (Virtual
Private Cloud).

:::

---

# Infrastructure as Code (IaC)

::: {.notes}

You can always create and manage your cloud resources using your cloud
providers console.  This is basically a web application that will
allow you to do things with links and buttons and menus.

But that will get tedious when you have a lot of resources.  And you
will forget how you did things.  You will often need to remember how
you set up things.

A better way to manage your cloud infrastructure is using code.  There
are special tools that help you manage cloud infrastructure using
code.

:::

---

## What is IaC?

- **Definition**: Manage infrastructure with code
- **Benefits**:
  - Consistency
  - Repeatability
  - Version control

::: {.notes}

IaC is like a recipe.  You write code to define your infrastructure in
a declarative manner.  You will not use manual clicks.  Doing things
this way is faster and more efficient.

With code, you can consistently re-create your infrastructure when you
need to, or extend things when you need to: add more VMs or storage or
networking, and you can assign them roles.  You will have greater
control over things.

With IaC, you can also document your setup better for future
reference.  You can also check your code in Git repositories.

:::

---

## Tools

- **Terraform**/**OpenTofu**: Multi-cloud IaC

  ```hcl
  terraform {
    required_providers {
      aws = {
        source  = "hashicorp/aws"
        version = "~> 4.16"
      }
    }

    required_version = ">= 1.2.0"
  }

  provider "aws" {
    region  = "us-west-2"
  }

  resource "aws_instance" "app_server" {
    ami           = "ami-830c94e3"
    instance_type = "t2.micro"

    tags = {
      Name = "example"
    }
}
  ```

## Other tools

- Ansible
- Chef
- Puppet
- Pulumi
- AWS CloudFormation
- Azure Resource Manager (ARM) Templates
- Google Cloud Deployment Manager


# FIN
