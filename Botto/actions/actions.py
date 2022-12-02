# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from sys import displayhook
from typing import Any, Text, Dict, List
from pyparsing import nestedExpr

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Any, Text, Dict, List

import json
from urllib import parse, request


class ActionUserName(Action):

     def name(self) -> Text:
         return "action_get_name"

     def run(self, dispatcher, tracker, domain):
        username = tracker.get_slot("username")
        if not username :
            dispatcher.utter_message(" Du hast mir Deinen Namen nicht gesagt.")
        else:
            dispatcher.utter_message(' Du bist {}'.format(username))
        
        print("Sender ID: ", tracker.sender_id)
        return []

class ActionHAskWithName(Action):

    def name(self) -> Text:
        return "action_ask_with_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        username = tracker.get_slot("username")
        if not username :
            dispatcher.utter_message("Hallo! Wie geht es dir?")
        else:
            dispatcher.utter_message(text="Hallo " + username + ", wie geht es dir?")

        return []

class ActionStoreUserSkills(Action):

     def skill(self) -> Text:
         return "action_store_skill"
         

     def run(self, dispatcher, tracker, domain):
        skill = tracker.get_slot("skill")
        print("Sender ID: ", tracker.sender_id)

        return []


class ActionUserName(Action):

     def skill(self) -> Text:
         return "action_get_skill"

     def run(self, dispatcher, tracker, domain):
        skill = tracker.get_slot("skill")
        if not skill :
            dispatcher.utter_message(" Du hast noch keine skills eingetragen.")
        else:
            dispatcher.utter_message(' Du hast {} als skill eingetragen'.format(skill))

        return []


class ActionGetGiphyGif(Action):

    def name(self) -> Text:
        return "action_get_gif"

    def run(self, dispatcher, tracker, domain):
        #url = "http://api.giphy.com/v1/gifs/search"
        url = "http://api.giphy.com/v1/gifs/random"

        searchTag = tracker.get_slot("searchTag")
        #searchTag = "mental health"

        params = parse.urlencode({
        "tag": searchTag,
        "api_key": "22dBtq030RTkmgFArEvXTUb46eutC3JZ",
        #"limit": "1"
        })

        with request.urlopen("".join((url, "?", params))) as response:
            data = json.loads(response.read())


        #image_url = data['data'][0]['images']['original']['url']
        image_url = data['data']['images']['original']['url']

        #print(json.dumps(image_url, sort_keys=True, indent=4))
        print(image_url)

        dispatcher.utter_message(image=image_url)
        return []