import streamlit as st
import time

# Enter title
st.title('Streamlit Newbie')

# adding text
st.write('Display Progress Bar')
'Start!'

latest_iteration = st.empty()  # 空の要素を格納。用意しておく
bar = st.progress(0)  # 0〜100または0.0〜1.0を指定

for i in range(100):
    # 上で定義したlatest_iterationの箇所にテキストを上書きしていく
    latest_iteration.text(f'Iteration {i+1}')
    # Progress Barを上書き
    bar.progress(i + 1)
    time.sleep(0.1)  # 0.1秒ストップ

left_column, right_column = st.columns(2)  # 数値はカラム数
button = left_column.button('Display in Right column.')
if button:
    right_column.write('This is Right column.')

expander1 = st.expander('Contact1')
expander1.write('Write your detail.')
expander2 = st.expander('Contact2')
expander2.write('Write your detail.')
