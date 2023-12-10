
# Ordinals Launcher Tracker

You can use the Ordinals Launcher Tracker tools to index mints from the [Ordinals Launcher](https://github.com/jerryfane/ord-launcher).

---

## Image Hash Generator

**What is it?**  
The Image Hash Generator is a tool designed to create a CSV file containing the SHA256 hashes of images uploaded through the Ordinals Launcher.

**Access the Tool:**  
You can open and use the Image Hash Generator tool directly at: [https://jerryfane.github.io/ord-launcher-tracker/src/html/](https://jerryfane.github.io/ord-launcher-tracker/src/html/)

----------

## Hash Inscription Checker

**Purpose:**  
The Hash Inscription Checker is a Python-based tool used to track inscription IDs from hashes using the OrdinalsBot API. It processes a CSV file containing image hashes and generates a JSON file with the corresponding inscription IDs. Currently, it works with free mints, since it only considers the first inscription of a hash as valid, whether it's paid or unpaid. For paid mints, you also need to check if the minter has sent the payment to the correct address.
The CSV File can be generated using the Image Hash Generator above. 

### Setting Up

**Requirements:**

-   Python 3.x
-   Pip (Python package manager)

**Installation:**

1.  **Install Python:**
    
    -   If Python is not already installed on your system, download it from [python.org](https://www.python.org/downloads/).
    -   Follow the installation instructions for your specific operating system.

2.  **Clone the Repository:**
    
    -   Open your terminal or command prompt.
    -   Choose a location on your local machine where you want to clone the repository.
    -   Run the following command to clone the repository:
        
        ```
        git clone https://github.com/jerryfane/ord-launcher-tracker.git
        ```

3.  **Navigate to the Repository Directory:**
    
    -   After cloning, navigate to the repository directory by running:
        
        ```
        cd [repository directory name]
        ```

    -   Replace `[repository directory name]` with the name of the directory created by the clone operation.

4.  **Install Dependencies:**
    
    -   In the repository directory, install the required Python packages using the command:
        
        ```
        pip install -r requirements.txt
        ```


### Running the Script

**Usage:**

`python3 generate_inscription_json.py --h <path_to_hash_csv> -f <output_filename.json> -n <asset_name>` 

**Parameters:**

-   `--h`: Path to the CSV file containing the image hashes.
-   `-f`, `--filename`: Filename for the output JSON file.
-   `-n`, `--asset_name`: Asset name prefix for the JSON output.

**Example:**


`python3 generate_inscription_json.py --h "/path/to/image_hashes.csv" -f outputfile.json -n MyAsset` 

This command will process the hashes in `image_hashes.csv` and generate an output JSON file named `outputfile.json`, with each asset prefixed as "MyAsset".

----------

**Note:** This tutorial assumes a basic understanding of how to navigate the command line or terminal. If you're unfamiliar with the command line, you might find resources online that provide a basic introduction to using terminal commands.

