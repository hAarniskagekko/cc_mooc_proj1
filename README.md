# Cyber Security Base 2021 Project 1

This is an insecure website developed for Cyber Security Base 2021 project 1 assignment. Any of this code should not be used in anything but to demonstrate how website security vulnerabilities work.

## Installation of the repository: //TODO


## FLAW 1:
/cc_mooc_proj1/cc_mooc_proj1/views.py#L14 (post_tweet() save without cleaning)

Saving the user input text that will be displayed in the website for all the user that access the page without sanitation introduces XSS vulnerability to the page. This allows attackers to input malicious JavaScript to the page and with it they can for example steal user cookies from the site.

To fix this issue the user input should be validated before saving it to the website database. This can be done in several different ways. For example by using Django's *strip_tags()* function which will remove all HTML tags from user input. If some HTML tags should be allowed in the input python library *bleach* could be used to sanitize the input with greater control on what to remove from the input.

## FLAW 2:
/cc_mooc_proj1/cc_mooc_proj1/views.py#L28 (no @login_required before the view)

Access control to /secret_of_the_day page is broken and users that are not logged in can access the page.

To fix this you have to make sure only users that are logged in can access the page. In django this is done by adding @login_required flag before the view function in question in views.py file. This makes sure that unauthenticated users are denied access.
