import json
from requests import request
from urllib.parse import urljoin
from exceptions import *
from constants import *


class ShipRocket:
    BASE_URL = "https://apiv2.shiprocket.in/v1/"
    token = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

        self.set_token()

    def send_request(self, method, relative_url, args, add_token=True):
        """
        :param args: Dict of request arguments like json, params, headers etc
        """
        assert relative_url and method, "Cannot send request without method and relative URL"

        if add_token:
            headers = args.get('headers', {})
            headers['Authorization'] = "Bearer {}".format(self.token)
            args['headers'] = headers

        url = urljoin(self.BASE_URL, relative_url)
        response = request(method=method, url=url, **args)
        return response
        # if response.status_code == 200 or response.status_code == 202:
        #     return response

    def set_token(self):
        """
        Generates an access token to be used in the requests to ShipRocket.
        """
        args = {
            "headers": {
                'Content-Type': 'application/json',
            },
            "json": {
                'email': self.email,
                'password': self.password
            }
        }
        response = self.send_request("POST", "external/auth/login", args, add_token=False)
        response_dict = response.json()
        self.token = response_dict['token']
        self.company_id = response_dict['company_id']

    def get_orders(self, filter_by, filter_value, per_page):
        """

        """
        args = {
            "json": {
                "filter": filter_value,
                "filter_by": filter_by,
                "per_page": per_page
            }
        }
        response = self.send_request("GET", "external/orders", args)

        return response

    def get_all_shipments(self, sort=None, sort_by=None, filter_value=None, filter_by=None):
        """
        Get the shipment details of all the shipments in your Shiprocket account.
        """
        if sort:
            if not (sort == "ASC" or sort == "DESC"):
                raise InvalidArgumentException("The value of `sort` can only be ASC or DESC")

        args = {
            "json": {
                "sort": sort,
                "sort_by": sort_by,
                "filter": filter_value,
                "filter_by": filter_by
            }
        }

        response = self.send_request("GET", "external/shipments", args)
        return response

    def get_label(self, shipment_ids):
        assert len(shipment_ids) > 0, "Cannot get label without Shipment Ids"

        args = {
            "headers": {
                'Content-Type': 'application/json',
            },
            "json": {
                "shipment_id": shipment_ids
            }
        }

        response = self.send_request("POST", "external/courier/generate/label", args)
        return response

    def get_invoice(self, order_ids):
        assert len(order_ids) > 0, "Cannot get invoice without order Ids"

        args = {
            "headers": {
                'Content-Type': 'application/json',
            },
            "json": {
                "ids": order_ids
            }
        }

        response = self.send_request("POST", "external/orders/print/invoice", args)
        return response
