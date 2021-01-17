## ask about population
* greet
  - utter_greet
* ask_population{"feature":"population"}
  - action_population
* ask_properties{"query_type":"count","feature":"bldg_typ"}
  - action_properties
  - action_count_plot
*ask_properties_category{"category":"RESIDENTIAL","feature":"bldg_typ"}
  - action_properties_category

## ask developer support
* contact_developer
  - contact_dev_form
  - form{"name": "contact_dev_form"}
  - form{"name": null}

## ask db details
* db_details
  - action_sql_query

## ask property count with flag
* ask_property_count
  - action_property_count
  - action_count_plot

## ask property ratio
* ask_ratio
  - action_feature_ratio

## ask taxation details
*ask_taxation
  - action_taxation

