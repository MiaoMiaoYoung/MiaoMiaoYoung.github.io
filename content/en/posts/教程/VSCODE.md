---
title: "VSCODE大法好"
date: 2024-08-27T11:02:33+08:00
draft: false
categories:
    - 教程

tags:
    - linux
    - vscode
enableTocContent: true
---

## launch.json

> https://blog.csdn.net/qq_41810539/article/details/139992228

Vscode的配置调试文件，一般在*项目根目录/.vscode*下，主要结构如下


```json
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
    
        {
            "name": "Python 调试程序: 当前文件",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "args": ["--output","./results"],
            "console": "integratedTerminal",
            "justMyCode": false
        }
    ]
}
```

主要配置了一下属性：

- type: 调试器类型，如 python，cppdbg，node，java,等
- request: 调试请求类型，通常为 1aunch(启动)或 attach(附加)。
- name: 配置名称，用户可以在调试配置列表中看到。
- program: 要调试的程序路径或文件,
- args: 传递给程序的命令行参数，数组形式。
- cwd: 当前工作目录。
- env: 环境变量设置。
- sourceMaps: 是否启用源映射(通常用于 JavaScript 调试)
- preLaunchTask: 调试前要执行的任务(通常用于编译等)
- postDebugTask: 调试结束后要执行的任务。
- stopOnEntry: 是否在程序入口处停止。
- console: 控制台类型，如 integratedTerminal,externalTerminal,或 internalconsole
- justMyCode: 是否只调试用户代码(用于 Python)
- pythonPath: Python 可执行文件的路径(用于 Python)


如果使用torchrun，program设置为torch，然后将文件名设置为参数传进去


```json
{
    "name": "working",
    "type": "python",
    "request": "launch",
    "program": "/home/user_x/anaconda3/envs/env_y/bin/torchrun",
    "console": "integratedTerminal",
    "justMyCode": true,
    "args": [
        "example_chat_completion.py",
        "--nproc_per_node", "1",
        "--ckpt_dir", "llama-2-7b-chat/",
        "--tokenizer_path", "tokenizer.model",
        "--max_seq_len", "512",
        "--max_batch_size", "6",
    ],
    "env": {
        "CUDA_VISIBLE_DEVICE": "0"
    },    
},
```