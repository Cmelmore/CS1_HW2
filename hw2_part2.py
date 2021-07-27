""" Author: Christina Elmore
    Purpose: Write a program that either encrypts or decrypts a string based on user choices.
"""
def encrypt(word):       #encrypts a string
     encrypted = word.replace(" a","%4%").replace("he","7!").replace("e","9(*9(").replace("y","*%$").replace("u","@@@").replace("an","-?").replace("th","!@+3").replace("o","7654")
     print ""
     print "Encrypted as ==>",encrypted
     print "Difference in length ==> %d" %(abs(len(word)-len(encrypted)))

def decrypt(word):       #decrypts a string
     decrypted = word.replace("7654","o").replace("!@+3","th").replace("-?","an").replace("@@@","u").replace("*%$","y").replace("9(*9(","e").replace("7!","he").replace("%4%"," a")
     print ""
     print "Deciphered as ==>",decrypted
     print "Difference in length ==> %d" %(abs(len(word)-len(decrypted)))     

Choice = str(raw_input ("Enter 'E' for encrypt or 'D' for decrypt ==> "))
print Choice
if Choice.lower() == "d":
     decrypt_me = str(raw_input ("Enter cipher text ==> "))
     print decrypt_me
     decrypt(decrypt_me)
    
elif Choice.lower() == "e":
     encrypt_me = str(raw_input ("Enter regular text ==> "))
     print encrypt_me
     encrypt(encrypt_me)  
else : 
     print "I didn't understand ... exiting"