import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import qrcode
from PIL import Image
import io

# 앱 제목
st.title("QR 코드 생성기")

# URL 입력 받기
url = st.text_input("QR 코드를 생성할 URL을 입력하세요:")

if url:
    try:
        # QR 코드 생성
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # QR 코드 이미지 생성
        img = qr.make_image(fill='black', back_color='white')

        # 이미지 파일로 변환
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        byte_im = buf.getvalue()

        # QR 코드 표시
        st.image(byte_im, caption='QR 코드', use_column_width=True)
        st.markdown(f"[여기서 링크 확인하기]({url})", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"QR 코드 생성 중 오류가 발생했습니다: {e}")
