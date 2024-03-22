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

>Full example:
>python main.py --make qwerty123 --pepper strongerhash --hash-type MD5 --iterations 500000
>>Output:
>>MD5@500000@967274c4840a87860275f669fcec14ef@a07c1d24ee0ab9c09afb738da687ea3e
### Click for example

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
  <summary>Example:</summary>
  
  ```bash
  python main.py --verify mypassword sha256@100000@303bb288988c281d9b199e240f2b6385@9d0563c55a5e713c1140e0d007bf6244f6d99f449cc5e6adb74ba962f4b9f2d7
  ```
  ```bash
  python main.py --verify mypassword "sha256@100000@303bb288988c281d9b199e240f2b6385@9d0563c55a5e713c1140e0d007bf6244f6d99f449cc5e6adb74ba962f4b9f2d7"
  ```
  ```bash
  python main.py --verify mypassword 'sha256@100000@303bb288988c281d9b199e240f2b6385@9d0563c55a5e713c1140e0d007bf6244f6d99f449cc5e6adb74ba962f4b9f2d7'
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


<b>Help<b>
```bash
python main.py --help or -h
```
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/lupusjm/SecurePasswordTool/blob/main/LICENSE)
