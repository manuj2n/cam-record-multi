#!/usr/bin/python3
# -*- coding: utf-8 -*-
# capture des fichiers videos successifs
import picamera
import os
import datetime

with picamera.PiCamera() as camera:
	camera.resolution = (1280, 720)
	hC = datetime.datetime.now()
	fichier = '{:%H%M%S}'.format(hC) 
	camera.start_recording('/home/pi/capture/%s.h264' % fichier)
	camera.wait_recording(300)
	for i in range(1, 3):
		hC = datetime.datetime.now()
		fichier = '{:%H%M%S}'.format(hC)
		camera.split_recording('/home/pi/capture/%s.h264' % fichier)
		camera.wait_recording(300)
	camera.stop_recording()
