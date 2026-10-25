#we are importing secrets module because it communicates with ubuntu hardware noice like tiny variation in CPU timing and keystrokes which helps to genarate truly unpredicable numbers
import secrets


#importing PasswordHasher is one of the argon2 folder and it is the one that put a PIN into Argon2 hash if the PIN matches
#importing VerifyMismatchError is a subfolder in the argon 2 and the message argon send when the person entered a wrong PIN instead of blocking them out it raise error issue


from argon2 import PasswordHasher

from argon2.exceptions import VerifyMismatchError 

#need the working hasher so we create it from PasswordHasher and this is more like package that has something inside. it is the real tool Python builds so we can use what is inside

ph_passwordHasher = PasswordHasher()


#hash_pin function is the action that takes pin and hide it using the argo2id hasher and give back an invicible hash

def hash_pin(pin):
    #return statement tell the function to give back what we asked

    return ph_passwordHasher.hash(pin)

#verify_pin means when the user enters the pin python check if the pin is correct that is why it use the try and except statement to verify the information. when the user enter the pin it try to use the stored hasha and pin and return the output if the input is incorrect it flaggered an error 

def verify_pin(stored_hash, entered_pin):
    try:
        #the system check from the stored ph-passwordHasher and return the results

        return ph_passwordHasher.verify(stored_hash, entered_pin)
    except VerifyMismatchError:

        #return false, after checking and the pin do not match the system return a false
        return False

#generate_2fa_code function generate 6 digit number randomly and the code does not need any input or paramenters inside the parentheses because everytime a user entered the pin it send them a 6 digit number for ferification. they convert those number into string because when a user entered a pin python the result will be send as a string

def generate_2fa_code():
    code = secrets.SystemRandom().randint(100000,999999)   #it generate random numbers between 100000 and 999999

    return str(code)

#if__name__== "__main__" is use the guard the code when you run a file like auth_verifier.py in the terminal it use the name to check if it not correct python skip the code

if __name__== "__main__":

    my_hash = hash_pin("2580")

    print(my_hash)

    #test1: testing verify pin with the correct pin 2580

    test1_result = verify_pin(my_hash, "2580")
    print(test1_result)

    #test2 testing verify_pin with wrong pin 0000

    test2_result = verify_pin(my_hash, "0000")
    print(test2_result)

    #test3: testing generate_2fa_code to see if the system can print 6 digit number for users

    test3_result = generate_2fa_code()
    print(test3_result)