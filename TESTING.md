# Testing

Return back to the [README.md](README.md) file.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

In this section, you need to convince the assessors that you have conducted enough testing to legitimately believe that the site works well.
Essentially, in this part, you should go over all of your project's features, and ensure that they all work as intended,
with the project providing an easy and straightforward way for the users to achieve their goals.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## Code Validation

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use the space to discuss code validation for any of your own code files (where applicable).
You are not required to validate external libraries/frameworks, such as imported Bootstrap, Materialize, Font Awesome, etc.

**IMPORTANT**: You must provide a screenshot for each file you validate.

**PRO TIP**: Always validate the live site pages, not your local code. There could be subtle/hidden differences.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- If you are copying/pasting your HTML code, use this link: https://validator.w3.org/#validate_by_input
- (*recommended*) If you are using the live deployed site pages, use this link: https://validator.w3.org/#validate_by_uri

It's recommended to validate the live pages (each of them) using the deployed URL.
This will give you a custom URL as well, which you can use on your testing documentation.
It makes it easier to return back to a page to validate it again in the future.
The URL will look something like this:

- https://validator.w3.org/nu/?doc=https%3A%2F%2FEfthymiaKakoulidou.github.io%2Fproject-management-tool%2Findex.html

Sample HTML code validation documentation (tables are extremely helpful!):

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FEfthymiaKakoulidou.github.io%2Fproject-management-tool%2Findex.html) | ![screenshot](documentation/html-validation-home.png) | Section lacks header h2-h6 warning |
| Login | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FEfthymiaKakoulidou.github.io%2Fproject-management-tool%2Fcontact.html) | ![screenshot](documentation/html-validation-login.png) | obsolete iframe warnings |
| Signup | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FEfthymiaKakoulidou.github.io%2Fproject-management-tool%2Fquiz.html) | ![screenshot](documentation/html-validation-signup.png) | Pass: No Errors |
| My Projects | n/a | ![screenshot](documentation/html-validation-myprojects.png) | Duplicate IDs found, and fixed |
| My Tasks | n/a | ![screenshot](documentation/html-validation-mytasks.png) | Pass: No Errors |
| New Project | n/a | ![screenshot](documentation/html-validation-newproject.png) | Pass: No Errors |
| My Profile Add | n/a | ![screenshot](documentation/html-validation-addprofile.png) | Pass: No Errors |
| My Profile | n/a | ![screenshot](documentation/html-validation-profiledetail.png) | Pass: No Errors |
| Members | n/a | ![screenshot](documentation/html-validation-profiles.png) | Pass: No Errors |
| Project details | n/a | ![screenshot](documentation/html-validation-projectdetail.png) | Pass: No Errors |
| Edit Project | n/a | ![screenshot](documentation/html-validation-editproject.png) | Pass: No Errors |
| Delete Project | n/a | ![screenshot](documentation/html-validation-deleteproject.png) | Pass: No Errors |
| Task detail | n/a | ![screenshot](documentation/html-validation-taskdetail.png) | Pass: No Errors |
| Edit Task | n/a | ![screenshot](documentation/html-validation-edittask.png) | Pass: No Errors |
| Delete Task | n/a | ![screenshot](documentation/html-validation-deletetask.png) | Pass: No Errors |
| Update Status | n/a | ![screenshot](documentation/html-validation-updatestatus.png) | Pass: No Errors |
| Profiles details | n/a | ![screenshot](documentation/html-validation-profiles.png) | Pass: No Errors |


🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

**IMPORTANT**: Python/Jinja syntax in HTML


In order to properly validate these types of files, it's recommended to
[validate by uri](https://validator.w3.org/#validate_by_uri) from the deployed Heroku pages.

Unfortunately, pages that require a user to be logged-in and authenticated (CRUD functionality),
will not work using this method, due to the fact that the HTML Validator (W3C) doesn't have
access to login to your pages.
In order to properly validate HTML pages with Jinja syntax for authenticated pages, follow these steps:

- Navigate to the deployed pages which require authentication
- Right-click anywhere on the page, and select **View Page Source** (usually `CTRL+U` or `⌘+U` on Mac).
- This will display the entire "compiled" code, without any Jinja syntax.
- Copy everything, and use the [validate by input](https://validator.w3.org/#validate_by_input) method.
- Repeat this process for every page that requires a user to be logged-in/authenticated.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- If you are copying/pasting your HTML code, use this link: https://jigsaw.w3.org/css-validator/#validate_by_input
- (*recommended*) If you are using the live deployed site, use this link: https://jigsaw.w3.org/css-validator/#validate_by_uri

It's recommended to validate the live site if you only have a single CSS file using the deployed URL.
This will give you a custom URL as well, which you can use on your testing documentation.
It makes it easier to return back to the page to validate it again in the future.
The URL will look something like this:

- https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2FEfthymiaKakoulidou.github.io%2Fproject-management-tool

If you have multiple CSS files, then individual [validation by input](https://jigsaw.w3.org/css-validator/#validate_by_input)
is recommended for the additional CSS files.

**IMPORTANT**: Third-Party tools

If you're using extras like Bootstrap, Materialize, Font Awesome, then sometimes the validator
will attempt to also validate this code, even if it's not part of your own actual code.
You are not required to validate the external libraries or frameworks!

Sample CSS code validation documentation (tables are extremely helpful!):

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2FEfthymiaKakoulidou.github.io%2Fproject-management-tool) | ![screenshot](documentation/css-validation-style.png) | Pass: No Errors |
| checkout.css | n/a | ![screenshot](documentation/css-validation-checkout.png) | Pass: No Errors |
| x | x | x | repeat for all remaining CSS files |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

If using modern JavaScript (ES6) methods, then make sure to include the following
line at the very top of every single JavaScript file (this should remain in your files for submission):

    /* jshint esversion: 11 */

If you are also including jQuery (`$`), then the updated format will be:

    /* jshint esversion: 11, jquery: true */

This allows the JShint validator to recognize modern ES6 methods, such as:
`let`, `const`, `template literals`, `arrow functions (=>)`, etc.

**IMPORTANT**: External resources

Sometimes we'll write JavaScript that imports variables from other files, such as an array of questions
from `questions.js`, which are used within the main `script.js` file elsewhere.
If that's the case, the JShint validation tool doesn't know how to recognize unused variables
that would normally be imported locally in your code.
These warnings are acceptable to showcase on your screenshots.

The same thing applies when using external libraries such as Stripe, Leaflet, Bootstrap, Materialize, etc..
To instantiate these components, we need to use their respective declarator.
Again, the JShint validation tool would flag these as undefined/unused variables.
These warnings are acceptable to showcase on your screenshots.

Sample JS code validation documentation (tables are extremely helpful!):

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| File | Screenshot | Notes |
| --- | --- | --- |
| script.js | ![screenshot](documentation/js-validation-script.png) | Unused variables from external files |
| questions.js | ![screenshot](documentation/js-validation-questions.png) | Pass: No Errors |
| quiz.js | ![screenshot](documentation/js-validation-quiz.png) | Unused variables from external files |
| stripe_elements.js | ![screenshot](documentation/js-validation-stripe.png) | Undefined Stripe variable |
| x | x | x | repeat for all remaining JavaScript files |

### Python

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

The CI Python Linter can be used two different ways.
- Copy/Paste your Python code directly into the linter.
- As an API, using the "raw" URL appended to the linter URL.
    - To find the "raw" URL, navigate to your file directly on the GitHub repo.
    - On that page, GitHub provides a button on the right called "Raw" that you can click on.
    - From that new page, copy the full URL, and paste it after the CI Python Linter URL (with a `/` separator).
    - Check the example table below for a live demo.

It's recommended to validate each file using the API URL.
This will give you a custom URL which you can use on your testing documentation.
It makes it easier to return back to a file to validate it again in the future.
Use the steps above to generate your own custom URLs for each Python file.

**IMPORTANT**: `E501 line too long` errors

You must strive to fix any Python lines that are too long ( >80 characters ).
In rare cases where you cannot break the lines [without breaking the functionality],
then by adding `# noqa` to the end of those lines will ignore linting validation.

`# noqa` = **NO Quality Assurance**

**NOTE**: You must include 2 *spaces* before the `#`, and 1 *space* after the `#`.

Do not use `# noqa` all over your project just to clear down validation errors!
This can still cause a project to fail, for failing to fix actual PEP8 validation errors.

Sometimes strings or variables get too long, or long `if` conditional statements.
These are acceptable instances to use the `# noqa`.

When trying to fix "line too long" errors, try to avoid using `/` to split lines.
A better approach would be to use any type of opening bracket, and hit Enter just after that.

Any opening bracket type will work: `(`, `[`, `{`.

By using an opening bracket, Python knows where to appropriately indent the next line of code,
without having to "guess" yourself and attempt to tab to the correct indentation level.

Sample Python code validation documentation below (tables are extremely helpful!).

**Note**: This gives examples of PP3 (Python-only), and Flask/Django files, so eliminate the ones not applicable to your own project.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EfthymiaKakoulidou/project-management-tool/main/run.py) | ![screenshot](documentation/py-validation-run.png) | W291 trailing whitespace |
| settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EfthymiaKakoulidou/project-management-tool/main/boutique-ado/settings.py) | ![screenshot](documentation/py-validation-settings.png) | E501 line too long |
| Blog views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EfthymiaKakoulidou/project-management-tool/main/blog/views.py) | ![screenshot](documentation/py-validation-blog-views.png) | Pass: No Errors |
| Checkout urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EfthymiaKakoulidou/project-management-tool/main/checkout/urls.py) | ![screenshot](documentation/py-validation-checkout-urls.png) | W292 no newline at end of file |
| Profiles models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EfthymiaKakoulidou/project-management-tool/main/profiles/models.py) | ![screenshot](documentation/py-validation-profiles-models.png) | Pass: No Errors |
| x | x | x | repeat for all remaining Python files |

**IMPORTANT**: Django settings.py

The Django settings.py file comes with 4 lines that are quite long, and will throw the `E501 line too long` error.
This is default behavior, but can be fixed by adding `# noqa` to the end of those lines.

Example:

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]
```

**IMPORTANT**: migration and pycache files

You do not have to ever validate files from the `migrations/` or `pycache/` folders!
Ignore these `.py` files, and validate just the files that you've created or modified.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browser-chrome-home.png) | ![screenshot](documentation/browser-chrome-login.png) | ![screenshot](documentation/browser-chrome-signup.png) |![screenshot](documentation/browser-chrome-signout.png) | ![screenshot](documentation/browser-chrome-myprojects.png) | ![screenshot](documentation/browser-chrome-mytasks.png) | ![screenshot](documentation/browser-chrome-newproject.png) | ![screenshot](documentation/browser-chrome-myprofileadd.png) | ![screenshot](documentation/browser-chrome-myprofile.png) | ![screenshot](documentation/browser-chrome-profiles.png) | ![screenshot](documentation/browser-chrome-profiledetail.png) | ![screenshot](documentation/browser-chrome-editproject.png) | ![screenshot](documentation/browser-chrome-deleteproject.png) | ![screenshot](documentation/browser-chrome-addtask.png) |![screenshot](documentation/browser-chrome-taskdetail.png) | ![screenshot](documentation/browser-chrome-edittask.png) | ![screenshot](documentation/browser-chrome-deletetask.png) | ![screenshot](documentation/browser-chrome-editprofile.png) | ![screenshot](documentation/browser-chrome-deleteprofile.png) | Works as expected |
| Firefox | ![screenshot](documentation/browser-firefox-home.png) | ![screenshot](documentation/browser-firefox-login.png) | ![screenshot](documentation/browser-firefox-signup.png) |![screenshot](documentation/browser-firefox-signout.png) | ![screenshot](documentation/browser-firefox-myprojects.png) | ![screenshot](documentation/browser-firefox-mytasks.png) | ![screenshot](documentation/browser-firefox-newproject.png) | ![screenshot](documentation/browser-firefox-myprofileadd.png) | ![screenshot](documentation/browser-firefox-myprofile.png) | ![screenshot](documentation/browser-firefox-profiles.png) | ![screenshot](documentation/browser-firefox-profiledetail.png) | ![screenshot](documentation/browser-firefox-editproject.png) | ![screenshot](documentation/browser-firefox-deleteproject.png) | ![screenshot](documentation/browser-firefox-addtask.png) |![screenshot](documentation/browser-firefox-taskdetail.png) | ![screenshot](documentation/browser-firefox-edittask.png) | ![screenshot](documentation/browser-firefox-deletetask.png) | ![screenshot](documentation/browser-firefox-editprofile.png) | ![screenshot](documentation/browser-firefox-deleteprofile.png) | Works as expected |
| Edge | ![screenshot](documentation/browser-edge-home.png) | ![screenshot](documentation/browser-edge-login.png) | ![screenshot](documentation/browser-edge-signup.png) |![screenshot](documentation/browser-chrome-signout.png) | ![screenshot](documentation/browser-edge-myprojects.png) | ![screenshot](documentation/browser-edge-mytasks.png) | ![screenshot](documentation/browser-edge-newproject.png) | ![screenshot](documentation/browser-edge-myprofileadd.png) | ![screenshot](documentation/browser-edge-myprofile.png) | ![screenshot](documentation/browser-edge-profiles.png) | ![screenshot](documentation/browser-edge-profiledetail.png) | ![screenshot](documentation/browser-edge-editproject.png) | ![screenshot](documentation/browser-edge-deleteproject.png) | ![screenshot](documentation/browser-edge-addtask.png) | ![screenshot](documentation/browser-edge-taskdetail.png) |![screenshot](documentation/browser-edge-edittask.png) | ![screenshot](documentation/browser-edge-deletetask.png) | ![screenshot](documentation/browser-edge-editprofile.png) | ![screenshot](documentation/browser-edge-deleteprofile.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsive-mobile-home.png) | ![screenshot](documentation/responsive-mobile-login.png) | ![screenshot](documentation/responsive-mobile-signup.png) | ![screenshot](documentation/responsive-mobile-login.png) | ![screenshot](documentation/responsive-mobile-signout.png) |![screenshot](documentation/responsive-mobile-myprojects.png) |![screenshot](documentation/responsive-mobile-mytasks.png) |![screenshot](documentation/responsive-mobile-myprofileadd.png) |![screenshot](documentation/responsive-mobile-myprofile.png) |![screenshot](documentation/responsive-mobile-profiles.png) |![screenshot](documentation/responsive-mobile-profiledetail.png) |![screenshot](documentation/responsive-mobile-editproject.png) |![screenshot](documentation/responsive-mobile-deleteproject.png) |![screenshot](documentation/responsive-mobile-addtask.png) |![screenshot](documentation/responsive-mobile-taskdetail.png) |![screenshot](documentation/responsive-mobile-edittask.png) |![screenshot](documentation/responsive-mobile-deletetask.png) |![screenshot](documentation/responsive-mobile-editprofile.png) |![screenshot](documentation/responsive-mobile-deleteprofile.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsive-tablet-home.png) | ![screenshot](documentation/responsive-tablet-login.png) | ![screenshot](documentation/responsive-tablet-signup.png) | ![screenshot](documentation/responsive-tablet-signout.png) | ![screenshot](documentation/responsive-tablet-myprojects.png) |![screenshot](documentation/responsive-tablet-mytasks.png) |![screenshot](documentation/responsive-tablet-myprofileadd.png) |![screenshot](documentation/responsive-tablet-myprofile.png) |![screenshot](documentation/responsive-tablet-profiles.png) |![screenshot](documentation/responsive-tablet-profiledetail.png) |![screenshot](documentation/responsive-tablet-editproject.png) |![screenshot](documentation/responsive-tablet-deleteproject.png) |![screenshot](documentation/responsive-tablet-addtask.png) |![screenshot](documentation/responsive-tablet-taskdetail.png) |![screenshot](documentation/responsive-tablet-edittask.png) |![screenshot](documentation/responsive-tablet-deletetask.png) |![screenshot](documentation/responsive-tablet-editprofile.png) |![screenshot](documentation/responsive-tablet-deleteprofile.png) | Works as expected |
| Desktop (DevTools) | ![screenshot](documentation/responsive-desktop-home.png) | ![screenshot](documentation/responsive-desktop-login.png) | ![screenshot](documentation/responsive-desktop-signup.png) | ![screenshot](documentation/responsive-desktop-signout.png)  ![screenshot](documentation/responsive-desktop-myprojects.png) |![screenshot](documentation/responsive-desktop-mytasks.png) |![screenshot](documentation/responsive-desktop-myprofileadd.png) |![screenshot](documentation/responsive-desktop-myprofile.png) |![screenshot](documentation/responsive-desktop-profiles.png) |![screenshot](documentation/responsive-desktop-profiledetail.png) |![screenshot](documentation/responsive-desktop-editproject.png) |![screenshot](documentation/responsive-desktop-deleteproject.png) |![screenshot](documentation/responsive-desktop-addtask.png) |![screenshot](documentation/responsive-desktop-taskdetail.png) |![screenshot](documentation/responsive-desktop-edittask.png) |![screenshot](documentation/responsive-desktop-deletetask.png) |![screenshot](documentation/responsive-desktop-editprofile.png) |![screenshot](documentation/responsive-desktop-deleteprofile.png) | Works as expected |

## Lighthouse Audit


I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse-home-desktop.png) | no warnings |
| Login | ![screenshot](documentation/lighthouse-login-mobile.png) | ![screenshot](documentation/lighthouse-login-desktop.png) | no warnings |
| Signup | ![screenshot](documentation/lighthouse-signup-mobile.png) | ![screenshot](documentation/lighthouse-signup-desktop.png) | no warnings |
| Signout | ![screenshot](documentation/lighthouse-signout-mobile.png) | ![screenshot](documentation/lighthouse-signout-desktop.png) | no warnings |
| My Projects | ![screenshot](documentation/lighthouse-myprojects-mobile.png) | ![screenshot](documentation/lighthouse-myprojects-desktop.png) | no warnings |
| Project details | ![screenshot](documentation/lighthouse-projectdetail-mobile.png) | ![screenshot](documentation/lighthouse-projectdetail-desktop.png) | no warnings |
| Add Project | ![screenshot](documentation/lighthouse-addproject-mobile.png) | ![screenshot](documentation/lighthouse-addproject-desktop.png) | no warnings |
| Edit Project | ![screenshot](documentation/lighthouse-editproject-mobile.png) | ![screenshot](documentation/lighthouse-editproject-desktop.png) | no warnings |
| Delete Project | ![screenshot](documentation/lighthouse-deleteproject-mobile.png) | ![screenshot](documentation/lighthouse-deleteproject-desktop.png) | no warnings |
| My Tasks | ![screenshot](documentation/lighthouse-mytasks-mobile.png) | ![screenshot](documentation/lighthouse-mytasks-desktop.png) | no warnings |
| Task details | ![screenshot](documentation/lighthouse-taskdetail-mobile.png) | ![screenshot](documentation/lighthouse-taskdetail-desktop.png) | no warnings |
| Add Task | ![screenshot](documentation/lighthouse-addtask-mobile.png) | ![screenshot](documentation/lighthouse-addtask-desktop.png) | no warnings |
| Edit Task | ![screenshot](documentation/lighthouse-edittask-mobile.png) | ![screenshot](documentation/lighthouse-edittask-desktop.png) | no warnings |
| Update Task Status | ![screenshot](documentation/lighthouse-updatetaskstatus-mobile.png) | ![screenshot](documentation/lighthouse-updatetaskstatus-desktop.png) | no warnings |
| Delete Task | ![screenshot](documentation/lighthouse-deletetask-mobile.png) | ![screenshot](documentation/lighthouse-deletetask-desktop.png) | no warnings |
| Profiles | ![screenshot](documentation/lighthouse-profiles-mobile.png) | ![screenshot](documentation/lighthouse-profiles-desktop.png) | no warnings |
| Profile Details | ![screenshot](documentation/lighthouse-profiledetail-mobile.png) | ![screenshot](documentation/lighthouse-profiledetail-desktop.png) | no warnings |
| Add Profile | ![screenshot](documentation/lighthouse-addprofile-mobile.png) | ![screenshot](documentation/lighthouse-addprofile-desktop.png) | no warnings |
| Edit Profile | ![screenshot](documentation/lighthouse-editprofile-mobile.png) | ![screenshot](documentation/lighthouse-editprofile-desktop.png) | no warnings |
| Delete Profile | ![screenshot](documentation/lighthouse-deleteprofile-mobile.png) | ![screenshot](documentation/lighthouse-deleteprofile-desktop.png) | no warnings |

## Defensive Programming

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Signup feature is expected to create a user when the form is filled successfully | Tested the feature filling the form | The feature behaved as expected, and created a user | Test concluded and passed | ![screenshot](documentation/feature01.png) |
| | Login feature is expected to login an existing user when the user fills the form| Tested the feature by filling the form | The feature behaved as expected, and logged in the user | Test concluded and passed | ![screenshot](documentation/feature02.png) |
| | Signout feature is expected to logout the user when the user confirms signout| Tested the feature by confirming sign out | The feature behaved as expected, and signed the user out | Test concluded and passed | ![screenshot](documentation/feature02.png) |
| My Projects | | | | | |
| | My projects' cards are expected to redirect the user to the project's details when the user clicks on them. | Tested the feature by clicking one of them | The feature behaved as expected and led me to the project's details page | Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | Project details page is expected to have the edit/delete buttons if the user is the creator of the project | Tested the feature by clicking a project I created | The feature behaved as expected and showed the buttons | Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | Project details page is expected not to have the edit/delete buttons if the user is not the creator of the project | Tested the feature by clicking a project I did not creat | The feature behaved as expected and did not show the buttons | Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | Edit Project page is expected to have a filled form with the details of the project for editing the project | Tested the feature by editing the details | The feature behaved as expected and edited the project | Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | Delete confirmation page is expected to delete the project when the user clicks on confirm | Tested the feature by clicking the button | The feature behaved as expected and deleted the project | Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | New Project page is expected to have a form for the creation of a project | Tested the feature by filling the form | The feature behaved as expected and created a project | Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | Add Task button is expected to add a task to the project associated to it | Tested the feature by clicking the Add Task button| The feature behaved as expected and directed me to the Add Task form| Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | Add Task form is expected to add a task to the project associated to it | Tested the feature by filling the form| The feature behaved as expected and created a task| Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | Update status of the task is expected to update the status of this particular task | Tested the feature by changinf the status | The feature behaved as expected and updated status of the task| Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | Edit Task form is expected to edit the task | Tested the feature by editing the details on the form| The feature behaved as expected and edited the task| Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | Task delete confirmation is expected to delete the task when the user clicks the button | Tested the feature by clicking the button to confirm deletion| The feature behaved as expected and deleted the task| Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | My Profile is expected to lead to the Add Profile form if the user does not have a profile or to the his/hers profile page if he/she have alreadya profile | Tested the feature by clicking on My Profile one time when I had a profile and one time if when I had not| The feature behaved as expected and led me to the respective page| Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | Add Profile is expected to add a profile for the user when the user fills the form successfully | Tested the feature by filling the form | The feature behaved as expected and created my profile | Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | Edit Profile is expected to show the form with the information of the profile to be able to edit it | Tested the feature by editing the information | The feature behaved as expected and edited my profile | Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | Profile delete confirm is expected to delete the profile if the user confirms it | Tested the feature by clicking on the confirm button | The feature behaved as expected and deleted my profile | Test concluded and passed | ![screenshot](documentation/feature03.png) |



🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Another way of performing defensive testing is a simple Pass/Fail for each test.
The assessors prefer the above method, with the full test explained, but this is also acceptable in most cases.

When in doubt, use the above method instead, and delete the table below.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| repeat for all remaining pages | x | x | x | x |


## User Story Testing


| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to sign up, so that I can enter the site. | ![screenshot](documentation/feature01.png) |
| As a new site user, I would like to create a project, so that I can start organizing my work. | ![screenshot](documentation/feature02.png) |
| As a new site user, I would like to create tasks for my projects, so that I can organize them into smaller segments. | ![screenshot](documentation/feature03.png) |
| As a new site user, I would like to assign tasks to others, so that I can delegate my work. | ![screenshot](documentation/feature03.png) |
| As a new site user, I would like to create my profile, so that others can see my information. | ![screenshot](documentation/feature03.png) |
| As a new site user, I would like to sign out, so that my work and my information are secure. | ![screenshot](documentation/feature03.png) |
| As a returning site user, I would like to login , so that I can have access to my previous work. | ![screenshot](documentation/feature04.png) |
| As a returning site user, I would like to create new projects and edit or delete me projects, so that I can update the information of my work. | ![screenshot](documentation/feature05.png) |
| As a returning site user, I would like to create, edit or delete tasks to the projects I have created, so that I can update the information of my work. | ![screenshot](documentation/feature05.png) |
| As a returning site user, I would like to edit or delete my profile, so that I can update my information. | ![screenshot](documentation/feature05.png) |
| As a returning site user, I would like to sign out, so that my work and information are secure. | ![screenshot](documentation/feature05.png) |

| As a site administrator, I should be able to see, create, edit and delete all the projects, tasks and profiles on the site, so that I can control the information on the site. | ![screenshot](documentation/feature07.png) |


## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### JavaScript (Jest Testing)

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I have used the [Jest](https://jestjs.io) JavaScript testing framework to test the application functionality.

In order to work with Jest, I first had to initialize NPM.

- `npm init`
- Hit `enter` for all options, except for **test command:**, just type `jest`.

Add Jest to a list called **Dev Dependencies** in a dev environment:

- `npm install --save-dev jest`

**IMPORTANT**: Initial configurations

When creating test files, the name of the file needs to be `file-name.test.js` in order for Jest to properly work.

Without the following, Jest won't properly run the tests:

- `npm install -D jest-environment-jsdom`

Due to a change in Jest's default configuration, you'll need to add the following code to the top of the `.test.js` file:

```js
/**
 * @jest-environment jsdom
 */

const { test, expect } = require("@jest/globals");
const { function1, function2, function3, etc. } = require("../script-name");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("index.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});
```

Remember to adjust the `fs.readFileSync()` to the specific file you'd like you test.
The example above is testing the `index.html` file.

Finally, at the bottom of the script file where your primary scripts are written, include the following at the bottom of the file.
Make sure to include the name of all of your functions that are being tested in the `.test.js` file.

```js
if (typeof module !== "undefined") module.exports = {
    function1, function2, function3, etc.
};
```

Now that these steps have been undertaken, further tests can be written, and be expected to fail initially.
Write JS code that can get the tests to pass as part of the Red-Green refactor process.

Once ready, to run the tests, use this command:

- `npm test`

**NOTE**: To obtain a coverage report, use the following command:

- `npm test --coverage`

Below are the results from the tests that I've written for this application:

| Test Suites | Tests | Screenshot |
| --- | --- | --- |
| 1 passed | 16 passed | ![screenshot](documentation/js-test-coverage.png) |
| x | x | repeat for all remaining tests |

#### Jest Test Issues

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this section to list any known issues you ran into while writing your Jest tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

### Python (Unit Testing)

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## Bugs

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/EfthymiaKakoulidou/project-management-tool/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/EfthymiaKakoulidou/project-management-tool/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/EfthymiaKakoulidou/project-management-tool/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/EfthymiaKakoulidou/project-management-tool/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/EfthymiaKakoulidou/project-management-tool/issues/3) | Closed |

**Open Issues**

Any remaining open issues can be tracked [here](https://github.com/EfthymiaKakoulidou/project-management-tool/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/EfthymiaKakoulidou/project-management-tool/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/EfthymiaKakoulidou/project-management-tool/issues/5) | Open |

## Unfixed Bugs

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

There are no remaining bugs that I am aware of.
