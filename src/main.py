import argparse
import os

def main():
    parser = argparse.ArgumentParser(
        description="YouTubeチャンネル/再生リストから字幕付き動画のメタ情報＋字幕を取得し、CSV/.txt形式で出力するツール (ミニマム版)"
    )
    parser.add_argument(
        "--version", action="version", version="keiei_youtube_info v0.1"
    )
    args = parser.parse_args()
    print("\n経営中毒 YouTube コンシェルジュ (ミニマム版)\n")
    print("--help で使い方を表示します。今後の実装で各種オプション追加予定。\n")

if __name__ == "__main__":
    main()
