# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from data_process import population, CountProperties, CatProperties, sql_query, property_count, calc_tax
from custom_action import save_data, register_complaint
from rasa_sdk.forms import FormAction
from custom_plots import plot_feat_count


class ActionPopulation(Action):

    def name(self) -> Text:
        return "action_population"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            print(tracker.sender_id)
            message = "There are total of {} properties in this LSGD".format(population())
            dispatcher.utter_message(text=message)
        except:
            message = dispatcher.utter_message(template="utter_sorry")
            dispatcher.utter_message(message)
        save_data(tracker.sender_id, (tracker.latest_message)['text'], message)
        return []
        
class ActionProperties(Action):

    def name(self) -> Text:
        return "action_properties"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            feat = eval(next(tracker.get_latest_entity_values("feature"), None))
            query = eval(next(tracker.get_latest_entity_values("query_type"), None))
            message = CountProperties(feat, query)
            print(tracker.sender_id)
            dispatcher.utter_message(text=message)
        except:
            message = dispatcher.utter_message(template="utter_sorry")
            dispatcher.utter_message(message)
        save_data(tracker.sender_id, (tracker.latest_message)['text'], message)
        return []

class ActionPropertiesCategory(Action):

    def name(self) -> Text:
        return "action_properties_category"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            feat = eval(next(tracker.get_latest_entity_values("feature"), None))
            cat = eval(next(tracker.get_latest_entity_values("category"), None))
            result = CatProperties(feat, cat)
            message = "There are total of {} {} properties in this LSGD".format(result, cat.lower())
            dispatcher.utter_message(text=message)
        except:
            message = dispatcher.utter_message(template="utter_sorry")
            dispatcher.utter_message(message)
        save_data(tracker.sender_id, (tracker.latest_message)['text'], message)
        return []

class ActionSQLQuery(Action):

    def name(self) -> Text:
        return "action_sql_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            message = sql_query(tracker.sender_id)
            message = str(message)
            dispatcher.utter_message(text=message)
        except:
            message = dispatcher.utter_message(template="utter_sorry")
            dispatcher.utter_message(message)
        save_data(tracker.sender_id, (tracker.latest_message)['text'], message)
        return []

class ActionPropertiesCount(Action):

    def name(self) -> Text:
        return "action_property_count"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            feat = eval(next(tracker.get_latest_entity_values("feature"), None))
            flag = eval(next(tracker.get_latest_entity_values("flag"), None))
            message = property_count(feat, flag)
            dispatcher.utter_message(text=message)
        except:
            message = dispatcher.utter_message(template="utter_sorry")
            dispatcher.utter_message(message)
        save_data(tracker.sender_id, (tracker.latest_message)['text'], message)
        return []

class ActionFeatureRatio(Action):

    def name(self) -> Text:
        return "action_feature_ratio"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        feat = eval(next(tracker.get_latest_entity_values("feature"), None))
        message = property_count(feat, "NIL")
        dispatcher.utter_message(text=message)

        return []

class ActionTaxation(Action):

    def name(self) -> Text:
        return "action_taxation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        feat = eval(next(tracker.get_latest_entity_values("feature"), None))
        flag = eval(next(tracker.get_latest_entity_values("flag"), None))
        message = calc_tax(tracker.sender_id, feat, flag)
        dispatcher.utter_message(text=message)

        return []

class ActionPropertiesCountPlot(Action):

    def name(self) -> Text:
        return "action_count_plot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            feat = eval(next(tracker.get_latest_entity_values("feature"), None))
            message = plot_feat_count(feat)
        except:
            message = None
        dispatcher.utter_message(text=message)

        return []

class RestaurantForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        """Unique identifier of the form"""
        return "contact_dev_form"


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["concern"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message or a list of them, where a first match will be picked"""

        return { "concern": [self.from_text()
                      ]}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        message = "Thank You for your feedback. Our developer will soon look into this matter and make the changes"
        register_complaint(tracker.sender_id, tracker.get_slot("concern"), message)
        dispatcher.utter_message(message)
        return []




#class ActionProperties(Action):
#
#    def name(self) -> Text:
#        return "action_properties"
#
#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#        
#        dispatcher.utter_message(text=message)
#
#        return []