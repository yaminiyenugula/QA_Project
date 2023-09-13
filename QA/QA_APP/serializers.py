from QA_APP.models import Questions, Options
from rest_framework import serializers
from random import shuffle


class OptionswithoutAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ('option','id','is_selected','is_true')

class OptionswithAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionswithoutAnswerSerializer(many=True)  

    class Meta:
        model = Questions
        fields ='__all__'

    def to_representation(self, instance):
        options_data = list(instance.options.all().values('option','id','is_selected'))
        shuffle(options_data)
        representation = super().to_representation(instance)
        representation['options'] = options_data
        return representation












# from jira import JIRA
# import openpyxl

# # Jira server URL and authentication credentials
# JIRA_SERVER = "https://your-jira-instance.atlassian.net"
# JIRA_USERNAME = "yenugulavineetha2001@gmail.com"
# JIRA_PASSWORD = "ATATT3xFfGF0X5lG9TsaRy7OQKYGPVqYL1aILI0ezIAhOXYK7QPjaMMN7_QeY-0vmxw2Ieel5g99-rEnKiz4pogxYwOOIeLmEAZS3ijlJBaThVPkdG2js0B4HyGiMdLqh8r_zZVV-5cxppRZBf59OppmKimD65qQ9_lPPShS8yhFH9h0Ml4qIIY=7ED6658A"

# # Excel file path
# EXCEL_FILE = "your-excel-file.xlsx"

# # Jira project key and issue type
# PROJECT_KEY = "YOUR_PROJECT_KEY"
# ISSUE_TYPE = "Task"  # Replace with the appropriate issue type in your Jira project

# # Connect to Jira
# jira = JIRA(server=JIRA_SERVER, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))

# # Load data from Excel file
# def read_excel_data(excel_file):
#     workbook = openpyxl.load_workbook(excel_file)
#     sheet = workbook.active
#     data = []
#     for row in sheet.iter_rows(min_row=2, values_only=True):  # Assuming data starts from row 2
#         summary, description, assignee, reporter = row[:4]  # Customize this based on your Excel columns
#         data.append((summary, description, assignee, reporter))
#     return data

# # Create Jira issues from Excel data
# def create_jira_issues(data):
#     for summary, description, assignee, reporter in data:
#         issue_dict = {
#             "project": {"key": PROJECT_KEY},
#             "issuetype": {"name": ISSUE_TYPE},
#             "summary": summary,
#             "description": description,
#             "assignee": {"name": assignee},
#             "reporter": {"name": reporter},
#         }
        
#         issue = jira.create_issue(fields=issue_dict)
#         print(f"Created Jira issue {issue.key} for summary: {summary}")

# if __name__ == "__main__":
#     data = read_excel_data(EXCEL_FILE)
#     create_jira_issues(data)
