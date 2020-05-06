# dotslash2020

A model designed with the [Google Magenta](https://magenta.tensorflow.org/) to create dynamic piano performances 

## Steps to Build :
1. install dependencies:  
``` pip install -r requirements ```
2. run the batch file with hyperparameters:  ``` sh pianoDynamic/piano.sh ```
3. MIDI files are generated in out/


## Sentiment based hyperparameter tunning :
```python weightedSenti.py```  can be run so as to implement sentiment based hyperparameter tunning \
 eg : sader music - > pitch_histogram follows a minor key etc..