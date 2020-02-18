# web-Design-Challenge
UCSD Data Science Bootcamp HW #11 - Data Analysis Website

Website URL: http://alexisperumal.github.io/web-Design-Challenge

Analysis github repo: https://github.com/alexisperumal/python-api-challenge

### Summary

Analysis attempting to understand the correlation between latitude and four weather indicators (temperature, Humidity, Cloudiness and Windspeed).  


### Approach

Analysis was done by hitting the OpenWeather API REST endpoint and extracting real time weather data for 500+ cities randomly selected from around the world.


### Findings

1.	Temperature correlates inversely with latitude with statistical significance.

2.	Humidity and Cloudiness correlate positively with latitude, with statistical significance for 12/28/19.

3.	Wind speed had statistically significant correlation with latitude (absolute value) on 12/28/19.

### Conclusion and Recommendations

1.	To gain a robust understanding requires a more detailed analysis: accounting for curvature of the earth with the application of transforms, looking at sample dates across the year, separate analysis for the northern and southern hemispheres.

2.	Recommend creation of a regression model that evaluates for other factors including time of day, hemisphere (northern or southern), distance to the coast, etc.

See the Jupyter Notebook for detailed analysis and dataset tables.
