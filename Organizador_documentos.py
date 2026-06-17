#Organizador de documentos
import os
import shutil

# O Python descobre automaticamente a pasta raiz do usuário atual
# Isso funciona para qualquer pessoa, em qualquer PC!
pasta_base = os.path.expanduser("~")

# Definimos os caminhos de forma dinâmica
pasta_origem = os.path.join(pasta_base, "Downloads")
pasta_destino_base = os.path.join(pasta_base, "Documentos", "Organizados")

# Define a extensão e o nome da pasta de destino
configuracao = {
    ".docx": "Documentos_Word",
    ".pdf": "PDFs",
    ".exe": "Programas",
    ".jpg": "Imagens",
    ".png": "Imagens",
    ".html": "Arquivos_Web"
}

def organizar_arquivos():
    # Verifica se a pasta de origem existe antes de começar
    if not os.path.exists(pasta_origem):
        print(f"Erro: A pasta {pasta_origem} não foi encontrada.")
        return

    arquivos = os.listdir(pasta_origem)
    
    for arquivo in arquivos:
        for extensao, nome_pasta in configuracao.items():
            if arquivo.lower().endswith(extensao):
                
                # Define o caminho completo da pasta de destino
                destino = os.path.join(pasta_destino_base, nome_pasta)
                
                # CRIA A PASTA AUTOMATICAMENTE
                os.makedirs(destino, exist_ok=True)
                print(f"DEBUG: Garantindo que a pasta existe em: {destino}") 
                # Monta os caminhos
                origem_completa = os.path.join(pasta_origem, arquivo)
                destino_completo = os.path.join(destino, arquivo)
                
                # Move o arquivo
                shutil.move(origem_completa, destino_completo)
                print(f"Sucesso: {arquivo} movido para {destino}")

if __name__ == "__main__":
    organizar_arquivos()
    print("Organização concluída!")