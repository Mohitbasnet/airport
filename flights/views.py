from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Airport, Flight,Passenger
# Create your views here.
def index(request):
    flight = Flight.objects.all()
    return render(request,"flights/index.html",{
        "flights":flight
    })

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flight=flight).all()

    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers,
        "non_passengers": non_passengers
    })


def book (request,flight_id):
    #for a post request add a new flight
    if request.method == "POST":
        #accessing the flight
        flight = Fligh.objects.get(pk = flight_id)
        #finding the passenger id from the submitted form data
        passenger_id = int(request.POST['passenger'])

        #finding the passenger based on the id
        passenger = Passenger.objects.get(pk= passenger_id)

        #adding passenger to the flight
        passenger.flights.add(flight)

       

        #redirecting user to flight page
        return HttpResposneRedirect(reverse("flight", args = (flight.id,)))