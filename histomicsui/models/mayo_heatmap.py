from bson import ObjectId
from girder.constants import AccessType
from girder.models.model_base import AccessControlledModel
from girder.models.file import File

# need cleanup for deleted images/users

class MayoHeatmap(AccessControlledModel):
    baseFields = (
        "imageId",
        "userId",
    )

    dataFields = (
        "heatmap"
    )
    
    def initialize(self): 
        self.exposeFields(AccessType.READ, self.baseFields)
        self.name = "mayoHeatmap"
        self.ensureIndices(self.baseFields)

    def getHeatmap(self, imageId, user):
        query = {
            "imageId":imageId,
            "userId":user["_id"]
        }
        docs = list(super().findWithPermissions(query=query, user=user))
        if(len(docs)):
            doc = docs[0]
            return doc
        else:
            return 

    def saveHeatmap(self, imageId, user, data):
        doc = {}
        existingDoc = self.getHeatmap(imageId, user)
        if existingDoc:
            doc["_id"] = existingDoc["_id"]
        else:
            doc["_id"] = ObjectId()
        doc["imageId"] = imageId
        doc["userId"] = user["_id"]
        fileModel = File()
# save image
        self.setUserAccess(doc, user=user, level=AccessType.ADMIN, save=False)
        self.save(doc, validate=False)
        return doc
