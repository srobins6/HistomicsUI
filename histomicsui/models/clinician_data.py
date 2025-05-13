from bson import ObjectId
from girder.constants import AccessType
from girder.models.model_base import AccessControlledModel

# need cleanup for deleted images/users

class ClinicianData(AccessControlledModel):
    baseFields = (
        "imageId",
        "userId",
    )

    dataFields = (
        "primaryTumorDesignation",
        "primaryTumorDepth",
        "primaryTumorTransected",
        "acantholyticHistologicalPattern",
        "bowenoidHistologicalPattern",
        "perineuralInvasion",
        "nerveDiameter",
        "slidePassesQc",
        "clinicalNotes"
    )
    
    def initialize(self):
        self.exposeFields(AccessType.READ, self.baseFields + self.dataFields)
        self.name = "clinicianData"

        self.ensureIndices([
            "imageId",
            "userId",
        ])

    def getData(self, imageId, user, filter=True):
        query = {
            "imageId":imageId,
            "userId":user["_id"]
        }
        docs = list(super().findWithPermissions(query=query, user=user))
        if(len(docs)):
            doc = docs[0]
            if(filter):
                return self.filterDocument(doc, self.dataFields)
            else:
                return doc
        else:
            return 

    def saveData(self, imageId, user, data):
        doc = data
        existingDoc = self.getData(imageId, user, False)
        if existingDoc:
            doc["_id"] = existingDoc["_id"]
        else:
            doc["_id"] = ObjectId()
        doc["imageId"] = imageId
        doc["userId"] = user["_id"]
        self.setUserAccess(doc, user=user, level=AccessType.ADMIN, save=False)
        self.save(doc, validate=False)
        return doc
