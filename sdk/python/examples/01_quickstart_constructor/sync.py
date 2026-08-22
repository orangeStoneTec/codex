import sys
from pathlib import Path

_EXAMPLES_ROOT = Path(__file__).resolve().parents[1]
if str(_EXAMPLES_ROOT) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES_ROOT))

from _bootstrap import (
    ensure_local_sdk_src,
    runtime_config,
    server_label,
)

ensure_local_sdk_src()

from openai_codex import Codex

with Codex(config=runtime_config()) as codex:
    print("Server:", server_label(codex.metadata))

    print("current model is gpt-5.6-luna")
    thread = codex.thread_start(model="gpt-5.6-luna", config={"model_reasoning_effort": "high"})
    result = thread.run("Say hello in one sentence. ans search beijing weather")
    print("Items:", len(result.items))
    print("Text:", result.final_response)
    print("all result:", result)
