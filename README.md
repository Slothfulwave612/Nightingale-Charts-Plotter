# Nightingale-Charts-Plotter

* To access the online hosted version of this web app click [here](https://nightingale-charts-plotter.herokuapp.com/).

* To install this web app on your local system follow these steps (prerequisite -> your system should have anaconda installed):

  1. **Download The Repository:**

      * Use one of the following options.

      * *Option 1:* You can download the repository by clicking on the Code button and then clicking on Download Zip. Make sure to unzip the file.

      * *Option 2:* Using git. Run this command on your terminal:

        `git clone https://github.com/Slothfulwave612/Nightingale-Charts-Plotter.git`

  2. **Create a New Conda Environment:**

      * Make a new environment for using this app. Run the following command: `conda create -n streamlit_env python=3.8.10`
        
      * Move to the new environment: `conda activate streamlit_env`

  3. **Install Required Packages:**

      * Navigate to the downloaded folder (on your terminal). And then run the following command:

        `pip install -r requirements.txt`

  4. **Run The Web Application:**

      * Once all required packages are installed, you can run the following command to run the web app:

        `streamlit run src/webapp.py [-- .streamlit/config.toml]`