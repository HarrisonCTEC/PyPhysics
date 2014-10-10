#!/usr/local/env python3

class Kilograms:

  def __init__(self, kilograms=None, pounds=None):
    self._pound_to_kilogram = 0.453592
    if kilograms is not None:
      self.value = kilograms
      self.pounds = kilograms / self._pound_to_kilogram
    elif pounds is not None:
      self.value = pounds * self._pound_to_kilogram
      self.pounds = pounds
    else:
      raise ValueError("You must specify kilograms or pounds.")
      
  def __int__(self):
    return self.value
      
