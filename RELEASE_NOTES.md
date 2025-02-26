# Frequenz Common API Release Notes

## Summary

This release contains
* additions of data definitions to the common specs, that are intended to be
  used by the Frequenz APIs.
* refactors of existing definitions, in order to make them more consistent and
  easier to use.

## Upgrading

- `lower` and `upper` bounds fields in the `Bounds` message are now `optional`

- `rated_bounds` field has been removed from the messages `Metric` and
  `MetricAggregation`

- `component_bounds` field has been removed from the messages `Metric` and
  `MetricAggregation`

- Inclusion and exclusion bounds have been removed from the metric definitions.
  These have been replaced with an array of inclusion bounds. This simplifies
  the message definition, and removes the requirement of clients having to check
  if a parameter is _not_ in a given pair of bounds. This also extends the
  possibility of having more than 2 pairs bounds for a given metric.

- Fields in `MetricAggregation` message have been suffixed with `_value`, to
  make them consistent with the `Metric` message.

- Timestamps have been introduced in the metric messages. This makes it easier
  to use these messages in a timeseries context.

- Renamed `Metric` message to `SimpleMetricSample`

- Renamed `MetricAggregation` message to `AggregatedMetricSample`

- Added a union type message `MetricSampleVariant` to represent both
  `SimpleMetricSample` and `AggregatedMetricSample`

- Added a message `MetricSample` to represent a metric sample with a timestamp
  and bounds.

- Added a message to represent metrics sampled from components.

- Added a message `SensorData` to represent metrics sampled from sensors.

- Added a message `Lifetime` as a wrapper over the start and end timestamps of
  an entity.

- Added a message `Sensor` to represent sensors installed in a microgrid.

- Added a message `Component` to represent components installed in a microgrid.

- Added a message `ComponentCategoryMetadataVariant` to represent the different
  types of sub-categories that can be associated with a component category.

- Added a message `ComponentConnection` to represent electrical connection
  between two components installed in a microgrid.

- Added a message `DeliveryArea` to represent a market contract delivery area.

- Added a message `Microgrid` to represent a microgrid.

- Updated the package name of `location.proto` to `frequenz.api.common.v1`.

- Added messages to support pagination in APIs.

- Removed `metrics/electrical.proto`, since it is no longer needed.
