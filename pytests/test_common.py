# License: MIT
# Copyright © 2023 Frequenz Energy-as-a-Service GmbH

"""Basic tests to check some code is generated."""


def test_package_import() -> None:
    """Test that the package can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api import common

    assert common is not None


def test_module_import_components() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common import components_pb2

    assert components_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common import components_pb2_grpc

    assert components_pb2_grpc is not None


def test_module_import_metrics() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common import metrics_pb2

    assert metrics_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common import metrics_pb2_grpc

    assert metrics_pb2_grpc is not None


def test_module_import_metrics_electrical() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.common import electrical_pb2

    assert electrical_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.common import electrical_pb2_grpc

    assert electrical_pb2_grpc is not None
