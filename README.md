# AML-project

Collaborating on making an ML model to predict credit defaults.

Dataset obtained from DOI [10.24432/C55S3H](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients)

## How to set up environment

### Make sure you have Python and pip installed.

1. Go to the main page of the repository on GitHub.
2. Click the green "< > Code" button.
3. Copy the HTTPS URL.
4. Open a terminal or command prompt on your computer, navigate to where you want to store the project, and run:
   git clone <PASTE_THE_URL_HERE>
5. Navigate into the project folder:
   cd <"type folder name here">
   Note that .ipynb files can be tricky to manage, but nbstripout makes sure output i omitted making it seemingly hassle free!

## If you have trouble pushing to git:
Open your terminal, navigate to your project folder, and run these three commands in order:

Activate your environment (to ensure we point to the correct new Python):
conda activate AML
#### Remember to change AML to the name of your environment

Ensure the tool is installed in this environment:
conda install nbstripout

Update the Git configuration: This command overwrites the old "broken path" with the currently active one.
nbstripout --install

2. Verify it worked
Run this command to see what path Git is using now:
git config filter.nbstripout.clean

Success: It should look like "/opt/anaconda3/envs/AML/bin/python" -m nbstripout (or similar), pointing to your current environment.