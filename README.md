# Quick Hack (Snowplow data to train VW)

This is a very quick POS during KDD 2018 to try the contextual bandits presented [here][contextual-bandit].

The idea is that I am reading the enriched event stream of [snwoplow][snowplow] Near Real-Time pipeline, which contain a new iglu context (as of yet uncommitted) that contains the vw_label data (this is a quick hack).

It then picks any other fields from the enriched event or any context (or other self-describing field) using the [snowplow python SDK][snowplow-python-sdk] and pipes it to the vw image built with this [vw-docker][vw-docker]
which then in turn spits out model data.

Here is an example training a [bandit][bandit]. The output can then be used to present one of the alternatives to show to the user, like so:

```bash

```

[snowplow]: https://github.com/snowplow/snowplow/
[snowplow-python-sdk]: https://github.com/snowplow/snowplow-python-analytics-sdk
[bandit]: https://en.wikipedia.org/wiki/Multi-armed_bandit
[vw-docker]: https://github.com/knservis/vowpal-wabbit-alpine-docker
[contextual-bandit]: http://hunch.net/~rwil/kdd2018.html 