dict={
    "fast": "in a Qick manner",
    "python" :"programming language",
    "age":[1,2,3],
    "anotherdict":{'python':'Snake'} #nested dictionary
}
dict["age"] =[21,23,42] #changing age
dict["fast"] = "run" #changing meaning
print(dict["python"])
print(dict["fast"])
print(dict["age"])
print(dict["anotherdict"]["python"])