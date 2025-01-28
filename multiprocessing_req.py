from typing import List
from tqdm import tqdm
import numpy as np
import requests
import string
import itertools
import json, os
import concurrent.futures
import requests
import pandas as pd


# PATH_TO_DATASETS = "merged_ukid_lt_generated_matching_df.csv"

# df = pd.read_csv(PATH_TO_DATASETS, index_col=0)


def generate_output(client, prompt_function, trio, id_, modelname, save_dir):
    
    messages = prompt_function(trio)
    output = client.chat.completions.create(
        model=modelname,
        messages=messages,
        stream=False,
        max_tokens=150,
        seed=2
    )

    pred = output.choices[0].message.content
    with open(os.path.join(save_dir, str(id_) + ".txt"), 'w') as f:
        f.write(pred)

    return pred, id_


def prepare_input_text(question, choices):
    out = f"""Question:\n{question}\n\nAnswers:\n"""

    for choice_label in ["A", "B", "C", "D"]:
        choice_text = [x for x in choices if x["label"] == choice_label][0]["text"]
        out += choice_label + ") " + choice_text + "\n"
    return out


def generate_answer(client, prompt_function, df, model_name, save_dir, prompt_lang):
# output_list will be populated with generated outputs as soon as they are available
    output_list = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:

        # language, modelname -> arguments for the generation function (generate_output) in order.
        # entries is a list of arguments to create tasks to complete

        if prompt_lang != "lt":
            future_to_entry = {
                executor.submit(generate_output, client, prompt_function, prepare_input_text(
                    sample["translated"]["question"]["stem"],
            sample["translated"]["question"]["choices"]), sample['id'], model_name, save_dir): sample['id']
                for sample in df
            }
        else:
            future_to_entry = {
                executor.submit(generate_output, client, prompt_function, prepare_input_text(sample["original"]["question"]["stem"],
            sample["original"]["question"]["choices"]), sample['id'], model_name, save_dir): sample['id']
                for sample in df
            }


        # execute whatever is in queue
        for future in tqdm(concurrent.futures.as_completed(future_to_entry), total=len(future_to_entry)):
            entry = future_to_entry[future]
            try:
                result = future.result()
                if result:
                    output_list.append(result)
            except Exception as e:
                print(f"Error {type(e)}:{e} processing entry: {entry}")

    return output_list



# print(output_list)
