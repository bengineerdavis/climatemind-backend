import csv 


def main ():
    with open ("source","rb") as source:
        init_csv = csv.reader(source)
        with open ("result", "wb") as result: 
            cleaned_csv = csv.writer(result)

            for row in cleaned_csv:
                print("row",row)


if __name__ == "__main__":
   main()