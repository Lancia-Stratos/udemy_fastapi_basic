def divide(a, b):
    try:
        result = a / b
    except Exception as e:
        print(f"エラー発生: {e}")
    finally:
        print("処理終了")

divide(10, 0)
divide(10, 2)