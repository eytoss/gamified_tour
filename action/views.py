import json
import apiai
from django.http import HttpResponse
from location.models import UserPositionHistory

CLIENT_ACCESS_TOKEN = '6e7c2f9db6c846e7bd71b417170a5c1f'

def welcome(request):
    # TODO: remove below fake creating
    pos = UserPosition.objects.create(
        position_x = 3,
        position_y = 4
    )
    return HttpResponse("There is no spoon. You know where you are.")

#@app.route('/hack/actions/text/', methods=["POST"])
def user_actions_text(request):
    """
    return text-based response on given text
    # TODO: need to configure and heavily train our API.AI agent
    """
    req_info = json.loads(request.body)
    text = req_info.get("text", "hello")
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    ai_request = ai.text_request()
    ai_request.lang = 'en'
    ai_request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
    ai_request.query = text
    ai_response = ai_request.getresponse()
    ai_response_str = ai_response.read().decode('utf-8')
    ai_response_json = json.loads(ai_response_str)
    res_text = ai_response_json["result"]["fulfillment"]["speech"]

    example_res = {
        "user_guid": "",
        "exhibit_guid": "",
        "session_id": "",
        "timestamp": "2017-09-15T15:52:32.901Z",
        "resolved_query": text,
        "solved_intent": "small_talk",
        "fulfillment": {
            "context_id": "",
            "speech": res_text
        }
    }
    return HttpResponse(json.dumps(example_res))

