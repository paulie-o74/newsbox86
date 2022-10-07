# The Newsbox Testing

:arrow_left: [Return to the README](README.md)

## Table of Contents
- [Performance](#performance)
  - [Google's Lighthouse Performance](#googles-lighthouse-performance)
- [Accessibility](#accessibility)
  - [Accessibility Validation](#accessibility-validation)
- [Code Validation](#code-validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [JS Validation](#js-validation)
  - [PEP8 Validation](#pep8-validation)
- [Testing](#testing)
  - [Manual Testing (BDD)](#manual-testing-bdd)

# Performance

## Google's Lighthouse Performance

[Google Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test the performance of the website. There are a couple of issues due to Bootstrap and general Heroku slowness.

![Lighthouse score](/static/images/lighthouse.png)

*Go back to the [top](#table-of-contents)*

---

# Accessibility

## Accessibility Validation

The [WAVE WebAIM web accessibility evaluation tool](https://wave.webaim.org/) was used to ensure the website met high accessibility standards. All pages pass with zero errors due to the and a few warnings due to style preferences detailed below.
* 


*Go back to the [top](#table-of-contents)*

---

# Code Validation

## HTML Validation

The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website. For logged in pages, the page source was copied and pasted into the validator. All pages pass except for the follwing errors due to footer: 
* stray footer tag (After checking this doesn't seem to be correct)

*Go back to the [top](#table-of-contents)*

---

## CSS Validation

The [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS of the website. The CSS passes with 0 errors.


*Go back to the [top](#table-of-contents)*

---

## JS Validation

[JSHint](https://jshint.com/) was used to validate the JavaScript/Jquery of the website. No major issues were found.


*Go back to the [top](#table-of-contents)*

---

## PEP8 Validation

A combination of the following Python packages was used to ensure the code is PEP8 compliant: flake8 and autopep8. The final flagged files were checked in [PEP8 Online](http://pep8online.com). The only issues found were a few longer lines in the base project's settings.py, models.py and webhook_handler.py and migrations files due to HTML blocks.

*Go back to the [top](#table-of-contents)*

---

# Testing

## Manual Testing (BDD)

BDD, or Behaviour Driven Development, is the process used to test user stories in a non-technical way, allowing anyone to test the features of an app.

User Story | BDD Test | Pass
--- | --- | :---:
As a first time user<br>I want to know what is expected of me on the home page<br>So that I can read some blog posts navigate the site and decide on whether or not I want to sign up | Given that I'm a first time user<br>When I view/scroll down the homepage<br>Then I should see what the purpose of the site is, easy navigation, a link to sign up and some news stories | :white_check_mark:
As a first time user<br>I want to be able to<br>read posts and comments, So that I can<br>decide on whether or not I think it is worth signing up to. | Given that I'm a first time user<br>When I view/scroll down the homepage<br>Then I read posts and comments, a link to sign up and some news stories | :white_check_mark:
As a first time user<br>I want to be able to<br>know how to sign up to the web site easily and create a profile. So that I can<br>post stories and engage and comment on other posts. | Given that I'm a first time user<br>When I sign up to the web site<br>post stories and engage and comment on other posts. | :white_check_mark:
As a Site User<br>I want to be able to<br>easily register a profile. So that I can<br>create a profile and access the main functionality of the site. | Given that I'm a site user<br>When I register a profile<br>Then I can access the main functionality of the site | :white_check_mark:
As a Site User<br>I want to be able to<br>easily login/log out. So that I can<br>access my information without filling in forms every time and ensure the security of my account. | Given that I'm a site user<br>When I login/log out<br>Then I can access my information without filling in forms every time and ensure the security of my account | :white_check_mark:
As a Site User<br>I want to be able to<br>easily recover my password if I forget it. So that I can<br>recover access to my account. | Given that I'm a site user<br>When I click forgot password<br>Then I should receive an email with simple instrucitons to reset password | :white_check_mark:
As a Site User<br>I want to be able to<br>receive a confirmation email after registering. So that I can<br>verify that my registration was successful. | Given that I'm a site user<br>When I sign up<br>Then I should receive a confirmation email after registering so that I can verify that my registration was successful | :white_check_mark:
As a Site User<br>I want to be able to<br>see different categories of posts. So that I can<br>identify specific posts and not waste time looking at other categories' posts. | Given that I'm a site user<br>When I click categories dropdown<br>Then I should see see the categories and be able to click and see all posts within that category | :white_check_mark:
As a Site User<br>I want to be able to<br>search for a post by name or description. So that I can<br>find a specific post I'd like I am interested in. | Given that I'm a site user<br>When I use the search bar<br>Then I should see specific post/s that match my search query | :white_check_mark:
As a Site User<br>I want to be able to<br>create/read/update/delete a post. So that I can<br>alter how I would like my post to look to allow for maximum engagement. | Given that I'm a site user<br>When I choose create/read/update/delete a post<br>Then I should receive a confirmation message and all functionality works as expected | :white_check_mark:
As a Site owner<br>I want to be able to<br>review all posts, categories, users, likes, etc.	So that I can<br>maintain the site and remove any offensive content. | Given that I'm a Site owner<br>When I navigate to the admin<br>Then I should see all posts, categories, users, likes, etc. | :white_check_mark:
As a Site owner<br>I want to be able to<br>edit/update/delete a post.	So that I can<br>maintain the site and remove any offensive content. | Given that I'm a Site owner<br>When I navigate to the admin<br>Then I should see be able to control all content on the website | :white_check_mark:
As a Site owner<br>I want to be able to<br>direct users to my social profiles. So that I can<br>increase social interaction and attract new users. | Given that I'm a Site owner<br>When I view/scroll down to the footer<br>Then I should see working links to my social media profiles | :white_check_mark:
As a Site owner<br>I want to be able to ensure<br>all areas of the site to function correctly and have no bugs. So that I can<br>ensure an enjoyable browsing experience for all newcomers. | Given that I'm a Site owner<br>When I check all site functionality<br>Then I should see that everything works as expected, there are no bugs and all links and forms work as expected | :white_check_mark:

*Go back to the [top](#table-of-contents)*

---