def executeCode(output, code_area, tk):
    code = code_area.get("1.0", tk.END)
    output.delete("1.0", tk.END)
    output.insert(tk.END, f"Executing...\n{code}")