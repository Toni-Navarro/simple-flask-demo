# WEBHOOK FOR CALLING DIALOGFLOW API (WHATSAUTO GATEWAY)

# import flask dependencies
from flask import Flask, request, make_response, jsonify



# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Probando, probando!'

'''
# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('action')

    # return a fulfillment response
    return {'fulfillmentText': 'Vete a la mierda. Desde el gateway'}
'''


# create a route for webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    
    
    print(request.form.get('app'))
    print(request.form.get('sender'))
    print(request.form.get('message'))
#    app = request.json['app']
#    sender = request.json['sender']
#    message = request.json['message']
    
    print('hola carapolla server')
    
    # return response
    return {'reply': 'Vete a la mierda. Desde el gateway'}

# create a route for webhook
@app.route('/detect_intent_text', methods=['POST'])
#def detect_intent_texts(project_id = 'irene-faab', session_id = 123456789, texts = request.form.get('message'), language_code = 'es'):

def detect_intent_text():
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    import dialogflow_v2 as dialogflow
    
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:\irene-faab-be926f8ee95d.json"
    
    project_id = 'irene-faab'
    session_id = 123456789
    text = request.form.get('message')
    language_code = 'es'
    
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))


    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
       response.query_result.intent.display_name,
       response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
       response.query_result.fulfillment_text))
    
    return {'reply': response.query_result.fulfillment_text}

# run the app
if __name__ == '__main__':
   app.run()
