import pandas as pd

data=pd.read_csv("central_park.csv")

black=data[data["Primary Fur Color"]=="Black"]
red=data[data["Primary Fur Color"]=="Red"]
gray=data[data["Primary Fur Color"]=="Gray"]

length_black=len(black)
length_gray=len(gray)
length_red=len(red)

dictionary={
    "colors_name":["red","black","gray"],
    "count":[length_red,length_black,length_gray]
}
dataframe=pd.DataFrame(dictionary)
dataframe.to_csv("colors_squreils.csv")