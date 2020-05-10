import random
class BaseEnum(object):
    @classmethod
    def keys(cls):
        return [e for e in cls.__dict__ if not e.startswith("__")]

    @classmethod
    def values(cls): 
        data = cls.__dict__
        return [data[e] for e in data if not e.startswith("__")]

    @classmethod
    def choices(cls):
        return [e for e in cls.__dict__.items() if not e[0].startswith("__")]

    @classmethod
    def getKey(cls, value):
        keys = [e[0] for e in cls.__dict__.items() if e[1] == value]
        return keys[0] if len(keys) > 0 else None


def ShipEnum(clname, dictValues):
    # clname = "ModelChoices__{}".format(random.randrange(int(1e6)))
    cls = type(clname, (BaseEnum,), dictValues)
    cls.__module__ = '__main__'
    return cls


OrderStatus = ShipEnum("OrderStatus", {
    "NEW_ORDER": "1",
    "INVOICED": "2",
    "READY_TO_SHIP": "3",
    "PICKUP_SCHEDULED": "4",
    "CANCELLED": "5",
    "SHIPPED": "6",
    "DELIVERED": "7",
    "EPAYMENT_FAILED": "8",
    "RETURNED": "9",
    "UNMAPPED": "10",
    "UNFULFILLABLE": "11",
    "PICKUP_QUEUE": "12",
    "PICKUP_RESCHEDULED": "13",
    "PICKUP_ERROR//_CREATED_WHEN_THERE_IS_AN_ERROR_ON_PICKUP_SCHEDULE": "14",
    "RTO_INITIATED": "15",
    "RTO_DELIVERED": "16",
    "RTO_ACKNOWLEDGED": "17",
    "CANCELLATION_REQUESTED": "18",
    "OUT_FOR_DELIVERY": "19",
    "IN_TRANSIT": "20",
    "RETURN_PENDING": "21",
    "RETURN_INITIATED": "22",
    "RETURN_PICKUP_QUEUED": "23",
    "RETURN_PICKUP_ERROR": "24",
    "RETURN_IN_TRANSIT": "25",
    "RETURN_DELIVERED": "26",
    "RETURN_CANCELLED": "27",
    "RETURN_PICKUP_GENERATED": "28",
    "RETURN_CANCELLATION_REQUESTED": "29",
    "RETURN_PICKUP_CANCELLED": "30",
    "RETURN_PICKUP_RESHEDULED": "31",
    "RETURN_PICKEDUP": "32",
    "LOST": "33",
    "OUT_FOR_PICKUP": "34",
    "PICKUP_EXCEPTION": "35",
    "UNDELIVERED": "36",
    "DELAYED": "37",
    "PARTIAL_DELIVERED": "38",
    "DESTROYED": "39",
    "DAMAGED": "40",
    "FULFILLED": "41",
    "ARCHIVED": "42",
    "REACHED_DESTINATION_HUB": "43",
    "MISROUTED": "44",
    "RTO_OFD": "45",
    "RTO_NDR": "46"
})

ShipmentStatus = ShipEnum("ShipmentStatus", {
    "AWB_ASSIGNED": "1",
    "LABEL_GENERATED": "2",
    "PICKUP_SCHEDULED/GENERATED": "3",
    "PICKUP_QUEUED": "4",
    "MANIFEST_GENERATED": "5",
    "SHIPPED": "6",
    "DELIVERED": "7",
    "CANCELLED": "8",
    "RTO_INITIATED": "9",
    "RTO_DELIVERED": "10",
    "PENDING": "11",
    "LOST": "12",
    "PICKUP_ERROR": "13",
    "RTO_ACKNOWLEDGED": "14",
    "PICKUP_RESCHEDULED": "15",
    "CANCELLATION_REQUESTED": "16",
    "OUT_FOR_DELIVERY": "17",
    "IN_TRANSIT": "18",
    "OUT_FOR_PICKUP": "19",
    "PICKUP_EXCEPTION": "20",
    "UNDELIVERED": "21",
    "DELAYED": "22",
    "PARTIAL_DELIVERED": "23",
    "DESTROYED": "24",
    "DAMAGED": "25",
    "FULFILLED": "26",
    "REACHED_DESTINATION_HUB": "38",
    "MISROUTED": "39",
    "RTO_NDR": "40",
    "RTO_OFD": "41",
    "PICKED_UP": "42"
})

FilterBy = ShipEnum("FilterBy",{
    "PAYMENT_METHOD": "payment_method",
    "CHANNEL_ORDER_ID": "channel_order_id",
    "STATUS": "status"
})

SortOrder = ShipEnum("SortOrder", {
    "ASCENDING": "ASC",
    "DESCENDING": "DESC"
})

Courier = ShipEnum("Courier", {
    "BLUEDART": "1",
    "FEDEX": "2",
    "FEDEX_PACKAGING": "7",
    "DHL_PACKET_INTERNATIONAL#": "8",
    "DELHIVERY": "10",
    "FEDEX_SURFACE": "12",
    "ECOMEXP": "14",
    "DOTZOT": "16",
    "XPRESSBEES": "33",
    "ARAMEX_INTERNATIONAL": "35",
    "DHL_PACKET_PLUS_INTERNATIONAL": "37",
    "DHL_PARCEL_INTERNATIONAL_DIRECT": "38",
    "DELHIVERY_SURFACE": "39",
    "GATI_SURFACE": "40",
    "FEDEX_FR": "41",
    "FEDEX_SL": "42",
    "DELHIVERY_SURFACE_STANDAR": "43",
    "DELHIVERY_SURFACE_LITE": "44",
    "ECOM_EXP_REVERSE": "45",
    "SHADOW_FAX_REVERSE": "46",
    "EKART": "48",
    "WOW_EXPRESS": "50",
    "XPRESSBEES_SURFACE": "51",
    "RAPID_DELIVERY": "52",
    "GATI_SG": "53",
    "EKART_SURFACE": "54",
    "DART_DART_PLUS": "55",
    "DHL_EXPRESS": "56",
    "PROFESSIONAL": "57",
    "SHADOWFAX_FORWARD": "58",
    "ECOM_ROS": "60",
    "FEDEX-SURFACE_1KG": "62",
    "DELHIVERY_FLASH_AIR": "63",
})
