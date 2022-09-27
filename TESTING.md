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

[Google Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test the performance of the website. There are a couple of issues due to Bootstrap, Stripe, Mailchimp and general Heroku slowness.

![Lighthouse score](/media/)

*Go back to the [top](#table-of-contents)*

---

# Accessibility

## Accessibility Validation

The [WAVE WebAIM web accessibility evaluation tool](https://wave.webaim.org/) was used to ensure the website met high accessibility standards. All pages pass with some errors due to the bootstrap navbar and 1-2 warnings due to style preferences detailed below.
* 


*Go back to the [top](#table-of-contents)*

---

# Code Validation

## HTML Validation

The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML of the website. For logged in pages, the page source was copied and pasted into the validator. All pages pass except fr the follwing errors due to bootstrap navbar: 
* 

*Go back to the [top](#table-of-contents)*

---

## CSS Validation

The [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS of the website. The CSS passes with 0 errors.

![CSS validation](/media/)
![CSS validation](/media/)

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



*Go back to the [top](#table-of-contents)*

---