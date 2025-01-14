import os

project_id = os.environ.get('PROJECT_ID')
background_jobs_topic = os.environ.get('BACKGROUND_JOBS_TOPIC')
background_jobs_subscriber = os.environ.get('BACKGROUND_JOBS_SUBSCRIBER')
mongo_connection_string = os.environ.get('MONGO_CONNECTION_STRING')
smtp_host = os.environ.get('SMTP_HOST')
smtp_login = os.environ.get('SMTP_LOGIN')
smtp_password = os.environ.get('SMTP_PASSWORD')
google_app_credentials = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
portal_url = os.environ.get('PORTAL_URL')
service_account_email = os.environ.get('SERVICE_ACCOUNT_EMAIL')
service_account_password = os.environ.get('SERVICE_ACCOUNT_PASSWORD')
save_inbox_leads = os.environ.get('SAVE_INBOX_LEADS', "false") == "true"
