import json
from django.shortcuts import render
from django.http import HttpResponse
from location.models import UserPositionHistory
from location.models import ExhibitPosition
from location import utils as location_utils

def welcome(request):
    return HttpResponse("In Hack: There is no spoon. You know where you are.")

# @app.route('/hack/user/positions/reach/', methods=["POST"])
def hack_positions_reach(request):
    """
    """
    json_request = json.loads(request.body)
    position = json_request["position"]
	# use visible rectangle instead of visible circle, to shorten response time.
    x = position["x"]
    y = position["y"]
    accuracy = position["accuracy"]
    orientation = position["orientation"]
    location_id = position["location_id"]
    # record user position history
    UserPositionHistory.objects.create(
		position_x=x, position_y=y, position_accuracy=accuracy,
		position_orientation=orientation, location_id=location_id
	)
    visible_exhibits = ExhibitPosition.objects\
        .filter(position_x_left__lte=x)\
        .filter(position_x_right__gte=x)\
        .filter(position_y_lower__lte=y)\
        .filter(position_y_upper__gte=y)
    #distance, _, _ = location_utils.get_distance_range(position["x"], position["y"], 3, 4, "veryHigh")
    found_exhibit = False
    exhibit_info = {}
    # TODO: use position_info["accuracy"] "+/- 1.8m" to adjust the below inequation
    if len(visible_exhibits) >= 1: # TODO: need to get one and only one
        found_exhibit = True
        exhibit = visible_exhibits[0]
        exhibit_info = {
            "distance": location_utils.get_distance_range(exhibit.position_x, exhibit.position_y, x, y, accuracy)[0],
            "guid": exhibit.guid,
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


