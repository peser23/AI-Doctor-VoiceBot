import gradio as gr
from brain_of_the_doctor import encode_image, analyse_image_with_query
from voice_of_the_patient import record_audio, speech_to_text_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts_with_VoiceOutput

system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""

def process_inputs(audio_filepath, image_filepath):
    voice_model = "whisper-large-v3-turbo"
   
    speech_to_text_output = speech_to_text_with_groq(voice_file_path=audio_filepath, model=voice_model)

    # Handle the image input
    if image_filepath:
        image_model = "meta-llama/llama-4-scout-17b-16e-instruct"
        doctor_response = analyse_image_with_query(user_query=system_prompt + speech_to_text_output, 
                                                   encoded_image=encode_image(image_filepath), 
                                                   model=image_model) 
    else:
        doctor_response = "No image provided for me to analyze"

    doctor_voice_filepath = "data\\doctor_voice\\final.mp3"
    voice_of_doctor = text_to_speech_with_gtts_with_VoiceOutput(input_text = doctor_response, output_filepath=doctor_voice_filepath) 

    return speech_to_text_output, doctor_response, voice_of_doctor


# Create the interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text", lines=5),
        gr.Textbox(label="Doctor's Response", lines=10),
        gr.Audio("Temp.mp3")
    ],
    title="AI Doctor with Vision and Voice"
)

iface.launch(debug=True)