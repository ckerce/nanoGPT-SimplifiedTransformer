transformer_block_type = 'SASP'
wandb_run_name = 'SASP-dr_0.1'
out_dir = 'analysis/SASP-dr_0.1'
wandb_project = 'SASP-analysis2'
dataset = 'shakespeare_char'
eval_interval = 200
eval_iters = 100
log_interval = 10
always_save_checkpoint = False
wandb_log = True
gradient_accumulation_steps = 1
batch_size = 128
block_size = 256
n_layer = 6
n_head = 6
learning_rate = 0.5e-3
max_iters = 16000
lr_decay_iters = 16000
min_lr = 0.5e-4
beta2 = 0.99
warmup_iters = 500
dropout = 0.1
use_v = False
n_embd = 420
