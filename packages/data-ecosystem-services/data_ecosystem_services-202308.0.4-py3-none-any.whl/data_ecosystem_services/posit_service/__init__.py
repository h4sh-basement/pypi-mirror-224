# Import from sibling directory ..\developer_service
from data_ecosystem_services.cdc_admin_service import environment_tracing
from data_ecosystem_services.cdc_admin_service import environment_logging
import sys
import os

OS_NAME = os.name

sys.path.append("..")
if OS_NAME.lower() == "nt":
    print("posit_service: windows")
    sys.path.append(os.path.dirname(os.path.abspath(__file__ + "\\..")))
    sys.path.append(os.path.dirname(os.path.abspath(__file__ + "\\..\\..")))
    sys.path.append(os.path.dirname(
        os.path.abspath(__file__ + "\\..\\..\\..")))
else:
    print("posit_service: non windows")
    sys.path.append(os.path.dirname(os.path.abspath(__file__ + "/..")))
    sys.path.append(os.path.dirname(os.path.abspath(__file__ + "/../..")))
    sys.path.append(os.path.dirname(os.path.abspath(__file__ + "/../../..")))


__all__ = ["posit_connect"]
