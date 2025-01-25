def count (path):
    try:
        with open(path,'r') as file:
            file_content = file.read()
            return f"data = {file_content.split()}\nLength of the words:{len(file_content.split())}"
    except FileNotFoundError:
        return "Please provide valid file path."

path= "exampleprac3.txt"
print (count(path))