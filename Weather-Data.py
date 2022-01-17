import requests


class c_ncei_data_service_api:
    """
    Name:           c_ncei_data_service_api.py
    Author:         Randy Runtsch
    Date:           April 11, 2021
    Description:    Python wrapper class for the NOA NCEI
                    Data Service API used to obtain weather and climate data.
    References:     NCIE Data Service APU User Documentation - https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation
    """

    def __init__(self, dataset, data_types, stations, start_date_time, end_date_time, bounding_box):
        # Set the base API URL.
        self._base_api_url = 'https://www.ncei.noaa.gov/access/services/data/v1/?'

        # Retrieve data.
        self._dataset = self.call_api(dataset, data_types, stations, start_date_time, end_date_time, bounding_box)

    def call_api(self, dataset, data_types, stations, start_date_time, end_date_time, bounding_box):

        # Create the full API request URL and submit it to the server. Add station names.

        full_url = self._base_api_url + 'dataset=' + dataset + '&dataTypes=' + data_types + \
            '&stations=' + stations + '&startDate=' + start_date_time + '&endDate=' + end_date_time + \
            '&boundingBox=' + bounding_box + \
            '&units=standard'

        response = requests.get(full_url)

        return response.text
    def get_data(self):

        # Return the data retrieved with the API call.

        return self._dataset
    def write_data_file(self, file_nm):

        # Write the weather dataset to the specified file.
        file = open(file_nm, 'w')
        file.write(self._dataset)
        file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("hello")
    #begin Weather pull
    api_result = c_ncei_data_service_api('daily-summaries', 'AWND', 'USW00094846', '2000-01-01', '2020-12-31', '90,-180,-90,180')
    #api_result = c_ncei_data_service_api('daily-summaries', 'AWND,WSF2,WSF5', 'USW00094846,USW00014925,USW00023293',
                                         #'2000-01-01', '2020-12-31', '90,-180,-90,180')

    print(api_result.get_data())
    #