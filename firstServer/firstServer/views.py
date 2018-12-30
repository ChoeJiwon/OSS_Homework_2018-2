
from django.shortcuts import render
import pprint
from .lol import predict
def index(request):
    want_predict = len(request.GET) > 0

    if(want_predict):

        print("GET Request Data")
        pprint.pprint(request.GET)
        team_a = [
            request.GET['ATOPchampion'],
            request.GET['AJUNGLEchampion'],
            request.GET['AMIDchampion'],
            request.GET['AADCARRYchampion'],
            request.GET['ASUPPORTchampion'],
        ]
        team_b = [
            request.GET['ETOPchampion'],
            request.GET['EJUNGLEchampion'],
            request.GET['EMIDchampion'],
            request.GET['EADCARRYchampion'],
            request.GET['ESUPPORTchampion'],
        ]
        winrate = predict.predict(
            team_a,
            team_b
        )
        data = {
            'has_winrate': True,
            'team1': team_a,
            'team2': team_b,
            'winrate': winrate,
            'enemy_winrate': 100 - winrate
        }

    else:
        data = {
            'has_winrate': want_predict
        }

    return render(request, "index.html", data)
