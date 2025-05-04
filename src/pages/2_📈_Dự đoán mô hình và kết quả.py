#Load libraries needed
import streamlit
import streamlit as st
import pandas as pd
import numpy as np
# import joblib
# from streamlit_lottie import st_lottie
from datetime import datetime
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title="Các mô hình và dự đoán",
    page_icon="./logo/logo.png",
    layout="wide"
)

# Set background ..
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



#define app section
header=st.container()
intro=st.container()
prediction=st.container()

# Define the Lottie animation URL

def load_data(path):
    dataset = pd.read_csv(path)
    dataset=dataset.set_index(dataset.Date)
    dataset.index = pd.to_datetime(dataset.index)
    dataset.drop(columns=['Date'], inplace=True)
    return dataset

test_data = None
test_result = None
train_result = None
df = None
hps = None
folder = ''
#define header
with header:
    header.title("DỰ ĐOÁN NỒNG ĐỘ KIM LOẠI TRONG BỤI MỊN PM2.5 BẰNG PHƯƠNG PHÁP HỌC SÂU")
    opt = st.selectbox("Chọn tập dữ liệu",
                       ['PM2.5(Nồng độ kim loại trong bụi mịn PM2.5 từ năm 2019)',
                        'PM10(Nồng độ kim loại trong bụi mịn PM10 từ năm 2019 đến năm 2023)'])
    if opt != 'PM2.5(Nồng độ kim loại trong bụi mịn PM2.5 từ năm 2019)':
        test_data = load_data("Dataset/test_PM10.csv")
        df = load_data("Dataset/Merge_2020_2023_PM10_KNN_Impute.csv")
        hps = pd.read_csv("Dataset/PM10_hyperparameters.csv")
        folder='pm10'
    else:
        test_data = load_data("Dataset/test_PM2.5.csv")
        df = load_data("Dataset/Merge_2019_PM25_KNN_Impute.csv")
        hps = pd.read_csv("Dataset/PM2.5_hyperparameters.csv")
        folder = 'pm25'

with intro:
    intro.markdown("## 1. Tổng quan về các mô hình áp dụng")
    option3 = st.selectbox("Các mô hình ",
                          ["Mô hình LSTM",
                           "Mô hình GRU",
                           "Mô hình BiLSTM",
                           "Mô hình Convolutional LSTM"])
    st.markdown("### "+option3)
    link_image = "images/"
    if option3 == "Mô hình LSTM":
        st.image("images/lstm.gif")
    elif option3 == "Mô hình GRU":
        st.image("images/gru.gif")
    elif option3 == "Mô hình BiLSTM":
        st.image("images/bilstm1.gif")
        st.image("images/bilstm.gif")
    else:
        st.image("images/ConvLSTM.png")

with prediction:
    prediction.markdown("## 2.Kết quả")
    option2 = st.selectbox("Các kim loại cần dự đoán ",
                          test_data.columns)
    tab1, tab2, tab3,tab4 =  st.tabs([
        'Các siêu tham số',
        'Kết quả huấn luyện', # 2 cột + biểu đồ đường so sánh
        'Kết quả đánh đánh giá', # Bảng 3 cot 2 hàng + bieu do cot so sanh
        'So sánh các mô hình ' # bảng so sánh các mô hình 6 bieu do
    ])

    with tab1:
        st.markdown("### Danh sách các siêu tham số của mô hình " + " sử dụng")
        st.write(hps)
        st.write("Riêng về ConvLSTM:")
        st.write("Kích thước kernel = 1")
        st.write("Số bộ lọc filters = 64")
    with tab2:
        st.markdown("### Bảng kết quả trên tập huấn luyện")
        bang1 = pd.read_csv("Dataset/" + folder + "/" + option2 + "/train_eval.csv")
        st.write(bang1)
        st.markdown("### Bảng kết quả trên tập kiểm tra")
        bang2 = pd.read_csv("Dataset/" + folder + "/" + option2 + "/test_eval.csv")
        st.write(bang2)
    with tab3:
        opt2 = st.selectbox("Danh sách các mô hình ",
                               ["Mô hình LSTM",
                                "Mô hình GRU",
                                "Mô hình BiLSTM"])
        if opt2 == "Mô hình LSTM":
            bang3 = pd.read_csv("Dataset/" + folder + "/" + option2 + "/data_test.csv")
            st.markdown("### Bảng dữ liệu thực tế và dữ liệu dự đoán bằng mô hình LSTM")
            st.write(bang3[['Thực tế', 'Dự đoán theo LSTM']])
            st.markdown("### Biều đồ dữ liệu thực tế và dữ liệu dự đoán bằng mô hình LSTM")
            # fig = px.line(bang3[['Thực tế', 'Dự đoán theo LSTM']], color='country')
            st.line_chart(bang3[['Thực tế', 'Dự đoán theo LSTM']], color=['#03cffc', '#fc3d03'])
        elif opt2 == "Mô hình GRU":
            st.markdown("### Bảng dữ liệu thực tế và dữ liệu dự đoán bằng mô hình LSTM")
            bang3 = pd.read_csv("Dataset/" + folder + "/" + option2 + "/data_test.csv")
            st.markdown("### Biều đồ dữ liêu thực tế và dữ liệu dự đoán bằng mô hình GRU")
            st.line_chart(bang3[['Thực tế', 'Dự đoán theo GRU']], color=['#03cffc', '#fc3d03'])
        else:
            st.markdown("### Bảng dữ liệu thực tế và dữ liệu dự đoán bằng mô hình LSTM")
            bang3 = pd.read_csv("Dataset/" + folder + "/" + option2 + "/data_test.csv")
            st.markdown("### Biều đồ dữ liêu thực tế và dữ liệu dự đoán bằng mô hnh BiLSTM")
            st.line_chart(bang3[['Thực tế', 'Dự đoán theo BiLSTM']], color=['#03cffc', '#fc3d03'])
    with tab4:

        bang3 = pd.read_csv("Dataset/" + folder + "/" + option2 + "/test_eval.csv")
        bang3 = bang3.set_index(bang3['Mô hình'])
        opt2 = st.selectbox("Chọn các độ đo",
                            bang3.columns[1:])
        st.column_config.BarChartColumn(width='small')
        st.bar_chart(bang3[opt2])
