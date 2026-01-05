import customtkinter as ctk
from mita_in_a_box import MitaInABox # Backend array implementation

# Window appearance configuration
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Window initialization
window = ctk.CTk()
window.title("Mita in a Box")
window.geometry("860x420")

# Status and error window popup
def status_window():
    new_window = ctk.CTkToplevel(window)
    new_window.title("Status")
    new_window.geometry("350x120")
    new_window.resizable(False, False)

def error_window():
    new_window = ctk.CTkToplevel(window)
    new_window.title("Error")
    new_window.geometry("350x120")
    new_window.resizable(False, False)


"""
Frame Setup
"""
# Main container
array_frame = ctk.CTkFrame(window, fg_color="transparent")
array_frame.pack(anchor="nw", padx=20, pady=10)

# Left frame
left_frame = ctk.CTkFrame(array_frame, fg_color="transparent")
left_frame.grid(row=0, column=0, sticky="nw")

# Divider
divider = ctk.CTkFrame(array_frame, width=2, height=120, fg_color="gray80")
divider.grid(row=0, column=1, padx=20, sticky="ns") # Adjust padx to control gap size

# Middle frame
middle_frame = ctk.CTkFrame(array_frame, fg_color="transparent")
middle_frame.grid(row=0, column=2, sticky="nw")

divider = ctk.CTkFrame(array_frame, width=2, height=120, fg_color="gray80")
divider.grid(row=0, column=3, padx=10, sticky="ns") # Adjust padx to control gap size

"""
Left frame
"""

# Array Length Label and Entry
label = ctk.CTkLabel(left_frame, text="Array Length (1-10)", font=ctk.CTkFont(size=14))
label.grid(row=0, column=0, sticky="w", padx=(0, 10))

def arrlength_validation(P):
    # P is the value that the text will have if the change is allowed
    if P == "": # Allow empty string
        return True
    if P.isdigit():
        value = int(P)
        if 1 <= value <= 10:
            # Update the IntVar only if valid
            array_length.set(value)
            return True   
    # Rejects the input if it's not a digit or out of range
    return False

array_length = ctk.IntVar(value=1)
vcmd = (window.register(arrlength_validation), '%P')

length_entry = ctk.CTkEntry(left_frame, width=140, validate="key", validatecommand=vcmd)
length_entry.grid(row=1, column=0, sticky="w", padx=(0, 20), pady=(10, 0))

# Array Data Type Combobox
array_data_type = ctk.StringVar(value="Data Type")
def data_type_function(choice):
    array_data_type.set(choice)
    print("combobox dropdown clicked:", array_data_type.get())

data_type_menu = ctk.CTkOptionMenu(left_frame, values=["String", "Integer", "Boolean", "Float"], command=data_type_function)
data_type_menu.set("Data Type")
data_type_menu.grid(row=2, column=0, sticky="w", padx=(0, 20), pady=(20, 0))

# Get data for the array
label_data_entry = ctk.CTkLabel(left_frame, text="Enter data (comma-separated):", font=ctk.CTkFont(size=14))
label_data_entry.grid(row=0, column=2, sticky="w")

data_entry = ctk.CTkEntry(left_frame, width=240, placeholder_text="E.g., 1, 2, 3, 4, 5")
data_entry.grid(row=1, column=2, sticky="w", pady=(10, 0))


# Create Array Button
def create_array():
    
    length = array_length.get()
    type = array_data_type.get()
    data = data_entry.get()
    try:
        pass
    except:
        pass
button = ctk.CTkButton(left_frame, text="Create Array", command = create_array)
button.grid(row=2, column=2, sticky="w", pady=(20, 0))


"""
Middle frame
"""

# Access index value

# Index Operations

index_label = ctk.CTkLabel(middle_frame, text="Index Operations", font=ctk.CTkFont(size=14))
index_label.grid(row=0, column=3, sticky="w", padx=(10, 0))

def access_index_popup():
    dialog = ctk.CTkInputDialog(text="Enter index to delete:", title="Delete Index")
    access_index = dialog.get_input()
    if access_index:
        pass
        # access(access_index) # for access class function
    else:
        print("Access index cancelled")
        
def delete_index_popup():
    dialog = ctk.CTkInputDialog(text="Enter index to delete:", title="Delete Index")
    delete_index = dialog.get_input()
    if delete_index:
        pass
        # delete(delete_index) # for delete class function
    else:
        print("Delete index cancelled")
        
def search_index_popup():
    dialog = ctk.CTkInputDialog(text="Enter index to search:", title="Search Index")
    search_index = dialog.get_input()
    if search_index:
        pass
        # search(search_index) # for search class function
    else:
        print("Search index cancelled")
        
def modify_index_popup():
    pass
    new_window = ctk.CTkToplevel(window)
    new_window.title("Modify Index")
    new_window.geometry("380x180")
    
    
access_button = ctk.CTkButton(middle_frame, text="Access Index", command=access_index_popup)
access_button.grid(row=1, column=3, sticky="w",  pady=(10, 0))

delete_button = ctk.CTkButton(middle_frame, text="Delete Index", command=delete_index_popup)
delete_button.grid(row=2, column=3, sticky="w",  pady=(10, 0))

search_button = ctk.CTkButton(middle_frame, text="Search Value", command=search_index_popup)
search_button.grid(row=1, column=4, sticky="w",  padx=20, pady=(10, 0))

modify_button = ctk.CTkButton(middle_frame, text="Modify Index", command=modify_index_popup)
modify_button.grid(row=2, column=4, sticky="w",  padx=20, pady=(10, 0))



window.mainloop()