# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         sfp_bigip_cookie_decoder
# Purpose:      SpiderFoot plug-in for decoding BigIP cookies.
#
# Author:       vpanal
#
# Created:      17/08/2023
# Copyright:    (c) vpanal 2023
# Licence:      GPL
# -------------------------------------------------------------------------------

import json
from spiderfoot import SpiderFootEvent, SpiderFootPlugin

# Function to process the cookie string and extract IP and port
def process_cookie_string(cookie_string):
    parts = cookie_string.split(".")
    if len(parts) != 3:
        raise ValueError('Format does not match')

    ip = hex(int(parts[0]))
    ip = (
        str(int(ip[8:10], base=16)) + "." +
        str(int(ip[6:8], base=16)) + "." +
        str(int(ip[4:6], base=16)) + "." +
        str(int(ip[2:4], base=16))
    )

    port = hex(int(parts[1]))
    port = str(int(port[4:6] + port[2:4], base=16))

    return ip, port

class sfp_bigip_cookie_decoder(SpiderFootPlugin):

    meta = {
        'name': "BigIP Cookie Decoder",
        'summary': "Decode BigIPCookies",
        'flags': [""],
        'useCases': ["Custom"],
        'categories': ["Decode BigIPCookies"]
    }

    opts = {
        'cookie_prefix': 'BigIP'  # Default value for the cookie prefix
    }

    optdescs = {
        'cookie_prefix': {'desc': "Prefix of the cookie string to check for", 'default': "BigIP"}
    }

    results = None

    def setup(self, sfc, userOpts=dict()):
        self.sf = sfc
        self.results = self.tempStorage()

        # Initialize options from user configuration
        for opt in list(userOpts.keys()):
            self.opts[opt] = userOpts[opt]

    # Define which events this module should watch for
    def watchedEvents(self):
        return ["WEBSERVER_HTTPHEADERS"]

    # Define the events this module can produce
    def producedEvents(self):
        return ["LINKED_URL_INTERNAL"]

    # Handling the received event
    def handleEvent(self, event):
        eventName = event.eventType
        srcModuleName = event.module
        eventData = event.data

        if eventData in self.results:
            return

        self.results[eventData] = True

        self.sf.debug(f"Received event, {eventName}, from {srcModuleName}")

        try:
            self.sf.debug(f"We use the data: {eventData}")
            print(f"We use the data: {eventData}")

            headers = json.loads(eventData)
            cookie_string = headers.get("set-cookie", "")

            if cookie_string.startswith(self.opts['cookie_prefix']):
                cookie_parts = cookie_string.split("=")
                if len(cookie_parts) == 2:
                    number_part = cookie_parts[1]

                    ip, port = process_cookie_string(number_part)
                    output = str(ip) + ":" + str(port)
                    print(f"Active: {output}")

                    # Create a new event and notify listeners
                    decoded_event = SpiderFootEvent("LINKED_URL_INTERNAL", output, self.__name__, event)
                    self.notifyListeners(decoded_event)

        except Exception as e:
            self.sf.error("Unable to perform the <ACTION MODULE> on " + eventData + ": " + str(e))
            return

# End of sfp_bigip_cookie_decoder class
