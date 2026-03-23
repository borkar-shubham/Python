'''
This is a simple banking app which is having below utilities -
#Show Balance
#Diposite Money
#Withdraw Money
'''
balance = 0.0
kyc_documents = {}

def check_balance():
    print(f"Your account balance is {balance}")

def deposite(amount):
    global balance
    if amount > 0:
        balance += amount
        print("\n")
        print("Amount Deposited..!")
    else:
        print("\n")
        print("Invalid Amount Entered")

def withdraw(amount):
    global balance
    if amount <= 0:
        print("\n")
        print("Invalid Amount Entered")
    elif amount > balance:
        print("\n")
        print("Insufficient Amount for Withdrawal")
    else:
        balance -= amount
        print("\n")
        print("Amount withdrawn..!")

def check_kyc():
    if len(kyc_documents) == 0:
        print("KYC Not Completed..!")
    else:
        for doc in kyc_documents:
            print(f"{doc}: {kyc_documents[doc]}")

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

#######################################################################################

if __name__ == "__main__":
    print("\n")
    print("###############################")
    print("# Welcome to Deutsche Bank..! #")
    print("###############################")

    while True:
        print("\n")
        print("Select the appropriate option from below menu:")
        print("1. Check Your Balance")
        print("2. Deposite Amount")
        print("3. Withdraw Amount")
        print("4. Check KYC Status")
        print("5. Update KYC")
        print("6. Quit")
        print("\n")
        choice = input("Enter Your Choice (1-6): ")
        print("\n")

        if choice == '1':
            check_balance()
        elif choice == '2':
            amt = float(input("Enter the amount to deposit: "))
            deposite(amt)
        elif choice == '3':
            amt = float(input("Enter the amount to withdraw: "))
            withdraw(amt)
        elif choice == '4':
            print("Your KYC Status:")
            check_kyc()
        elif choice == '5':
            kyc_docs = {}
            n_documents = int(input("Enter the number of KYC documents to add: "))
            for n in range(n_documents):
                key = input("Enter the KYC document type: ")
                value = input("Enter the document number: ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print()
            print("KYC Updated..!")
        elif choice == '6':
            print("Exiting Application.")
            break
        else:
            print("Invalid Choice, please try again..!")
    print("Thank you for banking with us..!")
    print("\n")