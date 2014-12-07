"""
Your company delivers breakfast via autonomous quadcopter drones. And something mysterious has happened.

Each breakfast delivery is assigned a unique ID, a positive integer. When one of the company's 100 drones
takes off with a delivery, the delivery's ID is added to an array, delivery_id_confirmations.
When the drone comes back and lands, the ID is again added to the same array. After breakfast this morning
there were only 99 drones on the tarmac. One of the drones never made it back from a delivery.
We suspect a secret agent from Amazon placed an order and stole one of our patented drones.
To track them down, we need to find their delivery ID. Given the array of IDs, which contains many
duplicate integers and one unique integer, find the unique integer.
"""


def find_unique(delivery_array):
    """
    Find the missing drone by XORing the bits of all elements. If a drone has a successful takeoff and delivery
    it cancels itself out. This is will work if one drone is missing.
    :param delivery_array: The delivery manifest that is missing one drone.
    :return: The id of the missing drone.
    """

    result = 0

    for item in delivery_array:
        result ^= item

    if result == 0:
        raise AttributeError("No values are missing")
    return result