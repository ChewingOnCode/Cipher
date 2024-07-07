# Original text to be decrypted
text = "mrttaqrhknsw ih puggrur"

# Custom key used for the Vigenère cipher
custom_key = "happycoding"


# Function to perform Vigenère cipher encryption/decryption
def vigenere(message, key, direction=1):
    # Initialize the key index for the key character
    key_index = 0

    # Define the alphabet used for encryption/decryption
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Variable to store the final encrypted/decrypted message
    final_message = ""

    # Iterate through each character in the message
    for char in message.lower():
        # If the character is not a letter, append it directly to the final message
        if not char.isalpha():
            final_message += char
        else:
            # Find the corresponding key character based on the key index
            key_char = key[key_index % len(key)]
            key_index += 1

            # Calculate the offset based on the key character's position in the alphabet
            offset = alphabet.index(key_char)

            # Find the index of the current character in the alphabet
            index = alphabet.find(char)

            # Calculate the new index for the character after applying the Vigenère cipher
            new_index = (index + offset * direction) % len(alphabet)

            # Append the encrypted/decrypted character to the final message
            final_message += alphabet[new_index]

    return final_message


# Function to encrypt a message using the Vigenère cipher
def encrypt(message, key):
    return vigenere(message, key)


# Function to decrypt a message using the Vigenère cipher
def decrypt(message, key):
    return vigenere(message, key, -1)


# Print the original encrypted text and the key used
print(f"\nEncrypted text: {text}")
print(f"Key: {custom_key}")

# Decrypt the text using the provided key
decryption = decrypt(text, custom_key)
print(f"\nDecrypted text: {decryption}\n")

# Uncomment the following lines to test encryption
# encryption = encrypt(text, custom_key)
# print(encryption)
