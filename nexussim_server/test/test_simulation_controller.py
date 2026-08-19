import unittest

from flask import json

from nexussim_server.models.service_chain import ServiceChain  # noqa: E501
from nexussim_server.models.simulation_status import SimulationStatus  # noqa: E501
from nexussim_server.test import BaseTestCase


class TestSimulationController(BaseTestCase):
    """SimulationController integration test stubs"""

    def test_simulation_post(self):
        """Test case for simulation_post

        Run a simulation
        """
        service_chain = ServiceChain()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/yaml',
            'X-API-KEY': 'special-key',
        }
        response = self.client.open(
            '/dynaa/simulation',
            method='POST',
            headers=headers,
            data=json.dumps(service_chain),
            content_type='application/yaml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_simulation_simulation_id_delete(self):
        """Test case for simulation_simulation_id_delete

        Delete simulation
        """
        headers = {'X-API-KEY': 'special-key'}
        response = self.client.open(
            '/dynaa/simulation/{simulation_id}'.format(simulation_id='simulation_id_example'),
            method='DELETE',
            headers=headers)
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_simulation_simulation_id_get(self):
        """Test case for simulation_simulation_id_get

        Get simulation status
        """
        headers = {'Accept': 'application/json', 'X-API-KEY': 'special-key'}
        response = self.client.open(
            '/dynaa/simulation/{simulation_id}'.format(simulation_id='simulation_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
