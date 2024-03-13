# Testing

Return back to the [README.md](README.md) file.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

In this section, you need to convince the assessors that you have conducted enough testing to legitimately believe that the site works well.
Essentially, in this part, you should go over all of your project's features, and ensure that they all work as intended,
with the project providing an easy and straightforward way for the users to achieve their goals.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| project_manager | add_profile.html | ![screenshot](documentation/validation/addprofile.jpg) | |
| project_manager | add_project.html | ![screenshot](documentation/validation/addproject.jpg) | |
| project_manager | add_task.html | ![screenshot](documentation/validation/addtask.jpg) | |
| project_manager | edit_profile.html | ![screenshot](documentation/validation/editprofile.jpg) | |
| project_manager | edit_project.html | ![screenshot](documentation/validation/editproject.jpg) | |
| project_manager | edit_task.html | ![screenshot](documentation/validation/edittask.jpg) | |
| project_manager | edit_task_status.html | ![screenshot](documentation/validation/edittaskstatus.jpg) | |
| project_manager | home.html | ![screenshot](documentation/validation/home.jpg) | |
| project_manager | my_tasks.html | ![screenshot](documentation/validation/mytasks.jpg) | |
| project_manager | profile_confirm_delete.html | ![screenshot](documentation/validation/profileconfirmdelete.jpg) | |
| project_manager | profile_detail.html | ![screenshot](documentation/validation/profiledetail.jpg) | |
| project_manager | profiles.html | ![screenshot](documentation/validation/profiles.jpg) | |
| project_manager | project_confirm_delete.html | ![screenshot](documentation/validation/projectconfirmdelete.jpg) | |
| project_manager | project_detail.html | ![screenshot](documentation/validation/path-to-screenshot.jpg) | |
| project_manager | projects.html | ![screenshot](documentation/validation/projectdetail.jpg) | |
| project_manager | task_confirm_delete.html | ![screenshot](documentation/validation/taskconfirmdelete.jpg) | |
| project_manager | task_detail.html | ![screenshot](documentation/validation/taskdetail.jpg) | |
| templates | 403.html | ![screenshot](documentation/validation/403.jpg) | |
| templates | base.html | ![screenshot](documentation/validation/base.jpg) | |

            
### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | base.css | ![screenshot](documentation/validation/css.jpg) | |

            
### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | script.js | ![screenshot](documentation/validation/script.jpg) | |

            
### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EfthymiaKakoulidou/project-management-tool/main/manage.py) | ![screenshot](documentation/validation/manage.jpg) | |
| my_project | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EfthymiaKakoulidou/project-management-tool/main/my_project/settings.py) | ![screenshot](documentation/validation/settings.jpg) | |
| my_project | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EfthymiaKakoulidou/project-management-tool/main/my_project/urls.py) | ![screenshot](documentation/validation/myprojecturls.jpg) | |
| project_manager | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EfthymiaKakoulidou/project-management-tool/main/project_manager/admin.py) | ![screenshot](documentation/validation/admin.jpg) | |
| project_manager | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EfthymiaKakoulidou/project-management-tool/main/project_manager/forms.py) | ![screenshot](documentation/validation/forms.jpg) | |
| project_manager | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EfthymiaKakoulidou/project-management-tool/main/project_manager/models.py) | ![screenshot](documentation/validation/models.jpg) | |
| project_manager | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EfthymiaKakoulidou/project-management-tool/main/project_manager/urls.py) | ![screenshot](documentation/validation/projectmanagerurls.jpg) | |
| project_manager | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/EfthymiaKakoulidou/project-management-tool/main/project_manager/views.py) | ![screenshot](documentation/validation/views.jpg) | |


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browser-chrome-home.jpg) | ![screenshot](documentation/browser-chrome-login.jpg) | ![screenshot](documentation/browser-chrome-signup.jpg) |![screenshot](documentation/browser-chrome-signout.jpg) | ![screenshot](documentation/browser-chrome-myprojects.jpg) | ![screenshot](documentation/browser-chrome-mytasks.jpg) | ![screenshot](documentation/browser-chrome-newproject.jpg) | ![screenshot](documentation/browser-chrome-myprofileadd.jpg) | ![screenshot](documentation/browser-chrome-myprofile.jpg) | ![screenshot](documentation/browser-chrome-profiles.jpg) | ![screenshot](documentation/browser-chrome-profiledetail.jpg) | ![screenshot](documentation/browser-chrome-editproject.jpg) | ![screenshot](documentation/browser-chrome-deleteproject.jpg) | ![screenshot](documentation/browser-chrome-addtask.jpg) |![screenshot](documentation/browser-chrome-taskdetail.jpg) | ![screenshot](documentation/browser-chrome-edittask.jpg) | ![screenshot](documentation/browser-chrome-deletetask.jpg) | ![screenshot](documentation/browser-chrome-editprofile.jpg) | ![screenshot](documentation/browser-chrome-deleteprofile.jpg) | Works as expected |
| Firefox | ![screenshot](documentation/browser-firefox-home.jpg) | ![screenshot](documentation/browser-firefox-login.jpg) | ![screenshot](documentation/browser-firefox-signup.jpg) |![screenshot](documentation/browser-firefox-signout.jpg) | ![screenshot](documentation/browser-firefox-myprojects.jpg) | ![screenshot](documentation/browser-firefox-mytasks.jpg) | ![screenshot](documentation/browser-firefox-newproject.jpg) | ![screenshot](documentation/browser-firefox-myprofileadd.jpg) | ![screenshot](documentation/browser-firefox-myprofile.jpg) | ![screenshot](documentation/browser-firefox-profiles.jpg) | ![screenshot](documentation/browser-firefox-profiledetail.jpg) | ![screenshot](documentation/browser-firefox-editproject.jpg) | ![screenshot](documentation/browser-firefox-deleteproject.jpg) | ![screenshot](documentation/browser-firefox-addtask.jpg) |![screenshot](documentation/browser-firefox-taskdetail.jpg) | ![screenshot](documentation/browser-firefox-edittask.jpg) | ![screenshot](documentation/browser-firefox-deletetask.jpg) | ![screenshot](documentation/browser-firefox-editprofile.jpg) | ![screenshot](documentation/browser-firefox-deleteprofile.jpg) | Works as expected |
| Edge | ![screenshot](documentation/browser-edge-home.jpg) | ![screenshot](documentation/browser-edge-login.jpg) | ![screenshot](documentation/browser-edge-signup.jpg) |![screenshot](documentation/browser-chrome-signout.jpg) | ![screenshot](documentation/browser-edge-myprojects.jpg) | ![screenshot](documentation/browser-edge-mytasks.jpg) | ![screenshot](documentation/browser-edge-newproject.jpg) | ![screenshot](documentation/browser-edge-myprofileadd.jpg) | ![screenshot](documentation/browser-edge-myprofile.jpg) | ![screenshot](documentation/browser-edge-profiles.jpg) | ![screenshot](documentation/browser-edge-profiledetail.jpg) | ![screenshot](documentation/browser-edge-editproject.jpg) | ![screenshot](documentation/browser-edge-deleteproject.jpg) | ![screenshot](documentation/browser-edge-addtask.jpg) | ![screenshot](documentation/browser-edge-taskdetail.jpg) |![screenshot](documentation/browser-edge-edittask.jpg) | ![screenshot](documentation/browser-edge-deletetask.jpg) | ![screenshot](documentation/browser-edge-editprofile.jpg) | ![screenshot](documentation/browser-edge-deleteprofile.jpg) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Home after login | Login | Signup | Signout | My Projects | My Tasks | New Project | My Profile (add) | My profile | Members | Profile detail | Edi Project | Delete Project | Add Task | Task Detail | Edit Task | Delete Task | Update Task Status | Edit Profile | Delete Profile | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsive-mobile-home.jpg) | ![screenshot](documentation/responsive-mobile-login.jpg) | ![screenshot](documentation/responsive-mobile-signup.jpg) | ![screenshot](documentation/responsive-mobile-login.jpg) | ![screenshot](documentation/responsive-mobile-signout.jpg) | ![screenshot](documentation/responsive-mobile-myprojects.jpg) | ![screenshot](documentation/responsive-mobile-mytasks.jpg) | ![screenshot](documentation/responsive-mobile-myprofileadd.jpg) | ![screenshot](documentation/responsive-mobile-myprofile.jpg) | ![screenshot](documentation/responsive-mobile-profiles.jpg) | ![screenshot](documentation/responsive-mobile-profiledetail.jpg) | ![screenshot](documentation/responsive-mobile-editproject.jpg) | ![screenshot](documentation/responsive-mobile-deleteproject.jpg) | ![screenshot](documentation/responsive-mobile-addtask.jpg) | ![screenshot](documentation/responsive-mobile-taskdetail.jpg) | ![screenshot](documentation/responsive-mobile-edittask.jpg) | ![screenshot](documentation/responsive-mobile-deletetask.jpg) | ![screenshot](documentation/responsive-mobile-editprofile.jpg) | ![screenshot](documentation/responsive-mobile-deleteprofile.jpg) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsive-tablet-home.jpg) | ![screenshot](documentation/responsive-tablet-login.jpg) | ![screenshot](documentation/responsive-tablet-signup.jpg) | ![screenshot](documentation/responsive-tablet-signout.jpg) | ![screenshot](documentation/responsive-tablet-myprojects.jpg) |![screenshot](documentation/responsive-tablet-mytasks.jpg) |![screenshot](documentation/responsive-tablet-myprofileadd.jpg) | ![screenshot](documentation/responsive-tablet-myprofile.jpg) | ![screenshot](documentation/responsive-tablet-profiles.jpg) | ![screenshot](documentation/responsive-tablet-profiledetail.jpg) | ![screenshot](documentation/responsive-tablet-editproject.jpg) |![screenshot](documentation/responsive-tablet-deleteproject.jpg) | ![screenshot](documentation/responsive-tablet-addtask.jpg) | ![screenshot](documentation/responsive-tablet-taskdetail.jpg) | ![screenshot](documentation/responsive-tablet-edittask.jpg) | ![screenshot](documentation/responsive-tablet-deletetask.jpg) | ![screenshot](documentation/responsive-tablet-editprofile.jpg) | ![screenshot](documentation/responsive-tablet-deleteprofile.jpg) | Works as expected |
| Desktop (DevTools) | ![screenshot](documentation/responsive-desktop-home.jpg) | ![screenshot](documentation/responsive-desktop-home2.jpg) | ![screenshot](documentation/responsive-desktop-login.jpg) | ![screenshot](documentation/responsive-desktop-signup.jpg) | ![screenshot](documentation/responsive-desktop-signout.jpg) | ![screenshot](documentation/responsive-desktop-myprojects.jpg) | ![screenshot](documentation/responsive-desktop-mytasks.jpg) | ![screenshot](documentation/responsive-desktop-newproject.jpg) | ![screenshot](documentation/responsive-desktop-myprofileadd.jpg) |![screenshot](documentation/responsive-desktop-myprofile.jpg) | ![screenshot](documentation/responsive-desktop-profiles.jpg) | ![screenshot](documentation/responsive-desktop-profiledetail.jpg) | ![screenshot](documentation/responsive-desktop-editproject.jpg) | ![screenshot](documentation/responsive-desktop-deleteproject.jpg) |![screenshot](documentation/responsive-desktop-addtask.jpg) | ![screenshot](documentation/responsive-desktop-taskdetail.jpg) | ![screenshot](documentation/responsive-desktop-edittask.jpg) | ![screenshot](documentation/responsive-desktop-deletetask.jpg) | ![screenshot](documentation/responsive-desktop-updatetaskstatus.jpg) | ![screenshot](documentation/responsive-desktop-editprofile.jpg) | ![screenshot](documentation/responsive-desktop-deleteprofile.jpg) | Works as expected |

## Lighthouse Audit


I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse-home-mobile.jpg) | ![screenshot](documentation/lighthouse-home-desktop.jpg) | no warnings |
| Login | ![screenshot](documentation/lighthouse-login-mobile.jpg) | ![screenshot](documentation/lighthouse-login-desktop.jpg) | no warnings |
| Signup | ![screenshot](documentation/lighthouse-signup-mobile.jpg) | ![screenshot](documentation/lighthouse-signup-desktop.jpg) | no warnings |
| Signout | ![screenshot](documentation/lighthouse-signout-mobile.jpg) | ![screenshot](documentation/lighthouse-signout-desktop.jpg) | no warnings |
| My Projects | ![screenshot](documentation/lighthouse-myprojects-mobile.jpg) | ![screenshot](documentation/lighthouse-myprojects-desktop.jpg) | no warnings |
| Project details | ![screenshot](documentation/lighthouse-projectdetail-mobile.jpg) | ![screenshot](documentation/lighthouse-projectdetail-desktop.jpg) | no warnings |
| Add Project | ![screenshot](documentation/lighthouse-addproject-mobile.jpg) | ![screenshot](documentation/lighthouse-addproject-desktop.jpg) | no warnings |
| Edit Project | ![screenshot](documentation/lighthouse-editproject-mobile.jpg) | ![screenshot](documentation/lighthouse-editproject-desktop.jpg) | no warnings |
| Delete Project | ![screenshot](documentation/lighthouse-deleteproject-mobile.jpg) | ![screenshot](documentation/lighthouse-deleteproject-desktop.jpg) | no warnings |
| My Tasks | ![screenshot](documentation/lighthouse-mytasks-mobile.jpg) | ![screenshot](documentation/lighthouse-mytasks-desktop.jpg) | no warnings |
| Task details | ![screenshot](documentation/lighthouse-taskdetail-mobile.jpg) | ![screenshot](documentation/lighthouse-taskdetail-desktop.jpg) | no warnings |
| Add Task | ![screenshot](documentation/lighthouse-addtask-mobile.jpg) | ![screenshot](documentation/lighthouse-addtask-desktop.jpg) | no warnings |
| Edit Task | ![screenshot](documentation/lighthouse-edittask-mobile.jpg) | ![screenshot](documentation/lighthouse-edittask-desktop.jpg) | no warnings |
| Update Task Status | ![screenshot](documentation/lighthouse-updatetaskstatus-mobile.jpg) | ![screenshot](documentation/lighthouse-updatetaskstatus-desktop.jpg) | no warnings |
| Delete Task | ![screenshot](documentation/lighthouse-deletetask-mobile.jpg) | ![screenshot](documentation/lighthouse-deletetask-desktop.jpg) | no warnings |
| Profiles | ![screenshot](documentation/lighthouse-profiles-mobile.jpg) | ![screenshot](documentation/lighthouse-profiles-desktop.jpg) | no warnings |
| Profile Details | ![screenshot](documentation/lighthouse-profiledetail-mobile.jpg) | ![screenshot](documentation/lighthouse-profiledetail-desktop.jpg) | no warnings |
| Add Profile | ![screenshot](documentation/lighthouse-addprofile-mobile.jpg) | ![screenshot](documentation/lighthouse-addprofile-desktop.jpg) | no warnings |
| Edit Profile | ![screenshot](documentation/lighthouse-editprofile-mobile.jpg) | ![screenshot](documentation/lighthouse-editprofile-desktop.jpg) | no warnings |
| Delete Profile | ![screenshot](documentation/lighthouse-deleteprofile-mobile.jpg) | ![screenshot](documentation/lighthouse-deleteprofile-desktop.jpg) | no warnings |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Signup feature is expected to create a user when the form is filled successfully | Tested the feature filling the form | The feature behaved as expected, and created a user | Test concluded and passed | ![screenshot](documentation/feature01.jpg) |
| | Login feature is expected to login an existing user when the user fills the form| Tested the feature by filling the form | The feature behaved as expected, and logged in the user | Test concluded and passed | ![screenshot](documentation/feature02.jpg) |
| | Signout feature is expected to logout the user when the user confirms signout| Tested the feature by confirming sign out | The feature behaved as expected, and signed the user out | Test concluded and passed | ![screenshot](documentation/feature03.jpg) |
| My Projects | | | | | |
| | My projects' cards are expected to redirect the user to the project's details when the user clicks on them. | Tested the feature by clicking one of them | The feature behaved as expected and led me to the project's details page | Test concluded and passed | ![screenshot](documentation/feature07.jpg) |
| | Project details page is expected to have the edit/delete buttons if the user is the creator of the project | Tested the feature by clicking a project I created | The feature behaved as expected and showed the buttons | Test concluded and passed | ![screenshot](documentation/feature12.jpg) |
| | Project details page is expected not to have the edit/delete buttons if the user is not the creator of the project | Tested the feature by clicking a project I did not creat | The feature behaved as expected and did not show the buttons | Test concluded and passed | ![screenshot](documentation/feature121.jpg) |
| | Edit Project page is expected to have a filled form with the details of the project for editing the project | Tested the feature by editing the details | The feature behaved as expected and edited the project | Test concluded and passed | ![screenshot](documentation/feature15.jpg) |
| | Delete confirmation page is expected to delete the project when the user clicks on confirm | Tested the feature by clicking the button | The feature behaved as expected and deleted the project | Test concluded and passed | ![screenshot](documentation/feature151.jpg) |
| | New Project page is expected to have a form for the creation of a project | Tested the feature by filling the form | The feature behaved as expected and created a project | Test concluded and passed | ![screenshot](documentation/feature09.jpg) |
| | Add Task button is expected to add a task to the project associated to it | Tested the feature by clicking the Add Task button| The feature behaved as expected and directed me to the Add Task form| Test concluded and passed | ![screenshot](documentation/feature12.jpg) |
| | Add Task form is expected to add a task to the project associated to it | Tested the feature by filling the form| The feature behaved as expected and created a task| Test concluded and passed | ![screenshot](documentation/feature122.jpg) |
| | Update status of the task is expected to update the status of this particular task | Tested the feature by changinf the status | The feature behaved as expected and updated status of the task| Test concluded and passed | ![screenshot](documentation/feature132.jpg) |
| | Edit Task form is expected to edit the task | Tested the feature by editing the details on the form| The feature behaved as expected and edited the task| Test concluded and passed | ![screenshot](documentation/feature14.jpg) |
| | Task delete confirmation is expected to delete the task when the user clicks the button | Tested the feature by clicking the button to confirm deletion| The feature behaved as expected and deleted the task| Test concluded and passed | ![screenshot](documentation/feature141.jpg) |
| | My Profile is expected to lead to the Add Profile form if the user does not have a profile or to the his/hers profile page if he/she have alreadya profile | Tested the feature by clicking on My Profile one time when I had a profile and one time if when I had not| The feature behaved as expected and led me to the respective page| Test concluded and passed | ![screenshot](documentation/feature10.jpg) |
| | Add Profile is expected to add a profile for the user when the user fills the form successfully | Tested the feature by filling the form | The feature behaved as expected and created my profile | Test concluded and passed | ![screenshot](documentation/feature101.jpg) |
| | Edit Profile is expected to show the form with the information of the profile to be able to edit it | Tested the feature by editing the information | The feature behaved as expected and edited my profile | Test concluded and passed | ![screenshot](documentation/feature16.jpg) |
| | Profile delete confirm is expected to delete the profile if the user confirms it | Tested the feature by clicking on the confirm button | The feature behaved as expected and deleted my profile | Test concluded and passed | ![screenshot](documentation/feature161.jpg) |


## User Story Testing


| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to sign up, so that I can enter the site. | ![screenshot](documentation/feature01.jpg) |
| As a new site user, I would like to create a project, so that I can start organizing my work. | ![screenshot](documentation/feature02.jpg) |
| As a new site user, I would like to create tasks for my projects, so that I can organize them into smaller segments. | ![screenshot](documentation/feature03.jpg) |
| As a new site user, I would like to assign tasks to others, so that I can delegate my work. | ![screenshot](documentation/feature03.jpg) |
| As a new site user, I would like to create my profile, so that others can see my information. | ![screenshot](documentation/feature03.jpg) |
| As a new site user, I would like to sign out, so that my work and my information are secure. | ![screenshot](documentation/feature03.jpg) |
| As a returning site user, I would like to login , so that I can have access to my previous work. | ![screenshot](documentation/feature04.jpg) |
| As a returning site user, I would like to create new projects and edit or delete me projects, so that I can update the information of my work. | ![screenshot](documentation/feature05.jpg) |
| As a returning site user, I would like to create, edit or delete tasks to the projects I have created, so that I can update the information of my work. | ![screenshot](documentation/feature05.jpg) |
| As a returning site user, I would like to edit or delete my profile, so that I can update my information. | ![screenshot](documentation/feature05.jpg) |
| As a returning site user, I would like to sign out, so that my work and information are secure. | ![screenshot](documentation/feature05.jpg) |

| As a site administrator, I should be able to see, create, edit and delete all the projects, tasks and profiles on the site, so that I can control the information on the site. | ![screenshot](documentation/feature07.jpg) |


## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### JavaScript (Jest Testing)

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
| 1 passed | 16 passed | ![screenshot](documentation/js-test-coverage.jpg) |
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
| Bag | test_forms.py | 99% | ![screenshot](documentation/py-test-bag-forms.jpg) |
| Bag | test_models.py | 89% | ![screenshot](documentation/py-test-bag-models.jpg) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/py-test-bag-urls.jpg) |
| Bag | test_views.py | 71% | ![screenshot](documentation/py-test-bag-views.jpg) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/py-test-checkout-forms.jpg) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/py-test-checkout-models.jpg) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/py-test-checkout-urls.jpg) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/py-test-checkout-views.jpg) |
| Home | test_forms.py | 99% | ![screenshot](documentation/py-test-home-forms.jpg) |
| Home | test_models.py | 89% | ![screenshot](documentation/py-test-home-models.jpg) |
| Home | test_urls.py | 100% | ![screenshot](documentation/py-test-home-urls.jpg) |
| Home | test_views.py | 71% | ![screenshot](documentation/py-test-home-views.jpg) |
| Products | test_forms.py | 99% | ![screenshot](documentation/py-test-products-forms.jpg) |
| Products | test_models.py | 89% | ![screenshot](documentation/py-test-products-models.jpg) |
| Products | test_urls.py | 100% | ![screenshot](documentation/py-test-products-urls.jpg) |
| Products | test_views.py | 71% | ![screenshot](documentation/py-test-products-views.jpg) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/py-test-profiles-forms.jpg) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/py-test-profiles-models.jpg) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/py-test-profiles-urls.jpg) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/py-test-profiles-views.jpg) |
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

    ![screenshot](documentation/bug01.jpg)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bug02.jpg)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.jpg)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bug04.jpg)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.jpg)

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

    ![screenshot](documentation/unfixed-bug01.jpg)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/unfixed-bug02.jpg)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/unfixed-bug03.jpg)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

There are no remaining bugs that I am aware of.
