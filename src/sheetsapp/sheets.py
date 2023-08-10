from pprint import pprint

import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'credentials.json'
spreadsheet_id = '1N2ZX4iKdldV62-XAbL5VyBeYsFN27OJXJfo3BqkkO_Y'

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)



# create_sheet_result = service.spreadsheets().batchUpdate(
#     spreadsheetId = spreadsheet_id,
#     body = {"requests": [{"addSheet": {"properties": {"title": "Result","gridProperties": {"rowCount": 50,"columnCount": 5}}}}]}
# ).execute()
#
# create_sheet_Links = service.spreadsheets().batchUpdate(
#     spreadsheetId = spreadsheet_id,
#     body = {"requests": [{"addSheet": {"properties": {"title": "Links","gridProperties": {"rowCount": 50,"columnCount": 1}}}}]}
# ).execute()

class SheetsService:

    def update_result(self,rows_quantity,values):
        results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheet_id, body = {
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": f"Result!A2:F{rows_quantity}",
                 "majorDimension": "ROWS",
                 "values": [
                            ["Link","Name","w/Ozoncard", "wo/Ozoncard","crossed"],
                            ["Link","Name","w/Ozoncard", "wo/Ozoncard","crossed"]
                           ]}
            ]
        }).execute()

sheets_service = SheetsService()