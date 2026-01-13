#Simple password generator
import random

def password_gen():
  spec_chars = ["!","£","$","%","^","&","*",".","/",":","@","~","#","_","-","=","+","?"]
  chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  pass_chars = 0

  random_list = []
  x = input('How many characters should your password be?')
  x = int(x)

  while pass_chars <x:
    random_char = random.choice(chars)
    random_specs = random.choice(spec_chars)
    random_i = random.randint(0,9)
    my_list = [random_char, random_specs , str(random_i)]
    random_letter = random.choice(my_list)
    random_list.append(random_letter)
    pass_chars = pass_chars + 1

  final_password = "".join(random_list)

  print(f"Your password is:\n {final_password}")

password_gen()