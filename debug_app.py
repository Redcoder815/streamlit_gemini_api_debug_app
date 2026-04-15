import streamlit as st
from api_calling import debug_error
from PIL import Image

st.title("Debug and solution")
st.markdown("Input images for debug and solution")
st.divider()

with st.sidebar:
    st.header("Controls")
    images = st.file_uploader("Upload images of your error", type=["jpg", "jpeg", "png"], accept_multiple_files = True)
    
    pil_images = []
    for img in images:
        pil_images.append(Image.open(img))
        
    if images:
        if len(images) > 3:
            st.error("Please upload at max 3 images")
        else:
            st.subheader("Uploaded Images")
            col = st.columns(len(images))

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)

    #select box
    selected_option = st.selectbox("Select ",("Hints", "Solution with code"), index = None)

    if selected_option:
        st.markdown(f"You selected **{selected_option}** as debug option")
    else:
        st.error("Please select a debug option")

    pressed = st.button("Debug code", type = "primary")

if pressed:
    if not images:
        st.error("Please upload images")
    if not selected_option:
        st.error("Please select the way of debug")

    if images and selected_option:
        #quiz
        with st.container(border = True):
            st.subheader(f"Debug ({selected_option})")
            with st.spinner("AI is generating debug for you..."):
                quizzes = debug_error(pil_images, selected_option)
                st.markdown(quizzes)