import os
from ailab.atp_dataset.dataset import AILabDataset
from ailab.atp_dataset.constant import Sources
from ailab.atp_finetuner.constant import Task, Framework
from ailab.atp_finetuner.finetuner import AILabFinetuner
from ailab.utils.other import install_requiremet


def train_progress(percent: float):
    pass


def chinese_llama_test():
    # todo     # fixed pretrained in train.py
    pretrained_model_name = os.environ.get("PRETRAINED_MODEL_NAME", "chinese_llama_vicuna")
    model_name = os.environ.get("MODEL_NAME", "")
    dataset_path = os.environ.get("DATASET_PATH")
    output_dir = os.environ.get("OUTPUT_DIR", f"/work/models/{model_name}")
    pretrained_model_path = os.environ.get("PRETRAINED_MODEL_PATH", f"/home/.atp/models/llama")
    tokenizer_path = os.environ.get("TOKENIZER_PATH", f"/home/.atp/models/chinese_llama_vicuna_tokenizer")

    if not model_name or not dataset_path:
        raise TypeError(
            f'os.environ should have (MODEL_NAME,DATASET_PATH)')

    dataset = AILabDataset.load_dataset(dataset_path, src=Sources.huggingface)
    dataset.train_test_split(test_size=0.2)
    args = {
        "model_args": {
        },
        "train_args": {
            "output_dir": output_dir,
            "evaluation_strategy": "steps",
            "save_strategy": "steps",
            "learning_rate": 3e-4,
            "per_device_train_batch_size": 4,
            "gradient_accumulation_steps": 1,
            "per_device_eval_batch_size": 4,
            "num_train_epochs": 10,
            "weight_decay": 0.01,
            "logging_steps": 10,
            "warmup_steps": 100,
            "fp16": True,
            "optim": "adamw_torch",
            "eval_steps": 200,
            "save_steps": 200,
            "max_steps": 5000,
            "resume_from_checkpoint": True,
        },
    }
    finetuner = AILabFinetuner(Task.question_answering_cn, Framework.Pytorch, dataset,
                               pretrained_model_name, train_progress,
                               pretrained_model_path,
                               tokenizer_path,
                               **args)
    finetuner.finetuner()


if __name__ == '__main__':
    chinese_llama_test()
