#!/usr/local/env python3

class Kilograms:
  _pound_to_kilogram = 0.453592

  def __init__(self, kilograms=None, pounds=None):
    if kilograms is not None:
      self.value = kilograms
      self.pounds = kilograms / _pound_to_kilogram
    elif pounds is not None:
      self.value = pounds * _pound_to_kilogram
      self.pounds = pounds
    else:
      raise ValueError("You must specify kilograms or pounds.")
      
  def __int__(self)__:
    return self.value
      
