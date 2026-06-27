from dataclasses import dataclass
from typing import Dict

@dataclass
class AIProvider:
    name: str
    endpoint: str

class AIProviderSDK:
    def __init__(self, provider: AIProvider):
        self.provider = provider

    def fetch(self, prompt: str) -> str:
        # Simulate a fetch call for demonstration purposes
        return f"{self.provider.name} response to {prompt}"

class OpenAIProvider(AIProviderSDK):
    def __init__(self):
        super().__init__(AIProvider("OpenAI", "https://api.openai.com"))

class AnthropicProvider(AIProviderSDK):
    def __init__(self):
        super().__init__(AIProvider("Anthropic", "https://api.anthropic.com"))

class CohereProvider(AIProviderSDK):
    def __init__(self):
        super().__init__(AIProvider("Cohere", "https://api.cohere.com"))

class Llama2Provider(AIProviderSDK):
    def __init__(self):
        super().__init__(AIProvider("Llama-2", "https://api.llama2.com"))

def get_provider(provider_name: str) -> AIProviderSDK:
    providers = {
        "OpenAI": OpenAIProvider(),
        "Anthropic": AnthropicProvider(),
        "Cohere": CohereProvider(),
        "Llama-2": Llama2Provider(),
    }
    return providers.get(provider_name)
