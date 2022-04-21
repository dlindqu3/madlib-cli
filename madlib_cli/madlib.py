import re 

#function1 that takes dsn.txt and takes out the {adj} {noun} etc., store in a list to be used later 

def read_template(filepath):
  # with open("./assets/dark_and_stormy_night_template.txt", "r") as f:  
  with open(filepath, "r") as f:
    stripped_str = f.read().strip()
    return stripped_str

def parse_template(template): 
  parts = []
  stripped = ""
  capturing = False 
  capture = ""
  for char in template: 
    if not capturing: 
      stripped += char 
      if char == "{":
        capturing = True
    else: 
      if char == "}": 
        stripped += char 
        parts.append(capture)
        capture = ""
        capturing = False
      else: 
        capture += char
  #this return value will be a nested tuple 
  return stripped, tuple(parts) 

# def parse_template(template):
#   #expects: ("It was a {} and {} {}.", ("Adjective", "Adjective", "Noun"))
#   # this will default to returning a tuple: return "It was a {} and {} {}.", ("Adjective", "Adjective", "Noun")
#   # with open("./assets/dark_and_stormy_night_template.txt", "r") as f:
#     # print(f, 'f')

#     regex = '{[^}]*}'
#     parts_with_curlies = str(re.findall(regex, template))
#     print('parts with curlies: ', parts_with_curlies)
#     #get words from pwc as a tuple and return that 
#     stripped = re.sub(regex, '{}', template)
#     print('stripped: ', stripped)
#     return stripped

# print(parse_template("./assets/dark_and_stormy_night_template.txt"))


def merge(stripped_template, parts):
  # *parts unpacks the tuple 
  return stripped_template.format(*parts)

def collect_input(parts): 
  result = []
  for part in parts: 
    response = input(f'enter a {part} ')
    result.append(response)
  return result

if __name__ == "__main__": 
  print('Welcome to our madlib cli. We will take your text input from the command line, then put each word of input into our madlib to make a complete text.')
  path = "assets/dark_and_stormy_night_template.txt"
  template = read_template(path)
  stripped, parts = parse_template(template)
  responses = collect_input(parts) 
  merged = merge(stripped, responses)
  print(merged)
  out_path = path.replace(".txt", "_completed.txt")
  with open(out_path, "w") as f: 
    f.write(merged)
  
  

