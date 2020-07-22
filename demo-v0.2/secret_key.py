"""
filename:secret_key.py
version: 0.2
author:elegance
"""

def get_secret_key(n):
    import string, random
    letters_set = string.digits +string.ascii_letters

    key = ''
    for i in range(1,n+1):
        key += random.choice(letters_set) 
        if i % 4 == 0 and i !=n: 
            key += '-'
    return key

if __name__ == '__main__':
    print(get_secret_key(20))