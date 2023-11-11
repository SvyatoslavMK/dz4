import random


class NumberEncryptor:

  def __init__(self, number):
    self.original_number = number
    self.number = number

  def _encrypt(self):
    operation = input("choose only(-,+,*,/)> ") #choose ur encryption

    operand = 5 + 98 / 32
    if operation == "+":
      self.number += operand
      print("+") #current operation
    elif operation == "-":
      self.number -= operand
      print("-")#current operation
    elif operation == "*":
      self.number *= operand
      print("*")#current operation
    elif operation == "/":
      print("/")#current operation
      if operand != 0:
        self.number /= operand

    return self.number

  def decryptor(self, operation):#choose ur decryption (same as encryption)
    operation = input("choose only(-,+,*,/)> ")
    original_number = self.original_number
    if operation == "+":
      decrypted_number = self.number - (5 + 98 / 32)
    elif operation == "-":
      decrypted_number = self.number + (5 + 98 / 32)
    elif operation == "*":
      decrypted_number = self.number / 8.0625
    elif operation == "/":
      decrypted_number = self.number * (5 + 98 / 32)
    return decrypted_number


# Example usage
number = 100
encryptor = NumberEncryptor(number)
encrypted_number = encryptor._encrypt()
decrypted_number = encryptor.decryptor("-")
print("Original number:", number)
print("Encrypted number:", encrypted_number)
print("Decrypted number:", decrypted_number)

#PROGRAM BY MASVKIR (i wanna sleep)