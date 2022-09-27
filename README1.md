<h1 align="center">The Newsbox, a blog to share stories</h1>


![Am I responsive]()

### **Live Site:**
[The Newsbox]()

### **Repository:**
[The Newsbox Repository](https://github.com/rashdogg74/)

### **Developer:**
Paul Thomas O'Riordan

# About
This is a full-stack project built using Django, Python, HTML, CSS, and JavaScript. I have created this website for my fourth project of the codeinstitute's Diploma in FullStack Development. It is a web application that will allow users to share what they see as newsworthy and allow for user interaction and commenting similar to that of reddit. 

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
<!-- + [Aim](#aim)
+ [Databases](#database)
+ [Scope](#scope)
+ [Wireframes](#wireframes)
+ [Epics and User Stories](#user-stories)
+ [Agile Methodologies](#agile)
+ [Features](#features)
+ [Marketing](#marketing)
+ [Bugs](#bugs)
+ [Technologies Used](#tech)
+ [Testing](#testing)
+ [Deployment](#deployment)
+ [Credits](#credits) -->

### Aim <a name="aim"></a>
To create a web application which will allow users to share blog posts and news articles similar to reddit and other users will be able to up and down vote posts according to how important/newsworthy they think they are. Users will also be able to comment on posts and engage in a discussion. 

## Database Design <a name="database"></a>
[Database Schema](media/readme_images/.webp)

#### **User Account**
This app enables authenticated users to save their information so that when they are logged in the order form is pre-filled, creating an improved user experience. The `UserProfile` model has a one-to-one field that is linked to the Django AllAuth user account, upon logging in the model method `create_or_update_user_profile` creates the profile if it isn't already present in the model.

#### **Blog App**

This app controls the main functionality associated witht he web application. I have created three models to store the necessary data: `Post`, `Comment` & `Category`.

`Category` stores the various category types of posts e.g. sport, coding, politics etc. This allows the user to filter the posts by the category if they are looking for something specifically.

`Post` enables individual posts to be added to the database in order for them to be shown on the post detail page. Only admin users are able to access this functionality and it can be done from the front end using the `AddPostView` view.

`Comment` allows users to comment and interact with the website, allowing a disucussion within the community increasing engagment. The `PostDetail` view which allows user to see the full detail when a post headline/image is clicked on then has a post method which allows user to fill in the comment form and interact with the post and other users.


## Scope <a name="scope"></a>

 * A simple, straightforward, intuitive UX experience;
 * Explicit content;
 * An easy navigation for the user through all the pages and features;
 * A site that is visually appealing on all screen sizes.

### Structure

* A clear and straightforward layout is in place to ensure users can navigate intuitively and have an enjoyable browsing experience.
* Mobile navigation is the same on all pages to ensure easy navigation.
* Footer is fixed on the bottom with links to social media.

## Skeleton <a name="wireframes"></a>

### UI/UX

Design inspiration came from various google searches for blogs and templates, the "I think therefor I blog" walkthrough project on Code Institute as well as reddit- the main inspiration.

The project was developed from initial wireframes by hand and then these were expanded digitally.
Each subsequent page after the home page has the same structure to ensure uniformity accross the site.

Click to see wireframes:

[1](/)<br>
[2](/media/)<br>
[3](/media/)<br>
[4](/media/)<br>
[5](/media/)<br>
[6](/media/)<br>
[7](/media/)<br>
[8](/media/)<br>
[9](/media/)<br>
[10](/media/)<br>
[11](/media/)<br>
[12](/media/)<br>
[13](/media/)<br>

## User Experience

### User Stories <a name="user-stories"></a>

* EPIC: Viewing and navigation of the web app works as expected

1. 

* EPIC: 



* EPIC: 


* EPIC: 



* EPIC: 






### Agile methodology <a name="agile"></a>

* All functionality and development of this project will be managed through GitHub issues, milestones and projects, along with google sheets for initial conception. 

<summary>All sprints are described here.</summary>

* Sprint 1 -  (Finished at //2022)

  + Initial setup
    - Install django
    - Install Allauth
    - Add Allauth templates to project templates
    - Create base.html
    - Create Home app
    - Create index.html, view and style
    - Create responsive navigation
    - Add to README.md file
  
* Sprint 2 - 2 (Finished on /2022)



* Sprint 3 - (Finished on 2022)


  * Sprint 4 -  (finished 2022)



* Sprint 5 - (Finished on 2022)


### Features <a name="features"></a>
* Responsive design.
* Website title and information on the site's purpose.
* Navigation Menu (Site Wide).
* Postgress databases to store information and user login/profile information.
* CRUD Functionality
* Login functionality.
* Logout functionality.
* Ability to view all posts.
* Ability to view post details.
* Ability to add and remove posts.
* Ability to Update posts.
* Ability to review a product.
* Ability to sign up to a newsletter.
* Ability to view a site policy.
* Ability to contact the site owners.
* Ability to comment on blog posts and edit & delete comments.
* Admin creation and management of products.

**Importance and Difficulty**

|       Feature         |   Difficulty   |   Importance   |
|:--------------------  |--------------- |--------------- |
|Postgress databases to |       5        |       5        |
|store information and  |                |                |
|user login/profile     |                |                |
|information            |                |                |
|:--------------------  |--------------- |--------------- |
|CRUD Functionality     |       5        |       5        |
|:--------------------  |--------------- |--------------- |
|Admin creation and     |       5        |       5        |
|management of Posts    |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to view all    |       2        |       5        |
|posts.                 |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to view        |       2        |       5        |
|post details           |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to add and     |       2        |       5        |
|remove a post          |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to update the  |       3        |       5        |
| or remove a post      |                |                |
|:--------------------  |--------------- |--------------- |
|Registered user can    |       5        |       5        |
|add a post/comment.    |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to signup to   |       2        |       5        |
|a newsletter.          |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to view a site |       2        |       5        |
|policy.                |                |                |
|:--------------------  |--------------- |--------------- |
|Ability to contact the |       2        |       5        |
|site owners.           |                |                |
|:--------------------  |--------------- |--------------- |
|:--------------------  |--------------- |--------------- |
|Login functionality    |       3        |       5        |
|:--------------------  |--------------- |--------------- |
|Navigation Menu        |       3        |       5        |
|(Site Wide)            |                |                |
|:--------------------  |--------------- |--------------- |
|Responsive design      |       2        |       5        |
|:--------------------  |--------------- |--------------- |
|Website title and      |       1        |       5        |
|information on the     |                |                |
|the site purpose       |                |                |
|:--------------------  |--------------- |--------------- |
|Logout functionality   |       1        |       5        |

### Future Features
As this is an educational project, it will not be maintained in the future. However, if it were a live site, some features that I would like to implement are listed below.
* Allow for the use of social sign ins.
* Better form validation.
* User permissions / groups to allow staff to have non-breaking access to the CMS.
* Link up user profiles and subscription list.
* Further improve user experience.
* Add a FAQs section.

## Marketing <a name="marketing"></a>

+ This site has an Instagram Page with a link on the page footer. It can be viewed here:
[Instagram Page](https://www.instagram.com/)
[Facebook Page Images](media/)

+ This site has a Facebook Business Page with a link on the page footer. It can be viewed here:
[Facebook Page](https://www.facebook.com/)
[Facebook Page Images](media/)

+ Users can subscribe to our newsletter to receive all offers in their email box. Subscription links are available on the footer on all pages. 

+ Upon registering, the user is shown a message confirming their subscription. The site owner can now see the new subscriber on their audience dashboard, and new campaigns will be sent to them too.


* Colours

The Colour scheme was generated using the eyedropper plugin to get one colour from the logo image and [colours](https://coolors.co/) to create the colour palette.

[View Pallet Here](media/readme_images/pallette.png)

* Font Selection
 
Two complimentary fonts were chosen with [Google Fonts](https://fonts.google.com/) to be used across the website.

The chosen fonts were Gloria Hallelujah for the logo and titles and Raleway for everything else on the site.


## Bugs <a name="bugs"></a>

| **Bug** | **Fix** |
| ----------- | ----------- |
| The logo would not stay in the footer when changing screen sizes.| Add the dorm-inline class to the div and justify content center as well as removing redundant classes |
| When scrolling up to show the nav bar again, the content underneath could be seen. | Remove the html height - 100% in css |
| If a search term which isn't recognised is used then messages would not be shown and all products would be shown. | I used for else statements to show an image and message if no results are found using the specific search term |
| When trying to pay, the order was going through but not going to the success page as it was stuck on the processing page. | There was an old webhook enabled from a preovious project and when this was deactivated and a new correct domain added then it worked correctly. |
| stripelements.js was not aligned to the billing details as there was only one field for name wheras in the profile model there as first name and second name  | Use of template strings to .trim the first name and second name. |
| A user could update the quanitity of original pieces (1 of a kind pieces) | In the quantity input script added a new function called handle enable diable cat. Where the category of the product was assigned to a variable and if theat category included the word original then the + - butoons were disabled. Then a if else statement for all quantity inputs on the page was used. Also in views.py an if else statement was used not to increment the quantity of the product in the bag if the user clicked the add to bag button multiple times. The user would then receive a message explaining what was happening. |


## Technologies Used <a name="tech"></a>

* [HTML](https://en.wikipedia.org/wiki/HTML)
	* This project uses HTML as the main language used to complete the structure of the Website.
* [CSS](https://en.wikipedia.org/wiki/CSS)
	* This project uses custom written CSS to style the Website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    * JavaScript is used on multiple pages to manipulate the DOM.
* [Python](https://www.python.org/)
    * This projects core was created using Python, the back-end logic and the means to run/view the Website.
    * Python Modules used (These can be found in the requirements.txt project file):

* [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
    * This project was created using the Django framework, the back-end logic and the means to run/view the Website.
* [Bootstrap](https://getbootstrap.com/)
    * The Bootstrap framework was used through the website for layout and responsiveness.
* [Google Fonts](https://fonts.google.com/)
	* Google fonts are used in the project to import the fonts for the site.
* [GitHub](https://github.com/)
	* GithHub is the hosting site used to store the source code for the Website, as well as github projects to manage the planning and implementation of all functionality using a kanban board. 
* [Gitpod](https://gitpod.io/)
	* Gitpod is used as version control software to commit and push code to the GitHub repository where the source code is stored.
* [Heroku](https://dashboard.heroku.com/apps)
    * Heroku was used to deploy the live website.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
	* Google chromes built in developer tools are used to inspect page elements and help debug issues with the site layout and test different CSS styles.
* [Font Awesome](https://fontawesome.com/)
    * All the Icons displayed throughout the website are Font Awesome icons.
* [Favicon](https://favicon.io/)
    * Favicon.io was used to make the site favicon 
* [Am I Responsive](http://ami.responsivedesign.is/#)
    * Multi Device Website Mockup Generator was used to create the Mock up image in this README
* [Cloudinary](https://cloudinary.com/)  
    * Cloudinary is an end-to-end image and video-management solution for websites and mobile apps, covering everything from image and video uploads, storage, manipulations, optimizations to delivery.
* [humanize](https://github.com/Humanizr/Humanizer) 
    * Provides an easy human readable time format when viewing posts.
* [crispyforms](https://django-crispy-forms.readthedocs.io/en/latest/#) 
    * To render django forms in an elegant manner and one which interacts very well with bootstrap styling.

## Testing <a name="testing"></a>

Testing is required on all features and user stories documented in the TESTING.md file linked from this README below as the testing is a large section. 
All clickable links must redirect to the correct pages. All forms linked to the database
must be tested to ensure they insert all given fields into the correct collections.

HTML Code must pass through the [W3C HTML Validator](https://validator.w3.org/#validate_by_uri).

CSS Code must pass through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

JavaScript code must pass through the [JSHint Validator](https://jshint.com/).

Python Code must pass through [PEP8 Validator](http://pep8online.com/)

The website was extensively tested as it was developed using:
* print().
* The terminal by printing the expected outcome.
* Testing User Stories.
* Testing scenarios manually.
* Testing functionallity manually.

This project has been tested throughout its inception. Each input has been thoroughly tested to make sure that any invalid inputs are handled correctly and a response is shown to the user.

Full test results can be found [here](TESTING.md)

## Deployment on Heroku <a name="deployment"></a>

This project was deployed through Heroku using the following steps:

### Requirements and Procfile
Heroku needs to know which technologies are being used and any requirements, so I created files to let it know. Before creating the Heroku app, create these files using the following steps in GitPod: 
* In the GitPod terminal, type ```pip3 freeze --local > requirements.txt``` to create your requirements file.
* Create your Procfile and insert the following code: ```web: ``` and make sure there is no additional blank line after it. 
* Push these files to your repository.

### Creating Heroku App
* Log into Heroku
* Select 'Create New App' from your dashboard
* Choose an app name (if there has been an app made with that name, you will be informed and will need to choose an alternative)
* Select the appropriate region based on your location
* Click 'Create App'

### Connecting to GitHub
* From the dashboard, click the 'Deploy' tab towards the top of the screen
* From here, locate 'Deployment Method' and choose 'GitHub'
* From the search bar newly appeared, locate your repository by name
* When you have located the correct repository, click 'Connect'

### Environment Variables
* Click the 'Settings' tab towards the top of the page
* Locate the 'Config Vars' and click 'Reveal Config Vars'
* Enter all variables needed.

<!-- ### Heroku Postgres Database
* AWS S3 Buckets
* Paste variable in to Heroku config vars. -->

### Heroku Postgres Database
* Go to the resources tab in Heroku.
* In the Add-ons search bar look for Heroku Postgres & select it.
* Choose the Hobby Dev-Free option in plans.
* Click submit order form.
* Go back to the build environment and install 2 more requirements:
  * ```pip3 install dj_databse_url```
  * ```pip3 install psycopg2-binary```
  make sure to add these to the requirements file using ```pip3 freeze > requirements.txt``` 

### Set up Emails

## I used Gmail for the email on the contact page. Others can be used but will need a few changes**

* Go to settings.py and change the EMAIL_HOST_USER to your chosen email address.
* If you want to set up a new Gmail account for the site, this is the time to do so.
* Go to the Gmail account and open the 'Settings' tab.
* Go to 'Accounts and Imports' > 'Other Google Account Settings'.
* Go to the 'Security' tab and open 'Signing in to Google'.
* Click on '2-step Verification', click 'Get Started' and turn on 2-step verification following their instructions.
* Go to 'Security' > 'Signing in to Google' > 'App Passwords'.
* (You may have to input your account password again) Set 'App' to 'Mail', 'Device' to Other, and name it Django.
* The passcode that appears will be used in your Heroku variables.

## Deploy
* In Heroku, once all the variables are in place, locate 'Manual Deploy' > choose the master branch and click 'Deploy Branch'.
* Once the app is built (it may take a few minutes), click 'Open App' from the top of the page.
* Go back to the 'Deploy' tab and you can now click 'Enable Automatic Deployment'. Changes automatically deploy when you make a git push.

## Forking the Repository
* Log in to GitHub and locate the GitHub Repository.
* At the top of the Repository above the "Settings" Button on the menu, locate the "Fork" Button.
* You will have a copy of the original repository in your GitHub account.
* You will now be able to make changes to the new version and keep the original safe. 

## Making a Local Clone
* Log into GitHub.
* Locate the repository.
* Click the 'Code' dropdown above the file list.
* Copy the URL for the repository.
* Open Git Bash on your device.
* Change the current working directory to the location where you want the cloned directory.
* Type ```git clone``` in the CLI and then paste the URL you copied earlier. This is what it should look like:
  * ```$ git clone https://github.com/```
* Press Enter to create your local clone.

You will need to install all of the packages listed in the requirements file you can use the following command in the terminal ```pip install -r requirements.txt``` which will do it for you. 

## Credits <a name="credits"></a>

### Code
* The project is broadly based on the I think therefor I blog project by the Code Institute and was used as a base for my project (https://github.com/Code-Institute-Solutions/Django3blog)
* The Blog functionality was built with help from (https://www.youtube.com/watch?v=XWbTKJeSgRQ&ab_channel=JamesQQuick) Codemy on youtube
* The navbar was built using references from (https://www.w3schools.com/css/css_navbar.asp)
* The blog was built using references from (https://djangocentral.com/building-a-blog-application-with-django/)
* Models were built with help from (https://www.youtube.com/c/CodeArtisanLab) Code Artisan Lab on youtube
* The footer was built using references from (https://mdbootstrap.com/docs/standard/navigation/footer/)

### Media
* Images - 

### Acknowledgments
* Code Institutes Tutor support for their help and guidance.
* My wife Ashley for her unwaivering support and advice.
* Students of Code Institute on slack that helped with certain bugs.