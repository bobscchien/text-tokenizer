# **Customized Text Tokenizer**

## **Description**
This is a project to build customized text tokenizers for NLP problems, using your own datasets or datasets from [TensorFlow Datasets](https://www.tensorflow.org/datasets/overview). The core module is TensorFlow's [Bert Tokenizer](https://www.tensorflow.org/text/api_docs/python/text/BertTokenizer) from [TensorFlow Text](https://www.tensorflow.org/text/api_docs/python/text), and the main structure of this project refers to [this guide](https://www.tensorflow.org/text/guide/subwords_tokenizer#customization_and_export).<br>
The result of tokenizers can be saved & loaded directly using `tf.saved_model.save` & `tf.saved_model.load` since they are `tf.Module` object. Meanwhile, the customized tokenizer can be combined with the trained model and be saved as a single pipeline<br>

<br>

## **Usage**
**Main Program**: <br>
The main program of this project is `src/custom_bert_tokenizer.ipynb`, which is directly written via Jupyter Notebook, for demonstration purpose. <br>
**Configuration**: <br>
`config/conf.ini` is the configuration file for main program to store `data` & `models` in a seperate data directory, while `config/conf-repo.ini` uses the paths in this repository.<br>
To generate your own tokenizers, follow the steps below:
1. Modify the path in `config/conf.ini` or replace the default configuration by `cd config && cp conf.ini conf.ini.copy && mv conf-repo.ini conf.ini` to store `data` & `models` directly in this repository.
2. Turn on Jupyter Notebook & open `src/custom_bert_tokenizer.ipynb`.
3. (Optional) Download and use other datasets by changing the arguments of `tfds.builder`. Available datasets can be found at [TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog/wikipedia).
4. Run all cells. The function `src.utils.tokenizer.build_bert_tokenizer` will train a customized tokenizer and the result will be saved at the final cell.  

<br>

## **Notice**
* For CJK (Chinese, Japanese, and Korean) languages, set `cjk=True` for `src.utils.tokenizer.build_bert_tokenizer` function. As a result, this function will first calculate the term frequency for each word in the specified dataset, sort the words based on their frequency, and finally save the vocabularies to a .txt file for [Bert Tokenizer](https://www.tensorflow.org/text/api_docs/python/text/BertTokenizer). <br>
* For now, this project only supports **English** & **Chinese**. To extend to other languages, the preprocess functions for other languages should be defined in `src.utils.preprocessor`.
* Chinese tokenizer used both Classical & Traditional Chinese datasets to build the vocabularies.  
  
<br>

## **Further**
The tokenization process of this project will be scripted in to python scripts in other projects, and thus they can generate their own tokenizers for specific tasks & datasets.

<br>

## **Reference**
This project is inspired & modified based on [this guide](https://www.tensorflow.org/text/guide/subwords_tokenizer#customization_and_export) from [TensorFlow Text](https://www.tensorflow.org/text/api_docs/python/text).
