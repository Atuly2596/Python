import pandas as pd

data_frame = pd.DataFrame(
    {
        "So.No.":[1,2,3,4,5,6,7,8,9,10],
        "RollNo.":[121,21,54,54,54,54,65,5,8,6],
        "class":["class1","class2","class10","class1","class5","class5","class2","class1","class8","class10",]
    }
)
print(data_frame.shape)
print("------------------------------")
print(data_frame)
print("------------------------------")
print(data_frame.head(2))
print("---------------------------")
print(data_frame.tail()) #by default it takes argument as 5

print(data_frame.info)


