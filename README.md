# moral-check-gpt

## 概要

OpenAI の ModerationAPI を使って文章の不適切さを判定するプログラムです。
AI-MOP 上での使用を想定しています

## 使用方法

後述のターミナル上での設定を行った後、
main.ipynb を jupyter notebook 上で実行してください(オーナーは VSCode 上で動かしてるので動かなかったらごめん)

### ターミナルでの設定(Ubuntu 22.04,Bash)

```
//環境変数を読み込む場合
$ export INIAD_OPENAI_API_KEY="{AI-MOPのAPIキー}"
$ bash init.sh

//もしくは
//"key.secret"という名前のファイルを直下に作成し、AI-MOPのAPIキーを直接書き込む

```
