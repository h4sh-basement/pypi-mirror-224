import pytest


@pytest.mark.test_func
def test_plots(RE, agent):
    RE(agent.initialize("qr", n_init=32))

    agent.plot_tasks()
    agent.plot_acquisition()
    agent.plot_feasibility()
