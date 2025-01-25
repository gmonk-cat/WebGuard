import webview

def create_window():

    webview.create_window(
        title="WebGuard",
        url="src/index.html",
        width=800,
        height=600,
    )
    webview.start()

if __name__ == "__main__":
    create_window()