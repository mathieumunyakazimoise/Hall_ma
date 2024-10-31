class MaintenanceConstants:
    STATUS_OPERATIONAL = 'Operational'
    STATUS_UNDER_MAINTENANCE = 'Under Maintenance'
    STATUS_CHOICES = [
        (STATUS_OPERATIONAL, 'Operational'),
        (STATUS_UNDER_MAINTENANCE, 'Under Maintenance'),
    ]

class SecuritySystemConstants:
    SYSTEM_CCTV = 'CCTV'
    SYSTEM_ACCESS_CONTROL = 'Access Control'
    SYSTEM_NONE = 'None'
    SYSTEM_CHOICES = [
        (SYSTEM_CCTV, 'CCTV'),
        (SYSTEM_ACCESS_CONTROL, 'Access Control'),
        (SYSTEM_NONE, 'None'),
    ]


class RoomConstants:
    ROOM_TYPE_SINGLE = 'Single'
    ROOM_TYPE_DOUBLE = 'Double'
    ROOM_TYPES = [
        (ROOM_TYPE_SINGLE, 'Single'),
        (ROOM_TYPE_DOUBLE, 'Double'),
    ]

    STATUS_VACANT = 'Vacant'
    STATUS_OCCUPIED = 'Occupied'
    STATUS_RESERVED = 'Reserved'
    STATUS_UNDER_MAINTENANCE = 'Under Maintenance'
    STATUS_CHOICES = [
        (STATUS_VACANT, 'Vacant'),
        (STATUS_OCCUPIED, 'Occupied'),
        (STATUS_RESERVED, 'Reserved'),
        (STATUS_UNDER_MAINTENANCE, 'Under Maintenance'),
    ]

    BILLING_STATUS_PAID = 'Paid'
    BILLING_STATUS_PENDING = 'Pending'
    BILLING_STATUS_OVERDUE = 'Overdue'
    BILLING_STATUS_CHOICES = [
        (BILLING_STATUS_PAID, 'Paid'),
        (BILLING_STATUS_PENDING, 'Pending'),
        (BILLING_STATUS_OVERDUE, 'Overdue'),
    ]
