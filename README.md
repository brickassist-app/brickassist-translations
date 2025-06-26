# BrickAssist App - Translations
## Introduction
BrickAssist is a mobile application dedicated to the world of brick building, designed to help users manage their brick inventory efficiently, it also helps users to track the availability of Pick a Brick content around the world, making it easier to find the pieces they need. Available on both Android and iOS, BrickAssist evolves with input from the community to ensure it meets the needs of builders everywhere.

This repository is specifically dedicated to the translations for BrickAssist. It contains the localized files that help bring BrickAssist to users in multiple languages, ensuring a smooth and accessible experience across regions.

For more information about the main project, visit our website: [BrickAssist.com](https://brickassist.com).

## How to Contribute with GitHub interface
### Using GitHub Interface
1. Edit Language Files: Navigate to the language file corresponding to the language you want to contribute to. Language files are typically named with the language code, like app_en.arb for English or app_fr.arb for French.

2. Click the Edit Button: Click the pencil icon (Edit this file) located at the top right corner of the file view.

3. Make Changes: Translate or modify the strings in the file as needed.

4. Propose Changes: After making your modifications, click on the green button 'Commit changes...' in the top right of the page. Provide a brief description of the changes you made in the "Commit message" section.

5. Submit Changes: Click on the "Commit changes" button to submit your modifications as a pull request. Your changes will be reviewed and merged into the main project by the repository maintainers.

### Opening an Issue - easy
1. Go to the Issues Tab: Click on the "Issues" tab located near the top of the repository page.

2. Create a New Issue: Click on the green "New issue" button.

3. Describe Your Contribution: In the issue description, explain the changes you'd like to make, such as adding a new language or suggesting modifications to existing translations.

4. Submit the Issue: Once you've provided all the necessary information, click on the "Submit new issue" button to create the issue. Your suggestion will be reviewed by the repository maintainers.

### Using Git - pro
1. Fork the Repository
    - On the project’s GitHub page, click the "Fork" button. This creates a copy of the repository under your own GitHub account. 
    - This step allows you to make changes without affecting the original project.
2. Clone the Repository to Your Local Machine
    - On your forked repository page, click "Code" and copy the HTTPS link.
    - Open a terminal and clone the repository using Git:
    ```
    git clone https://github.com/your-username/brickassist-translations.git
    ```
    - This will create a local copy of the project on your machine.
3. Set Up the Original Repository as an Upstream Remote
    - After cloning, it’s a good practice to keep your fork updated with the original repository. To do this, add the original repository as a remote called upstream:
    ```
    cd project-name
    git remote add upstream https://github.com/brickassist-app/brickassist-translations.git
    ```
4. Create a New Branch
    - Before making changes, create a new branch to avoid making modifications directly in the main or master branch:
    ```
    git checkout -b your-branch-name
    ```
5. Make Changes Locally
    - Now, make your changes to the project files on your local machine. This could involve fixing bugs, adding new features, or improving documentation.
6. Commit Your Changes
    - Once you’ve made the changes, stage and commit them:
    ```
    git add .
    git commit -m "Description of the changes you made"
    ```
7. Push the Changes to GitHub
    - Push your changes to your forked repository on GitHub:
    ```
    git push origin your-branch-name
    ```
8. Create a Pull Request (PR)
    - Go to your forked repository on GitHub, and you should see an option to create a Pull Request.
    - Click on "Compare & Pull Request". Make sure to write a clear description of what your changes do.
    - Submit the Pull Request. This will notify the maintainers of the original repository that you want them to review and possibly merge your changes.

## Copyright and Usage Notice
### About This Repository
This repository contains translations for the BrickAssist application (brickassist.com). Each file within this repository corresponds to translations used within the application's interface and content.

### Usage Restrictions
The content within this repository is subject to copyright and is intended solely for the purpose of providing translations for the BrickAssist application. Any unauthorized use, reproduction, or distribution of this content for purposes other than translation within the BrickAssist application is strictly prohibited.

### Copyright Information
All content within this repository, including but not limited to text, images, and other multimedia elements, is the intellectual property of BrickAssist and its respective owners. Unauthorized use of this content may infringe upon copyright laws and may result in legal action.

### Contributions and Licensing
Contributions made to this repository are subject to the repository's license agreement, which typically involves granting BrickAssist and its maintainers the right to use, modify, and distribute contributed content within the BrickAssist application.

### Contact Information
For inquiries regarding the usage of content within this repository or for permission to use content outside the scope of the BrickAssist application, please contact BrickAssist at sebastien.turrel@brickassist.com.

##  Acknowledgements
Thanks to Pascaline, Julie, Sham and JDLien.

Your work on translating is greatly appreciated. Thank you for your time and dedication to making our project accessible in multiple languages.

## Automated Validation
A GitHub Actions workflow automatically checks the formatting of translation files on each push and pull request.
