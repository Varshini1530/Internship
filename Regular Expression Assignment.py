#!/usr/bin/env python
# coding: utf-8

# In[3]:


def replace_characters(text):
    replacements = {' ': ':', ',': ':', '.': ':'}
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text

sample_text = 'Python Exercises, PHP exercises.'
output_text = replace_characters(sample_text)
print(output_text)


# In[4]:


import re

def find_words_starting_with_a_or_e(text):
    words = re.findall(r'\b[aeAE]\w+', text)
    return words

sample_text = "Apples are awesome and elephants eat apples."
matching_words = find_words_starting_with_a_or_e(sample_text)

print("Words starting with 'a' or 'e':")
for word in matching_words:
    print(word)


# In[5]:


import re

def find_long_words(text):
    pattern = re.compile(r'\b\w{4,}\b')
    words = pattern.findall(text)
    return words

sample_text = "This is a sample text with some longer words like Python and exercise."
long_words = find_long_words(sample_text)

print("Words with at least 4 characters:")
for word in long_words:
    print(word)


# In[6]:


import re 

def find_words_of_length(text, min_length, max_length):
    pattern = re.compile(r'\b\w{' + str(min_length) + ',' + str(max_length) + r'}\b')
    words = pattern.findall(text)
    return words

sample_text = "This is a sample text with various word lengths."
min_length = 3
max_length = 5

matching_words = find_words_of_length(sample_text, min_length, max_length)

print(f"Words with lengths {min_length} to {max_length}:")
for word in matching_words:
    print(word) 


# In[7]:


import re

def remove_parentheses(strings):
    pattern = re.compile(r'\([^)]*\)')
    clean_strings = [pattern.sub('', s) for s in strings]
    return clean_strings

sample_text = [
    "example (.com)",
    "hr@fliprobo (.com)",
    "github (.com)",
    "Hello (Data Science World)",
    "Data (Scientist)"
]

cleaned_strings = remove_parentheses(sample_text)

for cleaned_string in cleaned_strings:
    print(cleaned_string)


# In[12]:


import re

sample_text = "ImportanceOfRegularExpressionsInPython"
split_strings = re.split(r'(?=[A-Z])', sample_text)

print(split_strings)


# In[13]:


import re

def insert_spaces_between_numbers(text):
    result = re.sub(r'(?<=[0-9])(?=[A-Za-z])', ' ', text)
    return result

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
output_text = insert_spaces_between_numbers(sample_text)
print(output_text)


# In[14]:


import re

def insert_spaces_between_numbers(text):
    result = re.sub(r'(?<=[0-9])(?=[A-Za-z])', ' ', text)
    return result

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
output_text = insert_spaces_between_numbers(sample_text)
print(output_text)


# In[15]:


import re

def match_pattern(text):
    pattern = re.compile(r'^[A-Za-z0-9_]+$')
    return bool(pattern.match(text))

sample_strings = [
    "Hello_World123",
    "Python3",
    "user_name",
    "Password123!",
    "123Numbers",
    "alpha_beta",
]

for string in sample_strings:
    if match_pattern(string):
        print(f"'{string}' matches the pattern.")
    else:
        print(f"'{string}' does not match the pattern.")


# In[16]:


def starts_with_number(text, number):
    return text.startswith(str(number))

sample_strings = [
    "123abc",
    "456xyz",
    "789start",
    "987end",
    "abc123",
]

specific_number = 123

for string in sample_strings:
    if starts_with_number(string, specific_number):
        print(f"'{string}' starts with the number {specific_number}.")
    else:
        print(f"'{string}' does not start with the number {specific_number}.")


# In[17]:


def remove_leading_zeros(ip_address):
    components = ip_address.split('.')
    cleaned_components = [str(int(component)) for component in components]
    cleaned_ip_address = '.'.join(cleaned_components)
    return cleaned_ip_address

ip_addresses = [
    "192.168.001.001",
    "010.010.010.010",
    "001.002.003.004",
    "127.0.0.1",
    "000.000.000.000",
]

for ip_address in ip_addresses:
    cleaned_ip = remove_leading_zeros(ip_address)
    print(f"Original: {ip_address} | Cleaned: {cleaned_ip}")


# In[18]:


def search_words(text, searched_words):
    found_words = [word for word in searched_words if word in text]
    return found_words

sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']

found_words = search_words(sample_text, searched_words)

for word in found_words:
    print(f"'{word}' found in the text.")


# In[19]:


def search_word_with_location(text, searched_word):
    found_locations = []
    start = 0
    while True:
        index = text.find(searched_word, start)
        if index == -1:
            break
        found_locations.append(index)
        start = index + 1

    return found_locations

sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_word = 'fox'

found_locations = search_word_with_location(sample_text, searched_word)

if found_locations:
    print(f"'{searched_word}' found at locations:")
    for location in found_locations:
        print(f"Position {location}")
else:
    print(f"'{searched_word}' not found in the text.")


# In[20]:


def find_substrings(text, pattern):
    found_indices = []
    start = 0
    while True:
        index = text.find(pattern, start)
        if index == -1:
            break
        found_indices.append(index)
        start = index + len(pattern)

    return found_indices

sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

found_indices = find_substrings(sample_text, pattern)

if found_indices:
    print(f"'{pattern}' found at positions:")
    for index in found_indices:
        print(f"Position {index}")
else:
    print(f"'{pattern}' not found in the text.")


# In[21]:


def find_substring_occurrences(text, substring):
    occurrences = []
    start = 0
    while True:
        index = text.find(substring, start)
        if index == -1:
            break
        occurrences.append(index)
        start = index + len(substring)
    
    return occurrences

sample_text = 'Python exercises, PHP exercises, C# exercises'
substring = 'exercises'

occurrences = find_substring_occurrences(sample_text, substring)

if occurrences:
    print(f"'{substring}' occurrences:")
    for i, index in enumerate(occurrences):
        print(f"Occurrence {i+1} found at position {index}")
else:
    print(f"'{substring}' not found in the text.")


# In[22]:


def convert_date_format(date):
    parts = date.split('-')
    if len(parts) == 3:
        year, month, day = parts
        new_date = f"{day}-{month}-{year}"
        return new_date
    else:
        return "Invalid date format"

date_yyyy_mm_dd = "2023-08-21"
converted_date = convert_date_format(date_yyyy_mm_dd)

print(f"Original date: {date_yyyy_mm_dd}")
print(f"Converted date: {converted_date}")


# In[23]:


import re

def find_decimal_numbers(text):
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    decimal_numbers = pattern.findall(text)
    return decimal_numbers

sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
decimal_numbers = find_decimal_numbers(sample_text)

print(decimal_numbers)


# In[24]:


def separate_numbers_with_positions(text):
    numbers = []
    positions = []
    current_number = ''
    
    for index, char in enumerate(text):
        if char.isdigit() or char == '.':
            current_number += char
        elif current_number:
            numbers.append(current_number)
            positions.append(index - len(current_number))
            current_number = ''
    
    if current_number:
        numbers.append(current_number)
        positions.append(len(text) - len(current_number))
    
    return numbers, positions

sample_text = "This is a sample text with 123 numbers like 45.67 and 890.12."
numbers, positions = separate_numbers_with_positions(sample_text)

for number, position in zip(numbers, positions):
    print(f"Number: {number}, Position: {position}")


# In[25]:


import re

def extract_maximum_numeric_value(text):
    numbers = re.findall(r'\b\d+\b', text)
    if numbers:
        maximum_value = max(map(int, numbers))
        return maximum_value
    else:
        return None

sample_text = "My marks in each semester are: 947, 896, 926, 524, 734, 950, 642"
maximum_numeric_value = extract_maximum_numeric_value(sample_text)

if maximum_numeric_value is not None:
    print(f"The maximum numeric value is: {maximum_numeric_value}")
else:
    print("No numeric values found in the text.")


# In[26]:


import re

def insert_spaces_between_capital_words(text):
    modified_text = re.sub(r'(?<=\w)([A-Z])', r' \1', text)
    return modified_text

sample_text = "RegularExpressionIsAnImportantTopicInPython"
output_text = insert_spaces_between_capital_words(sample_text)
print(output_text)


# In[27]:


import re

pattern = r'[A-Z][a-z]+'

text = "AaBbCc AbCdEfGhIjKlM"

matches = re.findall(pattern, text)
print(matches)


# In[29]:


import re

def remove_continuous_duplicates(sentence):
    cleaned_sentence = re.sub(r'\b(\w+)\s+\1\b', r'\1', sentence, flags=re.IGNORECASE)
    return cleaned_sentence

sample_text = "Hello hello world world"
cleaned_text = remove_continuous_duplicates(sample_text)
print(cleaned_text)


# In[30]:


import re

def is_valid_string(text):
    pattern = re.compile(r'^.*[a-zA-Z0-9]$')
    return bool(pattern.match(text))

sample_strings = [
    "Hello123",
    "Test_456",
    "abc123 ",
    "ABC_",
    "12345",
]

for string in sample_strings:
    if is_valid_string(string):
        print(f"'{string}' is valid.")
    else:
        print(f"'{string}' is not valid.")


# In[31]:


import re

def extract_hashtags(text):
    pattern = re.compile(r'#\w+')
    hashtags = pattern.findall(text)
    return hashtags

sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same
has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
hashtags = extract_hashtags(sample_text)

print(hashtags)


# In[32]:


import re

def remove_special_symbols(text):
    pattern = re.compile(r'<U\+[A-F0-9]+>')
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text

sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"
cleaned_text = remove_special_symbols(sample_text)
print(cleaned_text)


# In[33]:


import re

def remove_words_with_length_between_2_and_4(text):
    pattern = re.compile(r'\b\w{2,4}\b')
    cleaned_text = pattern.sub('', text)
    return cleaned_text

sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
cleaned_text = remove_words_with_length_between_2_and_4(sample_text)
print(cleaned_text)


# In[ ]:




