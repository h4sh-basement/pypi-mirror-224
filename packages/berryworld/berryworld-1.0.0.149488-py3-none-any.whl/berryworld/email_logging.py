import math
from threading import Thread
import pandas as pd
import datetime
import time


class EmailLogging:
    """ Manage Error Logs in ApplicationLogs """

    def __init__(self, project_name, pipeline, ip_address, request_url, sql_con, timeout=30*60, print_sql=False):
        """ Initialize the class
        :param project_name: Name of the project being run. it must be already declared in PythonEmailProjectSeverity
        :param pipeline: Pipeline name being run. It must identify the process being executed uniquely
        :param ip_address: IP Address
        :param request_url: URL requested by the client
        :param sql_con: Connection to the Database to upload the Logs
        :param timeout: Time in seconds after which an unsuccessful log will be sent
        :param print_sql: Print the SQL statement sent to the server
        """
        self.log_df = pd.DataFrame({'ProjectName': [project_name], 'Pipeline': [pipeline],
                                    'Successful': [0], 'IPAddress': [str(ip_address).replace("'", '"')],
                                    'RequestUrl': [str(request_url).replace("'", '"')], 'Sent': [0],
                                    'StartedDate': [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")]})
        self.sql_con = sql_con
        self.timeout = timeout
        self.print_sql = print_sql
        self.failure_type = []
        Thread(target=self.start_threading).start()

    def start_threading(self):
        """ Start a threading to update on failure if the script breaks or the pipeline gets blocked
        """
        time_range = math.ceil(self.timeout / 10)
        for times in range(time_range):
            time.sleep(10)
            if len(self.failure_type) > 0:
                break

        if len(self.failure_type) == 0:
            elapsed_time = str(datetime.timedelta(seconds=round(self.timeout)))[2:]
            self.on_failure(error_message=f'The pipeline failed to succeed after running '
                                          f'for {elapsed_time} minutes')

    def on_success(self):
        """ Update log on success
        """
        if not any(self.failure_type):
            successful_columns = {'Successful': 1, 'Resolved': 1,
                                  'FinishedDate': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}
            self.log_df = self.log_df.assign(**successful_columns)
            self.sql_con.insert(self.log_df, 'Logging', 'PythonLogs', print_sql=self.print_sql)
            self.failure_type.append(True)

    def on_failure(self, error_message, section=None, critical=True):
        """ Update log on failure
        :param error_message: Error message to be sent in the Log
        :param section: Indicate the script section. Useful to locate the error
        :param critical: Indicate whether it should avoid sending successful logs
        """
        unsuccessful_columns = {'Successful': 0,
                                'FinishedDate': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
                                'Section': section,
                                'ErrorMessage': str(error_message).replace("'", '"'),
                                'Critical': 1 if critical is True else 0}
        self.log_df = self.log_df.assign(**unsuccessful_columns)
        self.sql_con.insert(self.log_df, 'Logging', 'PythonLogs', print_sql=self.print_sql)
        self.failure_type.append(critical)
