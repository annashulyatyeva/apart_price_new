import streamlit as st
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt

model_pkl_file = "apartment_prices_regression_pca.pkl"  

with open(model_pkl_file, 'rb') as file:  
    model = pickle.load(file)

hello = st.button('Интересуетесь ценами на недвижимость?')

if hello:
    st.write('Мы поможем Вам!')    

"Узнай актуальную стоимость квартиры"

df = pd.read_csv('data/processed/nnapartment_more_info_new_features.csv') #, index_col ="Unnamed: 0")
st.sidebar.write("График зависимости цены от площади:")

arr = df['price']
Y = df['area1']
fig, ax = plt.subplots()
plt.scatter(x=arr, y=Y)
#plt.plot(y_test,y_test,'r')
plt.xlabel('Цена')
plt.ylabel('Площадь')
st.sidebar.pyplot(fig)

#ax.plot(arr, Y)
#ax.set_title('price')
#st.pyplot(fig)
#st.sidebar.pyplot(fig)

area1 = st.slider('Площадь квартиры (кв.м.):', min_value = 15, max_value = 100, value = 50, step =1)
area3_bins = st.slider('Площадь кухни (0-без кухни ... 4 огромная кухня):', min_value = 0, max_value = 4, value = 2, step =1)
rooms = st.selectbox('Количество комнат:', ("Студия", "1", "2", "3", "4+"))
if rooms == "Студия":
    rooms = 0.8
elif rooms == "1":
    rooms = 1
elif rooms == "2":
    rooms = 2
elif rooms == "3":
    rooms = 3     
elif rooms == "4+":
    rooms = 4 
    
year = st.slider('Год постройки:', min_value = 1917, max_value = 2027, value = 1980, step =1)
no_first_no_last = st.slider('Первый или последний этаж?', min_value = 0, max_value = 1, value = 0, step =1) 
building_type = st.selectbox('Материал стен:', ('кирпич', 'панель', 'шлакоблок', 'блок+утеплитель', 'монолитный железобетон', 'дерево'))

district =  st.selectbox('Район города:', ('Автозаводский район', 'Советский район', 'Канавинский район', 'Московский район', 'дер. Анкудиновка', 'Нижегородский район', 'Сормовский район', 'Ленинский район'))

data_fill_in = {'rooms': [rooms], 'area1': [area1], 'district': [district], 'building_type': [building_type], 'year': [year], 'no_first_no_last':[no_first_no_last], 'area3_bins':[area3_bins]}
df_in = pd.DataFrame(data_fill_in)

y_pred = int(model.predict(df_in))

st.write(f'## Предположительная стоимость квартиры: {y_pred}')    

#st.write("График зависимости цены от площади:")

#grafic = st.checkbox('Построить график?')
#if grafic:
    #st.write("## График предсказаний модели: ")
    #arr2 = df[(df['area1'] < (area + 9)) & (df['area1'] > (area - 9))].price
    #Y2 = df[(df['area1'] < (area + 9)) & (df['area1'] > (area - 9))].area1
    #fig, ax = plt.subplots()
    #plt.scatter(x=arr2, y=Y2)
    #plt.plot(y_pred,area,'r')
    #plt.xlabel('Цена')
    #plt.ylabel('Площадь')
    #st.pyplot(fig)

    
                    #arr2 = df['price']
                    #Y2 = 
                    #fig, ax = plt.subplots()
                    #ax.hist(arr2, bins=50)
                    #st.pyplot(fig)
                    #plt.plot(area,y_pred,'r')

agree = st.checkbox('Вам помогла наша подсказка?')

if agree:
    st.write('Супер!')

#model.predict(np.array([[30]]))

#option = st.selectbox(
   # "How would you like to be contacted?",
   # ("Email", "Home phone", "Mobile phone"))
#st.write("You selected:", option)
