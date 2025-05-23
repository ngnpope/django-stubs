from typing import Any, Final

c_int_p: Any
GDAL_OF_READONLY: Final = 0x00
GDAL_OF_UPDATE: Final = 0x01
GDAL_OF_ALL: Final = 0x00
GDAL_OF_RASTER: Final = 0x02
GDAL_OF_VECTOR: Final = 0x04
register_all: Any
cleanup_all: Any
get_driver: Any
get_driver_by_name: Any
get_driver_count: Any
get_driver_description: Any
open_ds: Any
destroy_ds: Any
get_ds_name: Any
get_dataset_driver: Any
get_layer: Any
get_layer_by_name: Any
get_layer_count: Any
get_extent: Any
get_feature: Any
get_feature_count: Any
get_layer_defn: Any
get_layer_srs: Any
get_next_feature: Any
reset_reading: Any
test_capability: Any
get_spatial_filter: Any
set_spatial_filter: Any
set_spatial_filter_rect: Any
get_fd_geom_type: Any
get_fd_name: Any
get_feat_name: Any
get_field_count: Any
get_field_defn: Any
clone_feature: Any
destroy_feature: Any
feature_equal: Any
get_feat_geom_ref: Any
get_feat_field_count: Any
get_feat_field_defn: Any
get_fid: Any
get_field_as_datetime: Any
get_field_as_double: Any
get_field_as_integer: Any
get_field_as_integer64: Any
is_field_set: Any
get_field_as_string: Any
get_field_index: Any
get_field_name: Any
get_field_precision: Any
get_field_type: Any
get_field_type_name: Any
get_field_width: Any
