from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union, cast

from cognite.client.data_classes._base import (
    CogniteLabelUpdate,
    CogniteListUpdate,
    CogniteObjectUpdate,
    CognitePrimitiveUpdate,
    CognitePropertyClassUtil,
    CogniteResource,
    CogniteResourceList,
    CogniteUpdate,
    PropertySpec,
)

if TYPE_CHECKING:
    from cognite.client import CogniteClient


class RevisionCameraProperties(dict):
    """Initial camera position and target.

    Args:
        target (List[float]): Initial camera target.
        position (List[float]): Initial camera position.
    """

    def __init__(self, target: Optional[List[float]] = None, position: Optional[List[float]] = None, **kwargs: Any):
        self.target = target
        self.position = position
        self.update(kwargs)

    target = CognitePropertyClassUtil.declare_property("target")
    position = CognitePropertyClassUtil.declare_property("position")


class BoundingBox3D(dict):
    """The bounding box of the subtree with this sector as the root sector. Is null if there are no geometries in the subtree.

    Args:
        max (List[float]): No description.
        min (List[float]): No description.
    """

    def __init__(self, max: Optional[List[float]] = None, min: Optional[List[float]] = None, **kwargs: Any):
        self.max = max
        self.min = min
        self.update(kwargs)

    max = CognitePropertyClassUtil.declare_property("max")
    min = CognitePropertyClassUtil.declare_property("min")


class ThreeDModel(CogniteResource):
    """No description.

    Args:
        name (str): The name of the model.
        id (int): The ID of the model.
        created_time (int): The creation time of the resource, in milliseconds since January 1, 1970 at 00:00 UTC.
        metadata (Dict[str, str]): Custom, application specific metadata. String key -> String value. Limits: Maximum length of key is 32 bytes, value 512 bytes, up to 16 key-value pairs.
        cognite_client (CogniteClient): The client to associate with this object.
    """

    def __init__(
        self,
        name: Optional[str] = None,
        id: Optional[int] = None,
        created_time: Optional[int] = None,
        metadata: Optional[Dict[str, str]] = None,
        cognite_client: Optional[CogniteClient] = None,
    ):
        self.name = name
        self.id = id
        self.created_time = created_time
        self.metadata = metadata
        self._cognite_client = cast("CogniteClient", cognite_client)


class ThreeDModelUpdate(CogniteUpdate):
    """No description.

    Args:
        id (int): A server-generated ID for the object.
    """

    class _PrimitiveThreeDModelUpdate(CognitePrimitiveUpdate):
        def set(self, value: Any) -> ThreeDModelUpdate:
            return self._set(value)

    class _ObjectThreeDModelUpdate(CogniteObjectUpdate):
        def set(self, value: Dict) -> ThreeDModelUpdate:
            return self._set(value)

        def add(self, value: Dict) -> ThreeDModelUpdate:
            return self._add(value)

        def remove(self, value: List) -> ThreeDModelUpdate:
            return self._remove(value)

    class _ListThreeDModelUpdate(CogniteListUpdate):
        def set(self, value: List) -> ThreeDModelUpdate:
            return self._set(value)

        def add(self, value: List) -> ThreeDModelUpdate:
            return self._add(value)

        def remove(self, value: List) -> ThreeDModelUpdate:
            return self._remove(value)

    class _LabelThreeDModelUpdate(CogniteLabelUpdate):
        def add(self, value: List) -> ThreeDModelUpdate:
            return self._add(value)

        def remove(self, value: List) -> ThreeDModelUpdate:
            return self._remove(value)

    @property
    def name(self) -> _PrimitiveThreeDModelUpdate:
        return ThreeDModelUpdate._PrimitiveThreeDModelUpdate(self, "name")

    @property
    def metadata(self) -> _ObjectThreeDModelUpdate:
        return ThreeDModelUpdate._ObjectThreeDModelUpdate(self, "metadata")

    @classmethod
    def _get_update_properties(cls) -> list[PropertySpec]:
        return [
            PropertySpec("name", is_nullable=False),
            PropertySpec("metadata", is_container=True),
        ]


class ThreeDModelList(CogniteResourceList[ThreeDModel]):
    _RESOURCE = ThreeDModel


class ThreeDModelRevision(CogniteResource):
    """No description.

    Args:
        id (int): The ID of the revision.
        file_id (int): The file id.
        published (bool): True if the revision is marked as published.
        rotation (List[float]): No description.
        camera (Union[Dict[str, Any], RevisionCameraProperties]): Initial camera position and target.
        status (str): The status of the revision.
        metadata (Dict[str, str]): Custom, application specific metadata. String key -> String value. Limits: Maximum length of key is 32 bytes, value 512 bytes, up to 16 key-value pairs.
        thumbnail_threed_file_id (int): The threed file ID of a thumbnail for the revision. Use /3d/files/{id} to retrieve the file.
        thumbnail_url (str): The URL of a thumbnail for the revision.
        asset_mapping_count (int): The number of asset mappings for this revision.
        created_time (int): The creation time of the resource, in milliseconds since January 1, 1970 at 00:00 UTC.
        cognite_client (CogniteClient): The client to associate with this object.
    """

    def __init__(
        self,
        id: Optional[int] = None,
        file_id: Optional[int] = None,
        published: Optional[bool] = None,
        rotation: Optional[List[float]] = None,
        camera: Optional[Union[Dict[str, Any], RevisionCameraProperties]] = None,
        status: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
        thumbnail_threed_file_id: Optional[int] = None,
        thumbnail_url: Optional[str] = None,
        asset_mapping_count: Optional[int] = None,
        created_time: Optional[int] = None,
        cognite_client: Optional[CogniteClient] = None,
    ):
        self.id = id
        self.file_id = file_id
        self.published = published
        self.rotation = rotation
        self.camera = camera
        self.status = status
        self.metadata = metadata
        self.thumbnail_threed_file_id = thumbnail_threed_file_id
        self.thumbnail_url = thumbnail_url
        self.asset_mapping_count = asset_mapping_count
        self.created_time = created_time
        self._cognite_client = cast("CogniteClient", cognite_client)

    @classmethod
    def _load(cls, resource: Union[Dict, str], cognite_client: Optional[CogniteClient] = None) -> ThreeDModelRevision:
        instance = super()._load(resource, cognite_client)
        if isinstance(resource, Dict):
            if instance.camera is not None:
                instance.camera = RevisionCameraProperties(**instance.camera)
        return instance


class ThreeDModelRevisionUpdate(CogniteUpdate):
    """No description.

    Args:
        id (int): A server-generated ID for the object.
    """

    class _PrimitiveThreeDModelRevisionUpdate(CognitePrimitiveUpdate):
        def set(self, value: Any) -> ThreeDModelRevisionUpdate:
            return self._set(value)

    class _ObjectThreeDModelRevisionUpdate(CogniteObjectUpdate):
        def set(self, value: Dict) -> ThreeDModelRevisionUpdate:
            return self._set(value)

        def add(self, value: Dict) -> ThreeDModelRevisionUpdate:
            return self._add(value)

        def remove(self, value: List) -> ThreeDModelRevisionUpdate:
            return self._remove(value)

    class _ListThreeDModelRevisionUpdate(CogniteListUpdate):
        def set(self, value: List) -> ThreeDModelRevisionUpdate:
            return self._set(value)

        def add(self, value: List) -> ThreeDModelRevisionUpdate:
            return self._add(value)

        def remove(self, value: List) -> ThreeDModelRevisionUpdate:
            return self._remove(value)

    class _LabelThreeDModelRevisionUpdate(CogniteLabelUpdate):
        def add(self, value: List) -> ThreeDModelRevisionUpdate:
            return self._add(value)

        def remove(self, value: List) -> ThreeDModelRevisionUpdate:
            return self._remove(value)

    @property
    def published(self) -> _PrimitiveThreeDModelRevisionUpdate:
        return ThreeDModelRevisionUpdate._PrimitiveThreeDModelRevisionUpdate(self, "published")

    @property
    def rotation(self) -> _ListThreeDModelRevisionUpdate:
        return ThreeDModelRevisionUpdate._ListThreeDModelRevisionUpdate(self, "rotation")

    @property
    def camera(self) -> _ObjectThreeDModelRevisionUpdate:
        return ThreeDModelRevisionUpdate._ObjectThreeDModelRevisionUpdate(self, "camera")

    @property
    def metadata(self) -> _ObjectThreeDModelRevisionUpdate:
        return ThreeDModelRevisionUpdate._ObjectThreeDModelRevisionUpdate(self, "metadata")

    @classmethod
    def _get_update_properties(cls) -> list[PropertySpec]:
        return [
            PropertySpec("published", is_nullable=False),
            PropertySpec("rotation", is_nullable=False),
            PropertySpec("camera", is_nullable=False),
            PropertySpec("metadata", is_container=True),
        ]


class ThreeDModelRevisionList(CogniteResourceList[ThreeDModelRevision]):
    _RESOURCE = ThreeDModelRevision


class ThreeDNode(CogniteResource):
    """No description.

    Args:
        id (int): The ID of the node.
        tree_index (int): The index of the node in the 3D model hierarchy, starting from 0. The tree is traversed in a depth-first order.
        parent_id (int): The parent of the node, null if it is the root node.
        depth (int): The depth of the node in the tree, starting from 0 at the root node.
        name (str): The name of the node.
        subtree_size (int): The number of descendants of the node, plus one (counting itself).
        properties (Dict[str, Dict[str, str]]): Properties extracted from 3D model, with property categories containing key/value string pairs.
        bounding_box (Union[Dict[str, Any], BoundingBox3D]): The bounding box of the subtree with this sector as the root sector. Is null if there are no geometries in the subtree.
        cognite_client (CogniteClient): The client to associate with this object.
    """

    def __init__(
        self,
        id: Optional[int] = None,
        tree_index: Optional[int] = None,
        parent_id: Optional[int] = None,
        depth: Optional[int] = None,
        name: Optional[str] = None,
        subtree_size: Optional[int] = None,
        properties: Optional[Dict[str, Dict[str, str]]] = None,
        bounding_box: Optional[Union[Dict[str, Any], BoundingBox3D]] = None,
        cognite_client: Optional[CogniteClient] = None,
    ):
        self.id = id
        self.tree_index = tree_index
        self.parent_id = parent_id
        self.depth = depth
        self.name = name
        self.subtree_size = subtree_size
        self.properties = properties
        self.bounding_box = bounding_box
        self._cognite_client = cast("CogniteClient", cognite_client)

    @classmethod
    def _load(cls, resource: Union[Dict, str], cognite_client: Optional[CogniteClient] = None) -> ThreeDNode:
        instance = super()._load(resource, cognite_client)
        if isinstance(resource, Dict):
            if instance.bounding_box is not None:
                instance.bounding_box = BoundingBox3D(**instance.bounding_box)
        return instance


class ThreeDNodeList(CogniteResourceList[ThreeDNode]):
    _RESOURCE = ThreeDNode


class ThreeDAssetMapping(CogniteResource):
    """No description.

    Args:
        node_id (int): The ID of the node.
        asset_id (int): The ID of the associated asset (Cognite's Assets API).
        tree_index (int): A number describing the position of this node in the 3D hierarchy, starting from 0. The tree is traversed in a depth-first order.
        subtree_size (int): The number of nodes in the subtree of this node (this number included the node itself).
        cognite_client (CogniteClient): The client to associate with this object.
    """

    def __init__(
        self,
        node_id: Optional[int] = None,
        asset_id: Optional[int] = None,
        tree_index: Optional[int] = None,
        subtree_size: Optional[int] = None,
        cognite_client: Optional[CogniteClient] = None,
    ):
        self.node_id = node_id
        self.asset_id = asset_id
        self.tree_index = tree_index
        self.subtree_size = subtree_size
        self._cognite_client = cast("CogniteClient", cognite_client)


class ThreeDAssetMappingList(CogniteResourceList[ThreeDAssetMapping]):
    _RESOURCE = ThreeDAssetMapping
