#Simple password generator
# New feature that now uses cli
import random
import sys

def password_gen(x=0):
  spec_chars = ["!","£","$","%","^","&","*",".","/",":","@","~","#","_","-","=","+","?"]
  chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  pass_chars = 0

  random_list = []
 

  while pass_chars <x:
    random_char = random.choice(chars)
    random_specs = random.choice(spec_chars)
    random_i = random.randint(0,9)
    my_list = [random_char, random_specs , str(random_i)]
    random_letter = random.choice(my_list)
    random_list.append(random_letter)
    pass_chars = pass_chars + 1

  final_password = "".join(random_list)

  #print(f"Your password is:\n {final_password}")
  return final_password

if len(sys.argv) < 2:
  print('Welcome to my Password Generator.\n')
  x = int(input("Length: "))
else:
  x = int(sys.argv[1])

cli_pass = password_gen(x)
print(f'Your password is {cli_pass}')



