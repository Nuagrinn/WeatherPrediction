from wwo_hist import retrieve_hist_data
import pandas as pd
import requests

start_date = '01-OCT-2017'
end_date = '01-OCT-2020'
api_key = '' # Here you put in your api-token
location_list = ['moscow']

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency = 8,
                                location_label = False,
                                export_csv = True,
                                store_df = True)


