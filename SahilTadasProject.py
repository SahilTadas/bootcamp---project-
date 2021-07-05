import hashlib

# Initializing string
strhash = "SahilCode"

# Sending to md5()
result = hashlib.md5(strhash.encode())

# Printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())