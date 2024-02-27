import cv2
import numpy as np
import streamlit as st
from streamlit import session_state
from PIL import Image
from DataEntry import write
from TimeEntry import write_time

def scan_QR(image):
    img = Image.open(image)
    ocvImg=np.array(img)
    qrDetect =cv2.QRCodeDetector()
    data = qrDetect.detectAndDecode(ocvImg)
    return data[0]

def main():
    hide_streamlit_style = """
                <style>
                footer {
                    visibility: hidden;
                }
                footer:after {
                    content:'Made by Santa & Coding Saints';
                    font-weight: bold;
                    text-align: right;
                    font-size: 20px;
                    visibility: visible;
                    display: block;
                    position: absolute;
                    padding-right: 15px;
                    # top: 2px;
                    right: 0px;
                    bottom: 0px;
                }
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    flag=False

    st.title("Event Manager App")

    st.subheader("Scanner")
    toggle_scanning = st.radio('s',["Start","Stop"],label_visibility="collapsed")

    col1, col2 ,col3 = st.columns(3)

    with col1:
        selected_action = st.radio("Select a Action", ["Goodies", "Breakfast", "Lunch", "Snacks", "Check In/Out"])
        st.write(f"You selected: {selected_action}")

    with col2:
        if selected_action=="Check In/Out":
            in_out = st.radio("Select Check In or Out", ['Check In', 'Check Out'])
            st.write(f"You selected: {in_out}")

    with col3:
        st.header('')
        if toggle_scanning=="Start":
            image=st.sidebar.camera_input("Capture Image", label_visibility="collapsed", key='-ImgCap-')

            if session_state['-ImgCap-']:
                st.sidebar.image(session_state['-ImgCap-'])
                st.sidebar.write(session_state['-ImgCap-'])
                
            if session_state['-ImgCap-']:
                if scan_QR(session_state['-ImgCap-']):
                    data = scan_QR(session_state['-ImgCap-'])
                    if selected_action=="Check In/Out":
                        data=data+", "+in_out
                        write_time(data)
                        st.info(data)
                    else:
                        data=data+", "+selected_action
                        write(data)
                        st.info(data)

if __name__=="__main__":
    main()

# st.write(session_state)

