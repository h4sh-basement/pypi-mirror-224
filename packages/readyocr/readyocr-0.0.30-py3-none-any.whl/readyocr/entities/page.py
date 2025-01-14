import os
from PIL import Image

from readyocr.entities.bbox import SpatialObject
from readyocr.entities.entity_list import EntityList
from readyocr.entities.children_mixin import ChildrenMixin


class Page(SpatialObject, ChildrenMixin):
    """ 
    Creates a new document, ideally representing a single item in the dataset.
    
    :param page_number: Page number in the document linked to this Page object
    :type page_number: int
    :param width: Width of page, in pixels
    :type width: float
    :param height: Height of page, in pixels
    :type height: float
    :param children: Child entities in the Page
    :type children: List
    """

    def __init__(
        self,
        page_number: int,
        width: int,
        height: int,
        image: Image=None,
    ):
        self.page_number = page_number
        super().__init__(width=width, height=height)
        self.source = None
        self.metadata = {}
        self.image = image
        self._children = EntityList()
    
    def __repr__(self):
        return os.linesep.join([
            f"Page(page_number: {self.page_number}, width: {self.width}, height: {self.height})",
            f"Children - {len(self.children)}"
        ])
    
    def export_json(self):
        return {
            "pageNumber": self.page_number,
            "source": self.source,
            "dimension": {
                "width": self.width,
                "height": self.height
            },
            "entities": [x.export_json() for x in self.descendants]
        }