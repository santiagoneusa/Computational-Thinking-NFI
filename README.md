<h1 align="center"> Computational Thinking NFI </h1>
Resources for the computational thinking course in EAFIT university.

## Table of Contents
<ol>
  <li><a href="#about-the-project">About The Project</a></li>
  <li>
    <a href="#getting-started">Getting Started</a>
    <ul>
      <li><a href="#prerequisites">Prerequisites</a></li>
      <li><a href="#installation">Installation</a></li>
    </ul>
  </li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#contact">Contact</a></li>
</ol>

<!-- ABOUT THE PROJECT -->

## About the Automation of Monitoring & Accompaniment Project
Since the process of keeping track of students through the Moodle platform was a bit tedious, I decided to create this script to help those who belong to the group of monitors of the 'Computational Thinking' course offered by EAFIT University.

This program evaluates in a '.csv' file the grades of the students in a given group. Those who have not submitted the activity or have a grade lower than 100 in any of the activities of the workshop to be monitored, will be taken into account in a data dictionary, and then write files with this information.

As a result, the program outputs a '.txt' file containing a set of messages, whose content is a greeting, the title of the unperformed activities and their grade, and a warning about the delivery date of the workshop. In addition, we find an '.xlsx' file that serves to keep track of the dates of sending the messages that the '.txt' file returns and where the monitor will put the answers that the student gives to the messages sent to him/her.

> Disclamer: to date the project has only been implemented for workshops, not for quizzes.

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
The program is independent of the OS under which it is running, however, it is necessary to have Python3 and Pandas installed.

To install Pandas you can use the following command.
  ```sh
  pip install pandas
  ```
  
### Installation
To run the program it is only necessary to download a file by curling on the following document:
   ```sh
   curl -O https://raw.githubusercontent.com/sneusar/Computational-Thinking-NFI/main/Feedback-Automation/workshops_feedback.py
   ```
   
<!-- USAGE EXAMPLES -->
## Usage
The program is executed every time you want to track a group, i.e. if you have 2 groups, the program must be executed twice.

To run the script you need a '.csv' file containing the students' grades. That can be directly downloaded from Moodle.

* To download a csv file, go to the export --> plain text file tab.

![Select palin text file](https://user-images.githubusercontent.com/99107537/223928142-7defc6a7-6ec9-4eaf-a316-d362a8265486.png)
  
 > Note: Remember that where it says 'separate groups' is where you choose the list of the group you are going to download.

* Then, in the export format options you must select 'semicolon'. Once you have done this you can click on the 'download' button.

![Select semicolon](https://user-images.githubusercontent.com/99107537/223928857-4bd1573a-fdc7-433e-973f-3006e5871338.png)

* The file title must be the name of the group. If your group is '4850', the file should be named '4850.csv'. If you are downloading multiple files because you have multiple groups, do it the same way.

![Download name](https://user-images.githubusercontent.com/99107537/223929066-4ac7b9e6-77f4-4279-9209-a577763ed35b.png)

After you have the python file and the '.csv' downloaded, run the program via terminal or in your IDE of choice. The instructions to follow will appear on the screen.

<!-- CONTACT -->
## Contact
If any question, write to Santiago Neusa Ruiz (sneusar@eafit.edu.co).
Project Link: https://github.com/sneusar/Computational-Thinking-NFI
