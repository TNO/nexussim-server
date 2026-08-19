import connexion
from typing import Dict
from typing import Tuple
from typing import Union
import yaml
import uuid
import threading
import time
import logging
import polars

from nexussim_server.models.service_chain import ServiceChain  # noqa: E501
from nexussim_server import util


from nexussim.scene import (
    nexussim_simulation_from_dict,
    make_simulation_report,
)

RUNNING = 'running'
FINISHED = 'finished'
ERROR = 'error'
UNKNOWN = 'unknown'

simulation_statuses = {}
scenes_reports = {}

def simulate(id, specs):
    try:
        simulated_scene = nexussim_simulation_from_dict(desc=specs, max_simulation_time=10)
        report = make_simulation_report(simulated_scene)
        scenes_reports[id] = report
        simulation_statuses[id] = FINISHED
    except Exception as e:
        logging.error("==> Error during processing of simulation request. Cause: \n%s", e)
        simulation_statuses[id] = ERROR

def simulation_post(body) -> str:  # noqa: E501
    """Run a simulation

    Runs a simulation of the provided MIRTO-DynAA model, and return KPIs # noqa: E501

    :param service_chain: The MIRTO-DynAA model of the application service chain
    :type service_chain: dict | bytes

    :rtype: str
    """
    id = str(uuid.uuid4())
    simulation_statuses[id] = RUNNING
    
    specs = yaml.safe_load(body.decode("utf-8"))

    thread = threading.Thread(target=simulate, kwargs={'id': id, 'specs': specs})
    thread.start()

    return id

def simulation_simulation_id_delete(simulation_id):  # noqa: E501
    """Delete simulation

    Delete a specific simulation # noqa: E501

    :param simulation_id: id of the simulation to delete
    :type simulation_id: str

    :rtype: None
    """
    try:
        simulation_statuses.pop(simulation_id)
        scenes_reports.pop(simulation_id)
        return ('', 200)
    except KeyError:
        return ('', 404)

def simulation_simulation_id_get(simulation_id) -> str:  # noqa: E501
    """Get simulation status

    Get the status of an ongoing simulation # noqa: E501

    :param simulation_id: id of the simulation to get
    :type simulation_id: str

    :rtype: Dict[str, Union[str, Dict[str, str]]
    """
    return {'status': simulation_statuses.get(simulation_id, UNKNOWN),
            'kpis': scenes_reports.get(simulation_id, {})}