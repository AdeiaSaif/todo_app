import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkfont

class UltraTodoPro(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # App Configuration
        self.title("✨ Ultra Todo Pro")
        self.geometry("1000x700")
        self.configure(bg="#f5f7fa")
        
        # User Data
        self.current_user = tk.StringVar(value="User")
        self.tasks = []
        
        # Modern Color Scheme (Dark Theme)
        self.colors = {
            "primary": "#6c5ce7",
            "secondary": "#a29bfe",
            "success": "#00b894",
            "warning": "#fdcb6e",
            "danger": "#ff7675",
            "light": "#2d3436",
            "dark": "#1e272e",
            "text": "#dfe6e9",
            "entry_bg": "#57606f"
        }
        
        # Create UI
        self.create_navbar()
        self.create_main_panel()
        self.create_task_form()
        self.create_task_list()
        
        # Bind window resize
        self.bind("<Configure>", self.on_window_resize)
        
        # Sample Tasks
        self.add_sample_tasks()
    
    def on_window_resize(self, event):
        # Adjust column widths dynamically
        if hasattr(self, 'task_tree'):
            total_width = self.right_panel.winfo_width() - 30
            self.task_tree.column("id", width=int(total_width*0.08))
            self.task_tree.column("title", width=int(total_width*0.25))
            self.task_tree.column("desc", width=int(total_width*0.45))
            self.task_tree.column("status", width=int(total_width*0.15))
    
    def create_navbar(self):
        navbar = tk.Frame(self, bg=self.colors["dark"], height=60)
        navbar.pack(fill=tk.X, padx=0, pady=0)
        
        # User Label (updates automatically)
        self.user_label = tk.Label(navbar, textvariable=self.current_user, 
                                 bg=self.colors["dark"], fg=self.colors["text"],
                                 font=("Arial", 12, "bold"))
        self.user_label.pack(side=tk.LEFT, padx=20)
        
        # App Title
        title_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
        tk.Label(navbar, text="Ultra Todo Pro", bg=self.colors["dark"], 
                fg=self.colors["text"], font=title_font).pack(side=tk.LEFT, padx=10)
        
        # Settings Button
        settings_btn = tk.Button(navbar, text="⚙️", bg=self.colors["dark"], 
                               fg=self.colors["text"], bd=0, font=("Arial", 14),
                               command=self.show_settings)
        settings_btn.pack(side=tk.RIGHT, padx=20)
    
    def create_main_panel(self):
        main_frame = tk.Frame(self, bg=self.colors["light"])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left Panel - Task Form
        self.left_panel = tk.Frame(main_frame, bg=self.colors["dark"], bd=0, 
                                 relief=tk.RAISED, width=300)
        self.left_panel.pack_propagate(False)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        # Right Panel - Task List
        self.right_panel = tk.Frame(main_frame, bg=self.colors["light"], bd=0)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    def create_task_form(self):
        form_header = tk.Label(self.left_panel, text="➕ New Task", 
                             font=("Arial", 14, "bold"), 
                             bg=self.colors["dark"], fg=self.colors["text"])
        form_header.pack(pady=20, fill=tk.X)
        
        # Task Title
        tk.Label(self.left_panel, text="Title:", bg=self.colors["dark"], 
               fg=self.colors["text"], anchor="w").pack(fill=tk.X, padx=20)
        self.title_entry = tk.Entry(self.left_panel, font=("Arial", 12),
                                  bg=self.colors["entry_bg"], fg="white",
                                  insertbackground="white")
        self.title_entry.pack(fill=tk.X, padx=20, pady=5)
        
        # Task Description
        tk.Label(self.left_panel, text="Description:", bg=self.colors["dark"], 
               fg=self.colors["text"], anchor="w").pack(fill=tk.X, padx=20, pady=(15, 0))
        self.desc_text = tk.Text(self.left_panel, height=8, font=("Arial", 12),
                               bg=self.colors["entry_bg"], fg="white",
                               insertbackground="white")
        self.desc_text.pack(fill=tk.X, padx=20, pady=5)
        
        # Add Button
        add_btn = tk.Button(self.left_panel, text="ADD TASK", 
                          bg=self.colors["primary"], fg="white",
                          font=("Arial", 12, "bold"), bd=0,
                          activebackground=self.colors["secondary"],
                          command=self.add_task)
        add_btn.pack(fill=tk.X, padx=20, pady=20)
    
    def create_task_list(self):
        # Toolbar
        toolbar = tk.Frame(self.right_panel, bg=self.colors["dark"])
        toolbar.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(toolbar, text="📋 Your Tasks", font=("Arial", 14, "bold"), 
               bg=self.colors["dark"], fg=self.colors["text"]).pack(side=tk.LEFT, padx=20)
        
        # Task List Treeview
        self.task_tree = ttk.Treeview(self.right_panel, columns=("id", "title", "desc", "status"), 
                                  show="headings", height=20)
        
        # Style Configuration
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", 
                       background=self.colors["text"],
                       foreground=self.colors["text"],
                       fieldbackground=self.colors["dark"],
                       font=("Arial", 11))
        style.configure("Treeview.Heading", 
                       background=self.colors["primary"],
                       foreground="white",
                       font=("Arial", 12, "bold"))
        style.map("Treeview", 
                 background=[('selected', self.colors["secondary"])],
             foreground=[('selected', 'white')])
        
        # Configure Columns
        self.task_tree.heading("id", text="ID")
        self.task_tree.heading("title", text="Title")
        self.task_tree.heading("desc", text="Description")
        self.task_tree.heading("status", text="Status")
        
        self.task_tree.column("id", width=60, anchor=tk.CENTER)
        self.task_tree.column("title", width=200)
        self.task_tree.column("desc", width=400)
        self.task_tree.column("status", width=120, anchor=tk.CENTER)
        
        # Add Scrollbars
        v_scroll = ttk.Scrollbar(self.right_panel, orient=tk.VERTICAL, command=self.task_tree.yview)
        h_scroll = ttk.Scrollbar(self.right_panel, orient=tk.HORIZONTAL, command=self.task_tree.xview)
        self.task_tree.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
        # Force white text in all cases
        self.task_tree.configure(style="Custom.Treeview")
        style.configure("Custom.Treeview", foreground="white")
        self.task_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Action Buttons
        btn_frame = tk.Frame(self.right_panel, bg=self.colors["light"])
        btn_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Button(btn_frame, text="✅ Complete", bg=self.colors["success"], 
                fg="white", bd=0, padx=15, pady=8,
                activebackground="#00cec9",
                command=self.complete_task).pack(side=tk.LEFT, padx=5)
        
        tk.Button(btn_frame, text="✏️ Edit", bg=self.colors["warning"], 
                fg="black", bd=0, padx=15, pady=8,
                activebackground="#ffeaa7",
                command=self.edit_task).pack(side=tk.LEFT, padx=5)
        
        tk.Button(btn_frame, text="🗑️ Delete", bg=self.colors["danger"], 
                fg="white", bd=0, padx=15, pady=8,
                activebackground="#ff7675",
                command=self.delete_task).pack(side=tk.LEFT, padx=5)
    
    def add_sample_tasks(self):
        sample_tasks = [
            (1, "Buy groceries", "Milk, Eggs, Bread", "Pending"),
            (2, "Finish project", "Complete the GUI design", "Pending"),
            (3, "Call mom", "Discuss family plans", "Completed")
        ]
        for task in sample_tasks:
            self.task_tree.insert("", tk.END, values=task, tags=("odd" if task[0]%2 else "even"))
            self.tasks.append(task)
        
        # Configure row colors
        # Change these lines in add_sample_tasks() or wherever you set row colors
        self.task_tree.tag_configure("odd", background=self.colors["dark"], foreground=self.colors["text"])
        self.task_tree.tag_configure("even", background="#34495e", foreground=self.colors["text"])
    
    def add_task(self):
        title = self.title_entry.get().strip()
        desc = self.desc_text.get("1.0", tk.END).strip()
        
        if not title:
            messagebox.showwarning("Oops", "Title is required!", parent=self)
            return
            
        new_id = max([task[0] for task in self.tasks], default=0) + 1
        new_task = (new_id, title, desc, "Pending")
        
        self.task_tree.insert("", tk.END, values=new_task, 
                            tags=("odd" if new_id%2 else "even"))
        self.tasks.append(new_task)
        
        # Clear form
        self.title_entry.delete(0, tk.END)
        self.desc_text.delete("1.0", tk.END)
        
        messagebox.showinfo("Success", "Task added!", parent=self)
    
    def complete_task(self):
        selected = self.task_tree.selection()
        if selected:
            item = self.task_tree.item(selected)
            task_id = item['values'][0]
            
            for i, task in enumerate(self.tasks):
                if task[0] == task_id:
                    new_status = "Completed" if task[3] == "Pending" else "Pending"
                    updated_task = (task[0], task[1], task[2], new_status)
                    self.tasks[i] = updated_task
                    self.task_tree.item(selected, values=updated_task)
                    break
    
    def edit_task(self):
        selected = self.task_tree.selection()
        if selected:
            item = self.task_tree.item(selected)
            task_id = item['values'][0]
            
            # Create edit window
            edit_win = tk.Toplevel(self)
            edit_win.title(f"Edit Task #{task_id}")
            edit_win.geometry("500x400")
            edit_win.configure(bg=self.colors["dark"])
            
            # Title
            tk.Label(edit_win, text="Title:", bg=self.colors["dark"], 
                   fg=self.colors["text"]).pack(pady=(20,5))
            title_entry = tk.Entry(edit_win, font=("Arial", 12),
                                 bg=self.colors["entry_bg"], fg="white")
            title_entry.insert(0, item['values'][1])
            title_entry.pack(fill=tk.X, padx=20, pady=5)
            
            # Description
            tk.Label(edit_win, text="Description:", bg=self.colors["dark"], 
                   fg=self.colors["text"]).pack(pady=(15,5))
            desc_text = tk.Text(edit_win, height=10, font=("Arial", 12),
                              bg=self.colors["entry_bg"], fg="white")
            desc_text.insert("1.0", item['values'][2])
            desc_text.pack(fill=tk.BOTH, padx=20, pady=5, expand=True)
            
            # Save Button
            def save_changes():
                new_title = title_entry.get().strip()
                new_desc = desc_text.get("1.0", tk.END).strip()
                
                if not new_title:
                    messagebox.showwarning("Oops", "Title cannot be empty!", parent=edit_win)
                    return
                
                for i, task in enumerate(self.tasks):
                    if task[0] == task_id:
                        self.tasks[i] = (task_id, new_title, new_desc, task[3])
                        self.task_tree.item(selected, values=self.tasks[i])
                        break
                
                edit_win.destroy()
                messagebox.showinfo("Saved", "Task updated!", parent=self)
            
            tk.Button(edit_win, text="💾 Save Changes", bg=self.colors["primary"], 
                    fg="white", command=save_changes).pack(pady=20)
    
    def delete_task(self):
        selected = self.task_tree.selection()
        if selected:
            if messagebox.askyesno("Confirm", "Delete this task permanently?", parent=self):
                task_id = self.task_tree.item(selected)['values'][0]
                self.tasks = [task for task in self.tasks if task[0] != task_id]
                self.task_tree.delete(selected)
    
    def show_settings(self):
        settings = tk.Toplevel(self)
        settings.title("Settings")
        settings.geometry("400x300")
        settings.configure(bg=self.colors["dark"])
        
        tk.Label(settings, text="⚙️ Settings", font=("Arial", 16, "bold"), 
               bg=self.colors["dark"], fg=self.colors["text"]).pack(pady=20)
        
        # Username Change
        tk.Label(settings, text="Change Username:", bg=self.colors["dark"], 
               fg=self.colors["text"]).pack()
        name_entry = tk.Entry(settings, font=("Arial", 12),
                            bg=self.colors["entry_bg"], fg="white")
        name_entry.insert(0, self.current_user.get())
        name_entry.pack(pady=10)
        
        # Theme Selection
        # tk.Label(settings, text="Select Theme:", bg=self.colors["dark"], 
        #        fg=self.colors["text"]).pack(pady=(20,5))
        
        # theme_var = tk.StringVar(value="dark")
        # themes = [("Dark Theme", "dark"), ("Light Theme", "light")]
        
        # for text, mode in themes:
        #     tk.Radiobutton(settings, text=text, variable=theme_var, value=mode,
        #                  bg=self.colors["dark"], fg=self.colors["text"],
        #                  selectcolor=self.colors["primary"]).pack(anchor=tk.W)
        
        def apply_settings():
            self.current_user.set(name_entry.get())
            self.user_label.config(text=f"👤 {self.current_user.get()}")
            
            # Here you would implement theme changing logic
            messagebox.showinfo("Saved", "Settings updated!", parent=settings)
            settings.destroy()
        
        tk.Button(settings, text="Apply Changes", bg=self.colors["primary"], 
                fg="white", command=apply_settings).pack(pady=20)

if __name__ == "__main__":
    app = UltraTodoPro()
    app.mainloop()