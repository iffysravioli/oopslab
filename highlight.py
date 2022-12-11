import sys
import subprocess

student_file = "code/fizz_buzz.py"
expected_output = "['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']"
with open(student_file, "r") as code:
  student_code = code.readlines()
  
def check_output(file, expected_output):
  student_output = subprocess.check_output(["python3", file]).rstrip().decode("utf-8")
  return student_output == expected_output

def check_div_3(code):
  has_div_3 = False
  for line in code:
    if "% 3 == 0" in line:
      has_div_3 = True
  return has_div_3

def check_div_5(code):
  has_div_5 = False
  for line in code:
    if "% 5 == 0" in line:
      has_div_5 = True
  return has_div_5

def check_div_3_5(code):
  has_div_3_5 = False
  for line in code:
    if "% 3 == 0" in line and "% 5 == 0" in line:
      has_div_3_5 = True
  return has_div_3_5

def check_typecast(code):
  has_typecast = False
  for line in code:
    if "str" in line:
      has_typecast = True
  return has_typecast

def check_append(code):
  has_append = False
  for line in code:
    if ".append" in line:
      has_append = True
  return has_append

if not check_output(student_file, expected_output):
  print("<h2>Test did not pass</h2>")
  print(f"Output did not match: {expected_output}\n")
  
if not check_div_3(student_code):
  print("<h2>Test did not pass</h2>")
  print("Did not see <code>% 3 == 0</code> in student code\n")
  
if not check_div_5(student_code):
  print("<h2>Test did not pass</h2>")
  print("Did not see <code>% 5 == 0</code> in student code\n")
  
if not check_div_3_5(student_code):
  print("<h2>Test did not pass</h2>")
  print("Did not see <code>% 3 == 0</code> and <code>% 5 == 0</code> in student code\n")
  
if not check_typecast(student_code):
  print("<h2>Test did not pass</h2>")
  print("Student code did not typecast integers as strings\n")
  
if not check_append(student_code):
  print("<h2>Test did not pass</h2>")
  print("Student code did not append string to the list <code>result</code>\n")
  
if check_output(student_file, expected_output) and \
   check_div_3(student_code) and \
   check_div_5(student_code) and \
   check_div_3_5(student_code) and \
   check_typecast(student_code) and \
   check_append(student_code):
  print("<h2>Test passed!</h2>")
  sys.exit(0)
else:
  sys.exit(1)
