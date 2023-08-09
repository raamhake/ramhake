Scenario 

You are part of a team at Data Axle that is tasked with building a system for Sending automated Emails to Employees.



Task



Your task is to implement a small part of the backend API using Django/flask with business logic along with associated test cases that verify that the logic works according to the use cases below



Description:

The event email system is designed to automatically send emails on special occasions such as birthdays, and work anniversaries. The system retrieves the event details from its table containing employee ID, event types, and dates. Templates for each event type are also stored in the Django database. The system sends emails to the people on that date using the corresponding email templates. 

 

Use Case Flow:

 

1. The system retrieves the event data from the Table file using a Django command

2. The system identifies events based on the current date.

3. For each event:

  a. The system retrieves the name, event type, and date.

  b. The system fetches the corresponding email template from the Django database based on the event type.

  c. The system populates the email template with the members' details and event-specific content.

  d. The system sends the personalized email to the email address that should be saved in a separate table called Employee.

  e. The system logs the email sending status and any errors encountered.

 

Alternate Flow:

 

- If there are no events:

  - The system skips the email-sending process.

  - The system logs that no events are scheduled for the current period in the Django db.

 

Exceptional Flow:

 

- If an error occurs while sending an email:

  - The system logs the error in Django db and continues with the next scheduled email.

  - The system may retry sending the email a certain number of times before logging it as a failed attempt.

 

Post-Conditions:

 

- Emails are sent to the employees on their event dates.

- The system logs the status of each email sent, including successful deliveries and any encountered errors using Django db.

- The system may store the last successful execution time to ensure it only processes new events in subsequent runs using Django db.



Feel free to make your assumptions and move forward in case you are stuck at some point in terms of requirements.

