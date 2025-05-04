#Load libraries needed
import streamlit as st


# Set page configuration 
st.set_page_config(
    page_title="Khoá luận tốt nghiệp",
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




# Set the background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background: url("https://images.fpt.shop/unsafe/filters:quality(90)/fptshop.com.vn/uploads/images/tin-tuc/175505/Originals/background-xanh-la%20(4).jpg");
    background-size: 100vw;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
.image-logo{
    width: 200px;
    border-radius: 10px;
}
.container *{
    text-align:center;
    color: #362670;
}
</style>
"""


giangvien = """
<div class="container slide-in-animation">
<h3>Giảng viên hướng dẫn:</h3>
<ul style="list-style-type:none; color:blue">
  <li><h4 style="list-style-type:none; color:white">TS TRỊNH TẤN ĐẠT</h4></li>
  <li><h4 style="list-style-type:none; color:white">TS NGUYỄN THỊ TUYẾT NAM</h4></li>
</ul>
</div>
"""

sinhvien = """
<div class="container slide-in-animation">
<h3>Sinh viên thực hiện: LÊ NHẬT HUY</h3>
</div>
"""

title = '''
    <h1  style="text-align:center; color: #0089E1" class="slide-in-animation"> Dự đoán nồng độ kim loại trong bụi mịn PM2.5 <br>bằng phương pháp học sâu</h1>
'''

st.markdown(background_image, unsafe_allow_html=True)
st.image("logo/logover3-1.png", width=400)
st.markdown(title, unsafe_allow_html=True)
st.markdown(sinhvien, unsafe_allow_html=True)
st.markdown(giangvien, unsafe_allow_html=True)



# Add CSS for animation
st.write("""
    <style>
        @keyframes slide-in {
            0% {
                transform: translateX(-100%);
            }
            100% {
                transform: translateX(0);
            }
        }
        .slide-in-animation {
            animation: slide-in 1.5s ease-in-out;
        }
    </style>
""", unsafe_allow_html=True)


# Add CSS for animation
st.write("""
<style>
    @keyframes slide-in {
        0% {
            transform: translateX(-100%);
        }
        100% {
            transform: translateX(0);
        }
    }
    .slide-in-animation {
        animation: slide-in 1.5s ease;
    }
</style>
""", unsafe_allow_html=True)


