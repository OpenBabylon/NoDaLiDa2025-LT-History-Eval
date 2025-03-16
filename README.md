# Towards Multilingual LLM Evaluation for Baltic and Nordic Languages: A Study on Lithuanian History

This repository contains the code and datasets used in the paper "[Towards Multilingual LLM Evaluation for Baltic and Nordic Languages: A Study on Lithuanian History](https://arxiv.org/abs/2501.09154)" by Yevhen Kostiuk, Oxana Vitman, Łukasz Gagała, and Artur Kiulian. This paper was published in NB-REAL 2025 workshop.


## Overview

The study evaluates the historical knowledge of multilingual Large Language Models (LLMs) through a multiple-choice question-answering task. The models were tested on a dataset comprising Lithuanian national and general history questions, translated into various languages, including Baltic, Nordic, English, Ukrainian, and Arabic. The goal was to assess knowledge sharing among culturally and historically connected language groups.

## Contents

- **lt_translated_datasets/**: Contains the translated question-answer pairs in multiple languages.
- **annotation_guidelines**: guidelines for the annotators to evaluate the quality of the translated samples.
- **main.py**: run evaluation with the specified inference client.

To modify prompt strategies, change prompting functions in the file `prompts.py`. If you need to add prompting strategy function, update `list_of_prompts` in `main.py`

## Run 
```bash
python3 main.py --model <your_model> --output_dir <your_output_dir> --api_address <api_address>
```

Currently supports only huggingface InferenceClient.



## Models Evaluated

The following LLMs were evaluated:

- GPT-4o
- LLaMa3.1 (8B and 70B)
- QWEN2.5 (7B and 72B)
- Mistral Nemo (12B)
- LLaMa3 (8B)
- Mistral (7B)
- LLaMa3.2 (3B)
- Nordic fine-tuned models (GPT-SW3 and LLaMa3 8B)

## Citation

If you use this code or dataset in your research, please cite the paper:


```
@article{kostiuk2025multilingual,
  title={Towards Multilingual LLM Evaluation for Baltic and Nordic Languages: A Study on Lithuanian History},
  author={Kostiuk, Yevhen and Vitman, Oxana and Gagała, Łukasz and Kiulian, Artur},
  journal={arXiv preprint arXiv:2501.09154},
  year={2025}
}
```

---

For more details, refer to the full paper available on [arXiv](https://arxiv.org/abs/2501.09154).

