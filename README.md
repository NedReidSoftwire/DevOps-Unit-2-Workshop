# DevOps Unit 2 Workshop

Welcome to the Unit 2 Workshop! 

## Morning
### Our objectives
The objective of the morning is:

- To get familiarity with Git
- To get familiarity with GitHub workflows as you’ll apply them on this course and in your workplace
- To get familiarity with modifying an existing Python application 

### Set up
We’re going to start by forking an application. 
- This is a Pub Quiz written in Python that exists on GitHub.
- You can find it here: https://github.com/corndeladmin/devops-pub-quiz

Fork the repository by pressing the "Fork" button. 
- You can read more about forking on various resources, including [How to Fork a GitHub Repository – A Complete Workflow](https://www.freecodecamp.org/news/how-to-fork-a-github-repository/)

Next clone the repo to your machine by following these instructions:
- Go to the main page of the repository you want to clone on GitHub.com (in this case, just follow the link above)
- Click on the green "Code" button. A small window will pop up showing the repository URL.
- Copy the repository URL. You can click the copy icon next to the URL to copy it to your clipboard.
- Open your terminal (Mac/Linux, including ACG) or Git Bash (Windows).
- Navigate to the directory where you want the cloned repository to be saved using the cd command. For example: `cd /path/to/your/directory`
- Run the `git clone` command followed by the URL you copied. For example: `git clone https://github.com/username/repository.git`
- Press Enter. Git will start cloning the repository to your local machine to a subfolder with the repository name.

Once you have have cloned the repository locally, open the folder in Visual Studio Code.

### Making Improvements
Read the existing application and understand how it works.
- You can start the application by running `python app.py` in a terminal
- It should then run, and you will experience a simple quiz with 2 sample questions!

Once you're satisfied that the code works and you understand at least at some level how it works, let’s modify it.

Your goal for this exercise is to improve the Pub Quiz experience for the user
- The simplest way to do this is simply to add a single question!
- If you’ve done that, you should expand your efforts:
    - Replace the existing questions with ones of your own
    - You can give the user a score at the end by keeping track of it
    - You could create non-multiple choice questions 
    - Or any other change you are inspired to make!

### Following the Pull Request Workflow
Once you've made your first change (and are happy with it!), you should create a new branch and make a commit.

After making your first commit push the branch to GitHub and raise a Pull Request (PR)
- When pushing your local branch for the first time you will be asked to set the name of the upstream/remote branch (normally this is the same as your local branch name)
- Check that you are able to make a PR - read and follow these instructions: [Creating a pull request - GitHub Docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

**Roughly an hour to half an hour before lunch we’ll get everyone to give each other feedback.**
- At this point, you should update your PR to contain all your latest changes, and provide a link to the PR to your PDE. 
- Your PDE will pass your PR to someone else, and pass you a link to someone else’s PR.
- Download their code and run it on your machine. GitHub shows you how to do it here: [GitHub Guide](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/checking-out-pull-requests-locally)
- Play their quiz - prepare some feedback! 
    - Too easy? Too hard? Could use more questions? Fewer questions? Spotted a typo? 
    - Leave the feedback on their PR.

Normally in a PR workflow, your feedback will either indicate a change that will ideally be made before the PR is merged, or it can indicate a problem that definitely needs to be addressed before the PR is merged (e.g. a bug or security flaw). For the purposes of this exercise, all feedback can be considered optional - if you can action any of the feedback before merging the PR, please do. Otherwise, do just merge the PR and you can always work on the feedback later!
- In any case, after your PR has merged, you will have completed the core goals of the morning exercise - engage in stretch by continuing to action feedback until the Lunch break.

## Afternoon
This afternoon, we're going to be working in pairs to write a Python application from scratch to analyse a file that contains a list of instructions and data.

The file looks a little like this: 

```
goto 4
replace 1 2
remove 3
goto 2
goto calc x 3 5
replace 6 10
```
We're going to tackle the problem in steps.

### Step 1
- Write a Python version of a basic "calculator". ​
- It should accept 3 pieces of input from the user: 
    - a string that's one of `x`, `+`, `-`, or `/` (an operation)
    - an integer (parameter A)
    - and another integer (parameter B). ​
- It should then emit the result of performing the operation on A and B. ​
- For example:
    - If your application asks the user for an operation and 2 numbers, and the user enters "+", "1", "2", then the application should output "3". ​
    - If the user supplied "/", "5", "2", the application should output "2.5". ​
    - If the user supplied "x", "5", "0", the application should output 0.​

### Step 2
- Our next goal is to process the following file: [Step 2](https://gist.githubusercontent.com/Jonesey13/47029d880ab17a2df41df7a677fb4e89/raw/78e0e3516d46dbe10cfae147bc2e270b7e8cc2c0/step_2.txt)
- Each line contains a calculation statements prefixed by "calc", e.g.:

```
calc x 2 5​
calc / 10 5​
```

- Create a new Python script, and within it:​
    - Read in the new file.
    - Compute the value of each line using the approach from step 1​.
    - Add up the results from all the lines and send the results to the PDE.
- Some hints:
    - Hint 1: For reading the lines from the file you may want to use `file.read().splitlines()​` to build a list of lines.​
    - Hint 2: you may want to use `string.split()` to break up the parts of each calc line.
- When you complete this, give yourself a pat on the back! You've completed the core goals of the afternoon exercise. Get a cup of tea, if you haven't already, then engage in stretch by continuing with the following additional stretch goals.
​
### Step 3 (Stretch)
- For our first stretch goal, we are going to process the following file: [Step 3](https://gist.githubusercontent.com/Jonesey13/daee3b723eedbf955546adc7af12e3e7/raw/01e5329ae5d2445f63e67ed325856980418551cd/step_3.txt)
- This has goto statements like the following​:

```
goto 27
```

- This means go to line 27 in the file and read the statement there. Please note that calc and goto statements can be combined like so:​

```
goto calc / 27 9
```

- This is equivalent to `goto 3`​.
- For simplicity, assume that:
    - We cannot nest calc statements.
    - Decimals are rounded down.
    - Out of bounds gotos (i.e. invalid line numbers) do not occur.​
    
- Starting from line 1, use the rules above to navigate the document, stopping when you've hit a statement you’ve seen once before (they are allowed to be from different lines!)
- When finished please send the statement and line number the code has stopped on to your PDE – but feel free to carry on and start the next stage while you wait for confirmation.​

### Step 4 (Stretch)
- Finally, we will navigate the following file: [Step 4](https://gist.githubusercontent.com/Jonesey13/d722ce5dfb70770cdd83800e0f180e98/raw/ac0452c456e2bb7806a54c8c6433b96649fc9b25/step_4.txt)
- This has some additional statements.​
- The goal is to process the file, starting from line 1, stopping when you’ve hit a statement you’ve seen before or manage to jump outside the file by a goto.​
- When finished, please send the line number & statement to the PDE to confirm.​
- There are additional statements you need to be able to process.

#### New statement: Remove lines
```
remove {line_number}
```
- Remove line `{line_number}` from the file (if the line number does not exist do nothing) and then​
- Read the next instruction after this remove statement

#### New statement: Replace lines
```
replace {line_number_1} {line_number_2}
```
- Replace line `{line_number_1}` with line `{line_number_2}` (if either line number does not exist do nothing) and then​
- Read the next instruction after this statement
​
