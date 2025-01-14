from logger_local.LoggerLocal import logger_local as local_logger
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from circles_local_database_python.connection import Connection

GET_LOCATION_ID_BY_PROFILE_ID_METHOD_NAME = "LocationProfile.get_location_id_by_profile_id()"

LOCATION_PROFILE_LOCAL_COMPONENT_ID = 167
COMPONENT_NAME = 'location-profile-local/tests/location_profile.py'

object_to_insert = {
    'payload': 'method get_location_id_by_profile_id in location-profile-local',
    'component_id': LOCATION_PROFILE_LOCAL_COMPONENT_ID,
    'component_name': COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'testing_framework': LoggerComponentEnum.testingFramework.pytest.value,
    'developer_email': 'tal.g@circ.zone'
}

local_logger.init(object=object_to_insert)

class LocationProfile:

    @staticmethod
    def get_location_id_by_profile_id(connection, profile_id):
        local_logger.start(GET_LOCATION_ID_BY_PROFILE_ID_METHOD_NAME, object={'profile_id': profile_id})
        with Connection(database = "location_profile") as connection:   
            local_logger.info(object={'profile_id':profile_id})
            query_get = "SELECT location_id FROM location_profile.location_profile_view WHERE profile_id=%s"
            location_id = connection.fetchone(query_get, (profile_id,))

        local_logger.end(GET_LOCATION_ID_BY_PROFILE_ID_METHOD_NAME, object={'location_id':location_id})
        return location_id