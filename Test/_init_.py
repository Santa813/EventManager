import cv2
from pyzbar.pyzbar import decode
import streamlit as st

def main():
    st.title("QR Code Scanner App")

    # Initialize session state to store button state and QR code information
    if 'button_state' not in st.session_state:
        st.session_state.button_state = False

    if 'qr_code_info' not in st.session_state:
        st.session_state.qr_code_info = ""

    # Create a button to start/stop the scanning process
    if st.button("Toggle Scanning", key="toggle_scanning"):
        st.session_state.button_state = not st.session_state.button_state
        toggle_scanning()

    # Display the QR code information
    st.info(f"QR Code Information: {st.session_state.qr_code_info}")

def toggle_scanning():
    cap = cv2.VideoCapture(0)

    while st.session_state.button_state:
        ret, frame = cap.read()

        # Convert the frame to grayscale for QR code decoding
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Decode QR codes
        decoded_objects = decode(gray)

        # Draw rectangles around the QR codes
        for obj in decoded_objects:
            points = obj.polygon
            if len(points) == 4:
                hull = cv2.convexHull(points)
                cv2.polylines(frame, [hull], True, (0, 255, 0), 2)

                # Get the QR code data
                qr_data = obj.data.decode('utf-8')

                # Store the QR code information in session state
                st.session_state.qr_code_info = qr_data

                # Display the QR code information
                st.info(f"QR Code Information: {qr_data}")

        # Display the camera feed in the sidebar
        # st.sidebar.image(frame, channels="BGR", use_column_width=True)
        st.camera_input("Capture Image")

    # Release the camera and close the window when done
    cap.release()

if __name__ == "__main__":
    main()
