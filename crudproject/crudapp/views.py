from django.shortcuts import render, redirect


data_dict = [
    {
        "Id":1,
        "Name": "Ram",
        "Email":"ram@gmail.com",
        "Age": 20,
        "City": "Delhi"
    }
]
    


def create(request):
    count = len(data_dict)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        city = request.POST.get("city")
        count+=1
        newData = {
            "Id":count,
            "Name": name,
            "Email":email,
            "Age": age,
            "City": city
        }
        data_dict.append(newData)
        return redirect("/read")
    return render(request, "create.html")

def read(request):
    return render(request, "read.html", {"data": data_dict})

def update(request):
    if request.method == "POST":
        email = request.POST.get("email")
        age = request.POST.get("age")
        city = request.POST.get("city")
        for data in data_dict:
            if data['Email'] == email:
                data['Age'] = age
                data['City'] = city
                return redirect("/read")
    return render(request, "update.html")

def delete(request):
    if request.method == "POST":
        email = request.POST.get("email")
        for data in data_dict:
            if data["Email"] == email:
                data_dict.remove(data)
                return redirect("/read")
    return render(request, "delete.html")

