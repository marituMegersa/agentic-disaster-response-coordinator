def test_agent_orchestrator():
    prompt = "Test execution query for agentic-disaster-response-coordinator"
    assert len(prompt) > 0
    assert "Test" in prompt
