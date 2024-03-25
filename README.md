# BrickAssist App - Translations
## How to Contribute with GitHub interface
### Using GitHub Interface
1. Edit Language Files: Navigate to the language file corresponding to the language you want to contribute to. Language files are typically named with the language code, like app_en.arb for English or app_fr.arb for French.

2. Click the Edit Button: Click the pencil icon (Edit this file) located at the top right corner of the file view.

3. Make Changes: Translate or modify the strings in the file as needed.

4. Propose Changes: After making your modifications, click on the green button 'Commit changes...' in the top right of the page. Provide a brief description of the changes you made in the "Commit message" section.

5. Submit Changes: Click on the "Commit changes" button to submit your modifications as a pull request. Your changes will be reviewed and merged into the main project by the repository maintainers.

### Opening an Issue
1. Go to the Issues Tab: Click on the "Issues" tab located near the top of the repository page.

2. Create a New Issue: Click on the green "New issue" button.

3. Describe Your Contribution: In the issue description, explain the changes you'd like to make, such as adding a new language or suggesting modifications to existing translations.

4. Submit the Issue: Once you've provided all the necessary information, click on the "Submit new issue" button to create the issue. Your suggestion will be reviewed by the repository maintainers.

## How to Contribute with Git
### 1. Clone the Repository
Clone the original repository directly to your local machine:
```
git clone git@github.com:brickassist-app/brickassist-translations.git
```

### 2. Create a New Branch
Create a new branch to work on your translations:
```
git checkout -b my-new-branch
```
Replace my-new-branch with a descriptive branch name related to your changes (if possible)

### 3. Translate or Modify Existing Translations
Navigate to the appropriate language folder within the repository. If your language is not available, you can create a new file following the existing structure.
Edit the language file using a text editor. Translate the strings or modify existing translations as needed.

### 4. Commit Changes
Once you've made your translations, commit your changes with a descriptive message:
```
git add .
git commit -m "Fixing a typo on 'baguette' in the French translation"
```

### 5. Push Changes
Push your changes to the original repository:

```
git push origin my-new-branch
```

### 6. Create a Pull Request
Go to the original repository on GitHub and click on the "Pull Request" button. Provide a descriptive title and explanation of your changes.
Once reviewed, your changes will be merged into the main project.

### 7. Stay Updated
Keep your local repository updated with the latest changes from the original repository to avoid conflicts:
```
git checkout master
git pull origin master
```

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