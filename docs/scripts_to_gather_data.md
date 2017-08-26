
### Scripts to Gather data

This has scripts specific to data collection and is not part of the rawdata
package, though included for reference.


#### Location Data

Use Google to find a list of locations by name and return the 
Geo coordinates and full address details.

Steps:

 - download the location(s) matching that name<BR>
 - extract the JSON information relating to address<BR>
 - save data as flat CSV file<BR>


Example output

~~~
search_term	result_num	gps_lat	gps_lng	formatted_address	country	
Glenelg Jetty	1	-34.9802633	138.5156255	Jetty Rd, Glenelg SA 5045, Australia	AUSTRALIA	
Glenelg Jetty	2	-34.9792705	138.5171805	Jetty St, Glenelg SA 5045, Australia	AUSTRALIA	
Sydney Opera House	1	-33.8567844	151.2152967	Bennelong Point, Sydney NSW 2000, Australia	AUSTRALIA	
Uluru	1	-25.3444277	131.0368822	Uluru, Petermann NT 0872, Australia	AUSTRALIA
~~~

