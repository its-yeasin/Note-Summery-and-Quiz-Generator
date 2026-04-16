import streamlit as st
from PIL import Image
from api_calling import generate_note, generate_audio



# Sidebar
with st.sidebar:
    st.header("Controls")

    # Uploaded images
    images = st.file_uploader("Upload the photos of your note", type=["png", "jpg", "jpeg"], accept_multiple_files=True, )
    pil_images = [Image.open(img) for img in images if images]

    if images:
        if len(images) > 3:
            st.error("Maximum 3 images allowed")
        else:
            st.subheader("Uploaded images")
            col = st.columns(len(pil_images))
            for i, image in enumerate(pil_images):
                with col[i]:
                    img = image.resize((200, 200))
                    st.image(img, use_container_width=False )


    # Difficulty Selector
    difficulty  = st.selectbox("Enter the difficulty of your quiz", ("Easy", "Medium", "Hard"), index=None)

    # Action button
    pressed =  st.button("Click the button to initiate AI", type="primary")


st.header("Note Summary and Quiz Generator")
st.text("Upload upto 3 images to generate Note summary and Quizzes")

st.divider()


if pressed and not difficulty:
    st.error("You must select a difficulty")

# Note container
if pressed and pil_images:
    with st.container(border=True):
        st.subheader("Your note")
        
        with st.spinner("AI is generating your notes..."):
            note_summery = generate_note(pil_images)

        if note_summery:
            st.markdown(note_summery)



# Audio container
    with st.container(border=True):
        st.subheader("Transformed audio")
        with st.spinner("Transforming audio..."):
            if note_summery:
                clean_text = note_summery.replace("*", "")
                clean_text = note_summery.replace("#", "")
                clean_text = note_summery.replace('"', "")
                clean_text = note_summery.replace("-", "")
                clean_text = note_summery.replace("`", "")
                audio_buffer = generate_audio(clean_text)
            st.audio(audio_buffer)


# Quiz container
# with st.container(border=True):
#     st.subheader("Quizzes")

