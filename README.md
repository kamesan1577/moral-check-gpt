# moral-check-gpt

## 概要

OpenAI の ModerationAPI を使って文章の不適切さを判定するプログラムです。
AI-MOP 上での使用を想定しています
画像の入力にも対応しています

## 使用方法

https://scenex.jina.ai/にアクセスして、APIキーを取得(※めんどくさかったらkamesanに聞いてください)
後述のターミナル上での設定を行った後、
main.ipynb を jupyter notebook 上で実行してください(オーナーは VSCode 上で動かしてるので動かなかったらごめん)

### ターミナルでの設定(Ubuntu 22.04,Bash)

```
$ export INIAD_OPENAI_API_KEY="{AI-MOPのAPIキー}"
$ export SCENEX_API_KEY="{scenexのAPIキー}"
$ bash init.sh

```
