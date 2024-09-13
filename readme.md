# Selenium Form Submission with Multithreading

This project uses Selenium to automate form submissions on a website. It generates random user data using the Faker library and submits forms in parallel using Python's `concurrent.futures` for multithreading. The forms are continuously submitted with a fixed email domain and a fixed value for the domain field.

## Features

- **Form Automation**: Automates the process of filling out and submitting a form.
- **Multithreading**: Uses multithreading to speed up form submissions.
- **Fixed Email Domain**: Submits forms with a fixed email domain (`com.net`).
- **Continuous Operation**: The script continuously submits forms at defined intervals.

## Requirements

- Python 3.6 or higher
- Selenium
- Faker
- WebDriver Manager
- Google Chrome

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repository-name.git
    cd your-repository-name
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install Google Chrome if it's not already installed.**

## Configuration

- **URL**: Update the `url` variable in the `main()` function with the URL of your form.

## Usage

1. **Run the script:**

    ```bash
    python test.py
    ```

2. **The script will:**
   - Continuously submit forms with random names and a fixed email domain.
   - Wait for a fixed interval between each cycle.
   - Use multiple threads to increase the submission speed.

## Code Structure

- `test.py`: Main script for form submission and multithreading.
- `requirements.txt`: List of required Python packages.

## Example Output

