# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    returned_date = input().split(' ')
    due_date = input().split(' ')
    return_day = int(returned_date[0])
    return_month = int(returned_date[1])
    return_year = int(returned_date[2])

    due_day = int(due_date[0])
    due_month = int(due_date[1])
    due_year = int(due_date[2])
    fine = 0
    if return_year == due_year:
        if return_month == due_month:
            if return_day == due_date:
                fine = 0
            elif return_day > due_day : 
                fine = 15 * (return_day - due_day)
            else:
                fine = 0
        elif return_month > due_month:
            fine = 500 * (return_month - due_month)
        else:
            fine = 0
    elif return_year > due_year:
        fine = 10000
    else:
        fine = 0
        
    print(fine)
