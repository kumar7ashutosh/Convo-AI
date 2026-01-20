from config.settings import Settings

settings=Settings()

def get_ollama_models():
    models_list = settings.OLLAMA_MODELS
    return [
        model.strip()
        for model in models_list.split(",")
        if model.strip()
    ]


print(get_ollama_models())