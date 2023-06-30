# Bing-Search-Automation
This is a simple example of a browser automation tool. The tool opens the Microsoft Edge browser and searches random queries using the Bing search engine.

# Running the Project

This guide explains how to run a project that consists of a `main.py` file and a `requirements.txt` file.

## Prerequisites

Before running the project, make sure you have the following prerequisites installed on your system:

- Python (version 3.x)
- pip (Python package installer)

## Steps

Follow these steps to run the project:

1. **Clone the project**:
   - Clone the project repository to your local machine using Git or download the project as a ZIP file and extract it.

2. **Navigate to the project directory**:
   - Open your terminal or command prompt.
   - Use the `cd` command to navigate to the project's directory:
     ```
     cd /path/to/project/directory
     ```

3. **Create a virtual environment (optional but recommended)**:
   - It's recommended to create a virtual environment to isolate project dependencies. This step ensures that the project's dependencies won't conflict with other Python packages installed on your system.
   - Create a virtual environment by running the following command:
     ```
     python3 -m venv myenv
     ```
   - Activate the virtual environment:
     - For Windows:
       ```
       myenv\Scripts\activate
       ```
     - For macOS/Linux:
       ```
       source myenv/bin/activate
       ```

4. **Install project dependencies**:
   - Use pip to install the required packages specified in the `requirements.txt` file. Run the following command:
     ```
     pip install -r requirements.txt
     ```
   - This command will install all the necessary packages needed for the project to run.

5. **Run the project**:
   - After successfully installing the project dependencies, you can run the `main.py` file. Use the following command:
     ```
     python main.py
     ```
   - This command will execute the `main.py` file and start the project.

Congratulations! You have successfully run the project. If everything is set up correctly, the `main.py` file should execute without any issues.

Remember to deactivate the virtual environment after you're done with the project by running the `deactivate` command in the terminal.

Feel free to explore and modify the project code as needed. Happy coding!
