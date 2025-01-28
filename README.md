# ASAG
The code takes provided dataset in LT, extracts triplet *question*, *answer*, *generated answer*, passes it through LLM to verify if answers do match. <br/>  
I used following prompting strategies:

Zero Shot <br/> 
Few Shot <br/> 

If you want to modify prompts, you should modify prompting functions in the file `prompts.py`. If you add prompting strategy function, update `list_of_prompts` in `main.py`

The final output returned as a *.scv* file with the name of used model, results of each prompting strategy and ground truth column. 

**To run the code**:<br/> 
pass your model and output directory as arguments<br/> 
run `python3 main.py --model <your_model> --output_dir <your_output_dir>`

