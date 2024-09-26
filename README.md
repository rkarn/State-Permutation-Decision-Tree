# Locking of the Decision Tree Model using FSM State Permutation Obfuscation.

The technique is aimed at enhancing the security of decision tree models by implementing Finite State Machine (FSM) state permutation obfuscation. Decision tree models are commonly used in machine learning for classification and regression tasks. However, they can be vulnerable to attacks such as model theft or reverse engineering, where adversaries attempt to extract sensitive information from the model.

In this context, "locking" refers to the process of protecting the decision tree model from unauthorized access or manipulation. The term "FSM state permutation obfuscation" suggests that the technique involves reordering or rearranging the states of a Finite State Machine based on `secret key`, potentially making it more difficult for attackers to understand or replicate the internal logic of the model.

This is the source code to reproduce the results of the paper:

`Karn, Rupesh Raj, and Ozgur Sinanoglu. "Locking Decision Tree with State Permutation Obfuscation: Software Implementation." In 2024 22nd IEEE Interregional NEWCAS Conference (NEWCAS), pp. 353-357. IEEE, 2024.`

The python sklearn decision tree is converted into a finite state machine using `python's case` statement to simuate the `verilog HDL`.

## Requirements
1. Python version >= 3.10
2. MNIST Dataset (provided in the folder)
3. SKlearn
4. Jupyter notebook (Anaconda)

## Usage

Run the jupyter notebook file named `State Permutation Decision Tree.ipynb`. Other files in the repository are generated by this notebook. They are in `Generated files` folder.

The average accuracy across 100 interations of different partially correct keys are performed in folder `sweep_dt_study`. FOe each jupyter notebook, the architecture of decision tree, i.e. `depth` is different. 

The inference rate is calculated for the inferential dataset. 
