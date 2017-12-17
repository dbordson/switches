from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
channel = 7

def splash(request):
	
	channelstate = GPIO.input(channel)
	context = {
		'gpio_pin': channel,
		'gpio_state': channelstate,
	}
	# import control.blink_three
	return render(request, 'splash.html', context)

def turnoff(request):
	
	GPIO.output(7, 0)

	return HttpResponseRedirect(reverse('splash'))

	
def turnon(request):
	
	GPIO.output(7, 1)

	return HttpResponseRedirect(reverse('splash'))

	
