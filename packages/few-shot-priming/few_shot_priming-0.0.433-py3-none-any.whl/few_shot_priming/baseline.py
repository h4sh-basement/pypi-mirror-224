import logging

import numpy as np
import random
import torch
import wandb

from argparse import *
from debater_python_api.api.debater_api import DebaterApi
from random import randint
from sklearn.metrics import f1_score, accuracy_score
from torch import nn
from torch.utils.data import DataLoader
from transformers import  AutoModelForSequenceClassification, AutoTokenizer, AdamW

from few_shot_priming.config import *
from few_shot_priming.mylogging import *
from few_shot_priming.experiments import *

class Dataset(torch.utils.data.Dataset):
    def __init__(self,dataset, path=None, model='bert-base-cased'):
        topics, texts, stances = list(dataset["topic"].values), list(dataset["text"].values), list(dataset["stance"].values)
        print(topics)
        if path:
            tokenizer = AutoTokenizer.from_pretrained(path)
        else:
            tokenizer = AutoTokenizer.from_pretrained(model)
        self.labels = stances
        self.texts = tokenizer(topics, texts, padding=True
                               , truncation=True, return_tensors="pt")
        print(f"size of labels {len(self.labels)} and size of texts is {len(self.texts)}")

    def classes(self):
        return self.labels

    def __len__(self):
        return len(self.labels)

    def get_batch_labels(self, idx):
        return np.array(self.labels[idx])

    def get_batch_texts(self, idx):
        return {"input_ids":self.texts["input_ids"][idx],"attention_mask": self.texts["attention_mask"][idx]}

    def __getitem__(self, idx):
        batch_texts = self.get_batch_texts(idx)
        batch_y = self.get_batch_labels(idx)
        return batch_texts, batch_y


class DeBERTaClassifier(nn.Module):
    def __init__(self, hyperparameters, path=None, num_labels=2):
        super(DeBERTaClassifier, self).__init__()
        self.lr = hyperparameters["learning-rate"]
        self.batch_size = hyperparameters["batch-size"]
        if path:
            self.deberta = AutoModelForSequenceClassification.from_pretrained(path, num_labels=num_labels, ignore_mismatched_sizes=True)
        else:
            self.deberta = AutoModelForSequenceClassification.from_pretrained('microsoft/deberta-base', num_labels=num_labels, ignore_mismatched_sizes=True)
        self.labels = {"CON": 0, "PRO":1}

    def forward(self, input_ids, mask):
        pooled_output = self.deberta(input_ids=input_ids,  return_dict=False)

        return pooled_output

class BertClassifier(nn.Module):
    def __init__(self, hyperparameters, path=None, num_labels=2):
        super(BertClassifier, self).__init__()
        self.lr = hyperparameters["learning-rate"]
        self.batch_size = hyperparameters["batch-size"]
        if path:
            self.bert = AutoModelForSequenceClassification.from_pretrained(path, num_labels=num_labels, ignore_mismatched_sizes=True)
        else:
            self.bert = AutoModelForSequenceClassification.from_pretrained('bert-base-cased', num_labels=num_labels, ignore_mismatched_sizes=True)
        self.labels = {"CON": 0, "PRO":1}


    def forward(self, input_ids, mask):
        pooled_output = self.bert(input_ids=input_ids, attention_mask=mask, return_dict=False)
        return pooled_output




def parse_args():
    """
    Parse the arguments of the scripts
    :return:
    """
    parser = ArgumentParser()
    parser.add_argument("--validate", action="store_true")
    parser.add_argument("--test", action="store_true")
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--random", action="store_true")
    parser.add_argument("--majority", action="store_true")
    parser.add_argument("--ibm-api", action="store_true")
    parser.add_argument("--vast", action="store_true")
    return parser.parse_args()

def run_finetuning_experiment_baseline(config=None, params=None, offline=True, experiment="ibmsc", validate=False,
                                       logger=None, save=True):
    splits = load_splits(experiment, oversample=True, validate=validate)
    use_cuda = torch.cuda.is_available()

    if use_cuda:
        log_message(logger, "-.-.-.- using cuda -.-.-.-.-", level=logging.INFO)
    else:
        log_message(logger, "-.-..-. using cpu -.-.-.-.-..", level=logging.INFO)

    path = None
    if offline:
        #save_pre_trained_model()
        path = config["model-path"]
    model_name = config["model-name"]
    path_model_fine_tuned = config["model-path-fine-tuned"]

    if not params:
        params = get_baseline_best_params()
    else:
        log_message(logger, "Reading params from config file", level=logging.INFO)

    train_dataset = Dataset(splits["training"], path=path, model=model_name)
    if validate:
        experiment_type = "validate"
        test_dataset = Dataset(splits["validation"], path=path, model=model_name)
    else:
        experiment_type = "test"
        test_dataset = Dataset(splits["test"], path=path, model=model_name)

    train_dataloader = DataLoader(train_dataset, batch_size=params["batch-size"], shuffle=True)
    test_dataloader = DataLoader(test_dataset, batch_size=params["batch-size"], shuffle=True)
    eval_dataloader = DataLoader(test_dataset, batch_size=1, shuffle=False)

    device = torch.device("cuda" if use_cuda else "cpu")
    if experiment == "ibmsc":
        num_labels = 2
    else:
        num_labels = 3
    if model_name.startswith("bert"):
        model = BertClassifier(params, path=path, num_labels=num_labels)
    else:
        model = DeBERTaClassifier(params, path=path, num_labels=num_labels)

    if use_cuda:
        model = model.cuda()
    optimizer = AdamW(model.parameters(), lr=float(params["learning-rate"]))
    epochs = params["epochs"]
    criterion = nn.CrossEntropyLoss().cuda()

    best_f1 = 0
    best_epoch = 0
    best_metrics = None

    model.train()
    metrics = {}

    for epoch in range(epochs):
        train_loss = 0
        all_test_labels = []
        all_test_preds = []
        model.train()
        for step, (train_input, train_label) in enumerate(train_dataloader):
            train_label = train_label.to(device)
            mask = train_input["attention_mask"].to(device)
            input_ids = train_input["input_ids"].to(device)
            output = model(input_ids, mask)
            batch_loss = criterion(output[0], train_label)
            log_message(logger, str(output[0].shape), level=logging.INFO)
            log_message(logger, str(train_label.shape) ,level=logging.INFO)
            train_loss += batch_loss.item()
            batch_loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            metrics["train/loss"] = train_loss / (step +1)
            wandb.log(metrics)
        test_loss = 0
        model.eval()
        for step, (test_input, test_labels) in enumerate(test_dataloader):
            test_labels = test_labels.to(device)
            mask = test_input["attention_mask"].to(device)
            input_ids = test_input["input_ids"].to(device)
            output = model(input_ids, mask)
            batch_loss = criterion(output[0], test_labels)
            test_loss += batch_loss.item()
            metrics[f"{experiment_type}/loss"] = test_loss / (step+1)
            wandb.log(metrics)
        for step, (test_input, test_labels) in enumerate(eval_dataloader):
            test_labels = test_labels.to(device)
            mask = test_input["attention_mask"].to(device)
            input_ids = test_input["input_ids"].to(device)
            output = model(input_ids, mask)
            predictions = torch.argmax(output[0],dim=1)
            all_test_preds.extend(predictions.cpu())
            all_test_labels.extend(test_labels.cpu().tolist())

        test_accuracy = accuracy_score(all_test_labels, all_test_preds)
        if experiment == "vast":
            f1s = f1_score(all_test_labels, all_test_preds,average=None, labels=[0, 1, 2])
            neutral_f1 = f1s[2]
            metrics[f"{experiment_type}/neutral-f1"] = neutral_f1
        else:
            f1s = f1_score(all_test_labels, all_test_preds,average=None, labels=[0, 1])

        con_f1 = f1s[0]
        pro_f1 = f1s[1]
        macro_f1 = f1_score(all_test_labels, all_test_preds, average="macro")
        metrics[f"{experiment_type}/macro-f1"] = macro_f1
        metrics[f"{experiment_type}/pro-f1"] = pro_f1
        metrics[f"{experiment_type}/con-f1"] = con_f1
        metrics[f"{experiment_type}/accuracy"] = test_accuracy
        metrics["score"] = metrics[f"{experiment_type}/accuracy"]
        if macro_f1 > best_f1:
            best_f1 = macro_f1
            best_metrics = metrics
            best_epoch = epoch
            torch.save({"model_state_dict":model.state_dict()}, path_model_fine_tuned)
        wandb.log(metrics)
    log_message(logger, f"best epoch is {best_epoch}", level=logging.WARNING)
    log_metrics(logger, best_metrics, level=logging.WARNING)
    return metrics["score"]


def baseline(config, experiment, offline=True, validate=True, majority=False):
    splits = load_splits(experiment)
    if validate:
        test_split = splits["validation"]
    else:
        test_split = splits["test"]

    if offline:
        #save_pre_trained_model()
        path = config["model-path"]

    test_dataset = Dataset(test_split, path=path)
    test_dataloader = DataLoader(test_dataset, batch_size=8, shuffle=True)
    predictions = []
    labels = []
    for step, (test_input, test_labels) in enumerate(test_dataloader):
        labels.extend(test_labels)
        if majority:
            predictions.extend([1 for _ in test_labels])
        else:
            predictions.extend([randint(0,1) for _ in test_labels])
    print(f"size of test is {test_labels}")
    pro_f1 = f1_score(labels, predictions, average=None, labels= [1])
    con_f1 = f1_score(labels, predictions, average=None, labels =[0])
    if experiment == "vast":
        neutral_f1 = f1_score(labels, predictions, average=None, labels =[2])
        neutral_f1 = neutral_f1[0]
    else:
        neutral_f1 = None
    macro_f1 = f1_score(labels, predictions, average="macro")
    accuracy = accuracy_score(labels, predictions)

    return accuracy, pro_f1[0], con_f1[0], neutral_f1, macro_f1


def run_ibm_baseline(params, experiment, validate=True):

    splits = load_splits(experiment)
    if validate:
        test_split = splits["validation"]
    else:
        test_split = splits["test"]
    api_key = params["api-key"]
    debater_api = DebaterApi(api_key)
    pro_con_client = debater_api.get_pro_con_client()

    topics, texts, labels = list(test_split["topic"].values), list(test_split["text"].values), list(test_split["stance"].values)
    list_of_instances = []
    for i, text in enumerate(texts):
        list_of_instances.append({"sentence" : text, "topic": topics[i]})
    scores = pro_con_client.run(list_of_instances)
    upper_threshold = 0.2
    down_threshold = -0.2
    if experiment == "vast":
        predictions = []
        for score in scores:
            if score > upper_threshold:
                predictions.append(1)
            elif score < down_threshold:
                predictions.append(0)
            else:
                predictions.append(2)
    else:
        predictions = [score > 0 for score in scores]
    labels_map = {"PRO": 1, "CON": 0}
    accuracy = accuracy_score(labels, predictions)
    pro_f1 = f1_score(labels, predictions, average=None, labels = [1])
    con_f1 = f1_score(labels, predictions, average=None, labels = [0])
    if experiment == "vast":
        neutral_f1 = f1_score(labels, predictions, average=None, labels = [2])
        neutral_f1 = neutral_f1[0]
    else:
        neutral_f1 = None

    macro_f1 = f1_score(labels, predictions, average="macro")
    return accuracy, pro_f1[0], con_f1[0], neutral_f1, macro_f1

if __name__ == "__main__":
    args = parse_args()
    config = get_baseline_config()
    if args.vast:
        experiment = "vast"
    else:
        experiment = "ibmsc"
    if args.random:
        accuracy, pro_f1, con_f1, neutral_f1, macro_f1  = baseline(config, experiment= experiment, offline=args.offline, validate=args.validate)
        print(f"random baseline: accuracy {accuracy}, macro-f1 {macro_f1}, pro f1 {pro_f1}, con f1 {con_f1}, "
              f" neutral f1 {neutral_f1}")
    elif args.majority:
        accuracy, pro_f1, con_f1, neutral_f1, macro_f1  = baseline(config, experiment= experiment, offline=args.offline, validate=args.validate, majority=True)
        print(f"majority baseline: accuracy {accuracy}, macro-f1 {macro_f1}, pro f1 {pro_f1}, con f1 {con_f1} neutral f1 {neutral_f1}")
    elif args.ibm_api:
        accuracy, pro_f1, con_f1, neutral_f1, macro_f1  = run_ibm_baseline(config, experiment= experiment, validate=args.validate)
        print(f"ibm api: accuracy {accuracy}, macro-f1 {macro_f1}, pro f1 {pro_f1}, con f1 {con_f1} neutral f1 {neutral_f1}")
