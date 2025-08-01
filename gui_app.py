import tkinter as tk
from tkinter import filedialog, messagebox
from sku_mapper import SkuMapper

def run_mapper():
    try:
        sales_file = filedialog.askopenfilename(title="Select Sales CSV/XLSX")
        if not sales_file:
            return
        mapper = SkuMapper(mapping_file.get())
        mapper.map_skus(sales_file)
        messagebox.showinfo("Success", "Mapping complete. Check output_mapped_sales.csv")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("SKU Mapper")

tk.Label(root, text="Master SKU Mapping File:").pack(pady=5)
mapping_file = tk.Entry(root, width=50)
mapping_file.pack()
tk.Button(root, text="Browse", command=lambda: mapping_file.insert(0, filedialog.askopenfilename())).pack()

tk.Button(root, text="Run Mapping", command=run_mapper).pack(pady=10)

root.mainloop()
