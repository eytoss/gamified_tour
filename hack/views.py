import json
from django.shortcuts import render
from django.http import HttpResponse
from location.models import UserPosition
from location import utils as location_utils

def welcome(request):
    return HttpResponse("In Hack: There is no spoon. You know where you are.")

# @app.route('/hack/user/positions/reach/', methods=["POST"])
def hack_positions_reach(request):
    """
    """
    # TODO: remove below hardcorded exhibit, get info from table `exhibit`
    #   let exhibit A be at (3, 4) with visible range of 5.
    json_request = json.loads(request.body)
    position = json_request["position"]
    distance, _, _ = location_utils.get_distance_range(position["x"], position["y"], 3, 4, "veryHigh")
    found_exhibit = False
    exhibit_info = {}
    # TODO: use position_info["accuracy"] "+/- 1.8m" to adjust the below inequation
    if distance <= 5:
        found_exhibit = True
        exhibit_info = {
            "distance": distance,
            "guid": "<place_holder>",
            # TODO: get actual actions of found exhibit from table `exhibit_actions`
            "actions": [
                {
                    "guid": "<place_holder>",
                    "type": "take_photo",
                    "detail": "Phote should be taken with AR's full face captured."
                },
                {
                    "guid": "<place_holder>",
                    "type": "get_welcome_message",
                    "detail": "Back up, you are too close!"
                }
            ]
        }
    example_res = {
        "found_exhibit": found_exhibit,
        "exhibit": exhibit_info,
        "code": 200 # TODO: add error handling
    }
    return HttpResponse(json.dumps(example_res))


