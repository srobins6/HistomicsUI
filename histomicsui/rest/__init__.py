from . import aperio, system, tcga
from .hui_resource import HistomicsUIResource
from .image_browse_resource import ImageBrowseResource
from .clinician_data_resource import ClinicianDataResource
from .mayo_heatmap_resource import MayoHeatmapResource

def addEndpoints(apiRoot):
    """
    This adds endpoints from each module.

    :param apiRoot: Girder api root class.
    """
    system.addSystemEndpoints(apiRoot)
    apiRoot.tcga = tcga.TCGAResource()
    aperio.addItemEndpoints(apiRoot.item)
    aperio.addTcgaEndpoints(apiRoot.tcga)

    ImageBrowseResource(apiRoot)

    apiRoot.clinicianData = ClinicianDataResource()
    apiRoot.histomicsui = HistomicsUIResource()
    apiRoot.mayoHeatmap = MayoHeatmapResource()
