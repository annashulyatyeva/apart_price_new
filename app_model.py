import streamlit as st
import pickle
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge,Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import SelectFromModel


st.write("# Узнай актуальную цену квартиры в НН")
st.write("##### Отказ от ответственности: Пользователь использует приложение на свой страх и риск.")

area1 = st.slider(
    '### Площадь квартиры (кв.м.):',
    min_value=15.0,
    max_value=100.0,
    value=50.0,
    step=1.0
)

district = st.selectbox(
    "Район",
    ['Автозаводский район', 'Советский район', 'Канавинский район',
       'Московский район', 'дер. Анкудиновка', 'Приокский район',
       'Нижегородский район', 'Сормовский район', 'Ленинский район']
)

building_type = st.selectbox(
    "Материал стен",
    ['кирпич', 'панель', 'шлакоблок', 'блок+утеплитель', 'дерево',
       'монолитный железобетон']
)
year = st.slider(
    '### Год постройки:',
    min_value=1917,
    max_value=2027,
    value=2000,
    step=1
)
rooms = ["Студия", "Однокомнатная", "Двухкомнатная", "Трехкомнатная", " Четырехкомнатная"]
rooms_count = st.selectbox(
    "Комнаты",
    rooms,
    index = 2
)
rooms2count = dict(zip(rooms, [0.8, 1,2,3,4]))

no_first_no_last = st.checkbox("Не первый не последний этаж", value=True)

kitchen = ["Меньше 6м2", "От 6м2 до 12м2", "От 12м2 до 18м2", "От 18м2 до 24м2", "24м2 и больше"]

kitchen_count = st.selectbox(
    "Площадь кухни",
    kitchen,
    index = 1
)

area3_bins = dict(zip(kitchen, [0, 1, 2, 3, 4]))

appart =dict(zip(
    ['area1', 'district', 'building_type', 'year', 'rooms', 'no_first_no_last', 'area3_bins'],
    [area1, district, building_type, year, rooms2count[rooms_count], no_first_no_last, area3_bins[kitchen_count]]
))

new = pd.DataFrame(appart, index=[0])

st.write(new)


model_pkl_file = "models/apartment_prices_regression.pkl"
with open(model_pkl_file, 'rb') as file:
    model = pickle.load(file)


st.write("## Оценочная стоимость квартиры:","{:,}".format(int(model.predict(new)[0])))


