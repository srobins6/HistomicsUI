from girder.api import access
from girder.api.describe import Description, describeRoute
from girder.api.rest import Resource
from girder.constants import TokenScope

from ..models.clinician_data import ClinicianData

class ClinicianDataResource(Resource):
    def __init__(self):
        super().__init__()
        self.resourceName = 'clinicianData'
        self.route('POST', ('saveData', ':id'), self.createOrUpdateClinicianData)
        self.route('GET', ('getData', ':id'), self.getClinicianData)

    @describeRoute(
        Description('Create or update clinician data.')
        .param('id', 'The ID of the image.')
        .param('body', 'A JSON object containing the clinician data.', paramType='body')
    )
    @access.user(scope=TokenScope.DATA_WRITE)
    def createOrUpdateClinicianData(self, id, params):
        user = self.getCurrentUser()
        return ClinicianData().saveData(id, user, params)
    
    @describeRoute(
        Description('Get clinician data.')
    )
    @access.public(scope=TokenScope.DATA_READ)
    def getClinicianData(self, id, params):
        user = self.getCurrentUser()
        return ClinicianData().getData(id, user)
        
        