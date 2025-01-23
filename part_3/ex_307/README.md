**Exercise 3.07**

In part 2 we did a Job that made a backup of our Database using the command pg_dump. Unfortunately, the backup was not saved anywhere. 
Create now a CronJob that makes a backup of your database (once per 24 hours) and saves it to Google Object Storage.
In this exercise, you can create the secret for the cloud access from the command line, thus, there is no need to create it in the GitHub action.

When the cron job is working, you can e.g. download the backups using the Google Cloud Console: