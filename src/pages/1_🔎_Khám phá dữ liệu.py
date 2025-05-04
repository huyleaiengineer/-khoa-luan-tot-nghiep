##Load libraries
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly
# import july
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler

st.set_page_config(
    page_title="Khám phá dữ liệu",
    page_icon="./logo/logo.png",
    layout="wide"
)

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-image: linear-gradient(rgb(193, 212, 208), rgb(219, 225, 218));
    }
</style>
""", unsafe_allow_html=True)

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background: url("https://images.fpt.shop/unsafe/filters:quality(90)/fptshop.com.vn/uploads/images/tin-tuc/175505/Originals/background-xanh-la%20(4).jpg");
    background-size: 100vw;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
"""
st.markdown(background_image, unsafe_allow_html=True)


# Define functions
def load_data(path):
    dataset = pd.read_csv(path)
    dataset=dataset.set_index(dataset.Date)
    dataset.index = pd.to_datetime(dataset.index)
    dataset.drop(columns=['Date'], inplace=True)
    return dataset

df = None

def get_season(month):
    if month in [12, 1, 2]:
        return 'Đông'
    elif month in [3, 4, 5]:
        return 'Xuân'
    elif month in [6, 7, 8]:
        return 'Hạ'
    else:
        return 'Thu'

# Define section
data = st.container()

# Set up the data section that users will interact with
with data:
    data.title("KHÁM PHÁ DỮ LIỆU")
    st.write("")
    option = st.selectbox(
    'Chọn tập dữ liệu',
    (
     'Tập dữ liệu 2019 (dự đoán nồng độ kim loại trong bụi mịn PM2.5)',
     'Tập dữ liệu từ 2020-2023 (dự đoán nồng độ kim loại trong bụi mịn PM10)'))



    if option == 'Tập dữ liệu 2019 (dự đoán nồng độ kim loại trong bụi mịn PM2.5)':
        df = load_data('Dataset/Merge_2019_PM25_KNN_Impute.csv')
    else:
        df = load_data('Dataset/Merge_2020_2023_PM10_KNN_Impute.csv')

    st.subheader("Tổng quan về dữ liệu")
    # Button to preview the dataset
    tab1, tab2, tab3 = st.tabs(["Dữ liệu",
                                "Các dữ liệu thống kê",
                                "Các dữ liệu dự đoán"])
    with tab1:
        st.header(option)
        st.write(df)
    with tab2:
        st.header("Thống kê")
        st.write(pd.DataFrame(df.describe()))
    with tab3:
        st.header("Nồng độ các kim loại cần dự đoán")
        st.write(df[df.columns[-6:]])

    # Button to view the chart

    st.subheader("Trực quan hóa dữ liệu")
    tab1, tab2, tab3, tab4= st.tabs(["Biểu đồ đường",
                                "Biểu đồ tần suất",
                                "Biểu đồ cột",
                                "Biểu đồ nhiệt",
                                ])
    with tab1:
        x = df.columns
        option = st.multiselect(
            'Chọn đặc trưng', x)
        # st.write('You selected:', option)
        st.title("Biểu đồ đường")
        st.line_chart(df[option])

    with tab2:
        x = df.columns
        option = st.selectbox(
            'Chọn đặc trưng', x)

        st.markdown("### Biều đồ tần suất của " + option)
        fig = px.histogram(df[option])
        st.plotly_chart(fig, theme="streamlit")

        if st.button("Chuẩn hóa MinMax"):
            X = pd.DataFrame(df[option])
            X = MinMaxScaler().fit_transform(X)
            st.markdown("### Biều đồ tần suất của " + option + " sau khi chuẩn hóa dùng MinMaxScaler")
            fig = px.histogram(X)
            st.plotly_chart(fig, theme="streamlit")
        if st.button("Chuẩn hóa kiểu Standard Scaler"):
            X = pd.DataFrame(df[option])
            X = StandardScaler().fit_transform(X)
            st.markdown("### Biều đồ tần suất của " + option + " sau khi chuẩn hóa dùng StandardScaler")
            fig = px.histogram(X)
            st.plotly_chart(fig, theme="streamlit")

    with tab3:
        k = -6
        if (len(df)!=7237):
            k = -4

        x = df.columns[k:]
        option1 = st.selectbox(
            'Chọn đặc trưng muốn vẽ', x)
        option2 = st.selectbox(
            'Chọn chu kỳ',
            ('tuần',
             'tháng',
             'mùa'))
        st.title("Trung bình độ kim loại  " + option1 + " theo " + option2)
        if option2 == 'tuần':
            df['weeks'] = df.index.strftime("%U").astype('int')
            df = df.groupby(['weeks']).mean()
            # st.pyplot(df[option1])
            # df = df_new.copy()
        elif option2=='tháng':
            df['month'] = df.index.strftime("%m").astype('int')
            df = df.groupby(['month']).mean()
        else:
            df['month'] = df.index.strftime("%m").astype('int')
            df['season'] = df['month'].apply(get_season)
            df = df.groupby(['season']).mean()
        fig = px.bar(df[option])
        st.plotly_chart(fig, theme="streamlit")

    with tab4:
        st.subheader("Ma trận tương quan")
        st.write(df.corr())
        plt.figure(figsize=(8, 8))
        sns.heatmap(df.corr(), annot=False)
        st.pyplot(plt)











