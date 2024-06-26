import requests
import configuration
import data


def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_CLIENT_ORDER,
                         json=data.order_body)


def get_get_order_info(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO,
                        params={"t": track_number})
