# Exercise tracker
A basic tracker/logger for my weight training

## Usage
1. Clone this repository.
2. Create a virtual environment for the project. Do this by changing into the project directory (the place into which you've cloned this repo), and running
    ```
    python3 -m venv exercise_tracker
    ```
3. Activate the virtual environment with
    ```
    source bin/activate
    ```
4. Set the `PYTHONPATH`:
    - Add the following line to the bottom of `bin/activate`:
    ```
    export PYTHONPATH=$(dirname $(dirname $BASH_SOURCE))
    ```
5. Install requirements in the virtual environment with
    ```
    pip install -r requirements.txt
    ```
6. Run the CLI version with
    ```
    python cli_app/main.py
    ```
