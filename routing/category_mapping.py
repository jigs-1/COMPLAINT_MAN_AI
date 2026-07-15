def get_authority(category):

    mapping = {

        "Internet": "IT Support",

        "Food / Mess": "Mess Manager",

        "Hostel": "Hostel Warden",

        "Transport": "Transport Manager",

        "Infrastructure": "Maintenance Staff",

        "Laboratory": "Lab Assistant",

        "Library": "Library Staff",

        "Administration": "Admin Office",

        "Security": "Security Office",

        "Electrical": "Electrical Department"
    }

    return mapping.get(category, "Admin Office")