from girder.api import access
from girder.api.describe import Description, describeRoute
from girder.api.rest import Resource
from girder.constants import TokenScope
from girder.models.file import File
from girder.models.item import Item

from ..models.mayo_heatmap import MayoHeatmap

class MayoHeatmapResource(Resource):
    def __init__(self):
        super().__init__()
        self.resourceName = 'mayoHeatmap'
        self.route('POST', ('saveHeatmap', ':id'), self.saveHeatmap)
        self.route('GET', ('getHeatmap', ':id'), self.getHeatmap)

    @describeRoute(
        Description('Uploat heatmap')
        .param('id', 'The ID of the image.')
        .modelParam('fileId', 'The ID of the source file.', model=File, paramType='formData')
    )
    @access.user(scope=TokenScope.DATA_WRITE)
    def saveHeatmap(self, id, params):
        user = self.getCurrentUser()
        return MayoHeatmap().saveHeatmap(id, user, params)
    
    @describeRoute(
        Description('Get heatmap')
    )
    @access.public(scope=TokenScope.DATA_READ)
    def getHeatmap(self, id, params):
        user = self.getCurrentUser()
        query = {
            "name": id + "_heatmap.svs",
        }

        docs = list(File().findWithPermissions(query=query, user=user))
        if(len(docs)):
            doc = docs[0]
            return doc["itemId"]
        else:
            return 
        
        