from dataclasses import dataclass, field
import random
from typing import Union, List

import numpy as np
import torch
from transformers import HfArgumentParser


@dataclass
class Arguments:
    output_dir: str = field(
        metadata={"help": "The output directory where the checkpoints will be written."},
    )
    encoder_path: str = field(
        default="./ckpt/encoder/bert-large-uncased",
        metadata={"help": "The path of huggingface PLM"}
    )
    train_path: str = field(
        default=None,
        metadata={"help": "The path of training dataset"}
    )
    val_path: str = field(
        default=None,
        metadata={"help": "The path of validation dataset"}
    )
    test_path: str = field(
        default=None,
        metadata={"help": "The path of test dataset"}
    )
    ckpt_for_test: str = field(
        default=None,
        metadata={"help": "if test_path is not None, load the ckpt from ckpt_for_test and predict the results"}
    )
    top_n_for_eval: int = field(
        default=10,
        metadata={"help": "select the top n to evaluate the model during training"}
    )
    top_n_for_test: int = field(
        default=10,
        metadata={"help": "select the top n to predict the results during testing"}
    )
    test_out_path: str = field(
        default="./prediction.json",
        metadata={"help": "The path of writing prediction"}
    )
    per_device_train_batch_size: int = field(
        default=16,
        metadata={"help": "If the train_mode set to sample, the per_device_train_batch_size must set to 1, "
                          "else if the train_mode set to row, you can set the per_device_train_batch_size to larger"}
    )
    per_device_eval_batch_size: int = field(
        default=1,
        metadata={"help": "one is the best"}
    )
    dataloader_pin_memory: bool = field(
        default=False,
        metadata={"help": "Whether to enable memory pinning for DataLoader. "
                          "Setting this to True can speed up data transfer "
                          "between CPU and GPU during training by pinning "
                          "the loaded data to CPU memory."}
    )
    dataloader_num_workers: int = field(
        default=0,
        metadata={"help": "The number of workers for DataLoader. '0' means using the main process only."}
    )
    random_seed: int = field(default=42, metadata={"help": "Fix the random seed"})
    use_wandb: bool = field(default=True, metadata={"help": "Whether to use wandb for logging"})
    truncation: int = field(default=128, metadata={"help": "Maximum sequence length for text truncation"})
    eval_steps: int = field(default=10000, metadata={"help": "Evaluate the model every 'eval_steps' training steps"})
    train_mode: str = field(default="sample", metadata={"help": "Training mode. Possible values: 'sample', 'row'"})
    use_sampler: bool = field(default=False, metadata={"help": "Whether to use sampler for training data"})
    loss_fn_type: str = field(default="CE", metadata={"help": "Loss function type. Possible values: 'CE', 'BCE'"})
    learning_rate: float = field(default=1e-4, metadata={"help": "Learning rate for the optimizer"})
    num_train_epochs: int = field(default=1, metadata={"help": "Total number of training epochs"})
    lr_scheduler_type: str = field(default="linear", metadata={
        "help": "Learning rate scheduler type. Possible values: 'linear', 'cosine', etc."})
    warmup_steps: int = field(default=1000, metadata={"help": "Number of warmup steps for the learning rate scheduler"})
    logging_steps: int = field(default=100, metadata={"help": "Log training information every 'logging_steps' steps"})
    save_steps: int = field(default=10000, metadata={"help": "Save the model every 'save_steps' steps"})


def fix_seed(seed):
    # random
    random.seed(seed)
    # Numpy
    np.random.seed(seed)
    # Pytorch
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def get_training_args():
    return HfArgumentParser(
        Arguments
    ).parse_args_into_dataclasses()[0]


def get_recall(outputs, labels, top_n):
    if len(outputs.shape) > 1:
        outputs = outputs[:, 1]
    outputs, index = torch.sort(outputs, dim=0, descending=True)
    labels = labels[index]
    outputs[:top_n] = 1
    outputs[top_n:] = 0

    TP = ((outputs == 1).int() + (labels == 1).int()) == 2
    FN = ((outputs == 0).int() + (labels == 1).int()) == 2
    SE = float(TP.sum()) / (float((TP + FN).sum()) + 1e-6)
    return SE


def right_pad_sequences(sequences: List[list], padding_value: Union[int, bool] = 0,
                        max_len: int = -1, truncation: int = 512) -> torch.Tensor:
    max_len = max_len if max_len > 0 else max(len(s) for s in sequences)
    max_len = min(max_len, truncation)
    padded_seqs = []
    for seq in sequences:
        if len(seq) > truncation:
            seq = seq[:truncation]
        padded_seqs.append(
            torch.cat((torch.LongTensor(seq), (torch.full((max_len - len(seq),), padding_value, dtype=torch.long)))))
    return torch.stack(padded_seqs).cuda()
