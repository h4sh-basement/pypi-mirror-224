def test_import_NemAll_Python_Geometry():
    try:
        import pythonparts      # Without pythonparts import, path to NemAll_Python_Geometry is undefined
        import NemAll_Python_Geometry as AllplanGeo
    except ModuleNotFoundError:
        assert False, "No such module: NemAll_Python_Geometry"
    except ImportError:
        assert False, "Failed to import AllplanGeo from NemAll_Python_Geometry"
    assert True


def test_import_NemAll_Python_BaseElements():
    try:
        import pythonparts      # Without pythonparts import, path to NemAll_Python_BaseElements is undefined
        import NemAll_Python_BaseElements as AllplanBaseElements
    except ModuleNotFoundError:
        assert False, "No such module: AllplanBaseElements"
    except ImportError:
        assert False, "Failed to import AllplanBaseElements from NemAll_Python_BaseElements"
    assert True



def test_import_pythonparts():
    try:
        import pythonparts
    except ModuleNotFoundError:
        assert False, "No such module: pythonparts"


def test_import_geometry():
    try:
        from pythonparts.src import geometry
    except ModuleNotFoundError:
        assert False, "No such module: pythonparts"
    except ImportError:
        assert False, "Failed to import geometry from pythonparts"
    assert True


def test_import_geometry_coords():
    try:
        from pythonparts.src import geometry as geo 
        coords = geo.Coords()
    except ModuleNotFoundError:
        assert False, "No such module: geometry"
    except ImportError:
        assert False, "Failed to import geometry from pythonparts"
    assert True


def test_import_local_exception():
    try:
        from pythonparts.src import AttributePermissionError
        import pythonparts as pp
        print(AttributePermissionError)
    except ModuleNotFoundError:
        assert False, "No such exception: AttributePermissionError"
    except ImportError:
        assert False, "Failed to import AttributePermissionError from pythonparts"
    assert True


def test_import_utils_center_calc():
    try:
        import pythonparts as pp
        print(pp.src.utils.center_calc)
    except ModuleNotFoundError:
        assert False, "No such method: utils.center_calc"
    except ImportError:
        assert False, "Failed to import utils.center_calc from pythonparts"
    assert True


def test_public_interface():
    try:
        import pythonparts as pp
        print(pp.create_cuboid)
        print(pp.create_scene)
    except ModuleNotFoundError:
        assert False, "No such method: utils.center_calc"
    except ImportError:
        assert False, "Failed to import utils.center_calc from pythonparts"
    assert True

