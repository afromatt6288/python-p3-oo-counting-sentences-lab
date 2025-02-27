#!/usr/bin/env python3

class MyString:

  def __init__(self, value = ""):
    self._value = value
  
  def get_value(self):
    return self._value

  def set_value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")


  value = property(get_value, set_value,) 

  def is_sentence(self):
    if "." in self.value:
    # if self.value.__contains__("."):
    # if self._value.endswith("."):
      return True
    else:
      return False

  def is_question(self):
    # if "?" in self.value:
    if self.value.__contains__("?"):
    # if self._value.endswith("?"):
      return True
    else:
      return False

  def is_exclamation(self):
    # if "!" in self.value:
    # if self.value.__contains__("!"):
    if self._value.endswith("!"):
      return True
    else:
      return False
  
  def count_sentences(self):
    for n in range(len(self.value)):
      print(n)
    pass

  def count_sentences(value):
    for n in range(len(value)):
      print(n)

  def count_sentences(self):    
    words = self.value.split(" ")
    words_ending_with_punctuation = []
    for word in words:
      if word.endswith("!") or word.endswith(".") or word.endswith("?"):
        words_ending_with_punctuation.append(word)
    print(words_ending_with_punctuation)
    return len(words_ending_with_punctuation)