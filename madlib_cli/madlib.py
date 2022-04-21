import re 

print('Welcome to our madlib cli. We will take your text input from the command line, then put each word of input into our madlib to make a complete text.')

#function1 that takes dsn.txt and takes out the {adj} {noun} etc., store in a list to be used later 

def read_template(filepath):
  with open("./assets/dark_and_stormy_night_template.txt", "r") as f:  
    stripped_str = f.read().strip()
    return stripped_str


def parse_template(my_str):

  # with open("./assets/dark_and_stormy_night_template.txt", "r") as f:
    # print(f, 'f')

    regex = '{[^}]*}'
    parts_with_curlies = str(re.findall(regex,my_str))
    print('parts with curlies: ', parts_with_curlies)
    #get words from pwc as a tuple and return that 
    stripped = re.sub(regex, '{}', my_str)
    print('stripped: ', stripped)
    return stripped

# print(parse_template("./assets/dark_and_stormy_night_template.txt"))

# terms = regex.findall(r'/{[^}]*}/g')
# cleaned_str = regex.sub(terms, '{}', input_str)

#function2 >> give user a series of inputs (number of inputs can vary based on number of spaces to fill)
#function3 >> put inputted words into madlib text

#final text: put in commandline 
#final text: put in a new .txt file


def merge():
  pass


  
  

