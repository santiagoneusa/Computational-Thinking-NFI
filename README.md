<h1 align="center"> Computational Thinking NFI </h1>
Resources for the computational thinking course in EAFIT university.

## Table of Contents
<ol>
  <li><a href="#about-the-feedback-automation-project">About the Feedback Automation Project</a></li>
  <li>
    <a href="#getting-started">Getting Started</a>
    <ul>
      <li><a href="#prerequisites">Prerequisites</a></li>
      <li><a href="#installation">Installation</a></li>
    </ul>
  </li>
  <li>
    <a href="#usage">Usage</a>
    <ul>
      <li><a href="#workshops">Workshops</a></li>
      <li><a href="#quices">Quices</a></li>
    </ul>
  </li>
  <li><a href="#contact">Contact</a></li>
</ol>

<!-- About the Feedback Automation Project -->

## About the Feedback Automation Project
You can see the files [here](https://github.com/sneusar/Computational-Thinking-NFI/blob/main/Feedback-Automation).

Since the process of keeping track of students through the Moodle platform was a bit tedious, I decided to create this script to help those who belong to the group of monitors of the 'Computational Thinking' course offered by EAFIT University.

This program evaluates in a '.csv' file the grades of the students in a given group. Those who have not submitted the activity or have a grade lower than 100 in any of the workshops or a grade lower than 4 in any of the quices, will be taken into account in a data dictionary that will be used to write files with the given information.

As a result, the program outputs a '.txt' file containing a set of messages, whose content is a greeting, the title of the unperformed activities and their grade, and a warning about the delivery date of the workshop or offer accompaniment in the case of a quiz with low performance. In addition, we find an '.xlsx' file that serves to keep track of the dates of sending the messages that the '.txt' file returns and where the monitor will put the answers that the student gives to the messages sent to him/her.

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
The program is independent of the OS under which it is running, however, it is necessary to have Python, Openpyxl and Pandas installed.

To install openpyxl you can use the following command.
  ```sh
  pip install openpyxl
  ```
  
To install Pandas you can use the following command.
  ```sh
  pip install pandas
  ```
  
### Installation
* To run the **workshops** automation program it is only necessary to download this file by curling on the following document:

   ```sh
   curl -O https://raw.githubusercontent.com/sneusar/Computational-Thinking-NFI/main/Feedback-Automation/workshops_feedback.py
   ```
* To run the **quices** automation program it is only necessary to download this file by curling on the following document:

   ```sh
   curl -O https://raw.githubusercontent.com/sneusar/Computational-Thinking-NFI/main/Feedback-Automation/quices_feedback.py
   ```

<!-- USAGE -->
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

So far you should have something like this:

![Required files](https://user-images.githubusercontent.com/99107537/224457388-4a367c2d-2a21-4ccc-8de1-ee651282e2dc.png)


### Workshops
Run the workshop file in terminal:

  ```sh
  python3 workshop_feedback.py 
  ```

And file the data like this:

![Filling workshops data](https://user-images.githubusercontent.com/99107537/224457574-f6f1db49-bee3-484c-bc94-bad07f047f3a.png)

At the end, a window named 'Grupo {your group's code} - Taller {workshop's number}' will show up, with the feedback files.

![Workshops output directory](https://user-images.githubusercontent.com/99107537/224457708-72b5aa47-be7a-4a0c-9ba0-bc7b7a9cb54b.png)


### Quices
Run the quices file in terminal:

  ```sh
  python3 quices_feedback.py 
  ```

And file the data like this:

![Filling quices data](https://user-images.githubusercontent.com/99107537/224457974-a038edfe-f945-43ba-9f18-c800f6893f34.png)

At the end, a window named 'Grupo {your group's code} - Taller {workshop's number}' will show up, with the feedback files.

![Quices output directory](https://user-images.githubusercontent.com/99107537/224457977-c79aba1a-987d-40c3-84c2-5b9a5226b544.png)

<!-- CONTACT -->
## Contact
If any question, write to Santiago Neusa Ruiz (sneusar@eafit.edu.co).

Project Link: https://github.com/sneusar/Computational-Thinking-NFI
