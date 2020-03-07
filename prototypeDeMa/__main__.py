"""Run the application with 'prototypeDeMa' as the module. Uses an untracked
file for the file path when setting credentials.
"""

from prototypeDeMa import app
from google.auth import credentials
import os

if __name__ == "__main__":
    CREDENTIALS = "GOOGLE_APPLICATION_CREDENTIALS"
    if(os.getenv(CREDENTIALS) is None):
        try:
            envPath = open("prototypeDeMa/resources/meta.txt")
            os.environ[CREDENTIALS] = envPath.readline().strip()
            print("Getting credientials...")
            envPath.close()
        except credentials.DefaultCredentialsError:
            print("Please set the Google Application Credentials"
                  "environment variable")
            raise SystemExit
    app.main()
