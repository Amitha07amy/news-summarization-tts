import os

def deploy():
    os.system("git add .")
    os.system("git commit -m 'Deploying to Hugging Face Spaces'")
    os.system("git push origin main")

if __name__ == "__main__":
    deploy()
