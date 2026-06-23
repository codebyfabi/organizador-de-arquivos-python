import os
import shutil


pasta_base = os.path.expanduser("~")

pasta_origem = os.path.join(pasta_base, "Downloads")
pasta_destino_base = os.path.join(pasta_base, "Documentos", "Organizados")

#Define a extensão e o nome da pasta de destino
configuracao = {
    ".docx": "Documentos_Word",
    ".pdf": "PDFs",
    ".exe": "Programas",
    ".jpg": "Imagens",
    ".png": "Imagens",
    ".html": "Arquivos_Web"
}

def organizar_arquivos():
    if not os.path.exists(pasta_origem):
        print(f"Erro: A pasta {pasta_origem} não foi encontrada.")
        return

    arquivos = os.listdir(pasta_origem)
    
    for arquivo in arquivos:
        for extensao, nome_pasta in configuracao.items():
            if arquivo.lower().endswith(extensao):
                
           
                destino = os.path.join(pasta_destino_base, nome_pasta)
                
             
                os.makedirs(destino, exist_ok=True)
                print(f"DEBUG: Garantindo que a pasta existe em: {destino}") 
            
                origem_completa = os.path.join(pasta_origem, arquivo)
                destino_completo = os.path.join(destino, arquivo)
                
                
                shutil.move(origem_completa, destino_completo)
                print(f"Sucesso: {arquivo} movido para {destino}")

if __name__ == "__main__":
    organizar_arquivos()
    print("Organização concluída!")
