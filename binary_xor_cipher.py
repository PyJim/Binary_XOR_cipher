def intro():
    """_summary_
       Allow user inputs of the binary to be encrypted and the key to be used also in binary
    """
    global item, key
    item = input("Enter binary to enrypt: ")
    key = input("Enter key of encryption: ")


def verify():
    """_summary_
        Checks if the entries from the intro() function are indeed binary
    Returns:
        _bool_: _Returns True or False depending on the results_
    """
    global key, item
    binary = ["0","1"]
    result1 = all(bit in binary for bit in list(item))
    result2 = all(bit in binary for bit in list(key))
    return result1 and result2


def modify_key():
    """_summary_
       modifies the length of the key to ensure proper encryption
    """
    global key, item
    if len(key)<len(item):
        key = int(len(item)/len(key))*key
        if len(key)<len(item):
            key+=key[0:len(item)%len(key)]
    elif len(key)>len(item):
        key = key[0:len(item)]

def encrypt():
    """_summary_
        encrypts the value with the key and returns the encrypted value in binary format
    Returns:
        _string_: _encrypted value (cipher text)_
    """
    global encrypted, key, item
    encrypted = ""
    for bit in range(len(item)):
        if item[bit]==key[bit]:
            encrypted+="0"
        else:
            encrypted+="1"
    return encrypted

def error():
    """_summary_
        returns an error message for invalid inputs
    Returns:
        _string_: _custom error message_
    """
    return "Invalid key or value"

def binary_xor_encrypt():
    """_summary_
       Starts the program and calls the helper functions at appropriate times
    """
    intro()
    if verify():
        modify_key()
        print(encrypt())
    else:
        print(error())
