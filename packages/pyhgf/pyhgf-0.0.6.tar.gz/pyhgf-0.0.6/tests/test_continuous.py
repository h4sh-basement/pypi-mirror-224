# Author: Nicolas Legrand <nicolas.legrand@cas.au.dk>

import unittest
from unittest import TestCase

import jax.numpy as jnp
from jax.lax import scan
from jax.tree_util import Partial

from pyhgf import load_data
from pyhgf.continuous import (
    continuous_input_update,
    continuous_node_update,
    gaussian_surprise,
)
from pyhgf.structure import beliefs_propagation
from pyhgf.typing import Indexes


class Testcontinuous(TestCase):
    def test_continuous_node_update(self):
        # create a node structure with no value parent and no volatility parent
        input_node_parameters = {
            "pihat": 1e4,
            "surprise": 0.0,
            "time_step": 0.0,
            "value": 0.0,
            "kappas_parents": None,
            "psis_parents": None,
        }
        node_parameters_1 = {
            "pihat": 1.0,
            "pi": 1.0,
            "muhat": 1.0,
            "psis_children": None,
            "psis_parents": None,
            "kappas_parents": None,
            "kappas_children": None,
            "mu": 1.0,
            "nu": 1.0,
            "omega": 1.0,
            "rho": 0.0,
        }
        node_parameters_2 = {
            "pihat": 1.0,
            "pi": 1.0,
            "muhat": 1.0,
            "psis_children": None,
            "psis_parents": None,
            "kappas_parents": None,
            "kappas_children": None,
            "mu": 1.0,
            "nu": 1.0,
            "omega": 1.0,
            "rho": 0.0,
        }
        parameters_structure = (
            input_node_parameters,
            node_parameters_1,
            node_parameters_2,
        )
        node_structure = (
            Indexes(None, None, None, None),
            Indexes(None, None, None, None),
            Indexes(None, None, None, None),
        )
        data = jnp.array([0.2, 1.0])

        ###########################################
        # No value parent - no volatility parents #
        ###########################################
        sequence1 = 0, continuous_input_update
        update_sequence = (sequence1,)
        new_parameters_structure, _ = beliefs_propagation(
            parameters_structure=parameters_structure,
            node_structure=node_structure,
            update_sequence=update_sequence,
            data=data,
        )

        assert parameters_structure[1] == new_parameters_structure[1]
        assert parameters_structure[2] == new_parameters_structure[2]

    def test_gaussian_surprise(self):
        surprise = gaussian_surprise(
            x=jnp.array([1.0, 1.0]),
            muhat=jnp.array([0.0, 0.0]),
            pihat=jnp.array([1.0, 1.0]),
        )
        assert jnp.all(jnp.isclose(surprise, 1.4189385))

    def test_continuous_input_update(self):
        ###############################################
        # one value parent with one volatility parent #
        ###############################################
        input_node_parameters = {
            "pihat": 1e4,
            "surprise": 0.0,
            "time_step": 0.0,
            "value": 0.0,
            "kappas_parents": (1.0,),
            "psis_parents": (1.0,),
        }
        node_parameters_1 = {
            "pihat": 1.0,
            "pi": 1.0,
            "muhat": 1.0,
            "psis_children": (1.0,),
            "psis_parents": None,
            "kappas_parents": (1.0,),
            "kappas_children": None,
            "mu": 1.0,
            "nu": 1.0,
            "omega": 1.0,
            "rho": 0.0,
        }
        node_parameters_2 = {
            "pihat": 1.0,
            "pi": 1.0,
            "muhat": 1.0,
            "psis_children": None,
            "psis_parents": None,
            "kappas_parents": None,
            "kappas_children": (1.0,),
            "mu": 1.0,
            "nu": 1.0,
            "omega": 1.0,
            "rho": 0.0,
        }
        parameters_structure = (
            input_node_parameters,
            node_parameters_1,
            node_parameters_2,
        )

        node_structure = (
            Indexes((1,), None, None, None),
            Indexes(None, (2,), (0,), None),
            Indexes(None, None, None, (1,)),
        )

        # create update sequence
        sequence1 = 0, continuous_input_update
        sequence2 = 1, continuous_node_update
        update_sequence = (sequence1, sequence2)
        data = jnp.array([0.2, 1.0])

        # apply beliefs propagation updates
        new_parameters_structure, _ = beliefs_propagation(
            node_structure=node_structure,
            parameters_structure=parameters_structure,
            update_sequence=update_sequence,
            data=data,
        )

        for idx, val in zip(["time_step", "value"], [1.0, 0.2]):
            assert jnp.isclose(new_parameters_structure[0][idx], val)
        for idx, val in zip(
            ["pi", "pihat", "mu", "muhat", "nu"],
            [10000.119, 0.11920292, 0.20000952, 1.0, 7.389056],
        ):
            assert jnp.isclose(new_parameters_structure[1][idx], val)
        for idx, val in zip(
            ["pi", "pihat", "mu", "muhat", "nu"],
            [0.29854316, 0.26894143, -0.36260414, 1.0, 2.7182817],
        ):
            assert jnp.isclose(new_parameters_structure[2][idx], val)

    def test_scan_loop(self):
        timeserie = load_data("continuous")

        # Create the data (value and time steps vectors)
        data = jnp.array([timeserie, jnp.ones(len(timeserie), dtype=int)]).T

        ###############################################
        # one value parent with one volatility parent #
        ###############################################
        input_node_parameters = {
            "pihat": 1e4,
            "surprise": 0.0,
            "time_step": 0.0,
            "value": 0.0,
            "kappas_parents": None,
            "psis_parents": (1.0,),
        }
        node_parameters_1 = {
            "pihat": 1.0,
            "pi": 1.0,
            "muhat": 1.0,
            "psis_children": (1.0,),
            "psis_parents": None,
            "kappas_parents": (1.0,),
            "kappas_children": None,
            "mu": 1.0,
            "nu": 1.0,
            "omega": -3.0,
            "rho": 0.0,
        }
        node_parameters_2 = {
            "pihat": 1.0,
            "pi": 1.0,
            "muhat": 1.0,
            "psis_children": None,
            "psis_parents": None,
            "kappas_parents": None,
            "kappas_children": (1.0,),
            "mu": 1.0,
            "nu": 1.0,
            "omega": -3.0,
            "rho": 0.0,
        }

        parameters_structure = (
            input_node_parameters,
            node_parameters_1,
            node_parameters_2,
        )
        node_structure = (
            Indexes((1,), None, None, None),
            Indexes(None, (2,), (0,), None),
            Indexes(None, None, None, (1,)),
        )

        # create update sequence
        sequence1 = 0, continuous_input_update
        sequence2 = 1, continuous_node_update
        update_sequence = (sequence1, sequence2)

        # create the function that will be scaned
        scan_fn = Partial(
            beliefs_propagation,
            update_sequence=update_sequence,
            node_structure=node_structure,
        )

        # Run the entire for loop
        last, _ = scan(scan_fn, parameters_structure, data)
        for idx, val in zip(["time_step", "value"], [1.0, 0.8241]):
            assert jnp.isclose(last[0][idx], val)
        for idx, val in zip(
            ["pi", "pihat", "mu", "muhat", "nu"],
            [22792.508, 12792.507, 0.80494785, 0.7899765, 3.3479002e-05],
        ):
            assert jnp.isclose(last[1][idx], val)
        for idx, val in zip(
            ["pi", "pihat", "mu", "muhat", "nu"],
            [1.4523009, 1.4297459, -6.9464974, -7.3045917, 0.049787067],
        ):
            assert jnp.isclose(last[2][idx], val)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
