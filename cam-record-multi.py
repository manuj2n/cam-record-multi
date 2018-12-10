#!/usr/bin/python3
# -*- coding: utf-8 -*-
# capture des fichiers videos successifs
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.start_recording('/home/pi/capture/1.h264')
    camera.wait_recording(120)
    for i in range(2, 6):
        camera.split_recording('/home/pi/capture/%d.h264' % i)
        camera.wait_recording(120)
    camera.stop_recording()
