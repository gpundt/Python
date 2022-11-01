CLASS: NSSA221
Required OS: Linux (Rocky 9)

	This script analyzes a given syslog, and locates failed login attempts from remote users. From these failed login attempts, the IP address is isolated
  which we use to find the country of origin using geoip and geolite2 databases. 
  
  The number of login attempts from a specific IP are recorded, and the entries are sorted based on the number in ascending order. All of the information is
  then printed to standard output in a clean, organized format, for ease of access.
  
  Only IP's with more than 10 failed login attempts are recorded, to ensure we don't mistake them for employees forgetting their password.
