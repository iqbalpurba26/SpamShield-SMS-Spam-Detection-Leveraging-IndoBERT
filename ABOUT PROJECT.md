# SPAM DETECTOR : LEVERAGING FINE-TUNING INDOBERT FOR DETECTION SMS HAM

## Domain Project
The focus of this project is to detect and classify messages into two categories: HAM (legitimate or non-spam message) and SPAM (unsolicited or harmful messages). By automating process, we can improve user experience, reduce unwanted content, and safeguard against potential threats like phising and malware.

## Business Understanding
### Problem Statements
- How ca the model effectively detect and classify SMS messages as HAM or SPAM in Indonesian text?
- How does the fine-tuned IndoBERT model in accuracy, precision, recall, and F1-score?

### Goals
The primary of this project is to develop an effective ham/spam SMS detection system using fine-tuned IndoBERT for Indonesian text. This system aims to accurately classify SMS messages as either ham or spam, even in the presence of informal language. The model should achieve high performance accross key evaluation metrics such as accuracy, precision, recall, and F1-score, ensuring minimal fals positives and false negatives.

### Solution Statements
The proposed solution involves leveraging fine-tuned IndoBERT for the detection and classification of ham and spam SMS messages in the Indonesian Language. By fine-tuning IndoBERT on a labeled dataset of SMS messages, the model will be able to accurately differentiate between legitimate and unwanted messages.

## Data Understanding and Preparation
The dataset consist of 1,142 rows which can be access in this link [[HERE]](https://www.kaggle.com/datasets/gevabriel/indonesian-sms-spam). Data preprocessing ensures the dataset is ready for model training. First, we delete the symbol, link, and the othe irrelevant text. After that, we transform to lowercase. Not only that, we check the null values and were removed.

The final step is split the dataset into three parts: train dataset, val dataset, and test dataset.

## Modelling
To fine-tuning IndoBERT, we use a supervised learning approach, where the dataset is split into training, validation, and testing. The training set is used to update the model's weights, while the validation set is used to monitor the model's performance and avoid overfitting. The model's performance will be evaluated using metrics such as accuracy, precision, recall, and f1-scre.


## Evaluation
- accuracy: 99%
- recall: 99%
- precision: 99%
- f1-score: 99%

## Recommendation
Recommendations for similar project using the purpose include:
- Collect more data for fine-tuning IndoBERT
- Explore alternative models such as mBERT or IndoBERTweet


## Additional Resource
- Fine-tuned IndoBERT model, can access in here [[HERE]](https://huggingface.co/iqbalpurba26/indobert-ham-spam-detection)