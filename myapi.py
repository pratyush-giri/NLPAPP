import paralleldots


class  API:

    def __init__(self):
        paralleldots.set_api_key(<API KEY>)

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)

        return  response
    
    def ner_analysis(self,text):
        response = paralleldots.ner(text)
        return response

