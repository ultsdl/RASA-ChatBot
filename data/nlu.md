## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:contact_developer
- contact developer
- contact customer support
- contact support center
- raise a ticket
- raise a concern
- raise a question
- i have a concern

## intent:db_details
- show my db details
- show database details
- show me my details

## intent:ask_population
- total number of [population](feature:"population")
- total number of [population](feature:"population") in this lsgd
- total [population](feature:"population")
- total [population](feature:"population") here
- number of [population](feature:"population")
- what is the [population](feature:"population")

## intent:ask_properties
- [Total number](query_type:"count") of [properties](feature:"bldg_typ")
- [total no](query_type:"count") of [properties](feature:"bldg_typ")
- what is the [total no](query_type:"count") of [properties](feature:"bldg_typ")
- what are the [total no](query_type:"count") of [property](feature:"bldg_typ")
- what is the [total number](query_type:"count") of [properties](feature:"bldg_typ")
- [total](query_type:"count") [properties](feature:"bldg_typ") in this lsgd
- [number](query_type:"count") of [properties](feature:"bldg_typ")
- find me the [total number](query_type:"count") of [properties](feature:"bldg_typ")
- find [total number](query_type:"count") of [properties](feature:"bldg_typ")

- [types](query_type:"types") of [properties](feature:"bldg_typ")
- [types](query_type:"types") of [property](feature:"bldg_typ")
- total [types](query_type:"types") of [properties](feature:"bldg_typ")
- tell me [properties](feature:"bldg_typ") [types](query_type:"types")
- tell me [property](feature:"bldg_typ") [types](query_type:"types")
- different [type](query_type:"types") of [properties](feature:"bldg_typ")
- all [types](query_type:"types") of [properties](feature:"bldg_typ")
- show me different [properties](feature:"bldg_typ") [types](query_type:"types")
- show me different [types](query_type:"types") of [properties](feature:"bldg_typ")

## intent:ask_properties_category
- no of [residential](category:"RESIDENTIAL") [properties](feature:"bldg_typ")
- no of [recreational](category:"RECREATIONAL") [properties](feature:"bldg_typ")
- no of [religious](category:"RELIGIOUS") [properties](feature:"bldg_typ")
- no of [educational](category:"EDUCATION") [properties](feature:"bldg_typ")
- no of [commercial](category:"COMMERCIAL") [properties](feature:"bldg_typ")
- no of [public](category:"PUBLIC AND SEMI PUBLIC") [properties](feature:"bldg_typ")
- number of [residential](category:"RESIDENTIAL") [properties](feature:"bldg_typ")
- number of [recreational](category:"RECREATIONAL") [properties](feature:"bldg_typ")
- number of [religious](category:"RELIGIOUS") [properties](feature:"bldg_typ")
- number of [educational](category:"EDUCATION") [properties](feature:"bldg_typ")
- number of [commercial](category:"COMMERCIAL") [properties](feature:"bldg_typ")
- number of [public](category:"PUBLIC AND SEMI PUBLIC") [properties](feature:"bldg_typ")
- number of [semi public](category:"PUBLIC AND SEMI PUBLIC") [properties](feature:"bldg_typ")
- no of [residential](category:"RESIDENTIAL") [property](feature:"bldg_typ")
- no of [recreational](category:"RECREATIONAL") [property](feature:"bldg_typ")
- no of [religious](category:"RELIGIOUS") [property](feature:"bldg_typ")
- no of [educational](category:"EDUCATION") [property](feature:"bldg_typ")
- no of [commercial](category:"COMMERCIAL") [property](feature:"bldg_typ")
- no of [public](category:"PUBLIC AND SEMI PUBLIC") [property](feature:"bldg_typ")
- number of [residential](category:"RESIDENTIAL") [property](feature:"bldg_typ")
- number of [recreational](category:"RECREATIONAL") [property](feature:"bldg_typ")
- number of [religious](category:"RELIGIOUS") [property](feature:"bldg_typ")
- number of [educational](category:"EDUCATION") [property](feature:"bldg_typ")
- number of [commercial](category:"COMMERCIAL") [property](feature:"bldg_typ")
- number of [public](category:"PUBLIC AND SEMI PUBLIC") [property](feature:"bldg_typ")
- number of [semi public](category:"PUBLIC AND SEMI PUBLIC") [property](feature:"bldg_typ")

## intent:ask_property_count
- properties [without](flag:"NO") [electricity](feature:"elec_conn")
- property [without](flag:"NO") [electricity](feature:"elec_conn")
- number of properties [without](flag:"NO") [electricity](feature:"elec_conn")
- number of property [without](flag:"NO") [electricity](feature:"elec_conn")
- properties [with](flag:"YES") [electricity](feature:"elec_conn")
- property [with](flag:"YES") [electricity](feature:"elec_conn")
- number of properties [with](flag:"YES") [electricity](feature:"elec_conn")
- number of property [with](flag:"YES") [electricity](feature:"elec_conn")

- properties [without](flag:"NO") [gas](feature:"gas_conn") connection
- property [without](flag:"NO") [gas](feature:"gas_conn") connection
- number of properties [without](flag:"NO") [gas](feature:"gas_conn") connection
- number of property [without](flag:"NO") [gas](feature:"gas_conn") connection
- properties [with](flag:"YES") [gas](feature:"gas_conn") connection
- property [with](flag:"YES") [gas](feature:"gas_conn") connection
- number of properties [with](flag:"YES") [gas](feature:"gas_conn") connection
- number of property [with](flag:"YES") [gas](feature:"gas_conn") connection

- properties [without](flag:"NO") [toilets](feature:"bathroom") connection
- property [without](flag:"NO") [toilets](feature:"bathroom") connection
- number of properties [without](flag:"NO") [toilets](feature:"bathroom") connection
- number of property [without](flag:"NO") [toilets](feature:"bathroom") connection
- properties [with](flag:"YES") [toilets](feature:"bathroom") connection
- property [with](flag:"YES") [toilets](feature:"bathroom") connection
- number of properties [with](flag:"YES") [toilets](feature:"bathroom") connection
- number of property [with](flag:"YES") [toilets](feature:"bathroom") connection
- properties [without](flag:"NO") [bathrooms](feature:"bathroom") connection
- property [without](flag:"NO") [bathroom](feature:"bathroom") connection
- number of properties [without](flag:"NO") [bathrooms](feature:"bathroom") connection
- number of property [without](flag:"NO") [bathroom](feature:"bathroom") connection
- properties [with](flag:"YES") [bathrooms](feature:"bathroom") connection
- property [with](flag:"YES") [bathrooms](feature:"bathroom") connection
- number of properties [with](flag:"YES") [bathroom](feature:"bathroom") connection
- number of property [with](flag:"YES") [bathrooms](feature:"bathroom") connection

## intent:ask_ratio
- ratio of [unemployment](feature:"ownr_occup")
- show me the ratio of [unemployment](feature:"ownr_occup")
- give me the ratio of [unemployment](feature:"ownr_occup")
- people with no [job](feature:"ownr_occup")
- give me the details of people with no [employment](feature:"ownr_occup")

## intent:ask_taxation
- [highest](flag:"max") tax paying [property](feature:"bldg_typ")
- [high](flag:"max") tax paying [property](feature:"bldg_typ") type
- [property_type](feature:"bldg_typ") that pays [maximum](flag:"max") tax
- which [property type](feature:"bldg_typ") pays the [highest](flag:"max") tax
- Find me the [properties](feature:"bldg_typ") paying [maximum](flag:"max") tax
- [property](feature:"bldg_typ") paying [highest](flag:"max") tax
- which [property_type](feature:"bldg_typ") pays [maxium](flag:"max") tax
- List me the [properties](feature:"bldg_typ") paying [highest](flag:"max") tax
- Find me the [properties](feature:"bldg_typ") paying [high](flag:"max") tax
- Find me the [property](feature:"bldg_typ") who pays [largest](flag:"max") tax
- which [property type](feature:"bldg_typ") pays [high](flag:"max") tax
- which [property type](feature:"bldg_typ") pays [highest](flag:"max") tax
- Find me [property](feature:"bldg_typ") paying [high](flag:"max") tax
- [lowest](flag:"min") tax paying [property](feature:"bldg_typ")
- List me the [properties](feature:"bldg_typ") paying [lowest](flag:"min") tax
- Find me the [properties](feature:"bldg_typ") paying [low](flag:"min") tax
- Find me the [property](feature:"bldg_typ") who pays [lowest](flag:"min") tax
- which [property_type](feature:"bldg_typ") pays [low](flag:"min") tax
- which [property_type](feature:"bldg_typ") pays [lowest](flag:"min") tax
- Find me [property](feature:"bldg_typ") paying [low](flag:"min") tax
- [property_type](feature:"bldg_typ") that pays [minimum](flag:"min") tax
- Find me the [properties](feature:"bldg_typ") paying [minimum](flag:"min") tax
- which [property_type](feature:"bldg_typ") pays [minimum](flag:"min") tax

- [highest](flag:"max") tax paying [ward](feature:"Ward")
- [high](flag:"max") tax paying [ward](feature:"Ward") type
- [ward](feature:"Ward") that pays [maximum](flag:"max") tax
- which [ward](feature:"Ward") pays the [highest](flag:"max") tax
- Find me the [wards](feature:"Ward") paying [maximum](flag:"max") tax
- [ward number](feature:"Ward") paying [highest](flag:"max") tax
- which [ward no](feature:"Ward") pays [maxium](flag:"max") tax
- List me the [ward](feature:"Ward") paying [highest](flag:"max") tax
- Find me the [ward](feature:"Ward") paying [high](flag:"max") tax
- Find me the [ward](feature:"Ward") who pays [largest](flag:"max") tax
- which [ward no](feature:"Ward") pays [high](flag:"max") tax
- which [ward number](feature:"Ward") pays [highest](flag:"max") tax
- Find me [ward](feature:"Ward") paying [high](flag:"max") tax
- [lowest](flag:"min") tax paying [ward](feature:"Ward")
- List me the [wards](feature:"Ward") paying [lowest](flag:"min") tax
- Find me the [wards](feature:"Ward") paying [low](flag:"min") tax
- Find me the [ward](feature:"Ward") who pays [lowest](flag:"min") tax
- which [ward number](feature:"Ward") pays [low](flag:"min") tax
- which [ward no](feature:"Ward") pays [lowest](flag:"min") tax
- Find me [ward](feature:"Ward") paying [low](flag:"min") tax
- [ward no](feature:"Ward") that pays [minimum](flag:"min") tax
- Find me the [ward](feature:"Ward") paying [minimum](flag:"min") tax
- which [ward](feature:"Ward") pays [minimum](flag:"min") tax