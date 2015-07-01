# -*- coding: utf-8 -*-

from Eeboo import Eeboo
from _Framework.Debug import debug_print


def create_instance(c_instance):
	""" Creates and returns the Launchpad script """
	return Eeboo(c_instance)


#from _Framework.Capabilities import *  # noqa


#def get_capabilities():
	#return {
		#CONTROLLER_ID_KEY: controller_id(vendor_id=4661, product_ids=[14], model_name='Launchpad'),
		#PORTS_KEY: [inport(props=[NOTES_CC, REMOTE, SCRIPT]), outport(props=[NOTES_CC, REMOTE, SCRIPT])]}
