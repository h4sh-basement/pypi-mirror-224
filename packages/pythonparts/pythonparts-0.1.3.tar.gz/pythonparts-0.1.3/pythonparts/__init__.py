import sys
import os

try:
    from .config import (path_allplan_pp_api,
                        path_pp_framework,
                        path_pp_framework_general_sctips,)


    sys.path.append(path_allplan_pp_api())
    sys.path.append(path_pp_framework())
    sys.path.append(path_pp_framework_general_sctips())
    import NemAll_Python_Geometry as AllplanGeo    # type: ignore
except ModuleNotFoundError:
    print('unix-based system')

    
from .src import create_scene, create_cuboid_from_pyp, create_cuboid, geometry

