from __future__ import annotations

import openllm

class FlanT5Config(openllm.LLMConfig):
  """FLAN-T5 was released in the paper [Scaling Instruction-Finetuned Language Models](https://arxiv.org/pdf/2210.11416.pdf).

  It is an enhanced version of T5 that has been finetuned in a mixture of tasks.

  Refer to [FLAN-T5's page](https://huggingface.co/docs/transformers/model_doc/flan-t5) for more information.
  """
  __config__ = {"url": "https://huggingface.co/docs/transformers/model_doc/flan-t5", "architecture": "T5ForConditionalGeneration", "model_type": "seq2seq_lm",
                "default_id": "google/flan-t5-large", "model_ids": ["google/flan-t5-small", "google/flan-t5-base", "google/flan-t5-large", "google/flan-t5-xl", "google/flan-t5-xxl",]}
  class GenerationConfig:
    temperature: float = 0.9
    max_new_tokens: int = 2048
    top_k: int = 50
    top_p: float = 0.4
    repetition_penalty = 1.0

START_FLAN_T5_COMMAND_DOCSTRING = """\
Run a LLMServer for FLAN-T5 model.

\b
> See more information about FLAN-T5 at [huggingface/transformers](https://huggingface.co/docs/transformers/model_doc/flan-t5)

\b
## Usage

By default, this model will use the PyTorch model for inference. However, this model supports both Flax and Tensorflow.

\b
- To use Flax, set the environment variable ``OPENLLM_FLAN_T5_FRAMEWORK="flax"``

\b
- To use Tensorflow, set the environment variable ``OPENLLM_FLAN_T5_FRAMEWORK="tf"``

\b
FLAN-T5 Runner will use google/flan-t5-large as the default model. To change to any other FLAN-T5
saved pretrained, or a fine-tune FLAN-T5, provide ``OPENLLM_FLAN_T5_MODEL_ID='google/flan-t5-xxl'``
or provide `--model-id` flag when running ``openllm start flan-t5``:

\b
$ openllm start flan-t5 --model-id google/flan-t5-xxl
"""
DEFAULT_PROMPT_TEMPLATE = """Answer the following question:\nQuestion: {instruction}\nAnswer:"""
