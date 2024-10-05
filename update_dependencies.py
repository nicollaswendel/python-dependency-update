import os

def update_dependencies():
    os.system("pip install --upgrade -r requirements.txt")
    print("Dependências atualizadas com sucesso!")

if __name__ == "__main__":
    update_dependencies()
