#Import logo from art
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
restart="True"

#create function and write a logic inside it
def ceasar(message,shift_num,move):
    if move=="decode":
      shift_num*=-1
    end_code=""
  #Ittirate each letter in message
    for letter in message:
      #if the letter is available in alphabet list then only do the below operation
      if letter in alphabet:
        position=alphabet.index(letter)
        new_position=position+shift_num
        end_code+=alphabet[new_position]
      else:
        end_code+=letter

    print(f"The {direction} code is: {end_code}")

#call the function repeatedly until the user give input as no
while(restart):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #if the shift number is greater than 26 it will take remainder as a shift.
  if shift>26:
    shift%=26
  ceasar(message=text,shift_num=shift,move=direction)
  
  want_to_restart=input("if you want to restart game Type 'yes' otherwise Type 'no'").lower()
  if want_to_restart=="no":
    restart=False
    print("Good bye")


  

  