# Secure Password Tool

This is a simple password hashing and verification tool implemented in Python. The script allows users to generate salted hashes for plaintext passwords and verify plaintext against hashed information. It supports various hash types, allows customization of the number of iterations for hashing, and provides an option to include a pepper value for additional security. The tool provides a convenient command-line interface for interacting with its functionalities.
## Features

- Generate salted hashes for plaintext passwords.
- Verify plaintext against hashed information.
- Support for multiple hash types (default: SHA-256).
- Customizable number of iterations for hashing (default: 100,000).
- Option to include a pepper value for enhanced security.
- Simple command-line interface for easy interaction.

## Usage

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/LupusJM/SecurePasswordTool.git
    ```

2. Navigate to the project directory:

    ```bash
    cd SecurePasswordTool
    ```

## Generating Hashes
### Click for example
<br>

<b>This command generates a salted hash for a plaintext password, run:<b>
```bash
python main.py --make <plaintext>
```
<details>
  <summary>Example:</summary>

  ```bash
  python main.py --make mypassword
  ```
</details>
<br>


<b>This command verifies a plaintext password against hashed information, run:<b>
```bash
python main.py --verify <plaintext> <hash_info>
```
<details>
  <summary>Example Windows:</summary>

  ```bash
  python main.py --verify mypassword "sha256$100000$8248dcf46b2caa79f91361a26dc80608$db17de35bdeb5ecf5c9ae953f1383a8023e8494c2842e807fec49c7e4cdd8cdd"
  ```
</details>
<details>
  <summary>Example Linux:</summary>
  
  ```bash
  python main.py --verify mypassword 'sha256$100000$8248dcf46b2caa79f91361a26dc80608$db17de35bdeb5ecf5c9ae953f1383a8023e8494c2842e807fec49c7e4cdd8cdd'
  ```
</details>
<br>


<b>This command generates a salted hash with a specific hash type, run:<b>
```bash
python main.py --make <plaintext> --hash-type <hash_type>
```
<details>
  <summary>Example:</summary>

  ```bash
  python main.py --make mypassword --hash-type sha512
  ```
</details>
<br>


<b>This command generates a salted hash with a specific number of iterations, run:<b>
```bash
python main.py --make <plaintext> --iterations <iterations>
```
<details>
  <summary>Example:</summary>

  ```bash
  python main.py --make mypassword --iterations 200000
  ```
</details>
<br>


<b>This command generates a salted hash with a specified pepper value, run:<b>
```bash
python main.py --make <plaintext> --pepper <pepper>
```
<details>
  <summary>Example:</summary>

  ```bash
  python main.py --make mypassword --pepper somepepper
  ```
</details>
<br>


<b>Help:<b>
```bash
python main.py --help or -h
```
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/lupusjm/SecurePasswordTool/blob/main/LICENSE)
