import pandas as pd

# Series - a one-dimensional labeled array
# DataFrame - a two-dimensional labeled data structure

# Diff b/w excel and csv file 
# , is a concatination operator

# data = pd.read_csv('data.csv')
# print('this is a csv file \n' , data)


# xl_data = pd.read_excel('data.xlsx')
# print(xl_data)



# data = pd.read_csv('data.csv')
# data = pd.read_csv('data.csv',names=['no','student','course'])
# data = pd.read_csv('data.csv',names=['no','student','course'],skiprows=[0])
# data = pd.read_csv('data.csv',usecols=['sno','Name'])
# data = pd.read_csv('data.csv',nrows=3)
# data = pd.read_csv('data.csv',parse_dates=['sno'])

# data_from_url = "https://media.geeksforgeeks.org/wp-content/uploads/20241121154629307916/people_data.csv"

# data = pd.read_csv(data_from_url)



# print(data)
# print(data.info())


# Excel
file = 'data.xlsx'

exl_data_s1 = pd.read_excel(file,sheet_name=0)
exl_data_s2 = pd.read_excel(file,sheet_name=1)

full_data = pd.concat([exl_data_s1,exl_data_s2])
# full_data = pd.concat([exl_data_s1,exl_data_s2,exl_data_s1])
# print(full_data)
# print(full_data)
# print(full_data.head(2))
# print(full_data.tail(2))
# print(full_data.shape)
# print(full_data.sort_values(['sno'], ascending = False))
# print(full_data.sort_values(['sno'], ascending = True))
# print(full_data.describe())
# print(full_data['sno'].mean())
# print(full_data['sno'].count())
# print(full_data['sno'].max())


# export_file = full_data.describe()
# export_file.to_excel('abc.xlsx')
# export_file.to_csv('abc.csv')

# data = pd.read_excel('abc.xlsx')
# print(data)

