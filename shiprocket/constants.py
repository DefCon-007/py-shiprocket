import random
class BaseEnum(object):
    @classmethod
    def keys(cls):
        return [e for e in cls.__dict__ if not e.startswith("__")]

    @classmethod
    def choices(cls):
        return [e for e in iteritems(cls.__dict__) if not e[0].startswith("__")]

    @classmethod
    def getKey(cls, value):
        keys = [e[0] for e in iteritems(cls.__dict__) if e[1] == value]
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

FilterBy = ShipEnum("FilterBy",{
    "PAYMENT_METHOD": "payment_method",
    "CHANNEL_ORDER_ID": "channel_order_id",
    "STATUS": "status"
})
