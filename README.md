# Driftwatch-SWFSC

The SPOT_API file contains a script to pull in data from the APIs set up for the SPOT devices. It takes in the Feed ID and outputs
a Python pandas dataframe. It could be quickly modified to output in different formats.

The Interactive_Map file contains exploratory code on the API data to calculate:

1. Drift Speed (min, max, average)
2. Frequency and distribution of updates in the past 24 hours
3. A map that shows location and path of each device. The results of this are pretty nonsensical right now because they're
   approximately stationary in the test API
