---
title: "CICF Week 8: Cloud Computing"
format:
  # pptx:
  #   reference-doc: cicf-template.pptx
  #   fig-width: 300
  revealjs:
    slide-number: true
    theme: default
    transition: slide
---

# Welcome to week eight of CICF!

## The plan this week

# Cloud Computing

::: {.notes}

Set the stage: "Let’s start with the basics—what *is* the cloud, and
why does it matter?"

:::

---

## What is Cloud Computing?

- **Definition**: On-demand delivery of compute, storage, and networking over the internet, managed by a provider.

- **Key Traits**:
  - On-demand access
  - Scalability
  - Pay-as-you-go pricing

::: {.notes}

Explain simply: "Think of it like renting a computer you don’t own—use
it when you need it, scale it up or down, and only pay for what you
use."

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

Make it relatable: "Netflix streams to millions without owning
servers—cloud makes that possible. What’s a cloud service you use
daily?"

:::

---

## Evolution

- Physical servers → Virtualization → Cloud

::: {.notes}

Quick history: "We went from bulky server rooms to virtual machines,
then to the cloud—each step made IT faster and cheaper."

:::

---

# Service Models

::: {.notes}

Transition: "Now, let’s look at how the cloud serves us—three big
models to know."

:::

---

## IaaS (Infrastructure as a Service)

- **Description**: Raw infrastructure (VMs, storage, networks)
- **Example**: AWS EC2, Google Compute Engine
- **Use Case**: Build your own server setup

::: {.notes}

Analogy: "IaaS is like renting a bare apartment—you furnish it
yourself. Great for control freaks!"

:::

---

## PaaS (Platform as a Service)

- **Description**: Managed platforms for app development
- **Example**: Google App Engine, Heroku
- **Use Case**: Deploy a web app without server management

::: {.notes}

Contrast: "PaaS is the furnished apartment—move in and start coding,
no server hassles."

:::

---

## SaaS (Software as a Service)

- **Description**: Fully managed software
- **Example**: Microsoft 365, Dropbox
- **Use Case**: End-user applications

::: {.notes}

Engage: "SaaS is like a hotel—everything’s ready. Who’s used Google
Docs? That’s SaaS!"

:::

---

# Deployment Models

::: {.notes}

Shift gears: "Next, where does the cloud live? Three ways to deploy
it."

:::

---

## Public Cloud

- **Description**: Shared resources from a provider
- **Example**: AWS, Microsoft Azure
- **Pros**: Cost-effective, scalable

::: {.notes}

Keep it light: "Public cloud is like a shared coworking space—cheap
and flexible, but you’re with others."

:::

---

## Private Cloud

- **Description**: Dedicated resources for one organization
- **Example**: On-premise or hosted (e.g., VMware)
- **Pros**: Control, security

::: {.notes}

Contrast: "Private cloud is your own office—more control, but you pay
for it."

:::

---

## Hybrid and Multi-Cloud

- **Hybrid**: Public + private mix
  - e.g., Sensitive data on-premise, rest on AWS
- **Multi-Cloud**: Multiple providers
  - e.g., AWS + Google Cloud

::: {.notes}

Real-world: "Hybrid is like home + office; multi-cloud is mixing AWS
and Google for the best of both."

:::

---

# Core Components

::: {.notes}

Dive in: "Let’s break down the cloud’s building blocks—compute,
storage, networking."

:::

---

## Compute

- **Virtual Machines**: Rentable servers (e.g., AWS EC2)
- **Containers**: Lightweight units (e.g., Docker)
- **Serverless**: Run code without servers (e.g., AWS Lambda)

::: {.notes}

Simplify: "Compute is the brain—VMs are full servers, containers are
lean, serverless is magic."

:::

---

## Storage

- **Object Storage**: Files as objects (e.g., AWS S3)
- **Block Storage**: Hard drives for VMs (e.g., AWS EBS)
- **File Storage**: Shared systems (e.g., AWS EFS)

::: {.notes}

Analogy: "Storage is your closet—object for random stuff, block for
VMs, file for shared docs."

:::

---

## Networking

- **DNS**: Domain to IP resolution (e.g., Route 53)
- **Load Balancers**: Traffic distribution (e.g., AWS ELB)
- **Virtual Networks**: Isolated setups (e.g., AWS VPC)

::: {.notes}

Connect: "Networking ties it together—DNS finds your site, load
balancers share the load."

:::

---

# Infrastructure as Code (IaC)

::: {.notes}

Get practical: "Now, how do we *control* the cloud? Enter IaC."

:::

---

## What is IaC?

- **Definition**: Manage infrastructure with code
- **Benefits**:
  - Consistency
  - Repeatability
  - Version control

::: {.notes}

Sell it: "IaC is like a recipe—write once, build anywhere, no manual
clicks."

:::

---

## Tools

- **Terraform**: Multi-cloud IaC

  ```hcl
  resource "aws_s3_bucket" "example" {
    bucket = "my-bucket"
  }
  ```
