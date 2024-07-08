import google.generativeai as genai

def gemini(key):
    genai.configure(api_key = key)
    safety_settings = [{'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT',
                        'threshold': 'BLOCK_NONE'},
                        {
                        'category': 'HARM_CATEGORY_HATE_SPEECH',    
                        'threshold': 'BLOCK_NONE'
                        },
                        {
                        'category': 'HARM_CATEGORY_HARASSMENT',
                        'threshold': 'BLOCK_NONE'
                        },
                        {
                        'category': 'HARM_CATEGORY_DANGEROUS_CONTENT',
                        'threshold': 'BLOCK_NONE'
                        }
                    ]

    model = genai.GenerativeModel(model_name = "gemini-1.0-pro",
                                  generation_config = {'temperature':0.9},
                                  safety_settings=safety_settings)
    return model