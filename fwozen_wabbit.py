#!/usr/bin/env python

import snowplow_analytics_sdk.event_transformer
import snowplow_analytics_sdk.snowplow_event_transformation_exception
import sys

fields = sys.argv[1:]
if fields:
    print("Using fields: " + str(fields), file=sys.stderr)
else:
    print("Printing all fields as JSON", file=sys.stderr)

with open("/dev/stdin") as f:
    for event in f:
        try:
            event = snowplow_analytics_sdk.event_transformer.transform(event)
            if fields:
                if "contexts_com_snowplowanalytics_snowplow_fwozen_wabbit_1" in event:
                    fw = event['contexts_com_snowplowanalytics_snowplow_fwozen_wabbit_1'][0]['vw_input']
                    print("{} | {}".format(fw, " ".join(["{}={}".format(f, event[f]) for f in fields if f in event])))
            else:
                print(event)
            
        except snowplow_analytics_sdk.snowplow_event_transformation_exception.SnowplowEventTransformationException as e:
            for error_message in e.error_messages:
                print(error_message, file=sys.stderr)