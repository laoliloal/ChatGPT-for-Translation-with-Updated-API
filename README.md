# ChatGPT for Translation | ChatGPT用于翻译
Use ChatGPT to complete document translations. This tool accepts a text file (`.pdf`, `.txt`, `.md`, `.html`, or `.rtf`) or a folder containing text files. It will generate both a direct translation and a bilingual text file. Special optimization has been done for parsing PDFs.

使用ChatGPT完成文件翻译。该工具接受一个文本文件（`.pdf`, `.txt`, `.md`, `.html`或`.rtf`）或者一个包含文本的文件夹。它将生成一个直接翻译和一个双语文本文件。对于 PDF 解析做了优化。

对YuxuanXiu大佬工作的进一步修改：
1. 修改requirement.txt，更好兼容Google colab
2. 使用中转API（而非官方API），API调用地址："https://api.kwwai.top/v1"

To-do：把API调用地址做成文本填框形式

## Example | 例子

```
# Install （code in colab）
! git clone https://github.com/laoliloal/ChatGPT-for-Translation-with-Updated-API.git
%cd /content/ChatGPT-for-Translation-with-Updated-API
! pip install -r requirements.txt --quiet

# Run （code in colab）
! python ChatGPT-translate.py --input_path={input_file_path} --openai_key={openai_key} --num_threads=1
```

This command will translate the text in input.txt into simplified Chinese using ChatGPT. You can also specify any language you want. For example, `--target_language="Traditional Chinese"`.

这个命令将使用ChatGPT把`input.txt`中的文本翻译成简体中文。你也可以指定任何你想要的语言。例如，`--target_language="Traditional Chinese"`。

## Translate All Files Within the Folder | 翻译文件夹内所有文本文件

`python ChatGPT-translate.py --input_path=./folder_name/ --openai_key=password`

## Other Examples | 其它例子

Azure:
```
python ChatGPT-translate.py --input_path=input.pdf --use_azure --azure_endpoint=endpoint_uri --azure_deployment_name=deployment_name --openai_key=your_AOAI_key
```

GPT-4:
```
python ChatGPT-translate.py --input_path=input.txt --model=gpt-4 --openai_key=password
```

## Prerequisites | 要求
【自行去某宝买个API的key，中转key就行】

【未测试】OpenAI API key (https://beta.openai.com/signup/) or Azure

You need to link a payment method in the OpenAI API, otherwise you'll face extremely stringent API rate limits. 

OpenAI API 里面要绑定支付方式，否则会有极其严苛的API速率限制.

## Arguments | 可用参数
```
--num_threads: The number of threads to use for translation (default: 10).
--only_process_this_file_extension. For example, set only_process_this_file_extension="txt".
--not_to_translate_references. By default, not to translate references.
```

## Acknowledge 
The PDF parser is built on [Grobid](https://github.com/kermitt2/grobid), a machine learning-driven PDF content extraction tool.
