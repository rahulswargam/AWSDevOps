import string

def encrypt_reference_id(reference_id):
    # Basic encryption using a simple mapping
    encrypted_id = []
    for char in reference_id:
        if char.isalnum():  # Consider only alphanumeric characters
            encrypted_char = chr(ord(char) + 1)  # Example: Shift each character by 1
            encrypted_id.append(encrypted_char)
        else:
            encrypted_id.append(char)  # Preserve special characters as is
    return ''.join(encrypted_id)

def decrypt_reference_id(encrypted_id):
    # Basic decryption (reverse of encryption)
    decrypted_id = []
    for char in encrypted_id:
        if char.isalnum():
            decrypted_char = chr(ord(char) - 1)
            decrypted_id.append(decrypted_char)
        else:
            decrypted_id.append(char)  # Preserve special characters as is
    return ''.join(decrypted_id)

def main():
    print("Enter the Reference ID (should be 12 characters long):")
    reference_id = input().strip()

    # Step 2: Check Validity
    if len(reference_id) != 12 or not reference_id.isalnum():
        print("Invalid Reference ID. It should be exactly 12 alphanumeric characters.")
        return

    # Step 3: Encrypt the Reference ID
    encrypted_id = encrypt_reference_id(reference_id)
    print("Encrypted Reference ID:", encrypted_id)

    # Step 4: Enhancements - Decryption option
    choice = input("Do you want to decrypt the Reference ID (yes/no)? ").strip().lower()
    if choice == 'yes':
        decrypted_id = decrypt_reference_id(encrypted_id)
        print("Decrypted Reference ID:", decrypted_id)

if __name__ == "__main__":
    main()
