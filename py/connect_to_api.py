# %% [markdown]
# # 1.0 Libs and Fuctions

# %%
#data manipulation libs
import tkinter
import pandas as pd
# connect to api
import requests
import time
import pyautogui as pya
# windows explorer file
from tkinter import filedialog
from tkinter import *

# %% [markdown]
# # 2.0 Connect to the API

# %%
# display a message to connect to API
print("\n ######################## API ######################")
time.sleep(2)
print("\n Connect to the API")
url = r"https://reqres.in/api/users?page=2"
response = requests.get(url)
time.sleep(3)
# display a message about the connection of the api
print(f"\n The api response was: {response}")

# %% [markdown]
# # 3.0 Get The total of Pages

# %%
# get total pages
def total_pages_show():
    global total_pages
    print('\n Collecting the total of Pages...')
    time.sleep(3)
    # collect the total of pages
    total_pages = response.json()['total_pages']
    print(f"\n The Total of pages is {total_pages}")
total_pages_show()

# %% [markdown]
# # 4.0 Download all the API content

# %%
# get a feedback by the user and use this to get the data
print("\n ########### Data Collect #########")
data_proceed = str(input("""
\n Did you wish to proceed with the data collection?
if you wish to proceed type y otherwise type n. If you type n, the Api will close.

"""))
print("\n ################################################################")
# if the data_proceed equal to 'y' then the program will download the data
if data_proceed == 'y':
    print("\n Collecting all data from Api")
    time.sleep(1)
    print("\n Organize in columns and rows")
    time.sleep(1)
    data = dict()
    for page in range(1, total_pages+1):
        response = requests.get(url=url)
        data[page] = response.json()['data']
    df = pd.concat([pd.DataFrame(data[1]), pd.DataFrame(data[2])], axis=0)
else:
    # otherwhise close the api
    print('\n The Api will be Closed')
    import pyautogui as pya
    time.sleep(3)
    print('\n ############### CLOSING THE API #############')
    time.sleep(3)
    pya.hotkey('alt','f4')

quantity_of_records = len(df)
print(f'\n we find {quantity_of_records} registers inside all pages of the api')
time.sleep(2)
print("\n Now you gonna select your directory to save your file:")
time.sleep(2)
print("\n Select your directory")
root = Tk()
dir = filedialog.askdirectory()
root.update()
root.destroy()
print(f"\n You select this directory: {dir}")
filename = str(input("""\n For save the records please insert a filename.
if you just press enter, the record will be saved with the name users.csv
type your filename:

"""))

print("\n####################################################################")
if filename == '':
    print('\n you leave your filename empty')
    new_file = 'users'
    df.to_csv(fr'{dir}/{new_file}.csv')
    time.sleep(3)
    print('\n The File was save with success.')
else:
    print(f'\n Your Filename is: {filename}')
    full_path = f'{dir}/{filename}.csv'
    df.to_csv(full_path)
    print('\n The File was save with success.')

# %%
while True:
    print("\n Now, if you want to search some user id")
    id = int(input("Please Type. Only Numbers will be accepted: "))
    df_id = df.loc[df['id']==id]
    return_df = len(df_id)
    while return_df == 0 or '':
        print("\n This user ID was not found. Try again")
        id = int(input("Please Type. Only Numbers will be accepted: "))
        df_id = df.loc[df['id']==id]
        df_id = df_id.reset_index()
        return_df = len(df_id)
    else:
        print('\n Getting the id')
        df_id = df.loc[df['id']==id]
        df_id = df_id.reset_index()
        time.sleep(2)
        print('\n Getting user name')
        name_of_user =  df_id['first_name'][0] + ' ' + df_id['last_name'][0]
        #name_of_user = name_of_user[0]
        time.sleep(1)
        print(f'\n The id {id} belongs to the user: {name_of_user}')
        time.sleep(3)
        print("\n Closing the API.")
        print('\n ############### CLOSING THE API #############')
        time.sleep(3)
        pya.hotkey('alt','f4')


# %%



