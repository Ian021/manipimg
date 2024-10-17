import tkinter as tk
from tkinter import filedialog, messagebox
from logica import particionar_imagem

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Particionador de Imagem")
        
        # Variáveis para inputs
        self.tamanho_x = tk.IntVar()
        self.tamanho_y = tk.IntVar()
        self.caminho_imagem = ""
        self.pasta_destino = ""
        
        # Campos de input para X e Y
        tk.Label(root, text="Tamanho X:").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.tamanho_x).grid(row=0, column=1)
        
        tk.Label(root, text="Tamanho Y:").grid(row=1, column=0)
        tk.Entry(root, textvariable=self.tamanho_y).grid(row=1, column=1)

        # Botão para importar imagem
        tk.Button(root, text="Importar Imagem", command=self.importar_imagem).grid(row=2, column=0, columnspan=2)
        
        # Botão para selecionar pasta de destino
        tk.Button(root, text="Selecionar Pasta", command=self.selecionar_pasta).grid(row=3, column=0, columnspan=2)

        # Botão para particionar imagem
        tk.Button(root, text="Particionar Imagem", command=self.particionar).grid(row=4, column=0, columnspan=2)

    def importar_imagem(self):
        self.caminho_imagem = filedialog.askopenfilename(
            title="Selecione a imagem",
            filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")]
        )
        if self.caminho_imagem:
            messagebox.showinfo("Imagem Selecionada", f"Imagem: {self.caminho_imagem}")
    
    def selecionar_pasta(self):
        self.pasta_destino = filedialog.askdirectory(title="Selecione a pasta de destino")
        if self.pasta_destino:
            messagebox.showinfo("Pasta Selecionada", f"Pasta: {self.pasta_destino}")
    
    def particionar(self):
        if not self.caminho_imagem or not self.pasta_destino:
            messagebox.showerror("Erro", "Imagem ou pasta não selecionada.")
            return
        
        if self.tamanho_x.get() <= 0 or self.tamanho_y.get() <= 0:
            messagebox.showerror("Erro", "Tamanhos X e Y devem ser maiores que zero.")
            return
        
        try:
            particionar_imagem(self.caminho_imagem, self.pasta_destino, self.tamanho_x.get(), self.tamanho_y.get())
            messagebox.showinfo("Sucesso", "Imagem particionada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Inicializa a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
