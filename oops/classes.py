class Data_Structures:
  def __init__(self, *args, **kwargs):
    self.name = kwargs['name']

  def __repr__(self):
    return f"Data Structure is a collection of Classes"

class Stack:
  def __init__(self, *args):
    self.name = args

  def __repr__(self):
    return f"this is stack"

class Queue(Data_Structures):
  def __init__(self, *args):
    self.name = args

  def __repr__(self):
    return f"this is stack"
  



# class Listl(Linked): 


# an_obj = Linked('swld', name="bac")

# print(isinstance(an_obj, Linked))