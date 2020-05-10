from .constants import *

def does_ship_internationally(courier): 
    internation_couriers = [Courier.DHL_PARCEL_INTERNATIONAL_DIRECT, Courier.DHL_PACKET_PLUS_INTERNATIONAL, Courier.FEDEX_PACKAGING]
    return courier in internation_couriers

def does_handle_returns(courier): 
    return_couriers = [Courier.ECOM_EXP_REVERSE, Courier.SHADOW_FAX_REVERSE]
    return courier in return_couriers
