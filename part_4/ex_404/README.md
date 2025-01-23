**Exercise 4.04**

 Create an AnalysisTemplate for The Project that will follow the CPU usage of all containers in the namespace.
If the CPU usage rate sum for the namespace increases above a set value (you may choose a good hardcoded value for your project) within 10 minutes, revert the update.

Make sure that the application doesn't get updated, if the value is set too low.