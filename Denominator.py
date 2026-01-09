def n_notes(amount):
    notes=[1000,500,200,100,50,20,10,5,1]
    remaining_notes=0
    for i in range(9):
        note_r=notes[i]
        remaining_notes=amount//note_r
        print(f"Notes of {note_r} is {remaining_notes}")
        amount=amount%note_r
amount=int(input("Enter Amount: "))
n_notes(amount)