
# Tutorial

## Image Hash Generator

**What is it?**  
The Image Hash Generator is a tool designed to create a CSV file containing the SHA256 hashes of images uploaded through the Ordinals Launcher. It's an invaluable resource for tracking inscriptions onchain using the Hash Inscription Checker. This tool's primary function is to facilitate the easy identification and verification of image inscriptions in the blockchain context.

**Access the Tool:**  
You can open and use the Image Hash Generator tool directly in your web browser by visiting: [https://jerryfane.github.io/ord-launcher-tracker/src/html/](https://jerryfane.github.io/ord-launcher-tracker/src/html/)

----------

## Hash Inscription Checker

**Purpose:**  
The Hash Inscription Checker is a Python-based tool used to track inscription IDs from hashes using the OrdinalsBot API. It processes a CSV file containing image hashes and generates a JSON file with the corresponding inscription IDs.

### Setting Up

**Requirements:**

-   Python 3.x
-   Pip (Python package manager)

**Installation:**

1.  **Install Python:**
    
    -   If you don't have Python installed on your system, download it from [python.org](https://www.python.org/downloads/).
    -   Follow the installation instructions for your specific operating system.
2.  **Clone the Repository:**
    
    -   Clone or download the repository to your local machine.
3.  **Install Dependencies:**
    
    -   Navigate to the directory containing the cloned repository.
    -   Install the required Python packages using the following command:
        
        Copy code
        
        `pip install -r requirements.txt` 
        

### Running the Script

**Usage:**

phpCopy code

`python3 generate_inscription_json.py --h <path_to_hash_csv> -f <output_filename.json> -n <asset_name>` 

**Parameters:**

-   `--h`: Path to the CSV file containing the image hashes. (Required)
-   `-f`, `--filename`: Filename for the output JSON file. (Required)
-   `-n`, `--asset_name`: Asset name prefix for the JSON output. (Optional, default is "Test")

**Example:**

cssCopy code

`python3 generate_inscription_json.py --h "/path/to/image_hashes.csv" -f outputfile.json -n MyAsset` 

This command will process the hashes in `image_hashes.csv` and generate an output JSON file named `outputfile.json`, with each asset prefixed as "MyAsset".

----------

**Note:** This tutorial assumes a basic understanding of how to navigate the command line or terminal. If you're unfamiliar with the command line, you might find resources online that provide a basic introduction to using terminal commands.

