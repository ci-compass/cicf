# CICF

This repository contains the hands-on tutorials and auxiliary material for the
[CI Compass Fellowship](https://ci-compass.org/student-fellowships/) technical
course.

Videos and Slides are available to fellows on the shared CICF drive.

## Course Details

CICF is divided into two parallel themes which run over the entire semester:
the technical course and the research course.

The CICF technical program aims to give you an overview of cyberinfrastructure
concepts, tools, and skills.
This repository provides a way for you to try out commands and tools yourself.
Two of the skills we most want you to develop is a familiarity with using the command line
and comfort with using Git, a ubiquitous tool for contributing to technical projects.
There are also links to outside resources should you like to go into more depth on a topic.

For the technical class students are expected to do the following each week:

* Watch the technical lecture video for the week
* Do the technical exercises for that week (in this repository)
* Take the quiz for the week
* Come to class with questions and ready to talk about the exercises

In the technical session we will discuss the exercises for the week, answer questions, and you may be asked to present on your solution to the technical exercises.
The instructors are happy to answer questions, both in class and between classes.

**There is an expectation that you complete the exercises for each week.**

## Structure of this repository

The [getting started][started] directory contains instructions for setting up your computer for the class.

There is a directory for each week of the fellowship.
Inside each directory there is a `README` file describing the exercises for the week.
The exercises are in files starting with the word `exercise-`.
They may be shell scripts, or python scripts.

Each directory also has a test suite that will evaluate the exercises.
Run the test with the command `make` while you are in the current week's directory.
The goal is to get each test to pass.
If a test fails you can troubleshoot, and try again.
You are be expected to complete the exercises before the week's technical session.


## Spring 2026 Technical Program Calendar

| Week                | Content                                             |
|---------------------|-----------------------------------------------------|
| [Getting Started][started] | Setting things up for the course             |
| [Week 1][week01]    | The Command Line                                    |
| [Week 2][week02]    | Scientific Computing                                |
| [Week 3][week03]    | Using Python for Scientific Programming             |
| [Week 4][week04]    | Version Control                                     |
| [Week 5][week05]    | Containers and debugging                            |
| [Week 6][week06]    | FAIR data and systems                               |
| [Week 7][week07]    | Software architecture and systems; digital archives |
| [Week 8][week08]    | Cloud computing                                     |
| Week 9              | Spring break!                                       |
| [Week 10][week10]   | Data workflows                                      |
| [Week 11][week11]   | Machine Learning                                    |
| [Week 11b][week11b] | Neural Networks                                     |

## People and Contact

The CICF course was created and is run by the following team:

* Angela Murillo
* Nicole Virdone
* Don Brower
* Yaxue Guo
* Sarowar Hossain
* Jaya Bharti
* Christina Clark

And thanks to the following people who were previously involved:
* Sajith Sasidharan
* Erik Scott

You can reach the team by emailing cicf@ci-compass.org

## Thanks

The CICF course was developed with support from the National Science
Foundation Office of Advanced Cyberinfrastructure in the Directorate
for Computer Information Science under Grant #2127548.

## License

The lessons and text content in this repository is available under
[Creative Commons Attribution-ShareAlike 4.0 International][cc-by-sa]
license.  Code snippets may be used under [CC0 1.0 Universal][cc-zero]
license.


<!-- References -->

[started]: ./getting-started
[week01]: ./week01
[week02]: ./week02-python-and-jupyter
[week03]: ./week03-scientific-computing
[week04]: ./week04-git-and-coding-standards
[week05]: ./week05-containers-and-debugging
[week06]: ./week06-fair-data
[week07]: ./week07-architecture-and-archives
[week08]: ./week08-cloud-computing
[week10]: ./week10-data-workflows
[week11]: ./week11-machine-learning
[week11b]: ./week11b-neural-networks

[cc-by-sa]: https://creativecommons.org/licenses/by-sa/4.0/
[cc-zero]: https://creativecommons.org/publicdomain/zero/1.0/
