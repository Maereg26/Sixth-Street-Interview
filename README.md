# Sixth-Street-Interview

Due to the limited time I had to have limited error handling and the compromise was that I only checked for missing data and API keys errors. This can have issue wtih handling network errors and rate limiting by API. In production environments this is cruical to ensure there is a stable and reliable environement. I also had limited or basic data caching, to reduce API calls and improve performance a caching mechanism could have been used.
There was also limited testing and documentation. 

If versioning the libaray was needed I would have a path to fix bugs and errors in the code but ensure backward compatibility. <ajor version updates could require a lot of changes and cause API changes that would cayse some users to modify their code to the new version. A small update could result in new features whilst ensuring backward compatibility.

To publish the libray i wold create a setup.py file as I have that contains all the needed metadata for the library.

If I did this for service rather than as a library I would have an API layer, a load balancer and a caching layer to have the frequently accessed data. I would also have a database to store metadata about the stock data to make querey easier and allow more advanced searches.
This will allow the handling of traffic across multiple instances of API layer. ANother thing that could be implemented is asynchronous task queue which can be used to manage tasks that run for a longer time a d help fetch data from the Alpha vantage API. This can help response time and also prevent blocking on the API Layer.

This assessment took me two hours and 4 minutesas I had to debug a lot of errors from the API link as I had mistakenly used the direct link in the instructions. I also wanted the code to be cleaner which took me a bit of time to clean up and format correctly.
