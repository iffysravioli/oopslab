class MyInputError:
  def _init_(self,variable="m"):
    self.variable = variable
  def _str_(self):
      return "The variable is:" + self
      raise("The variable is incorrect")
if __name__ == "__main__":
    m1 = MyInputError()
    print(m1)
    print(MyInputError)
    

if __name__=="__main__":
  print(MyInputError)
