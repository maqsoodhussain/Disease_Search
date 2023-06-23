import streamlit as st
import openai

st.set_page_config(
        page_title="SEARCH ABOUT DISEASE",
        page_icon="icon.png"
    )




openai.api_key=""




def get_responce_from_chatgpt(text):
    messages =[
        { "role":"system" , "content" : "you are trained to tell about Diseases. The discription is not more than 3000 words and less than 500 words"},
        { "role":"user" , "content": f"""Tell about this disease {text}
                                    The description should contain following formate .
                                    1.About disease.
                                    2.Symptoms of Disease.
                                    3 Caused by.
                                    4.Can be Prevented by.
                                    5.Conslusion
                                    

         """}
    ]
    
    response = openai.ChatCompletion.create(
        model ="gpt-3.5-turbo",
        messages = messages,
        max_tokens = 3000,
        n=1,
        stop= None,
        temperature=0.1
    )

    result= response.choices[0].message.content
    return result



st.title("WRITE ANY DISEASE AND CHATGPT GIVE'S YOU EVERYTHING ABOUT IT")

# model = 'gpt-3.5-turbo'
# st.text(model)
text= st.text_input("Enter Disease:", value ="Fungus") 

if st.button('Submit'):
    #we create a spinner that continues runs and get responce
    with st.spinner('OpenAI processing in Progress'):
        sentiment = get_responce_from_chatgpt(text)
        st.success("SUCCESSFULLY GENERATED : ")
        st.header(f"{sentiment}")

st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f8f9fa;
            color: #6c757d;
            text-align: center;
            padding: 10px;
        }
        </style>
        <div class="footer">
            CREATED BY MAQSOOD HUSSAIN WANI
        </div>
        """,True
    
    )
