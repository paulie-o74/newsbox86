# The Newsbox, a blog designed to share stories
(Developer: Paul Thomas O'Riordan)

[View live site](https://.herokuapp.com/)

![Screenshot of ](https://res.cloudinary.com/rashdogg74/image/upload/v1655415295/static/images/amires.3c1b4c515a1e.png)

## Table of Contents

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Stories](#user-stories)
    3. [Scope](#scope)
    4. [Design](#design)
    5. [Wireframes](#wireframes)
3. [Technical Design](#technical-design)
    1. [Flowchart](#flowchart)
    2. [Data Models](#data-models)   
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
5. [Features](#features)
6. [Testing](#validation)
    1. [Python Validation](#Python-validation)
    2. [Testing user stories](#testing-user-stories)
8. [Bugs](#Bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgments](#acknowledgments)

## Project Goals 

- To create a web application which will allow users to share blog posts and news articles similar to reddit and other users will be able to up and down vote posts according to how important/newsworthy they think they are. Users will also be able to comment on posts and engage in a discussion. 

### User Goals
- To be able sign up and create an online profile to share blog posts/news articles.
- To be able to upvote and down vote posts according to importance.
- To be able to comment on a post and engage in a discussion.

### Site Owner Goals
- Create a django application that functions in a similar manner to that which can be found on reddit
- Create a django application which users will be able to follow intuitively.
- Create a django application which is fit for purpose and does not have any bugs.
- Create a django application which will have full CRUD functionality. 

## User Experience
### Target Audience
- People who follow the news.
- People who are interested in blogs.
- People who are interested in online forums.

### User Stories

#### First-time User 
1. As a first time user, I want to know what is expected of me on the home page.
2. As a first time user, I want to be able to sign up to the web site easily and create a profile. 
3. As a first time user, I want to be able to read posts but not be able to comment or post. 
4. As a first time user, I want to be able to add posts after I have signed up.
5. As a first time user, I want to be able to log out of the web site easily.
6. As the user, I want to be able to edit/update/delete a post.
7. As the user, I want to be able to engage in a discussion on a post.
8. As the user, I want to be able to see all posts from a particular category.

#### Site Owner
9. As the site-owner, I want to be able to review all posts, categories, users, upvotes, downvotes, etc.
10. As the site-owner, I want to be able to edit/update/delete a post. 
11. As the site-owner, I want to be able to direct users to my social profiles. 
12. As the site-owner, I want all areas of the site to function correctly and have no bugs. 

### Scope
In this first version a sign on using social profiles won't be implemented as well as password recovery. The user model would also be altered. In this first version, the upvote/down vote functionality also unfortunately was not implemented due to time constraints.

## Technical Design

### ERD of the database 

Below you can see the ERD, created with ![lucidchart](https://res.cloudinary.com/rashdogg74/image/upload/v1655558307/static/images/Database_ER_diagram_The_NewsBox_1_tvhfrs.jpg)

### UI/UX

Design inspiration came from (https://zyro.com/es/preview/bronx?utm_medium=affiliate&utm_source=aff1635&utm_campaign=aff35&transaction_id=1021ce1d83add930c49518a342eb22) as well as the hello django walkthrough project on Code Institute.


### Data models

For this project I have used the following features:
- list comprehension making a list from an iteration, a more succinct way to create a list from a for loop. 
- If/else/elif statements
- Dictionaries e.g. in the username/password checking. 

## Technologies Used

### Languages

- [Python 3](https://www.python.org/)
- [Http](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
- [Javascript](https://www.javascript.com/)

### Frameworks and Tools

1. [Heroku](https://heroku.com/) - Heroku was used to deploy the project and to provide a virtual terminal to for examiners. 
2. [GitHub](https://github.com/) - GitHub was used as a remote repository to store project code. 
3. [Gitpod](https://gitpod.com/) - Gitpod was used as the main IDE for this project.
4. [lucidchart.com](https://www.lucidchart.com/pages/) - was used to draw flowchart and the ERD.
3. [Trello](https://trello.com/) - Trello was used as an agile took to manage the planning and implementation of all functionality.


#### Libraries

### 3rd Party Libraries
1. [Cloudinary](https://cloudinary.com/) - JUSTIFICATION:  For the purposes of the project spec, I wanted to host images uploaded by users to an external CDN. Cloudinary is an end-to-end image- and video-management solution for websites and mobile apps, covering everything from image and video uploads, storage, manipulations, optimizations to delivery.

2. [humanize](https://github.com/Humanizr/Humanizer) - JUSTIFICATION: For the purposes of the project spec, I wanted to give the user an easy human readable time format when viewing posts.

3. [crispyforms](https://django-crispy-forms.readthedocs.io/en/latest/#) - JUSTIFICATION: For the purposes of the project spec, I wanted touse crispyforms to allow me to render django forms in an element manner and which interacts very well with bootstrap styling.

## Features

### 

![Screenshot of ](https://res.cloudinary.com/rashdogg74/image/upload/v1655415294/static/images/Home.8f0c1c10abd7.png)

**This screen covers the following user stories:**

1. As a first time user, I want to know what is expected of me on the home page.
2. As a first time user, I want to be able to sign up to the web site easily and create a profile. 
3. As a first time user, I want to be able to read posts but not be able to comment or post. 


### 

![Screenshot of ](https://res.cloudinary.com/rashdogg74/image/upload/v1655415296/static/images/Sign%20up.49337418e64f.png)

**This screen covers the following user stories:**

2. As a first time user, I want to be able to sign up to the web site easily and create a profile. 

![Screenshot of ](https://res.cloudinary.com/rashdogg74/image/upload/v1655415292/static/images/Add.b48618f16fec.png)

**This screen covers the following user stories:**

4. As a first time user, I want to be able to add posts after I have signed up.
8. As the user, I want to be able to see all posts from a particular category.

![Screenshot of ](https://res.cloudinary.com/rashdogg74/image/upload/v1655559044/static/images/Screenshot_2022-06-18_at_15.30.39_vne23y.png)

**This screen covers the following user stories:**

6. As the user, I want to be able to edit/update/delete a post.


![Screenshot of ](https://res.cloudinary.com/rashdogg74/image/upload/v1655415299/static/images/delete.4731114973b7.png)

**This screen covers the following user stories:**

6. As the user, I want to be able to edit/update/delete a post.


![Screenshot of ](https://res.cloudinary.com/rashdogg74/image/upload/v1655415290/static/images/%20%20db.67a8a00c2572.png)

**This screen covers the following user stories:**

9. As the site-owner, I want to be able to review all posts, categories, users, upvotesetc.
10. As the site-owner, I want to be able to edit/update/delete a post.


![Screenshot of ](https://res.cloudinary.com/rashdogg74/image/upload/v1655558820/static/images/Screenshot_2022-06-18_at_15.26.55_zaaqba.png)

**This screen covers the following user stories:**

7. As the user, I want to be able to engage in a discussion on a post. 

![Screenshot of ](https://res.cloudinary.com/rashdogg74/image/upload/v1655415299/static/images/footer.4d55cfa180f5.png)

**This screen covers the following user stories:**

11. As the site-owner, I want to be able to direct users to my social profiles.  

**All of the above plus testing resolves in the final user story passing:**

12. As the site-owner, I want all areas of the site to function correctly and have no bugs. 


## Validation

### Python Validation
The Python code of each module was validated using [PEP8 Validation Service](http://pep8online.com/).  All modules returned a pass with 0 errors and few warnings due to django integration.

### HTML Validation
The html code of each file was validated using W3C Markup Validation Service .  Some files returned warnings but only due to djangos templates and variables. 

### CSS Validation
The W3C Jigsaw CSS Validation Service was used to validate the CSS of the website. It did not return any errors.


### Testing user stories

All user stories were extensively tested and the clear and simple interface, feedback messages as well as gaining insight from different people, testing it without any prior knowledge of the site, all helped in the deployment of this project. Coverage and Test Case were originally used also used for 50% of the application in it's past repository but due to time constraints I was not able to include it in this version.. 


1. As a first time user, I want to know what is expected of me on the home page.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Nav bar  |  Vavigate to the different pages of the site  | Works as expected with no broken links | Works as expected with no broken links |


2. As a first time user, I want to be able to sign up to the web site easily and create a profile. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Sign up link/page      | Go to sign up page and add details | Works as expected with no broken links or empty forms valid | Works as expected with no broken links |

3. As a first time user, I want to be able to read posts but not be able to comment or post. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Home page with all posts | Read all posts but not able to comment/edit/delete | Works as expected with no broken links | Works as expected with no broken links |

4. As a first time user, I want to be able to add posts after I have signed up.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| After signing up, the link to add posts appears | Link brings you to the add post page with form | Works as expected with no broken links or empty forms valid | Works as expected with no broken links |

5. As a first time user, I want to be able to log out of the web site easily.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|   Log out button     |   Click log out        | link works as expected and logs the user out | link works as expected and logs the user out |

6. As the user, I want to be able to edit/update/delete a post.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Once a user is logged in, any post that they have submitted will have an edit/delete button which then appears next to it| Press edit/delete buttons| Link works as expected and brings user to confirmation page | Link works as expected and brings user to confirmation page|

7. As the user, I want to be able to engage in a discussion on a post. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Once a user is logged in, they can comment and engage in a discussion on any post| Comment box appears at the bottom of each post| Link works as expected and page reloads showing comment| Link works as expected and page reloads showing comment|

8. As the site-owner, I want to be able to review all posts, categories, users, upvotes, downvotes, etc.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Django admin panel | Go to the desired model and review| Django admin panel is displayed correctly and all actions work as expected| Django admin panel is displayed correctly and all actions work as expected|

9. As the site-owner, I want to be able to edit/update/delete a post. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Django admin panel| Go to the post model and do what is required| Go to the post model and do what is required | Go to the post model and do what is required|

10. As the site-owner, I want to be able to direct users to my social profiles. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Footer| Click on social links| Links work as expected and open in new tab  | Links work as expected and open in new tab  |

11. As the site-owner, I want all areas of the site to function correctly and have no bugs. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Entire site | Multiple- see above| No bugs found| No bugs found  |

## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| Original plan was to use up and downvote functionality and subsequently order posts by that.| As my level of ajax is not up to a sufficient level I removed this funcitonality for this version of the project and added just an upvote button. |
| Footer was not sticking to the bottom of the page | Use 100% vh |
| Success messages not displaying  | Add javascript code at the bottom of base html page |
| Close to final deployment the database was comprimised because I tried to hard revert to an old commit, I and my tutors tried to debug, remove migrations etc but to no avail | Restart project in new repository and add everything again.. |
| I tried to include summernote in the html via an import but my tutor nor I could debug so that was removed and may be included in a later version | Due to time constraints this was not possible for this version of the product. |


## Deployment

### Heroku

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars, add your sensitive data (creds.json for example)
6. For this project, I set buildpacks to and in that order.
7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
8. Enter your repository name and click on it when it shows below
9. Choose the branch you want to buid your app from
10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository

### Forking the GitHub Repository

### Code
In order of appearance:
- Blog functionality was built with help from (https://www.youtube.com/watch?v=XWbTKJeSgRQ&ab_channel=JamesQQuick) Codemy on youtube
- Models were built with help from (https://www.youtube.com/c/CodeArtisanLab) Code Artisan Lab on youtube
- Views were built with help from (https://www.youtube.com/channel/UCxj-ETPjJu_qs-oHws7YtKQ) Media Upload on youtube
- General django understanding, added to from (https://www.youtube.com/c/CodingWithMitch) Coding with Mitch on youtube

## Acknowledgements
I would like to take the opportunity to thank:
- To the lovely people on the Code Institute Slack for encouraging all the way.
- To the Code Institute tutors for helping me with a couple of critical issues.
- To my wife Ashley for her support during a difficult personal time completing this project. 