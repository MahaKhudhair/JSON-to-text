import streamlit as st
import json

st.set_page_config(page_title="JSON Chat Converter", layout="wide")
st.title("JSON Chat to text Converter")

uploaded_file = st.file_uploader("Choose JSON file", type=['json'])

if uploaded_file:
  try:
      # Read the file
      content = json.load(uploaded_file)
      
      # Display content
      st.subheader("Chat Content:")
      chat_text = ""
      
      # Access the messages array from the content
      for message in content.get('messages', []):
          sender_info = message.get('sender', {})
          sender_type = sender_info.get('t', '')
          sender_name = sender_info.get('n', '')
          
          # Format sender name
          if sender_type == 'v':
              sender = "Visitor"
          else:
              sender = sender_name if sender_name else "Agent"
          
          # Get message text
          msg = message.get('msg', '')
          time = message.get('time', '')
          
          # Format chat line
          chat_line = f"[{time}] {sender}: {msg}\n\n"
          chat_text += chat_line
          st.text(chat_line)
      
      # Create download button for text
      if chat_text:
          st.download_button(
              label="Download as Text",
              data=chat_text,
              file_name="chat.txt",
              mime="text/plain"
          )
          
  except Exception as e:
      st.error(f"Error occurred: {str(e)}")

st.markdown("""
### How to use:
1. Click 'Browse files' to select a JSON file
2. Chat content will appear automatically
3. Click 'Download as Text' to save the file
""")