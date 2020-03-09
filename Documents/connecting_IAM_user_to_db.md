1. Ensure RDS db is mysql (for these steps) and that IAM authetication is enabled. 
    - Ensure that you record the endpoint, admin_username, admin password
2. You'll need to create a db user from within the mysql shell:

`mysql -h {database or cluster endpoint} -P {port number database is listening on} -u {master db username} -p`

3. Create a database user account that uses an AWS authentication token instead of a password:

`CREATE USER {dbusername} IDENTIFIED WITH AWSAuthenticationPlugin as 'RDS';`

4. Create IAM user with permission to read and write to RDS
    - Note the access and secret codes, as well as the username
