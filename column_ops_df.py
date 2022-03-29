import pandas as pd

def lowercase(my_string):
  return my_string.lower()

df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
  columns=['Name', 'Email']
)

# Add column here
def lowercase(my_string):
  return my_string.lower()

df['Lowercase Name'] = df['Name'].apply(lowercase)

print(df)