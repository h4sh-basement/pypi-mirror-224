from __future__ import annotations

from typing import List

from promptgen.model.prompt import Prompt

from .prompts import (
    ExampleCreatorPrompt,
    PromptCreatorPrompt,
    PromptOptimizerPrompt,
    PythonCodeGeneratorPrompt,
    TextCategorizerPrompt,
    TextCondenserPrompt,
    TextSummarizerPrompt,
)


def load_predefined_prompts() -> List[Prompt]:
    prompts = [
        PromptCreatorPrompt(),
        TextCategorizerPrompt(),
        TextSummarizerPrompt(),
        ExampleCreatorPrompt(),
        PromptOptimizerPrompt(),
        PythonCodeGeneratorPrompt(),
        TextCondenserPrompt(),
    ]

    return prompts
