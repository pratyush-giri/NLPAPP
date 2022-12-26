import paralleldots


class  API:

    def __init__(self):
        paralleldots.set_api_key('tYiB5P1Tr5k8UTRDVWMgzAXaA8fwA2bKrNrILzAxDsM')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)

        return  response
    
    def ner_analysis(self,text):
        response = paralleldots.ner(text)
        return response

