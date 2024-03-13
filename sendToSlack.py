

import json
import requests
from links import * 

def sendToSlack (thisCoupon):
   
   webhook = strSlackWebhook
   payload = {"text": thisCoupon.createPayloadMessage()}
   # Skickar en meddelande till SLACK-kanalen via en webhook
   return requests.post(webhook, json.dumps(payload))