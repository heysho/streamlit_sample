import streamlit as st
from PIL import Image

#テキスト関連

st.title('Sho App')
st.caption('これはしょうの動画用のテストアプリです。')
st.subheader('自己紹介')
st.text('Pythonに関する情報をYouTube上で公開しているShoです。\n'
        'よろしければチャンネル登録をお願いします。')
code = '''
import streamlit as st

st.title('Shoアプリ')
'''
st.code(code, language='python')

# 画像
image = Image.open('ai-shiba.png')
st.image(image, width=200)

with st.form(key='profile_form'):
    # テキストボックス  
    name = st.text_input('名前')
    address = st.text_input('住所')

    # セレクトボックス
    age_category = st.selectbox(
        '年齢層',
        ('子供（18才未満）','大人（18歳以上）')
    )

    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'ようこそ！{name}さん！{address}に書籍を送りました！')
    

