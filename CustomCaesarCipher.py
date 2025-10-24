def CustomCaesarCipher(key, message):
    if key < 0:
        return "INVALID INPUT"
    
    result = ""
    
    for char in message:
        
        if char.isupper():
            result += chr((ord(char) - 65 + key) % 26 + 65)
        
        
        elif char.islower():
            result += chr((ord(char) - 97 + key) % 26 + 97)
        
        
        elif char.isdigit():
            result += str((int(char) + key) % 10)
        
        
        else:
            result += char
    
    return result
plain_text = input("Enter your PlainText: ")
key = int(input("Enter the Key: "))

encrypted_text = CustomCaesarCipher(key, plain_text)
print("The encrypted Text is:", encrypted_text)
