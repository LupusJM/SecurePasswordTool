import argparse
import hashlib
import secrets
import sqlite3

DATABASE_FILE = 'passwords.db'

def make_hash(plaintext, hash_type='sha256', iterations=100000, pepper=None):
    salt = secrets.token_hex(16)
    if pepper:
        plaintext += pepper
    hashed = hashlib.pbkdf2_hmac(hash_type, plaintext.encode('utf-8'), salt.encode('utf-8'), iterations)
    return f"{hash_type}@{iterations}@{salt}@{hashed.hex()}"

def delete_password(password_id):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM passwords WHERE id = ?', (password_id,))
    conn.commit()
    conn.close()

def verify_hash(plaintext, hashed_info, pepper=None):
    hash_type, iterations, salt, expected_hash = hashed_info.split('@')
    iterations = int(iterations)
    if pepper:
        plaintext += pepper
    hashed = hashlib.pbkdf2_hmac(hash_type, plaintext.encode('utf-8'), salt.encode('utf-8'), iterations)
    return hashed.hex() == expected_hash

def create_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                        id INTEGER PRIMARY KEY,
                        hashed_password TEXT
                    )''')
    conn.commit()
    conn.close()

def insert_password(hashed_password):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO passwords (hashed_password) VALUES (?)', (hashed_password,))
    conn.commit()
    conn.close()

def main():
    create_database()

    parser = argparse.ArgumentParser(description='Simple password hashing and verification tool')
    parser.add_argument('--make', metavar='<plaintext>', help='Generate salted hash for plaintext')
    parser.add_argument('--verify', metavar=('<plaintext>', '<hash_info>'), nargs=2, help='Verify plaintext against hashed info')
    parser.add_argument('--hash-type', metavar='<hash_type>', default='sha256', help='Hash type (default: sha256)')
    parser.add_argument('--iterations', metavar='<iterations>', type=int, default=100000, help='Number of iterations (default: 100000)')
    parser.add_argument('--pepper', metavar='<pepper>', help='Pepper value')
    parser.add_argument('--delete', metavar='<password_id>', help='Delete saved hash with specified ID')
    args = parser.parse_args()

    if args.make:
        hashed = make_hash(args.make, args.hash_type, args.iterations, args.pepper)
        print(hashed)
        insert_password(hashed)
    elif args.verify:
        plaintext, hashed_info = args.verify
        if hashed_info.startswith("'") and hashed_info.endswith("'"):
            hashed_info = hashed_info[1:-1]
        if verify_hash(plaintext, hashed_info, args.pepper):
            print("Hashes match!")
        else:
            print("Hashes don't match!")
    elif args.delete:
        delete_password(args.delete)
        print("Hash with ID {} deleted successfully.".format(args.delete))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
