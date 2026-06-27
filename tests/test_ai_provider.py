from ai_provider import AIProviderSDK, get_provider

def test_get_provider():
    provider = get_provider("OpenAI")
    assert isinstance(provider, AIProviderSDK)

def test_fetch_openai():
    provider = get_provider("OpenAI")
    response = provider.fetch("Hello, world!")
    assert response == "OpenAI response to Hello, world!"

def test_fetch_anthropic():
    provider = get_provider("Anthropic")
    response = provider.fetch("Hello, world!")
    assert response == "Anthropic response to Hello, world!"

def test_fetch_cohere():
    provider = get_provider("Cohere")
    response = provider.fetch("Hello, world!")
    assert response == "Cohere response to Hello, world!"

def test_fetch_llama2():
    provider = get_provider("Llama-2")
    response = provider.fetch("Hello, world!")
    assert response == "Llama-2 response to Hello, world!"

def test_get_provider_invalid_name():
    provider = get_provider("Invalid")
    assert provider is None

def test_fetch_invalid_provider():
    class InvalidProvider(AIProviderSDK):
        def __init__(self):
            super().__init__(None)
    provider = InvalidProvider()
    try:
        provider.fetch("Hello, world!")
        assert False, "Expected AttributeError"
    except AttributeError:
        assert True
