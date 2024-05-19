from customtkinter import *
from Calc_Function import Calc
from Exc import InvalidEntryException
from pywinstyles import *


global bg
bg="#000000"

global again,end_btn


def Calculator(n,land):

    def hover_btn(event):
        btn.configure(fg_color="white", text_color="black")

    def leave_btn(event):
        btn.configure(fg_color="#111111", text_color="white")

    def hover_again(event):
        again.configure(fg_color="white", text_color="black")

    def leave_again(event):
        again.configure(fg_color="#111111", text_color="white")

    def hover_end(event):
        end_btn.configure(fg_color="red", text_color="black")

    def leave_end(event):
        end_btn.configure(fg_color="#111111", text_color="white")





    # Function to close the window upon clicking exit button
    def close():
        land.destroy()
        exit()

    # Function to open the calc window again on clicking the 'again' button

    def calc_again():
        root.withdraw()
        Calculator(n,land)

    # Function to take input,calculate the SGPA

    def calc():

        global again, end_btn

        flag=0    # flag variable to check for Value errors before calculating the SGPA

        # try-except block to take input of credit points for each subject.

        try:
            for i in range(n):
                val=int(creds_widgets[i].get())
                if val<=0:
                    raise ValueError
                creds.append(val)
        except ValueError:
            error_creds.configure(text_color="red")
            flag=1

        # try-except block to take user input for grades obtained in each subject

        try:
            for i in range(n):
                val=int(grads_widgets[i].get())
                if val>10 or val<=0:
                    raise InvalidEntryException
                grads.append(val)
        except ValueError:
            error_grads.configure(text_color="red")
            flag=1

        except InvalidEntryException: # User defined exception raised when value>10
            error_grads.configure(text_color="red")
            flag=1

        # Logic to calculate the SGPA

        if flag==0: # Check for errors in user input
            SGPA = Calc(creds, grads, n)    # Call the Calc function to calculate the SGPA using the user input

            # Destroy all the widgets (by destroying all the frames)

            lbl_frm.destroy()
            cred_frm.destroy()
            grad_frm.destroy()
            btn_frm.destroy()

            root.configure(fg_color='black')

            # Create Labels to display the result

            final=CTkLabel(root,text="SGPA",font=("Digital-7",80))
            final.place(relx=0.5,rely=0.35,anchor="center")

            value=CTkLabel(root,text=f"{SGPA}",font=("Digital-7",80))
            value.place(relx=0.5,rely=0.5,anchor='center')

            # Create Buttons for recalculation , exiting

            again=CTkButton(root,text="Calculate Again",command=calc_again,text_color="white",fg_color="#111111",height=45,width=95,font=("Digital-7",20))
            again.place(relx=0.40,rely=0.65,anchor=CENTER)

            end_btn=CTkButton(root,text="Exit",command=exit,text_color="white",fg_color="#111111",height=45,font=("Digital-7",20))
            end_btn.place(relx=0.60,rely=0.65,anchor=CENTER)

            # Hover

            again.bind('<Enter>', hover_again)
            again.bind('<Leave>', leave_again)

            end_btn.bind('<Enter>', hover_end)
            end_btn.bind('<Leave>', leave_end)
        else:

            # Clear the creds and grads values in case of wrong entry (flag!=0)

            creds.clear()
            grads.clear()


    creds=[]
    grads=[]

    creds_widgets=[]
    grads_widgets=[]
    labels=[]
    labels2 = []

    fnt=("Digital-7",35)

    # Root window config

    root=CTk()
    root.config(background=bg)
    root.after(0,lambda:root.state('zoomed'))
    root.wm_attributes("-fullscreen",True)
    root.geometry("10x10")
    change_header_color(root, color=bg)
    root.title("")

    # Grid layout config
    root.grid_rowconfigure((0,1,3,4),weight=0,uniform='a')
    root.grid_columnconfigure((0,1),weight=1,uniform='a')
    root.grid_rowconfigure(2,weight=1)

    # Frames and Widget creation

    lbl_frm=CTkFrame(root,fg_color="black",bg_color=bg)
    cred_frm=CTkFrame(root,fg_color="black",bg_color=bg)
    grad_frm=CTkFrame(root,fg_color="Black",bg_color=bg)
    btn_frm=CTkFrame(root,fg_color="Black",bg_color=bg)


    cred_lbl=CTkLabel(lbl_frm,text="Enter the subject credits",font=fnt)
    grad_lbl=CTkLabel(lbl_frm,text="Enter the subject grade-points",font=fnt)


    btn=CTkButton(btn_frm,text="Calculate",fg_color="#111111",text_color="White",height=50,font=("Digital-7",20))


    # Label and Cred frames grid config

    lbl_frm.grid(row=1,column=0,columnspan=4,sticky="nsew",padx=10)
    lbl_frm.grid_columnconfigure((0,1),weight=1)
    lbl_frm.grid_rowconfigure(0,weight=1)

    cred_lbl.grid(row=0,column=0)
    grad_lbl.grid(row=0,column=1)

    cred_frm.grid(row=2,column=0,sticky="nsew",padx=10,pady=10)
    cred_frm.grid_columnconfigure((0,1,2,3),weight=1)

    end=int(n/2)

    if n%2==0:
        for i in range(end+1):
            cred_frm.grid_rowconfigure(i, weight=1)
        end=i
    else:
        for i in range(end+2):
            cred_frm.grid_rowconfigure(i, weight=1)
        end=i

    # Cred entry and label widgets creation

    j=0
    for i in range(0,n):
        creds_widgets.append(CTkEntry(cred_frm))
        labels.append(CTkLabel(cred_frm))
        if i%2==0:
            creds_widgets[i].grid(row=j, column=1)
            labels[i].grid(row=j,column=0)
            labels[i].configure(text=f"Subject {i+1}:",font=("Digital-7",26))
        else:
            creds_widgets[i].grid(row=j, column=3)
            labels[i].grid(row=j,column=2)
            labels[i].configure(text=f"Subject {i+1}:",font=("Digital-7",26))
            j+=1
        creds_widgets[i].configure(corner_radius=15, fg_color="gray12", width=200, height=40, border_color="white", justify=CENTER, font=("Digital-7", 26),border_width=1)

    error_creds=CTkLabel(cred_frm,text="Please enter positive integers",text_color="black",font=("Dot Matrix",22))
    error_creds.grid(row=end,column=0,columnspan=4,sticky="nsew")

    # Grade frame grid config

    grad_frm.grid(row=2,column=1,sticky="nsew",padx=10,pady=10)
    grad_frm.grid_columnconfigure((0,1,2,3),weight=1)

    end=int(n/2)

    if n%2==0:
        for i in range(end+1):
            grad_frm.grid_rowconfigure(i,weight=1)
        end=i
    else:
        for i in range(end+2):
            grad_frm.grid_rowconfigure(i, weight=1)
        end=i



    j=0
    for i in range(n):
        grads_widgets.append(CTkEntry(grad_frm))
        labels2.append(CTkLabel(grad_frm))
        if i%2==0:
            grads_widgets[i].grid(row=j, column=1)
            labels2[i].grid(row=j,column=0)
        else:
            grads_widgets[i].grid(row=j, column=3)
            labels2[i].grid(row=j, column=2)
            j+=1
        grads_widgets[i].configure(corner_radius=15, fg_color="gray12", width=200, height=40, border_color="white", justify='center',font=("Digital-7",26),border_width=1)
        labels2[i].configure(text=f"Subject {i + 1}:", font=("Digital-7", 26))

    error_grads=CTkLabel(grad_frm,text="Please enter positive integers lesser than or equal to 10",text_color="black",font=("Dot Matrix",22))
    error_grads.grid(row=end,column=0,columnspan=4,sticky="nsew")


    btn_frm.grid(row=3,column=0,columnspan=2,rowspan=2,sticky="nsew",pady=10,padx=10)
    btn_frm.grid_rowconfigure(0,weight=1)
    btn_frm.grid_columnconfigure((0,1,2),weight=1)



    btn.grid(row=0,column=1)
    btn.bind('<Enter>', hover_btn)
    btn.bind('<Leave>', leave_btn)
    btn.configure(command=calc)
    root.protocol("WM_DELETE_WINDOW",close)

    root.mainloop()

