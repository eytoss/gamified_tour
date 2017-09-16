import json
import math
from django.http import HttpResponse
from location.models import Position

def welcome(request):
	# TODO: remove below fake creating
    pos = Position.objects.create(
        position_x = 3,
        position_y = 4
    )
    return HttpResponse("There is no spoon. You know where you are.")


# @app.route('/hack/user/positions/reach/', methods=["POST"])
def user_positions_reach(request):
    """
    """
    # TODO: remove below hardcorded exhibit, get info from table `exhibit`
    #   let exhibit A be at (3, 4) with visible range of 5.
    json_request = json.loads(request.body)
    position = json_request["position"]
    distance, _, _ = _get_distance_range(position["x"], position["y"], 3, 4, "veryHigh")
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

# ref. http://developer.estimote.com/indoor/ios-tutorial/
ACCURACY_DEF = {
    "veryHigh": 1,
    "high": 1.62,
    "medium": 2.62,
    "low": 4.24,
    "verylow": 50,
    "unknown": None
}

def _get_distance_range(x_1, y_1, x_2, y_2, accuracy):
    """
    based on accuracy level of the detected postion
    return (distance, lower_bound, upper_bound)
    """
    distance = _get_distance(x_1, y_1, x_2, y_2)
    dist_delta = ACCURACY_DEF[accuracy]
    return (distance, max(distance-dist_delta, 0), distance+dist_delta)

def _get_distance(x_1, y_1, x_2, y_2):
    """
    return distance between two points
    TODO: potential improvement
        return orientation info:
        For example orientation=0 means (x_1, y_1) is to the north of (x_2, y_2)
    """
    return math.sqrt(math.pow(abs(x_2-x_1), 2) + math.pow(abs(y_2-y_1), 2))
